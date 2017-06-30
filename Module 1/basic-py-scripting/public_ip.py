import requests

def get_public_ip(request_target):
    try:
        public_ip_address = requests.get(request_target).text;
    except requests.HTTPError as error:
        print("There was an error trying to get your Public IP: %s" % (error));
        public_ip_address = "None";
    return public_ip_address;

#public_ip = "None";
target_url = "http://ip.42.pl/raw";
public_ip = get_public_ip(target_url);

if not("None" in public_ip):
    print("Your Public IP Address is %s" % (str(public_ip)));
else:
    print("Your public IP Address was not found!");