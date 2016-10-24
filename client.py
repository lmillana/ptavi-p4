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
Line = sys.argv[4]
Exp_Value = sys.argv[5]


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((Ip, Port))
    #Creamos la petición SIP:
    print('Enviando:', Method, 'sip:', Line, 'SIP/2.0\r\n\r\n', )
    print('Expires:', Exp_Value)

    #Enviamos la petición:
    my_socket.send(bytes(Method, 'utf-8') + b' sip:' + bytes(Line, 'utf-8'))
    my_socket.send(b' SIP/2.0\r\n' + b'Expires:')
    my_socket.send(bytes(Exp_Value, 'utf-8') + b'\r\n\r\n')

    try:
        data = my_socket.recv(1024)
    except ConnectionRefusedError:
        sys.exit('Connection refuses')

    print('Recibido? -- ', data.decode('utf-8'))

print("Socket terminado.")
