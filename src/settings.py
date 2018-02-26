# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:02:00 2018

@author: Misha
"""

# python 2-proofing
import sys

if sys.version_info[0] == 2:
    import ConfigParser as configparser
elif sys.version_info[0] == 3:
    import configparser

EMERGENCY_DEFAULT = """
[Speedtester]
rec_file = speed_record.ilog
location = Wherever
freq = 0.5
verbosity = 3
force_server = None

[Analytics]
analyze_file = None
analytics_rec_file = report.txt
standards_enable = False
standard_ping = 0.0
standard_down = 0.0
standard_up = 0.0

[CSV]
csv_input_file = None
csv_output_file = Internet_speed_record.csv
csv_clear_infile = False

[Upload]
url = mcv156.163.und.nodak.edu
port = 11356
"""

try:
    f = open('config.ini')
    f.close()
except IOError:
    with open('config.ini', 'w') as configfile:
        configfile.write(EMERGENCY_DEFAULT)

parser = configparser.ConfigParser()
parser.read("config.ini")

REC_FILE = parser.get('Speedtester', 'rec_file')
LOCATION = parser.get('Speedtester', 'location')
FREQ = float(parser.get('Speedtester', 'freq'))
VERBOSITY = int(parser.get('Speedtester', 'verbosity'))
server = parser.get('Speedtester', 'force_server')
FORCE_SERVER = None if server == 'None' else server

ANALYZE_FILE = parser.get('Analytics', 'analyze_file')
ANALYTICS_REC_FILE = parser.get('Analytics', 'analytics_rec_file')
STANDARDS_ENABLE = parser.get('Analytics', 'standards_enable') in ['true', '1', 
                         't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
STANDARD_PING = float(parser.get('Analytics', 'standard_ping') or 0)
STANDARD_DOWN = float(parser.get('Analytics', 'standard_down') or 0)
STANDARD_UP = float(parser.get('Analytics', 'standard_up') or 0)

CSV_INPUT_FILE = parser.get('CSV', 'csv_input_file')
CSV_OUTPUT_FILE = parser.get('CSV', 'csv_output_file')
CSV_CLEAR_INFILE = parser.get('CSV', 'csv_clear_infile')

UPLOAD_URL = parser.get('Upload', 'url')
UPLOAD_PORT = int(parser.get('Upload', 'port'))