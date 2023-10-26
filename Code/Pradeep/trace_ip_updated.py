from scapy.all import traceroute, IP
import os

def trace_and_log(ip, directory):
    trace_file = open(f"{directory}/trace_results.txt", "a")
    trace_file.write(f"Trace Route: {ip}\n")
    print(f"Trace Route: {ip}")
    
    answers, _ = traceroute(ip, maxttl=100, verbose=0, timeout=3)
    
    for entry in answers.res:
        if entry[1].type == 3:
            status = f"Destination unreachable"
        else:
            status = f"{entry[1].ttl} hops away: {entry[1].src}"
        
        trace_file.write(f"{status} for {ip}\n")
        print(status)
    
    trace_file.write("-----------------------------------------------\n")
    print("-----------------------------------------------")
    trace_file.close()

def trace_ips(prefix, output_directory, start_octet, end_octet, start_fourth_octet, end_fourth_octet):
    active_ips_file = open(f"{output_directory}/active_ip_sets.txt", "a")
    
    for i in range(start_octet, end_octet):
        if i > 255:
            break
        for j in range(start_fourth_octet, end_fourth_octet):
            if j > 255:
                break
            ip_address = f"{prefix}.{i}.{j}"
            trace_and_log(ip_address, output_directory)
            active_ips_file.write(f"Routes for {ip_address}:\n")
    
    active_ips_file.close()

if __name__ == "__main__":
    prefix = "138.238"
    output_directory = f"Data/{prefix}"
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    trace_ips(prefix, output_directory, start_octet=251, end_octet=256, start_fourth_octet=0, end_fourth_octet=256)
