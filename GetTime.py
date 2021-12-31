from datetime import datetime
import pytz
import csv

airport_tz = {}
city_tz = {}

with open('airport_tz.csv', mode='r') as inp:
    reader = csv.reader(inp)
    airport_tz = {rows[4]:rows[11] for rows in reader}
with open('airport_tz.csv', mode='r') as inp:
    reader = csv.reader(inp)
    city_tz = {rows[2]:rows[11] for rows in reader}
    
class Time:
    def __init__(self, code):
        self.time = None
        self.timezone = None
        if code == '':
            pass
        elif code.isupper() and len(code) == 3:
            if code in airport_tz.keys():
                if airport_tz[code] != "\\N":
                    self.timezone = pytz.timezone(airport_tz[code])
                    self.time = datetime.now(self.timezone)
                    print("The time at", code, "airport is", self.time.strftime("%H:%M"))
                else: print("The time at", code, "airport is unavailable")
            else:
                print("No such airport found")
        elif code in city_tz.keys():
            if city_tz[code] != "\\N":
                self.timezone = pytz.timezone(city_tz[code])
                self.time = datetime.now(self.timezone)
                print("The time at", code, "City is", self.time.strftime("%H:%M"))
            else: print("The time at", code, "City is unavailable")
        else:
            print("No such city or airport found")          
#t = Time("")
