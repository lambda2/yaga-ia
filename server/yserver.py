#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import SocketServer as ss

class YThreadedTCPRequestHandler(ss.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class YThreadedTCPServer(ss.ThreadingMixIn, ss.TCPServer):
    pass

class YTCPHandler(ss.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        question = self.rfile.readline()
        self.server.engine.changeQuery(question)
        response = self.server.engine.serverDigest()
        self.wfile.write(response)

class YTCPServer(ss.TCPServer):
    
    def setEngine(self, engine):
        self.engine = engine

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

class YServer:
    
    def __init__(self, engine, port=1990, host="localhost"):
        # Serveur http de base
        self.engine = engine
        self.port = port
        self.host = host
        
        """        
        self.server = YThreadedTCPServer((self.host, self.port), YThreadedTCPRequestHandler)
        ip, port = self.server.server_address
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        self.server_thread.daemon = True
        """
        self.server = YTCPServer((self.host, self.port), YTCPHandler)
        self.server.setEngine(engine)


    def start(self):
        self.server.serve_forever()
        """
        self.server_thread.start()
        print "Server loop running in thread:", self.server_thread.name
        """

    def stop(self):
        self.server.shutdown()