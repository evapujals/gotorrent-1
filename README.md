# **GoTorrent**
-----------------------------
###### _Gossip-Bassed BitTorrent_
-------------------------------------

### How to use
GoTorrent has two types of actors:
* tracker.py 
* peer.py

#### tracker.py
It's the responsible to connect all the peers. You only need ONE active tracker at the same time.
Use: python tracker.py

#### peer.py
It's the client of a torrent. You can run how many peers as you want.
Use: python peer.py type\_of\_peer torrent_hash dataLength seedFile
Where:
* type\_of\_peer can be pull, push or pull-push
* torrent_hash is the hash of the torrent you want to share
* dataLength is the length of your file's string
* seedFile is an optional argument. It's the path of the file that contains the original message. This message will be shared to all the peers that will be connected in the same torrent_hash

-----------------------------

Commits are build and tested automatically at [Travis-CI](https://travis-ci.org/miquelsabate/gotorrent).

[![Build Status](https://travis-ci.org/miquelsabate/gotorrent.svg?branch=master)](https://travis-ci.org/miquelsabate/gotorrent)

The code is also checked for its health at every push by [landscape.io](https://landscape.io/github/miquelsabate/gotorrent).

[![Code Health](https://landscape.io/github/miquelsabate/gotorrent/master/landscape.svg?style=flat)](https://landscape.io/github/miquelsabate/gotorrent/master)
