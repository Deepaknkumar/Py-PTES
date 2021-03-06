import os
import socket
import struct
import uuid
import requests
if os.name != "nt":
    import fcntl



def get_ip(inter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_addr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,struct.pack('256s',inter[:15])))[20:24];
    return ip_addr;


def get_mac_address(inter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s',inter[:15]));
    mac_address = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
    return mac_address;


def get_localhost_details(interfaces_eth, interfaces_wlan):
    hostdata = "None";
    hostname = "None";
    windows_ip = "None";
    eth_ip = "None";
    wlan_ip = "None";
    host_fqdn = "None";
    eth_mac = "None";
    wlan_mac = "None";
    windows_mac = "None";
    hostname = socket.gethostbyname(socket.gethostname());
    if hostname.startswith("127.") and os.name != "nt":
        hostdata = socket.gethostbyaddr(socket.gethostname());
        hostname = str(hostdata[1]).strip('[]')
        host_fqdn = socket.getfqdn()
        for interface in interfaces_eth:
            try:
                eth_ip = get_ip(interface)
                if not "None" in eth_ip:
                    eth_mac = get_mac_address(interface)
                    break
            except IOError:
                pass

        for interface in interfaces_wlan:
            try:
                wlan_ip = get_ip(interface)
                if not "None" in wlan_ip:
                    wlan_mac = get_mac_address(interface);
                    break;
            except IOError:
                pass
    else:
        windows_ip = socket.gethostbyname(socket.gethostname());
        windows_mac = hex(uuid.getnode()).lstrip('0x');
        windows_mac = ':'.join(pos1+pos2 for pos1,pos2 in zip(windows_mac[::2],windows_mac[1::2]))
        hostdata = socket.gethostbyaddr(socket.gethostname());
        hostname = str(hostdata[1]).strip("[]\'")
        host_fqdn = socket.getfqdn();
    return hostdata, hostname, windows_ip, eth_ip, wlan_ip, host_fqdn, eth_mac, wlan_mac, windows_mac


def get_public_ip(request_target):
    public_ip_address = "None";
    try:
        public_ip_address = requests.get(request_target).text;
    except requests.HTTPError as error:
        print("There was an error trying to get your Public IP : %s" % (error));
    return public_ip_address;
