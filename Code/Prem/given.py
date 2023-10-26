from scapy.all import IP, sr1, UDP

'''
This python script:
given in the project definition.
'''

def given(ipaddr):
    for i in range(1, 100):
        pkt = IP(dst=ipaddr, ttl=i) / UDP(dport=33434)
        
        # Send the packet and get a reply
        reply = sr1(pkt, verbose=0, timeout=10)
        
        if reply is None:
            # No reply
            print("No reply")
            break
        elif reply.type == 3:
            # We've reached our destination
            print("Done!", reply.src)
            break
        else:
            # We're in the middle somewhere
            print("%d hops away: " % i, reply.src)


ipaddr = "96.110.40.29"
given(ipaddr)


'''
Condition -> reply == None: No reply -> Timeout
Conclusion -> 


Condition: reply.type == 3 
Conclusion -> Destination unreachable -> reply from the router

Condition: hops away:
Conclusion: Host/Routers (They returns -> Done / No reply)


Routers:
10.0.0.1
68.87.142.129


Example
ipaddr = 1.1.1.1
1 hops away:  10.0.0.1 = Active -> Done = Router
2 hops away:  10.61.212.194 = Active -> No reply = Not Active
3 hops away:  68.87.142.129 = Active -> Done = Router
4 hops away:  96.110.235.177 = Active -> Done = Router
5 hops away:  68.85.115.165 = Active -> Done = Router
6 hops away:  96.110.235.69 = Active -> Done = Router
7 hops away:  96.110.40.29 =  Active -> Done / No reply = Different Results
8 hops away:  96.110.37.142 = Active -> No reply = Not Active
No reply -> Offline/Host/Router
'''