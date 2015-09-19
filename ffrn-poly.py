import requests
import json
import copy

# config
url = "http://m.ffrn.de/nodes.json"

r = requests.get(url)
data = r.json()
location_id_list = []
meta_info = {}
area_template = {}
frame = {}
area_list = []

def dedub(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

for node in data['nodes']:
    id = None
    max_level = 0
    name = None
    if node['geo']:
        ald = requests.get('http://global.mapit.mysociety.org/point/4326/' + str(node['geo'][1]) + ',' + str(node['geo'][0]))
        for e in ald.json().items():
            # hack to get the dict behind echa element, can't be adressed otherwise
            e = e[1]
            '''
            check for highest admin level between 6 and 8
            more info: http://wiki.openstreetmap.org/wiki/DE:Grenze
            '''
            if e['type'] == 'O08':
                max_level = 8
                id = e['id']
                name = e['name']
            elif e['type'] == 'O07':
                if max_level < 7:
                    max_level = 7
                    id = e['id']
                    name = e['name']
            elif e['type'] == 'O06':
                if max_level < 6:
                    max_level = 6
                    id = e['id']
                    name = e['name']
        if id:
            # convert id to string
            id = str(id)
            # add id to location list
            location_id_list.append(id)
            # store a relation between id and area names and count nodes for the map
            if id in meta_info.keys():
                meta_info[id]['count'] += 1
            else:
                meta_info[id] = {}
                meta_info[id]['name'] = name
                meta_info[id]['count'] = 1
        else:
            print("No admin layer found for node: " + node['name'])

# remove doubles
dedub_loc_ids = dedub(location_id_list)

# read geojson area template
with open('area.json', 'r') as atmpl:
    area_template = json.loads(atmpl.read())

# read geojson frame template
with open('frame.json', 'r') as ftmpl:
    frame = json.loads(ftmpl.read())

with open('nodes.geojson', 'w') as f:
    for id in dedub_loc_ids:
        area = copy.deepcopy(area_template)
        area_poly = requests.get('http://global.mapit.mysociety.org/area/' + id + '.geojson').json()
        area['properties']['name'] = meta_info[id]['name']
        area['properties']['count'] = meta_info[id]['count']
        area['geometry']['type'] = area_poly['type']
        area['geometry']['coordinates'] = area_poly['coordinates']
        area_list.append(area)
    frame['features'] = area_list
    f.write(json.dumps(frame))
