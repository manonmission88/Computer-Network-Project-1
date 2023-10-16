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
                with open("lkd.txt","a") as f:
                    f.append(f"Time out at {i} hops away.")
                print(f"Time out at {i} hops away.")
                break
            elif reply.type == 3:
                # We've reached our destination
                with open("lkd.txt","a") as f:
                    f.append(f"Time out at {i} hops away.")
                print("Done!", reply.src)
                break

            else:
                # We're in the middle somewhere
                with open("lkd.txt","a") as f: # change the txt files accordingly 
                    f.append(f"{i} hops away: {reply.src} ")
                print(f"{i} hops away: ", reply.src)
        except Exception as e:
            with open("lkd.txt","a") as f:
                    f.append(f"Error at {i} hops: {e}")
                    
            print(f"Error at {i} hops: {e}")
# trace_route(ipaddr)

def main():
    for i in range(1,256):
        for j in range(1,256): # can skip by 16 
            trace_route(f"10.199.{i}.{j}")      # change ipaddr prefix accordingly   
main()
            



