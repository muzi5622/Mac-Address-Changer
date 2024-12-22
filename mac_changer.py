#!/usr/bin/env python3

import subprocess as subpro
import optparse as op   #it is used to get arguments form the user
import re


def get_current_mac(options,new_mac):
    ifconfig_result = subpro.check_output(["ifconfig",options]).decode("utf-8")

    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
                           ifconfig_result)  # rule for searching mac address in the output of the ifconfig
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read MAc Address")


def get_arguments():
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter the interface name")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac")
    (options , arguments ) = parser.parse_args()

    if not options.interface:
        #code for the error if the user did not put the value of interface
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        #code for the error if the user did not put the value of interface
        parser.error("[-] Please specify an new mac, use --help for more info")
    return options


def change_mac(option , new_mac):
    print(f"[#] Changing Mac Address for {option} to {new_mac}")

    subpro.call(["ifconfig", option, "down"])
    subpro.call(["ifconfig", option, "hw", "ether", new_mac])
    subpro.call(["ifconfig", option, "up"])

def mac_address_cheacker(interface,old_mac, new_changed_mac):
    if old_mac != new_changed_mac:
        print(f"[+] The Mac Address of {interface} from {old_mac} to {new_changed_mac} Changed!")
    else:
        print(f"[-] The Mac Address of {interface} does not changed!")


# option = options.interface
# new_mac = options.new_mac

options = get_arguments()
old_mac = get_current_mac(options.interface,options.new_mac)
print("OLD MAC:",old_mac)
change_mac(options.interface,options.new_mac)
new_changed_mac = get_current_mac(options.interface,options.new_mac)
mac_address_cheacker(options.interface,old_mac,new_changed_mac)
