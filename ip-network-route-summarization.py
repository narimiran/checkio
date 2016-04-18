def checkio(data):
    binIPs = [''.join(format(int(d), '08b') for d in a.split('.')) for a in data]
    subnet = 32
    while len(set(i[:subnet] for i in binIPs)) > 1:
        subnet -= 1
    bin_route = binIPs[0][:subnet].ljust(32, '0')
    route = '.'.join(str(int(bin_route[i:i+8], 2)) for i in range(0, 32, 8))
    return '{}/{}'.format(route, subnet)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
