
# Written by me

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __twitter__ = ""
# __credits__ = [""]
# __license__ = "Apache2.0"
# __version__ = "1.0.0"
# __maintainer__ = ""
# __email__ = ""

import json
from utilities.p1 import haversine

emoryRiddleLongitude = 34.6172
emoryRiddleLatitude = 112.4505

# Opening JSON file
with open('./vectors.json', 'r') as fh:
    vectors = json.load(fh)

baselineDistance = 1000000
baselineRate = 0


# Iterating through the json
# list
for i in vectors:
    #print(i['callsign'])
    #print(i['longitude'])
    #print(i['latitude'])
    distanceFromEmoryRiddle = haversine(i['latitude'],i['longitude'], emoryRiddleLongitude, emoryRiddleLatitude)
    #(distanceFromEmoryRiddle)

    if distanceFromEmoryRiddle < baselineDistance:
        #print('less')
        closestPlaneDistance = distanceFromEmoryRiddle
        closestPlaneCallsign = i['callsign']
        baselineDistance = distanceFromEmoryRiddle

print('-------------------------')
print("Closest Plane Distance : %s, Closest Plane Call Sign : %s" % (str(closestPlaneDistance), closestPlaneCallsign))

for i in vectors:
    if i['vertical_rate'] < baselineRate:
        mostAscendingPlane = i['vertical_rate']
        mostAsendingCallSign = i['callsign']
        baselineVerticalRate = i['vertical_rate']
print('-------------------------')
print("Most Ascending Plane : %s, Most Ascending Plane Call Sign : %s" % (mostAscendingPlane, mostAsendingCallSign))









# Closing file
fh.close()
