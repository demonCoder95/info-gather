import configparser
import common.info_gatherer
import argparse

program_description = """
Information Gatherer

This program gathers information from remote hosts as provided in the
configuration file. It can gather basic information like:
- The kernel log from /var/log/messages
- The information of currently running processes from 'ps -aux'
- Detailed hardware information of the host from 'lshw'
- List of all installed packages with their version numbers
- Kernel version of the host
It puts all the files of the output in respective ".log" files and bundles
all the information of a host in a "$HOST.zip" file.
"""
arg_parser = argparse.ArgumentParser(description=program_description)
arg_parser.add_argument('config', action='store', nargs=1,
    help='The configuration file for the program')
args = arg_parser.parse_args()
config_file_name = args.config

# Initiate the configuration parser
config = configparser.ConfigParser()

print("[DEBUG] Reading the configuration file {}".format(config_file_name))
# Read in the configuration file
config.read(config_file_name)
print("[DEBUG] Config file reading successful")

hosts = config.sections()

msg = "[DEBUG] Working on hosts:\n"
for each_host in hosts:
    msg += each_host + "\n"
print(msg)

operations = config['DEFAULT']['info_type'].split(",")
msg = "[DEBUG] Will gather the following information:\n"
for each_op in operations:
    msg += each_op + "\n"
print(msg)

info_collector = common.info_gatherer.InfoGatherer(config, operations)
info_collector.gather_info()

