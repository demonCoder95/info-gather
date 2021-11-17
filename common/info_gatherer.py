# ############################################################################
# This script will get all the statistics information from sniffer servers
# as a means for performing troubleshooting.
# Live monitoring is not an option in this case, so this script is essential
#
# Author: Noor
# Date: August 10, 2021
#
# ############################################################################
import common.ssh_handler

# The information to be gathered is below

class InfoGatherer():
    def __init__(self, config, operations):
        # the list of hosts to operate on
        self.config = config
        # the operation to perform on each host
        self.operations = operations

    # Gather information on all the hosts through handlers and print it on the screen
    def gather_info(self):

        # Process all the hosts assigned to this gatherer
        for each_host in self.config.sections():

            # Create a handler for this host
            host_handler = common.ssh_handler.SSHHandler(each_host,
                self.config[each_host]['username'],
                self.config[each_host]['password'])

            # Perform all the info gathering operations for this host
            for each_operation in self.operations:

                # for now, print information on the screen
                host_handler.run_command(each_operation)