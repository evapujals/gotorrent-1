#announce -> subscribe
#getpeers -> retorna la llista de peers
#semblant a publish-subscribe. el topic seria el id del que es volen baixar

from pyactor.context import set_context, create_host, sleep, shutdown

class Tracker(object):
        _tell = ['announce', 'update']
        _ask = ['get_peers']
        _ref = ['announce']

        peers = {}

        def get_peers(self, torrent_hash):
            return self.peers[torrent_hash]

        def announce(self, torrent_hash, peer):
            if not(self.peers.has_key(torrent_hash)):
    		          self.peers[torrent_hash] = []
            tup = (peer, 1)
            self.peers[torrent_hash].append(tup)

        def update(self):
            for key in self.peers.keys():
                peers_temp = list(self.peers[key])
                for tup in self.peers[key]:
                    if 0 in tup:
                        peers_temp.remove(tup)
                    else:
                        newTup = (tup[0], 0)
                        peers_temp.remove(tup)
                        peers_temp.append(newTup);
                    self.peers[key] = peers_temp


class Peer(object):
        _tell = ['get_peers', 'announce', 'set_hash']
        _ask = []

        torrent_hash = ""

        def announce(self, torrent_hash):
            self.torrent_hash = torrent_hash
            tracker = self.host.lookup('tracker')
            tracker.announce(torrent_hash, self.id)

        #def set_hash(self, torrent_hash):
        #    self.torrent_hash = torrent_hash

        def get_peers(self):
            tracker = self.host.lookup('tracker')
            neighbors = tracker.get_peers(self.torrent_hash)
            for neig in neighbors:
                print neig[0]

if __name__ == "__main__":
    set_context()
    h = create_host()
    e1 = h.spawn('tracker', Tracker)
    bot1 = h.spawn('bot1', Peer)
    bot2 = h.spawn('bot2', Peer)

    bot1.announce('hash1')
    bot2.announce('hash1')

    sleep(1)
    e1.update()

    bot1.get_peers()
    bot1.announce('hash1')
    sleep(1)
    e1.update()

    bot1.get_peers()

    sleep(1)
    shutdown()
