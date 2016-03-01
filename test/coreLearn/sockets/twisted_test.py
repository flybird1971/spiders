#!/usr/bin/env python
# coding:utf8

import optparse
import traceback
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.defer import Deferred


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

    This is the Get Poetry Now! client, Twisted version 3.1
    Run it like this:

      python get-poetry-1.py port1 port2 port3 ...

    If you are in the base directory of the twisted-intro package,
    you could run it like this:

      python twisted-client-3/get-poetry-1.py 10001 10002 10003

    to grab poetry from servers on ports 10001, 10002, and 10003.

    Of course, there need to be servers listening on those ports
    for that to work.
    """

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


class DemoProtocol(Protocol):

    data = ''

    def dataReceived(self, data):
        self.data += data

    def connectionLost(self, reason):
        self.factory.callback(self.data)


class DemoProtocolFactory(ClientFactory):

    protocol = DemoProtocol

    def __init__(self, callback, errorback, done):
        self.callback = callback
        self.errorback = errorback

    def clientConnectionFailed(self, reactor, reason):
        self.errorback(reason)


def downer(host, port, callback, errorback):
    from twisted.internet import reactor
    factory = DemoProtocolFactory(callback, errorback)
    reactor.connectTCP(host, port, factory)


def demo():
    address = parse_args()

    poets = []
    error = []

    from twisted.internet import reactor

    def getDone():
        if len(poets) + len(error) >= len(address):
            reactor.stop()

    def getDown(data):
        poets.append(data)
        getDone()

    def getError(reason):
        error.append(reason)
        getDone()

    for host, port in address:
        downer(host, port, getDown, getError)

    reactor.run()

    for i, poet in enumerate(poets):
        print "task %s down %s bytes " % (i + 1, len(poet))

    for i, err in enumerate(error):
        print "error info : " % str(err)


def gotPoets(res):
    print "server start....."
    print res
    print "server start.....end"


def gotFailed(err):
    print "has error"
    print err


def test():
    d = Deferred()
    d.addCallbacks(gotPoets, gotFailed)
    # traceback.print_stack()
    # d.callback('tips poetm short')
    d.errback(Exception('tips poetm shorts'))
    print "....end....."

test()


if __name__ == '__main__':
    # demo()
    pass
