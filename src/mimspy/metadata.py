"""Metadata class for NIMS data files."""

import time

from .configs import APP_NAME, APP_VERSION


class Metadata:
    """Metadata class for NIMS data files."""

    def __init__(
        self,
        sitename="NGFLAB",
        stateprov="Oregon",
        country="USA",
        runid="lab001",
        operator="Nikola Tesla",
        nimsid="2612-01",
        magid="2612-01",
        nsdipolelen=100,
        nsdipoleazi=0,
        ewdipolelen=100,
        ewdipoleazi=90,
        ndipoleid="1",
        sdipoleid="2",
        edipoleid="3",
        wdipoleid="4",
        gndelectrode="Cpr",
        survey_layout="X",
        gpstimestamp="",
        comptimestamp="",
        comments="Default comments, needs updating.",
    ):
        self.file_header: str = ""
        self.sitename = sitename
        self.stateprov = stateprov
        self.country = country
        self.runid = runid
        self.operator = operator
        self.nimsid = nimsid
        self.magid = magid
        self.nsdipolelen = nsdipolelen
        self.nsdipoleazi = nsdipoleazi
        self.ewdipolelen = ewdipolelen
        self.ewdipoleazi = ewdipoleazi
        self.survey_layout = survey_layout
        self.ndipoleid = ndipoleid
        self.sdipoleid = sdipoleid
        self.edipoleid = edipoleid
        self.wdipoleid = wdipoleid
        self.gndelectrode = gndelectrode
        self.gpstimestamp = gpstimestamp
        self.comptimestamp = comptimestamp
        self.comments = comments
        self.fileheader = ""

    def set_head_comp_time(self):
        """Set the computer time."""
        # get the current computer time
        curtime = time.localtime()
        # parse the time zone of the computer time
        tzone = time.tzname[curtime[8]]
        # format the computer time of 'Start Run' clicked and time zone
        self.comptimestamp = time.strftime("%Y/%m/%d %H:%M:%S") + " " + tzone

    def make_header(self):
        """Make the header for the NIMS data file."""
        header_len = 2048
        header = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        header += ">>>user field>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        header += "SITE NAME: %s\n" % self.sitename
        header += "STATE/PROVINCE: %s\n" % self.stateprov
        header += "COUNTRY: %s\n" % self.country
        header += ">>> The following code in double quotes is REQUIRED to start the NIMS <<\n"
        header += ">>> The next 3 lines contain values required for processing <<<<<<<<<<<<\n"
        header += ">>> The lines after that are optional <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        header += f'"{self.runid}"\t<-- 2 CHAR EXPERIMENT CODE + 3 CHAR SITE CODE + RUN LETTER\n'
        header += "%s; %s\t<-- SYSTEM BOX I.D.; MAG HEAD ID (if different)\n" % (
            self.nimsid,
            self.magid,
        )
        header += "%i  %i\t<-- N-S Ex WIRE LENGTH (m); HEADING (deg E mag N)\n" % (
            self.nsdipolelen,
            self.nsdipoleazi,
        )
        header += "%i  %i\t<-- E-W Ex WIRE LENGTH (m); HEADING (deg E mag N)\n" % (
            self.ewdipolelen,
            self.ewdipoleazi,
        )
        header += "{}\t<-- Survey Layout\n".format(self.survey_layout)
        header += "%s\t<-- N ELECTRODE ID\n" % self.ndipoleid
        header += "%s\t<-- E ELECTRODE ID\n" % self.edipoleid
        header += "%s\t<-- S ELECTRODE ID\n" % self.sdipoleid
        header += "%s\t<-- W ELECTRODE ID\n" % self.wdipoleid
        header += "%s\t<-- Ground ELECTRODE INFO\n" % self.gndelectrode
        header += "GPS INFO: %s\n" % self.gpstimestamp
        header += "COMPUTER TIME STAMP: %s\n" % self.comptimestamp
        header += f"OPERATOR: {self.operator}\n"
        header += f"SOFTWARE: {APP_NAME} v{APP_VERSION}\n"
        header += f"COMMENTS: {self.comments}"

        self.file_header = header

        while len(self.file_header) < header_len - 1:
            self.file_header += " "
        self.file_header += "\n"

        print(f"{self.file_header}")
