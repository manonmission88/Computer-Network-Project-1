from scapy.all import *

unique_ip = set()
ipaddr="10.199.0.0"  # change subnet accordingly 
def trace_route(ipaddr):
    # print('Tracing route to', ipaddr)
    f = open("UglSubnet199/ugl_sn199.txt","a") # change accordingly
    for i in range(1, 28):
        pkt = IP(dst=ipaddr, ttl=i) / UDP(dport=33434)
        # print(pkt)
        reply = sr1(pkt, verbose=0, timeout=3)
        try: 
            if reply is None:
                f.write(f"Time out at {i} hops away for {ipaddr}.\n")
                print(f"Time out at {i} hops away for {ipaddr}.")
                break
            elif reply.type == 3:
                f.write(f"Destination {ipaddr} reached in {i} hops. Source: {reply.src}\n")
                print(f"Destination {ipaddr} reached in {i} hops. Source: {reply.src}")
                break
            else:
                f.write(f"{i} hops away: {reply.src} \n")
                print(f"{i} hops away: ", reply.src)
                unique_ip.add(reply.src)
        except Exception as e:
            print(f"Error at {i} hops : {e}\n")
    print(" ============== ")
    f.write("===============\n")
    print()
    f.close()
    
def main():
        for i in range(5, 256):
            for j in range(1, 256):  
                trace_route(f"10.199.{i}.{j}") # change the subnet accordingly 
                with open("UglSubnet199/unique_ip_uglsn199.txt","a") as f:  # create the different folder  
                    f.write(f"routes : {unique_ip}\n") 
main()