# Peer pyTorrent
# Jesus Gracia & Miquel Sabate
# GEI URV 2016/2017
# Version 2.1
# Last-update 15.03.17

from pyactor.context import set_context, create_host, shutdown, serve_forever
from random import randint
import random
import sys

class Peer(object):
    _tell = ['get_peers', 'announce', 'set_hash', 'init', 'missatge', 'push', 'pull']
    _ask = ['request']
    _ref = ['get_peers', 'push', 'pull']

    torrent_hash = ""
    tracker=""
    neighbors=""
    data=""
    lenData=0
    type_of_peer=""


    def init(self, torrent_hash):
        self.tracker = host.lookup_url('http://127.0.0.1:1277/tracker', 'Tracker', 'tracker')
        self.interval1 = self.host.interval(5, self.proxy, "announce", torrent_hash)
        # peer will send an announce every 5 seconds to tracker
        self.interval2 = self.host.interval(10, self.proxy, "get_peers")
        # peer will do the method get_peers every 10 seconds
        if type_of_peer == "push":
            self.interval3 = self.host.interval(4, self.proxy, "push")
        elif type_of_peer == "pull":
            self.interval3 = self.host.interval(4, self.proxy, "pull")
        elif type_of_peer == "hybrid":
            self.interval3 = self.host.interval(4, self.proxy, "push")
            self.interval4 = self.host.interval(4, self.proxy, "pull")

    def announce(self, torrent_hash):
        self.torrent_hash = torrent_hash
        self.tracker.announce(torrent_hash, self.proxy)

    def get_peers(self):
        self.neighbors = self.tracker.get_peers(self.torrent_hash)
        print "".join(data)


    def push(self):
        rndm = random.choice(self.neighbors)
        index = random.randint(0, len(data))
        if (data[index] != ''):
            rndm.missatge(data[index], index)

    def missatge(self, msg, index):
        data[index] = msg

    def pull(self):
        rndm = random.choice(self.neighbors)
        index = random.randint(0, len(data))
        if (data[index] == ''):
            data[index] = rndm.request(index)

    def request(self, index):
        return data[index]


if __name__ == "__main__":
    set_context()
    rand = randint(1000, 1999)
    host = create_host('http://127.0.0.1:' + str(rand))

    print 'peer' + str(rand)

    peer = host.spawn('peer' + str(rand), Peer)

    if len(sys.argv) > 5:
        print "Error in the argument. Use: python peer.py type_of_peer torrent_hash length [gossip]"
        shutdown()
        exit()
    if len(sys.argv) < 4:
        print "Error in the argument. Use: python peer.py type_of_peer torrent_hash length [gossip]"
        shutdown()
        exit()
    if len(sys.argv) == 4:
        type_of_peer = str(sys.argv[1])
        torrent_hash = str(sys.argv[2])
        lenData = int(sys.argv[3])
        data = ['']*lenData
    if len(sys.argv) == 5:
        type_of_peer = str(sys.argv[1])
        torrent_hash = str(sys.argv[2])
        lenData = int(sys.argv[3])
        if len(str(sys.argv[4])) != lenData:
            print "Error in length. Length should be ", lenData, " and message has a length of ", len(str(sys.argv[3]))
            shutdown()
            exit()
        data = list(str(sys.argv[3]))

    peer.init(torrent_hash)

    serve_forever()
