#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class. Maneja las peticiones.
    """

    def handle(self):
        """
        Ejecuta cada vez que recibimos una petición al servidor.
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        print(self.client_address[0])
        print(self.client_address[1])
        for line in self.rfile:
            print("El cliente nos manda: ", line.decode('utf-8'))

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
