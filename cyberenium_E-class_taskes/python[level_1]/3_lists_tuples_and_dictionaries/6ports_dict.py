ports_dict = {
    80: "http",
    443: "https",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    110: "pop3",
    143: "imap",
    3306: "mysql",
    5432: "postgresql",
    6379: "redis",
    27017: "mongodb"
    }
port = int(input("Enter a port number: "))
print(ports_dict[port])