from paramiko import SSHClient
from zipfile import ZipFile
from os import system

# This class represents basic functionality of performing SSH operations on a remote host
# Each handler corresponds to one host
# This is so that in future the functionality can be extended to invoke multiple handlers
# in parallel that will gather information from individual host
class SSHHandler():
    def __init__(self, host, uname, pwd):
        self.host = host

        # Initialize the SSH connection
        self.ssh_client = SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.connect(host, username=uname, password=pwd)

        # Initialize the ZIP archive for storing the information
        self.zip_file = ZipFile(self.host + ".zip", "w")

    def __del__(self):
        # Close the SSH client when exiting
        self.ssh_client.close()
        # Cleanup all the temporary .log files
        system("rm *.log")

    # This method runs a command specified by 'cmd_str' on a remote host.
    def run_command(self, cmd_str):
        cmd = ""
        if cmd_str == "var_log":
            cmd = self._get_var_log()
        elif cmd_str == "ps_aux":
            cmd = self._get_ps_aux()
        elif cmd_str == "packages":
            cmd = self._get_packages()
        elif cmd_str == "hw_details":
            cmd = self._get_hardware_details()
        elif cmd_str == "kernel_version":
            cmd = self._get_kernel_version()

        print(f'[DEBUG] Running command {cmd} on host {self.host}')
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd)

        # store the information in a temp file
        with open(cmd_str+".log", 'w') as file:
            file.write(stdout.read().decode("utf8"))
        
        print(f'Return Code: {stdout.channel.recv_exit_status()}')


        # free up the file objects when done
        stdin.close()
        stdout.close()
        stderr.close()

        # Add the command output file to the zip archive
        self.zip_file.write(cmd_str+".log")


    # Functions to generate command strings for each operation that is to be
    # performed on a remote host
    def _get_var_log(self):
        return "cat /var/log/messages"

    def _get_ps_aux(self):
        return "ps aux"

    def _get_packages(self):
        return "yum list installed"

    def _get_hardware_details(self):
        return "lshw"

    def _get_kernel_version(self):
        return "uname -r"