import time

from geopy.geocoders import Nominatim
import csv


# geolocator = Nominatim(timeout=3)
# geolocator = Nominatim(user_agent="geoapiExercises")
geolocator = Nominatim(user_agent="NewTry")

file1 = open("./CountryName.txt", "a")
count = 1

with open("./CityName.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    cityName = (','.join(row))
    location = geolocator.geocode(cityName, language='en')
    loc_dict = location.raw

    file1.write(loc_dict['display_name'].rsplit(',' , 1)[1] + "\n")

    print(count)
    count += 1
    print(loc_dict['display_name'])
    print ('Country:' + loc_dict['display_name'].rsplit(',' , 1)[1])
    print()
    print()

    # if(count % 10 == 0):
    #   time.sleep(10)

file1.close()


#
# location = geolocator.geocode('Phoenix, Arizona',language='en')
#
# loc_dict = location.raw
#
# print('DispleName: ' + str(loc_dict['display_name']))
#
# print ('Spilited DisplayName: ' + loc_dict['display_name'].rsplit(',' , 1)[1])
