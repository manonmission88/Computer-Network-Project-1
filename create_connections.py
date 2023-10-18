import re
# Read data from the text file
with open('stokes_library_2.txt', 'r') as file:
    lines = file.readlines()

connections = []
current_sources = []

for line in lines:
    # Extract IP addresses using regular expressions
    ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)

    # If there is an IP address in the line, update current_sources
    if len(current_sources) == 2:
        print(current_sources)
        connections.append(tuple(current_sources))
        current_sources.pop(0)
    if line.startswith("For ip address") and len(current_sources)!=0:
        current_sources = []
    if not ip_addresses:
        current_sources = []
    if ip_addresses:
        current_sources.append(ip_addresses[0])

# If there are remaining IP addresses at the end of the file, create a tuple for them
if current_sources:
    connections.append(tuple(current_sources))

# Print connections
with open('connections.py', 'w') as output_file:
    output_file.write("connections = " + repr(connections))
print("Connections written to 'connections.py' file.")