import netifaces

# Returns all the interfaces for the system
def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces


def get_gateways():
    gateway_dict = {};
    gws = netifaces.gateways()
    for gw in gws:
        try:
            gateway_iface = gws[gw][netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list = [gateway_ip, iface]
            gateway_dict[gw] = gw_list
        except:
            pass
    return gateway_dict
