"""Metadata class for NIMS data files."""

import time

from .configs import APP_NAME, APP_VERSION


class Metadata:
    """Metadata class for NIMS data files."""

    def __init__(
        self,
        site_name: str = "NGFLAB",
        state_province: str = "Oregon",
        country: str = "USA",
        run_id: str = "lab001",
        operator: str = "Nikola Tesla",
        nims_id: str = "2612-01",
        mag_id: str = "2612-01",
        ns_length: float = 100.0,
        ns_azimuth: float = 0.0,
        ew_length: float = 100.0,
        ew_azimuth: float = 90.0,
        electrode_north_id: str = "1",
        electrode_south_id: str = "2",
        electrode_east_id: str = "3",
        electrode_west_id: str = "4",
        ground: str = "Cpr",
        survey_layout: str = "",
        gps_timestamp: str = "",
        computer_timestamp: str = "",
        comments: str = "Default comments, needs updating.",
    ):
        self.file_header: str = ""
        self.site_name = site_name
        self.state_province = state_province
        self.country = country
        self.run_id = run_id
        self.operator = operator
        self.nims_id = nims_id
        self.mag_id = mag_id
        self.ns_length = ns_length
        self.ns_azimuth = ns_azimuth
        self.ew_length = ew_length
        self.ew_azimuth = ew_azimuth
        self.survey_layout = survey_layout
        self.electrode_north_id = electrode_north_id
        self.electrode_south_id = electrode_south_id
        self.electrode_east_id = electrode_east_id
        self.electrode_west_id = electrode_west_id
        self.ground = ground
        self.gps_timestamp = gps_timestamp
        self.computer_timestamp = computer_timestamp
        self.comments = comments
        self.file_header = ""

    def set_head_comp_time(self) -> None:
        """Set the computer time."""
        # get the current computer time
        current_time = time.localtime()
        # parse the time zone of the computer time
        timezone = time.tzname[current_time[8]]
        # format the computer time of 'Start Run' clicked and time zone
        self.computer_timestamp = time.strftime("%Y/%m/%d %H:%M:%S") + " " + timezone

    def make_header(self) -> None:
        """Make the header for the NIMS data file."""
        header_len = 2048
        header = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        header += ">>>user field>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        header += "SITE NAME: %s\n" % self.site_name
        header += "STATE/PROVINCE: %s\n" % self.state_province
        header += "COUNTRY: %s\n" % self.country
        header += ">>> The following code in double quotes is REQUIRED to start the NIMS <<\n"
        header += ">>> The next 3 lines contain values required for processing <<<<<<<<<<<<\n"
        header += ">>> The lines after that are optional <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        header += f'"{self.run_id}"\t<-- 2 CHAR EXPERIMENT CODE + 3 CHAR SITE CODE + RUN LETTER\n'
        header += "%s; %s\t<-- SYSTEM BOX I.D.; MAG HEAD ID (if different)\n" % (
            self.nims_id,
            self.mag_id,
        )
        header += "%i  %i\t<-- N-S Ex WIRE LENGTH (m); HEADING (deg E mag N)\n" % (
            self.ns_length,
            self.ns_azimuth,
        )
        header += "%i  %i\t<-- E-W Ex WIRE LENGTH (m); HEADING (deg E mag N)\n" % (
            self.ew_length,
            self.ew_azimuth,
        )
        header += "%s\t<-- N ELECTRODE ID\n" % self.electrode_north_id
        header += "%s\t<-- E ELECTRODE ID\n" % self.electrode_east_id
        header += "%s\t<-- S ELECTRODE ID\n" % self.electrode_south_id
        header += "%s\t<-- W ELECTRODE ID\n" % self.electrode_west_id
        header += "%s\t<-- Ground ELECTRODE INFO\n" % self.ground
        header += "GPS INFO: %s\n" % self.gps_timestamp
        header += "COMPUTER TIME STAMP: %s\n" % self.computer_timestamp
        header += f"OPERATOR: {self.operator}\n"
        header += f"SOFTWARE: {APP_NAME} v{APP_VERSION}\n"
        header += f"COMMENTS: {self.comments}"

        self.file_header = header

        while len(self.file_header) < header_len - 1:
            self.file_header += " "
        self.file_header += "\n"

        print(f"{self.file_header}")
