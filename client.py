#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys


Ip = str(sys.argv[1])
Port = int(sys.argv[2])
Method = sys.argv[3].upper()
Line = ' '.join(sys.argv[4:])


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((Ip, Port))
    #Creamos la petición SIP:
    print('Enviando:', Method, 'sip:', Line, 'SIP/2.0\r\n\r\n')
    #Enviamos la petición:
    my_socket.send(bytes(Method, 'utf-8') + b' sip:'+ bytes(Line,'utf-8') + b' SIP/2.0\r\n\r\n')
    data = my_socket.recv(1024)
    print('Recibido? -- ', data.decode('utf-8'))

print("Socket terminado.")
