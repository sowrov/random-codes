# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import socket
import struct
import textwrap

def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        rawData, add = connection.recvfrom(65536)
        destMac, srcMac, protocol, data = ethernet_frame(rawData)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(destMac, srcMac, protocol))

# unpack ethernet frame
def ethernet_frame(data):
    destMac, srcMac, protocol = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(destMac), get_mac_addr(srcMac), socket.htons(protocol), data[14:]

# Retrun properly formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{0:02X}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

main()