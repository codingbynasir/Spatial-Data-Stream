import math


#Dhaka
from_lat=23.7808875
from_lon=90.2792375

#Comilla
to_lat=23.4531337
to_lon=91.1482907

#Earth's radius in Killometer
R=6371

# Getting latitude in radian
lat1=math.radians(from_lat)
lat2=math.radians(to_lat)

# Getting Theta and Sigma in radian
theta=math.radians(to_lat-from_lat)
sigma=math.radians(to_lon-from_lon)

a=math.sin(theta/2)*math.sin(theta/2)+math.cos(lat1)*math.cos(lat2)*math.sin(sigma/2)*math.sin(sigma/2)
c=2*math.atan2(math.sqrt(a), math.sqrt(1-a))
d=R*c
print(d)