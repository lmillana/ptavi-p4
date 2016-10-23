#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

    # Constantes(Mayusculas). Dirección IP del servidor y contenido a enviar
    #SERVER = 'localhost'
    #PORT = 6001
    #LINE = '¡Hola mundo!'

Ip = str(sys.argv[1])
Port = int(sys.argv[2])
Line = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((Ip, Port))
    print("Enviando:", Line)
    my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
