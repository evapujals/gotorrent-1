# Tracker pyTorrent
# Jesús Gracia & Miquel Sabaté
# GEI URV 2016/2017
# Version 1.1
# Last-update 08.03.17

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

if __name__ == "__main__":
    set_context()
    h = create_host()
    e1 = h.spawn('tracker', Tracker)

    serve_forever()