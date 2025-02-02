"""Generate a Application."""

import subprocess
import sys
from pathlib import Path

import click
import toml

from update_version import add_version, update_spec


def fixture(func):
    """Fixture decorator."""

    def wrapper():
        """Read the project config and set up support."""
        config_path = Path("pyinstaller.toml")
        # Get the os platform
        platform = sys.platform

        # Get the path to the executable
        # print(sys.executable)
        python_path = Path(sys.executable)
        bin_path = python_path.parent

        # Load the config info and initialize the meta
        config = toml.load(config_path)

        func(platform, bin_path, config)

    return wrapper


def translate(data: list, platform: str) -> list[str]:
    """Replace the `:` with `;` on windows."""
    seperator = ":" if platform == "darwin" else ";"
    return [item.replace(":", seperator) for item in data]


@fixture
def generate_spec_file(platform: str, bin_path: Path, config: dict):
    """Generate a Application."""
    application_name: str = config["project"]["name"]
    cmd: Path = Path(bin_path, "pyi-makespec")
    args: list = []

    # Check if the spec file exists and delete it if it does
    spec_path = Path(f"{application_name}.spec")
    print(f"Removing {spec_path} if it exists")
    if spec_path.exists():
        spec_path.unlink()

    # Add the path to the cmd
    cmd = Path(bin_path, cmd)

    args += config["arguments"]["base"]
    args.append("--name=" + config["project"]["name"])
    args.append(
        "--icon="
        + (
            config["project"]["macos_icon"]
            if platform == "darwin"
            else config["project"]["windows_icon"]
        )
    )
    # args += translate(config["arguments"]["data"], platform)
    args += config["arguments"]["data"]

    args += config["arguments"]["exclude"]
    args += config["arguments"]["hidden"]

    if platform == "darwin":
        args.append("--codesign-identity=Developer ID Application: Brady Fry (LT3LJEF3CS)")
        args.append("--osx-bundle-identifier=com.bradyfry.lt3ljef3cs." + config["project"]["name"])
        args += config["arguments"]["macos"]
    elif platform == "win32":
        args += config["arguments"]["windows"]

    args.append(config["project"]["entry_point"])

    run_cmd(cmd, args)

    # Add the version number to the spec file
    if platform == "darwin":
        add_version(application_name)
        update_spec(application_name)


@fixture
def make_app(platform: str, bin_path: Path, config: dict):
    """Generate the application with PyInstaller."""
    application_name: str = config["project"]["name"]
    cmd: Path = Path(bin_path, "pyinstaller")
    args: list = [
        "--clean",
        "-y",
    ]

    # Update the spec version number
    if platform == "darwin":
        update_spec(application_name)

    cmd = Path(bin_path, cmd)
    args.append(f"{application_name}.spec")

    run_cmd(cmd, args)


@fixture
def make_dmg(_: str, bin_path: Path, config: dict):
    """Generate the application with PyInstaller."""
    application_name: str = config["project"]["name"]
    cmd = Path(bin_path, "dmgbuild")
    args = [
        "-s",
        "dmg-settings.json",
        f'"{application_name} Installation"',
        f"{application_name}.dmg",
    ]

    run_cmd(cmd, args)


def run_cmd(cmd: Path, args: list[str]):
    """Run a command with the given arguments."""
    print(f"\n{'-' * 80}")
    print(f"Running command: {cmd} {' '.join(args)}")
    print(f"{'-' * 80}\n")
    subprocess.run([cmd, *args])


@click.command()
@click.option("-s", "--spec", is_flag=True, help="Generate the spec file")
@click.option("-a", "--app", is_flag=True, help="Make application")
@click.option("-d", "--dmg", is_flag=True, help="Make dmg file")
def main(spec: bool = False, app: bool = False, dmg: bool = False):
    """Update the version number in pyinstaller spec file and Info.plist file."""
    if spec:
        generate_spec_file()
    if app:
        make_app()
    if dmg:
        make_dmg()


if __name__ == "__main__":
    main()
