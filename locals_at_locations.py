from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os



def locals_at_location(ipaddr, locals, location):

    f = open(f"{directory}/locals_at_locations.txt", "a")
    f.write(f"Local Networks (prefix: 10) at {location} are:\n")

    traceroute_result, _ = traceroute(target=ipaddr, maxttl=100)

    for snd, rcv in traceroute_result:
        ipaddr = rcv.src
        if str(ipaddr)[0:2] == "10":
            f.write(f"{ipaddr}\n")
            locals.add(ipaddr)
    f.write("----------------\n")
    f.close()
    return locals






if __name__ == "__main__":

    ipaddr = "8.8.8.8"
    location = input("Enter your Location: ")
    locals = set()
    directory = f"Results"
    if not os.path.exists(directory):
        os.makedirs(directory)

    local_at_locations_result = locals_at_location(ipaddr, locals, location)

    
    
