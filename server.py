#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class. Maneja las peticiones.
    """
    dicc = {}

    def handle(self):
        """
        Ejecuta cada vez que recibimos una petición al servidor.
        """
        line = self.rfile.read()

        list = line.decode('utf-8').split(' ')
        if list[0] == 'REGISTER':
            name = list[1].split(':')[1]
            exp = int(list[2].split(':')[1])

            self.dicc[name] = self.client_address[0]

            if exp == 0:
                del self.dicc[name]
            self.wfile.write(b'SIP/2.0 OK\r\n\r\n')
            print(self.dicc)
        if not line: 
            print('Usage: client.py ip puerto register sip_addr expires_value')


if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
