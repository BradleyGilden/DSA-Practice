# calculates the network address given an ip and a subnet
def calculateNetwork(ip: str, subnet):
    ipValues = ip.split('.')
    subnetValues = subnet.split('.')

    network = []

    for ipVal, subnetVal in zip(ipValues, subnetValues):
        network.append(str(int(ipVal) & int(subnetVal)))

    network = '.'.join(network)
    
    diff = None
    i = 0
    while i < len(network) and i < len(ip):
        if network[i] != ip[i]:
            diff = i
            break
        i += 1

    if diff is not None:
        host = ip[diff:]
    else:
        host = 'Host address not found'

    return f"ip: {ip}\nsubnet mask: {subnet}\nnetwork address: {network}\nhost address: {host}"


print(calculateNetwork('172.19.42.181', '255.255.255.255'))
