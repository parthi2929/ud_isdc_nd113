import math
romania_location_map = {
    'A' : {'pos': (46.18656,21.31227), 'connections': ['S','T','Z'] },
    'S' : {'pos': (45.79833,24.12558), 'connections': ['F','RV','O'] },
    'Z' : {'pos': (46.62251,21.51742), 'connections': ['O'] },
    'T' : {'pos': (45.74887,21.20868), 'connections': ['LU'] },
    'O' : {'pos': (47.04650,21.91894), 'connections': [] },
    'F' : {'pos': (45.84164,24.97310), 'connections': ['B'] },
    'LU' : {'pos': (45.69099,21.90346), 'connections': ['M'] },
    'RV' : {'pos': (45.09968,24.36932), 'connections': ['C','P'] },
    'M' : {'pos': (44.90411,22.36452), 'connections': ['D'] },
    'D' : {'pos': (44.63692,22.65973), 'connections': ['C'] },
    'C' : {'pos': (44.33018,23.79488), 'connections': [] },
    'P' : {'pos': (44.85648,24.86918), 'connections': ['B','C'] },
    'B' : {'pos': (44.42677,26.10254), 'connections': ['G','U'] },
    'G' : {'pos': (43.90371,25.96993), 'connections': [] },
    'U' : {'pos': (44.71653,26.64112), 'connections': ['H','V'] },
    'V' : {'pos': (46.64069,27.72765), 'connections': ['LA'] },
    'LA' : {'pos': (47.15845,27.60144), 'connections': ['N'] },
    'N' : {'pos': (46.97587,26.38188), 'connections': [] },
    'H' : {'pos': (44.68935,27.94566), 'connections': ['E'] },
    'E' : {'pos': (44.04911,28.65273), 'connections': [] }
}

# Euclidean - best if cartesian (x,y) coordinates
def calculate_ED(start, end):
    (x1,y1) = romania_location_map[start]['pos']
    (x2,y2) = romania_location_map[end]['pos']
    return math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))

# Geodesic - best if lat,lon coordinates
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
import geopy.distance
def calculate_GD(start, end):

    coords_1 = romania_location_map[start]['pos']
    coords_2 = romania_location_map[end]['pos']
    return geopy.distance.geodesic(coords_1, coords_2).miles

for each_loc_key in romania_location_map:
    for each_connection_key in romania_location_map[each_loc_key]['connections']:
        distance = calculate_GD(each_loc_key,each_connection_key)
        print('Distance from {} to {} is  {}'.format(each_loc_key,each_connection_key,distance))

#Straight line distance from all to Bucharest
for each_loc_key in romania_location_map:
        distance = calculate_GD(each_loc_key,'B')
        print('Distance from {} to {} is  {}'.format(each_loc_key,'B',distance))