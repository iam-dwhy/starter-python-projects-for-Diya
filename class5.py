houses_in_abk = {
   "FMC": 15,
   "ATC": 5,
   "FOODCO": 6
}


ages_in_atc = {
    "ola": [1, 2, 3],
    "tola": 3,
    1: "olamide"
}

# house = houses_in_abk["ATC3"]

house = houses_in_abk.get("ATC3")

houses = houses_in_abk.copy()

houses.clear()

houses_in_abk["SS"] = 12

print(houses_in_abk.keys())

print(houses_in_abk.items())

print(houses_in_abk.values())

print(houses_in_abk.update( {"ATC": 15} ))

houses_in_abk.setdefault("ATC", 1)

print(houses_in_abk)