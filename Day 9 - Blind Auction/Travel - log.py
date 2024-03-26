# Travel - log

country = input("Country: ") # Add country name
visits = input("Number of Visits: ") # Number of visits
cities = input("Cities visited (starting with favorite): ") #cities visited in country
cities = [city for city in cities.split(",")]

travel_log = [
    {"country" : "France", 
    "total_visits": 12,
    "cities visited" : ["Paris", "Lille", "Dijon"] 
    }, 
    
    {"country" : "Germany", 
    "total_visits": 8,
    "cities visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = name
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

