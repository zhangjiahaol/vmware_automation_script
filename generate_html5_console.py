#!/usr/bin/env python3
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from binascii import hexlify
from getpass import getpass
import ssl
import atexit
import webbrowser
import argparse
import time

def option():
    parser = argparse.ArgumentParser(prog='vmware_connect_web_console.py',
                                     add_help=True,
                                     description='Tool to open VMware web console.')

    parser.add_argument('--host', '-vc',
                        type=str, required=True,
                        help='Specify FQDN or IP address for vCenter.')
    parser.add_argument('--username', '-u',
                        type=str, default='administrator@vsphere.local',
                        help='Specify vCenter username.')
    parser.add_argument('--password', '-p',
                        type=str,
                        help='Specify vCenter user password.')
    parser.add_argument('--vm-name', '-v',
                        type=str, required=True,
                        help='Open web console Specify target vm name.')
    args = parser.parse_args()

    if (not (args.password)):
        args.password = getpass()

    return args

def main():
    # Options.
    args = option()

    # SSL warning measures.
    context = None
    if hasattr(ssl, '_create_unverified_context'):
        context = ssl._create_unverified_context()

    # Server Connect.
    si = SmartConnect(host=args.host,
                      user=args.username,
                      pwd=args.password,
                      sslContext=context)
    atexit.register(Disconnect, si)

    # Get content and obj list.
    content = si.content
    obj_list = content.viewManager.CreateContainerView(content.rootFolder,
                                                       [vim.VirtualMachine],
                                                       True)

    # Get VM Object.
    vm_obj = None
    for obj in obj_list.view:
        if(obj.name == args.vm_name):
            vm_obj = obj

    if(vm_obj):
        # Create Session Ticket.
        session = content.sessionManager.AcquireCloneTicket()

        # Create ServerGuid.
        server_guid = content.about.instanceUuid

        # Get fingerprint.
        cert = ssl.get_server_certificate((args.host, 443))
        cert_deserialize = x509.load_pem_x509_certificate(cert.encode(), default_backend())
        finger_print = hexlify(cert_deserialize.fingerprint(hashes.SHA1())).decode('utf-8')
        finger_print_format = ":".join([finger_print[i: i+2] for i in range(0, len(finger_print), 2)])

        # Create Console URL.
        web_console_url = 'https://' + args.host + ':' + '9443' + '/vsphere-client/webconsole.html?' + 'vmId=' + vm_obj._moId \
                          + '&vmName=' + vm_obj.name + '&serverGuid=' + server_guid + '&host=' + args.host + ':443' \
                          + '&sessionTicket=' + session + '&thumbprint=' + finger_print_format.upper()

        # Open URL.
        print(web_console_url)
        time.sleep(60)
        # webbrowser.open(web_console_url)
    else:
        print("%s not found." % args.vm_name)

if __name__ == "__main__":
    main()
