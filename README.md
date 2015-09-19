# Freifunk Rhein Neckar expansion map
The map shows the the admin areas in which the defined community has nodes even if the are offline.
To use this software you need the d3map backend nodes.json file. You have to define the url to the file
in the python script ffrn_poly.py. This scirpt querys the mapi API. This is an API provided by the mysociety
for low frequecy querys, so please only query one or two times a day. I'm sure your areas dosn't change that often.
If you need to query more frequently please install an onwn instance of the mapit tools. You can find it here:
https://github.com/mysociety/mapit
