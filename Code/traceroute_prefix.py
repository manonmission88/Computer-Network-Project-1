from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

'''
This python script:
creates -> trace_results.txt and active_ip_sets.txt and write in those files
trace_results.txt contains traceroute to the given ip address: from x.x.0.0 to x.x.255.255
active_ip_sets.txt contains the sets in each line where each set is a traceroute for the given ip address
'''

def trace_helper(ipaddr, directory, active_ip_sets):
    f = open(f"{directory}/trace_results.txt", "a")
    f.write(f"Trace Route: {ipaddr} \n")
    print(f"Trace Route: {ipaddr}")
    for ttl in range(1, 100):
        pkt = IP(dst=ipaddr, ttl=ttl) / UDP(dport=33434)
        reply = sr1(pkt, verbose=0, timeout=3)
        if reply is None:
            f.write(f"Timeout at {ttl} hops away for {ipaddr}\n")
            print(f"Timeout at {ttl} hops away for {ipaddr}")
            break
        elif reply.type == 3:
            f.write(f"Destiation unreachable at {ttl} hops away for {ipaddr}\n")
            print(f"Destiation unreachable at {ttl} hops away for {ipaddr}\n")
            break
        else:
            f.write(f"{ttl} hops away: {reply.src}\n")
            print(f"{ttl} hops away: {reply.src}")
            active_ip_sets.add(str(reply.src))
    f.write("-----------------------------------------------\n")
    print("-----------------------------------------------")
    f.close()
    return active_ip_sets

def trace(prefix, directory, active_ips_set, ts, te, fs, fe):
    f = open(f"{directory}/active_ip_sets.txt", "a")
    for i in range(ts, te):
        if i > 255:
            break
        for j in range(fs, fe):
            if j > 255:
                break
            ipaddr = f"{prefix}.{i}.{j}"
            trace_helper_result = trace_helper(ipaddr, directory, active_ips_set)
            f.write(f"routes: {trace_helper_result}\n")
            #print(f"routes: {trace_helper_result}\n")
    f.close()
    return trace_helper_result

if __name__ == "__main__":
    # change the values here - from where to where you want to run - 3rd octet and 4th octet
    ts = 251
    te = 256
    fs = 0
    fe = 256
    # change the prefix here - 1st octet and 2nd octet which you want to fix
    prefix = "138.238"
    active_ips_set = set()
    # change directory here - where you want to save the files
    directory = f"Data/{prefix}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    trace_results = trace(prefix, directory, active_ips_set, ts, te, fs, fe)