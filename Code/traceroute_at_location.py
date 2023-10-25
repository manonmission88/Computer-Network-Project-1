from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

'''
This python script:
Inputs:
Location

creates -> traceroute_at_location.txt and writes in it
raceroute_at_location.txt contains traceroute to the given ip address
'''

def traceroute_at_location(ipaddr, location, results):
    f = open(f"{directory}/traceroute_at_location.txt", "a")
    f.write(f"Traceroute to {ipaddr} at {location}:\n")
    traceroute_result, _ = traceroute(target=ipaddr, maxttl=100)
    for snd, rcv in traceroute_result:
        ipaddr = rcv.src
        f.write(f"{ipaddr}\n")
        results.add(f"{ipaddr}")
    f.write(f"{results}\n")
    f.write("----------------\n")
    f.close()
    return results

if __name__ == "__main__":
    # change ip address here - up to which you want to traceroute the packet in the network
    ipaddr = "8.8.8.8"
    location = input("Enter your Location: ")
    results = set()
    # change directory here - where you want to save the files
    directory = f"Location/1"
    if not os.path.exists(directory):
        os.makedirs(directory)
    traceroute_at_location_results = traceroute_at_location(ipaddr, location, results)

    
    
