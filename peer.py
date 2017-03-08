# Peer pyTorrent
# Jesús Gracia & Miquel Sabaté
# GEI URV 2016/2017
# Version 1.1
# Last-update 08.03.17

from pyactor.context import set_context, create_host, sleep, shutdown

class Peer(object):
        _tell = ['get_peers', 'announce', 'set_hash']
        _ask = []

        torrent_hash = ""

        def announce(self, torrent_hash):
            self.torrent_hash = torrent_hash
            tracker = self.host.lookup('tracker')
            tracker.announce(torrent_hash, self.id)

        def get_peers(self):
            tracker = self.host.lookup('tracker')
            neighbors = tracker.get_peers(self.torrent_hash)
            for neig in neighbors:
                print neig[0]

if __name__ == "__main__":
    set_context()
    h = create_host()
    bot1 = h.spawn('bot1', Peer)

    bot1.announce('hash1')

    sleep(1)

    bot1.get_peers()
    bot1.announce('hash1')
    sleep(1)

    bot1.get_peers()

    sleep(1)
    shutdown()
