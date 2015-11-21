# Freifunk Rhein Neckar expansion map
The map shows the administrative areas in which the defined community has nodes even if they are offline.
To use this software you need the d3map backend nodes.json file or the meshviewer nodelist.json file. This script queries the mapi API. This is an API provided by the [mysociety](https://github.com/mysociety/mapit) for low frequecy queries, so please only query one or two times a day. I'm sure your areas doesn't change that often.

But to mitigate this we now have a great caching mechanism.

## Usage

### nodelist (meshviewer FFDA Version)
./mkpoly -f nodelist https://map.darmstadt.freifunk.net/data/nodelist.json

### nodes.json (ffmap FFRN Version)
./mkpoly  -f ffmap http://map.ffrn.de/nodes.json

### Help
./mkpoly  -h

### Example Map

http://overview.ffrn.de
