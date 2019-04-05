# ************************************************************************
#  File Name: nims.py
#
#  Created By: Brady Fry (frybr)
#
#  Purpose:
# ************************************************************************

""" NIMS Data Packet Breakdown - 1 Hz
Byte 1      h'01    SOH - Start of Packet
Byte 2      h'19    Packet Length (d'25)
Byte 3              Status Byte:
            b'0     (LSB) General Alarm Bit
            b'1     X-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'2     Y-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'3     Z-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'4     X-out of range: magnetometer connot home
            b'5     Y-out of range: magnetometer connot home
            b'6     Z-out of range: magnetometer connot home
            b'7     1 Hz clock not valid for this data block
Byte 4              GPS Byte or Telluric Amplifier Gain:
            h'00    Power-on initialization prior to first GPS lock and sync
            h'C7    Power has been applied to the GPS receiver for a NIMS resync
            h'D3    Power has been applied to the GPS receiver, for an Almanac
                    download (2000 seconds)
            h'C8    High gain, both telluric channels
            h'CC    Low gain, both telluric channels
            h'D8    High gain on X, low gain on Y
            h'D9    Low gain on X, high gain on Y
Byte 5              Sequence byte (h'00 - h'FF)
Byte 6,7            Electronics unit temperature - twos compliment
Byte 8,9            Head temperature - twos compliment
Byte 10-12          Hx sample, twos compliment, MSB - LSB
Byte 13-15          Hy sample, twos compliment, MSB - LSB
Byte 16-18          Hz sample, twos compliment, MSB - LSB
Byte 19-21          Ex sample, twos compliment, MSB - LSB
Byte 22-24          Ey sample, twos compliment, MSB - LSB
Byte 25     h'04    EOH - End of Packet
"""
LEN1HZ = '19'
LEN8HZ = '83'

SOH = '01'
EOH = '04'

HCONVERSION = 0.01
ECONVERSION = 2.441412210479e-05
MAGHIGHRANGE = 100
MAGLOWRANGE = -100

LENGTHSRT = 1
LENGTHSTP = 2
STATUSSRT = 2
STATUSSTP = 3
GPSSRT = 3
GPSSTP = 4
GAINSRT = 3
GAINSTP = 4
HXSTART = 9
HXSTOP = 12
HYSTART = 12
HYSTOP = 15
HZSTART = 15
HZSTOP = 18
EXSTART = 18
EXSTOP = 21
EYSTART = 21
EYSTOP = 24

""" NIMS Data Packet Breakdown - 8 Hz
Byte 1      h'01    SOH - Start of Packet
Byte 2      h'83    Packet Length (d'131)
Byte 3              Status Byte:
            b'0     (LSB) General Alarm Bit
            b'1     X-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'2     Y-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'3     Z-ranging: The X-component has changed bins at the beginning
                    of this data block.
            b'4     X-out of range: magnetometer connot home
            b'5     Y-out of range: magnetometer connot home
            b'6     Z-out of range: magnetometer connot home
            b'7     1 Hz clock not valid for this data block
Byte 4              GPS Byte or Telluric Amplifier Gain:
            h'00    Power-on initialization prior to first GPS lock and sync
            h'C7    Power has been applied to the GPS receiver for a NIMS resync
            h'D3    Power has been applied to the GPS receiver, for an Almanac
                    download (2000 seconds)
            h'C8    High gain, both telluric channels
            h'CC    Low gain, both telluric channels
            h'D8    High gain on X, low gain on Y
            h'D9    Low gain on X, high gain on Y
Byte 5              Sequence byte (h'00 - h'FF)
Byte 6,7            Electronics unit temperature - twos compliment
Byte 8,9            Head temperature - twos compliment
Byte 10-12          Hx, sample 1, twos compliment, MSB - LSB
Byte 13-15          Hy, sample 1, twos compliment, MSB - LSB
Byte 16-18          Hz, sample 1, twos compliment, MSB - LSB
Byte 19-27          Hx, Hy, Hx, sample 2, twos compliment, MSB - LSB
Byte 28-36          Hx, Hy, Hx, sample 3, twos compliment, MSB - LSB
Byte 37-45          Hx, Hy, Hx, sample 4, twos compliment, MSB - LSB
Byte 46-54          Hx, Hy, Hx, sample 5, twos compliment, MSB - LSB
Byte 55-63          Hx, Hy, Hx, sample 6, twos compliment, MSB - LSB
Byte 64-72          Hx, Hy, Hx, sample 7, twos compliment, MSB - LSB
Byte 73-81          Hx, Hy, Hx, sample 8, twos compliment, MSB - LSB
Byte 82             Logical redundancy check (XOR of bytes 1 - 81)
Byte 83-85          Ex, sample 1, twos compliment, MSB - LSB
Byte 86-88          Ey, sample 1, twos compliment, MSB - LSB
Byte 89-94          Ex, Ey, sample 2 twos compliment, MSB - LSB
Byte 95-100         Ex, Ey, sample 3 twos compliment, MSB - LSB
Byte 101-106        Ex, Ey, sample 4 twos compliment, MSB - LSB
Byte 107-112        Ex, Ey, sample 5 twos compliment, MSB - LSB
Byte 113-118        Ex, Ey, sample 6 twos compliment, MSB - LSB
Byte 119-124        Ex, Ey, sample 7 twos compliment, MSB - LSB
Byte 125-130        Ex, Ey, sample 8 twos compliment, MSB - LSB
Byte 131    h'04    EOH - End of Packet
"""
MINERVA = 0
OWL = 1

INITIAL = 0

METAEMPTY = 0
METAPARTIAL = 1
METACOMPLETE = 2

"""GPS NMEA Sentence
The nims receive 2 data type sentences.  The first sentence is RMC,
recommended minimum data for gps.  The second sentence is GGA, Fix information.
For the header information, the date is pulled from the GPRMC sentence, and the
time, latitude, longitude, and altitude is pulled from the GPGGA sentence.

Sentence breakdown:
$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A

Where:
     RMC          Recommended Minimum sentence C
     123519       Fix taken at 12:35:19 UTC
     A            Status A=active or V=Void.
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     022.4        Speed over the ground in knots
     084.4        Track angle in degrees True
     230394       Date - 23rd of March 1994
     003.1,W      Magnetic Variation
     *6A          The checksum data, always begins with *


$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

Where:
     GGA          Global Positioning System Fix Data
     123519       Fix taken at 12:35:19 UTC
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     1            Fix quality: 0 = invalid
                               1 = GPS fix (SPS)
                               2 = DGPS fix
                               3 = PPS fix
                               4 = Real Time Kinematic
                               5 = Float RTK
                               6 = estimated (dead reckoning) (2.3 feature)
                               7 = Manual input mode
                               8 = Simulation mode
     08           Number of satellites being tracked
     0.9          Horizontal dilution of position
     545.4,M      Altitude, Meters, above mean sea level
     46.9,M       Height of geoid (mean sea level) above WGS84
                      ellipsoid
     (empty field) time in seconds since last DGPS update
     (empty field) DGPS station ID number
     *47          the checksum data, always begins with *
"""
# GPS Sentence position
GPSDATE = 9
GPSTIME = 1
GPSLATI = 2
GPSLATD = 3
GPSLONG = 4
GPSLOND = 5
GPSALTI = 9
GPSDECL = 10
GPSDECD = 11

# GPS Metadata String position
GPSSTRINGDATE = 0
GPSSTRINGTIME = 1
GPSSTRINGLATI = 2
GPSSTRINGLATD = 3
GPSSTRINGLONG = 4
GPSSTRINGLOND = 5
GPSSTRINGALTI = 6

# GPS States:
GPSINITIAL = '00'
GPSAQLOCK = 'C7'
GPSRECEIVING = 'C9'
GPSRECEIVED = 'CA'
GPSALMANAC = 'D3'

MAGSLEWING = '00'
MAGREADY = '81'
MAGERROR = 'FF'

EXLEYL = 'CC'
EXHEYL = 'D8'
EXLEYH = 'D9'
EXHEYH = 'C8'
EXUEYU = 'FF'

# Owl board states
SENDNIMS = '03'
SENDUSD = '02'

# NIMS Data Packet Breakdown - 1 Hz
# NIMS Commands
SHORTCYCLE = '04'
ALMANAC = '06'
NIMSLEDS = '74'
MAGLIGHTON = '1B'
MAGLIGHTOFF = '1C'
REBOOTMAG = '52'
GAINXLYL = '59'
GAINXLYH = '02'
GAINXHYL = '01'
GAINXHYH = '5A'
FLENAME = '14'
HEADER = '15'
RECORD = '19'
ENDREC = '1A'
