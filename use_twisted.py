#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/25/2018 2:49 PM
# @Author  : Aries
# @Site    : 
# @File    : use_twisted.py
# @Software: PyCharm



from twisted.internet import protocol,reactor
from time import ctime


# Server socket
PORT=21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt=self.clnt=self.transport.gePeer().host
        print('...connected from:',clnt)
    def dataReceived(self,data):
        self.transport.write('[%s] %s' % (ctime(),data))

factory=protocol.Factory()
factory.protocol=TSServProtocol
print('wating for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()


# Client Socket
HOST ='localhost'
PORT=21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data=input('> ')
        if data:
            print('...sending %s....' % data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol=TSClntProtocol
    clientConnectionLost=clientConnectionFailed=lambda self,connector,reason:reactor.stop()


reactor.connectTCP(HOST,PORT,TSClntFactory)
