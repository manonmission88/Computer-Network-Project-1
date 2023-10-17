from scapy.all import *

ipaddr = "10.199.0.0"  # private ip # possible ips to ping  # 138.238.3.33  # 10.26.96.1 # 66.44.94.195
def trace_route(ipaddr):
    print('ipaddr is',ipaddr)
    for i in range(1, 28):
        pkt = IP(dst=ipaddr, ttl=i) / UDP(dport=33434)
        try:
            # Send the packet and get a reply
            reply = sr1(pkt, verbose=0, timeout=3)
            if reply is None:
                # No reply, consider increasing the timeout if this happens too frequently
                with open("sanjay_location.txt","a") as f:
                    f.write(f"No reply, Time out at {i} hops away.\n")
                print(f"Time out at {i} hops away.")
                break
            elif reply.type == 3:
                # We've reached our destination
                with open("sanjay_location.txt","a") as f:
                    f.write(f"Destination reach, Time out at {i} hops away.\n")
                print("Done!", reply.src)
                break

            else:
                # We're in the middle somewhere
                with open("sanjay_location.txt","a") as f: # change the txt files accordingly 
                    f.write(f"{i} hops away: {reply.src}\n ")
                print(f"{i} hops away: ", reply.src)
        except Exception as e:
            with open("sanjay_location.txt","a") as f:
                    f.write(f"Error at {i} hops: {e}\n")
                    
            print(f"Error at {i} hops: {e}")
# trace_route(ipaddr)

def main():
    for i in range(1,256):
        for j in range(1,256): # can skip by 16 
            with open("sanjay_location.txt","a") as f:
                    f.write(f"For traceroute: 10.199.{i}.{j}")
            trace_route(f"10.199.{i}.{j}")      # change ipaddr prefix accordingly   
main()
            



