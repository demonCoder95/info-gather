# Information Gatherer

This is a basic application that can gather information from remote hosts.
The information it can gather includes:

1. Kernel log from ``/var/log/messages``
2. List of all installed packages and their versions as reported by ``yum``
3. Kernel version of the remote host as reported by ``uname -r``
4. Detailed hardware information as reported by ``lshw``
5. Status of currently running processes as reported by ``ps -aux``

It generates log files per information element and then bundles them together
into a ZIP archive. Each remote host has its own archive.

The application accepts a configuration file which includes information about
the remote hosts as well as indicators as to what information to collect.

A sample configuration file can look as follows:

```ini
[DEFAULT]
info_type=var_log,ps_aux,packages,hw_details,kernel_version
[192.168.10.10]
username=root
password=s0m3p4ssw0rd
[192.168.10.16]
username=root
password=s0m3p4ssw0rd
```

Each host has its own section with the username and password specified. Since
a typical use case of this application is in off-site locations, passwords can
be safely written in a configuration file and then deleted upon conclusion
of the information gathering activity.

## How to Use the Program

1. Install the dependencies of the application.

```bash
    pip3 install -r requirements.txt
```

2. Prepare a configuration file as suggested, say named ``config-file.ini``.
3. Run the application.

```bash
    python3 main.py config-file.ini
```
