#! /bin/bash

python trackerG.py

python peerG.py $1 torrentHash 10 seedFile
python peerG.py $1 torrentHash 10 & > dades1
python peerG.py $1 torrentHash 10 & > dades2
python peerG.py $1 torrentHash 10 & > dades3
python peerG.py $1 torrentHash 10 & > dades4
python peerG.py $1 torrentHash 10 & > dades5
python peerG.py $1 torrentHash 10 & > dades6
python peerG.py $1 torrentHash 10 & > dades7
python peerG.py $1 torrentHash 10 & > dades9
python peerG.py $1 torrentHash 10 & > dades8
python peerG.py $1 torrentHash 10 & > dades10
python peerG.py $1 torrentHash 10 & > dades11
python peerG.py $1 torrentHash 10 & > dades12
python peerG.py $1 torrentHash 10 & > dades13
python peerG.py $1 torrentHash 10 & > dades14
python peerG.py $1 torrentHash 10 & > dades15
