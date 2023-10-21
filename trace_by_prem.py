from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

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
    '''
    res = set()
    prefix = input("Enter subnet prefix: ")
    ts = int(input("Enter 3rd Octet starting: "))
    te = int(input("Enter 3rd Octet ending: "))
    fs = int(input("Enter 4rd Octet starting: "))
    fe = int(input("Enter 4rd Octet ending: "))
    '''

    ts = 110
    te = 111
    fs = 0
    fe = 256
    prefix = "10.26"
    active_ips_set = set()

    #seg = f"{ts}"
    directory = f"Results/{prefix}/{ts}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    trace_results = trace(prefix, directory, active_ips_set, ts, te, fs, fe)