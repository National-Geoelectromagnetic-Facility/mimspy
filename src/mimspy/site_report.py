"""A module to generate a site report."""

from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QSettings

from .configs import APP_NAME, APP_VERSION


class SiteReport:
    """A class to generate a site report."""

    def __init__(self) -> None:
        self.status = "Install"
        self.settings = QSettings("NGF", "mimspy")
        save_path_setting: str | None = self.settings.value("save_path")
        self.save_path = Path(save_path_setting) if save_path_setting else Path.home()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.save_name = "{}_.txt".format(self.date)
        self.sw = "{} v{}".format(APP_NAME, APP_VERSION)
        self.crew = ""
        self.site_id = ""
        self.site_name = ""
        self.site_state = ""
        self.country = ""
        self.nims_id = ""
        self.mag_id = ""
        self.electrode_north_id = ""
        self.electrode_south_id = ""
        self.electrode_east_id = ""
        self.electrode_west_id = ""
        self.lat = ""
        self.lon = ""
        self.alt = ""
        self.dec = ""
        self.battery = ""
        self.gain = ""
        self.ex_gps = ""
        self.ey_gps = ""
        self.last_ts = ""
        self.first_ts = ""
        self.pre_e_ns_r = ""
        self.pre_e_sn_r = ""
        self.pre_e_ew_r = ""
        self.pre_e_we_r = ""
        self.pre_e_ns_v = ""
        self.pre_e_ew_v = ""
        self.e_ns_r = ""
        self.e_sn_r = ""
        self.e_ew_r = ""
        self.e_we_r = ""
        self.e_gn_r = ""
        self.e_ng_r = ""
        self.e_ns_vdc = ""
        self.e_ew_vdc = ""
        self.e_ng_vdc = ""
        self.e_ns_vac = ""
        self.e_ew_vac = ""
        self.e_ng_vac = ""
        self.comments = ""

    def update_save_name(self, run_id: str) -> None:
        """Update the save name for the site report."""
        self.site_id = run_id
        self.save_name = "{}_{}.txt".format(self.date, run_id)

    def update_save_path(self, path_dir: Path) -> None:
        """Update the save path for the site report."""
        self.settings.setValue("save_path", str(path_dir))
        self.save_path = Path(self.settings.value("save_path"))

    def write_file(self) -> None:
        """Write the site report to a file."""
        divider = "--------------------------------------------------------------------"

        with open(Path(self.save_path, self.save_name), "w", encoding="utf-8") as fle_ptr:
            fle_ptr.write("Date: \t\t\t{}\n\n".format(self.date))
            fle_ptr.write("Software: \t\t{}\n\n".format(self.sw))
            fle_ptr.write("Crew: \t\t\t{}\n\n".format(self.crew))
            fle_ptr.write("Run ID: \t\t{}\n".format(self.site_id))
            fle_ptr.write(
                "Site Name: \t\t{}, {}, {}\n\n".format(
                    self.site_name, self.site_state, self.country
                )
            )
            fle_ptr.write("Status: \t\t{}\n".format(self.status))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("NIMS ID: \t\t{}\n".format(self.nims_id))
            fle_ptr.write("Mag ID: \t\t{}\n".format(self.mag_id))
            fle_ptr.write("Electrodes ID:\tN\t{}\n".format(self.electrode_north_id))
            fle_ptr.write("\t\tS\t{}\n".format(self.electrode_south_id))
            fle_ptr.write("\t\tE\t{}\n".format(self.electrode_east_id))
            fle_ptr.write("\t\tW\t{}\n".format(self.electrode_west_id))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Electrode Parameters, prior to installation:\n\n")
            fle_ptr.write("Resistance (ohms):\n")
            fle_ptr.write("(S- to N+) = \t\t{}\n".format(self.pre_e_ns_r))
            fle_ptr.write("(N- to S+) = \t\t{}\n".format(self.pre_e_sn_r))
            fle_ptr.write("(W- to E+) = \t\t{}\n".format(self.pre_e_ew_r))
            fle_ptr.write("(E- to W+) = \t\t{}\n\n".format(self.pre_e_we_r))
            fle_ptr.write("Voltage (mV):\n")
            fle_ptr.write("(S- to N+) DVC = \t{}\n".format(self.pre_e_ns_v))
            fle_ptr.write("(W- to E+) DVC = \t{}\n".format(self.pre_e_ew_v))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Electrode Parameters, at {}:\n\n".format(self.status))
            fle_ptr.write("Resistance (ohms):\n")
            fle_ptr.write("(S- to N+) = \t\t{}\n".format(self.e_ns_r))
            fle_ptr.write("(N- to S+) = \t\t{}\n".format(self.e_sn_r))
            fle_ptr.write("(W- to E+) = \t\t{}\n".format(self.e_ew_r))
            fle_ptr.write("(E- to W+) = \t\t{}\n".format(self.e_we_r))
            fle_ptr.write("(G- to N+) = \t\t{}\n".format(self.e_ng_r))
            fle_ptr.write("(N- to G+) = \t\t{}\n\n".format(self.e_gn_r))
            fle_ptr.write("Voltage (mV):\n")
            fle_ptr.write("(S- to N+) DVC = \t{}\n".format(self.e_ns_vdc))
            fle_ptr.write("(W- to E+) DVC = \t{}\n".format(self.e_ew_vdc))
            fle_ptr.write("(G- to N+) DVC = \t{}\n\n".format(self.e_ng_vdc))
            fle_ptr.write("(S- to N+) AVC = \t{}\n".format(self.e_ns_vac))
            fle_ptr.write("(W- to E+) AVC = \t{}\n".format(self.e_ew_vac))
            fle_ptr.write("(G- to N+) AVC = \t{}\n".format(self.e_ng_vac))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Gain = \t\t\t{}\n".format(self.gain))
            fle_ptr.write("(Ex Gain- to GPS+) = \t{}\n".format(self.ex_gps))
            fle_ptr.write("(Ey Gain- to GPS+) = \t{}\n".format(self.ey_gps))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Last time stamp for previous run = \t{}\n".format(self.last_ts))
            fle_ptr.write("First time stamp for run = \t\t{}\n\n".format(self.first_ts))
            fle_ptr.write("Lat = \t\t\t{}\n".format(self.lat))
            fle_ptr.write("Long = \t\t\t{}\n".format(self.lon))
            fle_ptr.write("Altitude = \t\t{}\n".format(self.alt))
            fle_ptr.write("Declination = \t\t{}\n".format(self.dec))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Battery (V) = \t\t{}\n".format(self.battery))

            fle_ptr.write("{}\n".format(divider))
            fle_ptr.write("Comments:\n\n{}".format(self.comments))
