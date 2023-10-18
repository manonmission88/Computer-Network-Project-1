from scapy.all import ARP, Ether, srp
import os



####################################  task1_helper1 Function  ##################################################################################
def task1_helper1(network_identifier, dict_results, uniques_in_Folders, folder_name):
    # Create an ARP request packet to get the MAC address corresponding to an IP address
    ip_range = f"{network_identifier}/24"
    arp = ARP(pdst=ip_range)
    # Create an Ether broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ether and ARP packets
    packet = ether/arp
    # Send the packet and receive the response
    result = srp(packet, timeout=3, verbose=False)[0]
    # List of active IPs and MACs
    active_hosts = []
    dict_results[network_identifier] = set()

    for sent, received in result:
        active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
        dict_results[network_identifier].add(str(received.psrc))

        # Create directory if not exist
        directory = f"{folder_name}/{network_identifier}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        chk = uniques_in_Folders[folder_name].get(network_identifier, 0)
        if chk != 0:
            uniques_in_Folders[folder_name][network_identifier].add(str(received.psrc))

    return active_hosts, dict_results, uniques_in_Folders
####################################  task1_helper1 Function  ##################################################################################



####################################  task1 Function  ##################################################################################
def task1(network_identifier, dict_results, uniques_in_Folders, folder_name):

    # uniques_in_Folders cannot be empty
    if len(uniques_in_Folders) == 0:
        uniques_in_Folders[folder_name] = dict()
        uniques_in_Folders[folder_name][f"{network_identifier}"] = set()
    
    # Create directory if not exist
    directory = f"{folder_name}/{network_identifier}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # find active hosts
    print("Scanning for active hosts...")
    active_hosts, dict_results, uniques_in_Folders = task1_helper1(network_identifier, dict_results, uniques_in_Folders, folder_name)

    #dict_results.txt
    f = open(f"{folder_name}/{network_identifier}/dict_results.txt", "a")
    f.write(f"{str(uniques_in_Folders)}\n")
    f.write("---------------------------------------------------------------------------------------\n")
    f.close()

    # results.txt
    g = open(f"{folder_name}/results.txt", "a")
    g.write(f"{str(uniques_in_Folders)}\n")
    g.write("---------------------------------------------------------------------------------------\n")
    g.close()

    # {network}.txt
    h = open(f"{directory}/{network_identifier}.txt", "a")
    h.write(f"Active Hosts on the Network or Subnet: {network_identifier}\n")
    print("Active hosts are:")
    for host in active_hosts:
        ipaddr = host['ip']
        h.write(f"{ipaddr}\n")
        print(f"{host['ip']} at {host['mac']}")
    h.write("---------------------------------------------------------------------------------------\n")
    h.close()

    return dict_results
#task_results = {'10.0.0.0': {'10.0.0.1', '10.0.0.72', '10.0.0.226'}}
####################################  task1 Function  ########################################################################################





####################################  Script Run  ########################################################################################
if __name__ == "__main__":

    network_identifier = input("Enter Network Identifier: ")
    dict_results = dict()
    uniques_in_Folders = dict()
    folder_name = "Subnets"

    for i in range(10):
        task1_results = task1(network_identifier, dict_results, uniques_in_Folders, folder_name)
        print(f"Task-1 Result")
        print(task1_results)


####################################  Script Run  ########################################################################################








