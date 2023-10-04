from scapy.all import *

ipaddr = "10.0.0.0"  # Example target from the university's public IP block

def trace_route():
    
    for i in range(1, 28):
        pkt = IP(dst=ipaddr, ttl=i) / UDP(dport=33434)
        try:
            # Send the packet and get a reply
            reply = sr1(pkt, verbose=0, timeout=1)
            
            if reply is None:
                # No reply, consider increasing the timeout if this happens too frequently
                print(f"Time out at {i} hops away.")
                break
            
            elif reply.type == 3:
                # We've reached our destination
                print("Done!", reply.src)
                break

            else:
                # We're in the middle somewhere
                print(f"{i} hops away: ", reply.src)
                
        except Exception as e:
            print(f"Error at {i} hops: {e}")
trace_route()


