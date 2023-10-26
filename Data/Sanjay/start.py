from scapy.all import *
import random

addresse =  "8.8.4.4"
ipaddr = addresse

for ttl in range(1, 90):
    pkt = IP(dst=ipaddr, ttl=ttl) / UDP(dport=33434)
    reply = sr1(pkt, verbose=0, timeout=3)
    if reply is None:
        print(f"Hop {ttl} dropped")
    elif reply.type == 3:
        print("Done!", reply.src)
        break
    else:
        print(f"Hop {ttl} away: ", reply.src)
