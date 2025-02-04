"""Mimspy application entry point."""

import multiprocessing as mp
import os
import sys
from pathlib import Path

from loguru import logger as log
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from mimspy import Mimspy, configs

# needed for click, macOS to run as a compiled app with pyinstaller
os.environ["LC_ALL"] = "en_US.utf-8"
os.environ["LANG"] = "en_US.utf-8"
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6"
mp.freeze_support()


def get_img_path() -> Path:
    """
    Get the path to the 'img' directory.

    This function is used to retrieve the path to the 'img' directory, particularly
    when bundling the application with PyInstaller. It checks if the application is
    running in a bundle and adjusts the path accordingly.

    Returns
    -------
    Path
        The path to the 'img' directory.
    """
    img_path = Path(os.path.dirname(__file__), "mimspy", "img")
    if getattr(sys, "frozen", False) and os.path.basename(sys.argv[0]) == configs.APP_NAME:
        # we are running in a bundle
        # noinspection PyProtectedMember
        img_path = Path(sys._MEIPASS, "img")  # type: ignore[attr-defined]
    return img_path


def init_app() -> QApplication | QCoreApplication:
    """
    Initialize and return a QApplication instance.

    This function creates a new QApplication instance or returns an existing one.
    It also adjusts application settings based on the operating system, e.g., enabling
    dark mode on Windows.

    Returns
    -------
    QtWidgets.QApplication
        The initialized QApplication instance.
    """
    # import platform

    # # 'Windows', 'Darwin', or 'Linux'
    # os_name = platform.system()
    # if os_name == "Windows":
    #     sys.argv += ["-platform", "windows:darkmode=2"]

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    return app


def main():
    """Run the main application."""
    log.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level=configs.LOG_LEVEL
    )
    log.debug("Starting the application")
    # Get the path to the img directory, need when bundling with pyinstaller
    icon_path: Path = Path(Path(__file__).parent, "mimspy", "icons")
    if getattr(sys, "frozen", False):
        # we are running in a bundle
        # noinspection PyProtectedMember
        icon_path = Path(sys._MEIPASS, "icons")  # type: ignore[attr-defined]

    mp.set_start_method("spawn", force=True)  # required for Linux
    if sys.platform.startswith("darwin"):
        # set bundle name on macOS (app name shown in the menu bar)
        # this must be done before the app is created
        # from Foundation import NSBundle
        #
        # bundle = NSBundle.mainBundle()
        # info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        # info["CFBundleName"] = app_name
        ...

    app = init_app()
    app.setApplicationName(configs.APP_NAME)
    app.setOrganizationName(configs.APP_ORGANIZATION)
    app.setApplicationVersion(configs.APP_VERSION)
    app.setFont(configs.FONT)  # type: ignore[attr-defined]
    theme = QApplication.styleHints().colorScheme()
    QIcon.setThemeName(theme.name.lower())
    if sys.platform.startswith("darwin"):
        app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
        if isinstance(app, QApplication):
            app.setWindowIcon(QIcon(str(Path(icon_path, "NGF_logo_sqr.icns"))))
    else:
        if isinstance(app, QApplication):
            app.setWindowIcon(QIcon(str(Path(icon_path, "NGF_logo_sqr.ico"))))
    if sys.platform.startswith("win"):
        if isinstance(app, QApplication):
            font = app.font()
            font.setPointSize(10)
            app.setFont(font)
            app.setStyle("fusion")
    # img_path = get_img_path()
    window = Mimspy(icon_path=icon_path)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
