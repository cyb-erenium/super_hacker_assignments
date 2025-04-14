def check_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    else:
        return True
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False
        else:
            return True
        if octet[0] == '0' and len(octet) > 1:
            return False
        else:
            return True
ip = input("Enter an IP address: ")
if check_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")        
            