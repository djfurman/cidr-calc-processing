from ipaddress import ip_network

def network_analysis(event, context):
    cidr = ip_network(event['cidr'])

    return {
        'network_address': str(cidr.network_address),
        'broadcast_address': str(cidr.broadcast_address),
        'addresses': str(cidr.num_addresses),
    }

if __name__ == '__main__':
    print(network_analysis({'cidr': '10.100.0.0/16'}, {}))
