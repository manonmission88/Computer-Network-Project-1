import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

'''
This Script:
creates -> png file containing topology
'''

def active_ips_from_file(fname, outname):

    f = open(f"{outname}", "a")
    
    with open(fname, 'r') as file:

        lines = file.readlines()
        end = False
        route = []

        for line in lines:

            if "hops away" in line and ":" in line:

                ip = line.split(":")[1].strip()
                parts = ip.split(".")

                if parts[0] == "10":
                    end = True
                    print("Entered")
                    route.append(ip)
                    f.write(f"{ip}\n")
                
                if parts[0] == "138" and int(parts[1]) <= 238:
                    end = True
                    route.append(ip)
                    f.write(f"{ip}\n")
                    print("Entered")
                
            elif "STOP" in line:
                print(f"Stopped at line {line}")
                break

            elif end == True:
                f.write(f"Line End:\n")


            else:
                end = False
                continue
                
                #f.write(f"Route Started:\n")
                #route = []
    f.close()


if __name__ == "__main__":

    active_ips_from_file("data.txt", "active_ips_from_file.txt")

    
    routes = []
    route = []

    with open("active_ips_from_file.txt", 'r') as file:

        lines = file.readlines()
        
        for line in lines:
            #print("Line: ", line)

            if "Line End:" in line:
                routes.append(route)
                #print("routes: ")
                #print(routes)
                route = []
            
            else:
                #print("Entered Append")
                route.append(line)
    
    #print("routes", routes)

    f = open(f"routes.txt", "a")
    for i in routes:
        f.write(f"{i}\n")
    f.close()