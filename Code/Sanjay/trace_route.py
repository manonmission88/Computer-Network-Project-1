from scapy.all import *
#10.78.96.1, 10.199.4.249
unique_ip_addresses = set()
def trace_route(ipaddr):
    print('ipaddr is',ipaddr)
    for i in range(1, 28):
        pkt = IP(dst=ipaddr, ttl=i) / UDP(dport=33434)
        try:
            # Send the packet and get a reply
            reply = sr1(pkt, verbose=0, timeout=3)
            if reply is None:
                # No reply, consider increasing the timeout if this happens too frequently
                with open("location_ilab.txt","a") as f:
                    f.write(f"No reply, Time out at {i} hops away.\n")
                print(f"Time out at {i} hops away.")
                break
            elif reply.type == 3:
                # We've reached our destination
                with open("location_ilab.txt","a") as f:
                    f.write(f"Destination reach at {i} hops away.\n")
                print("Done!", reply.src)
                break

            else:
                # We're in the middle somewhere
                with open("location_ilab.txt","a") as f: # change the txt files accordingly 
                    f.write(f"{i} hops away: {reply.src}\n ")
                print(f"{i} hops away: ", reply.src)
                unique_ip_addresses.add(reply.src)

        except Exception as e:
            with open("location_ilab.txt","a") as f:
                    f.write(f"Error at {i} hops: {e}\n")
                    
            print(f"Error at {i} hops: {e}")
# trace_route(ipaddr)

def main():
    for i in range(13,256):
        for j in range(1,256): # can skip by 16 
            with open("location_ilab.txt","a") as f:
                    f.write(f"For traceroute: 10.199.{i}.{j}\n")
            trace_route(f"10.199.{i}.{j}")  
            with open("location_set.txt","a") as f:
                    f.write(f"Unique ipaddr: {unique_ip_addresses}\n")
            # change ipaddr prefix accordingly  
main()
            



