# Tracker pyTorrent
# Jesus Gracia & Miquel Sabate
# GEI URV 2016/2017
# Version 2.0
# Last-update 08.03.17

from pyactor.context import set_context, create_host, serve_forever, sleep

class Tracker(object):
        _tell = ['announce', 'update', 'init']
        _ask = ['get_peers']
        _ref = ['announce']

        peers = {}

        def init(self):
            sleep(5) # sleep implemented in order to avoid an update when execTime=0
            self.interval1 = self.host.interval(5, self.proxy, "update")

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
            print self.peers

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1277/')

    track = host.spawn('tracker', Tracker)

    track.init()
    serve_forever()
