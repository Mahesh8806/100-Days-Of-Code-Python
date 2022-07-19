

travel_log = [
{
    "country": "France",
    "visited": 12,
    'cities': ["Paris",'lille','Dijon'],
},
{
    "country": "Germany",
    "visited": 5,
    "cities": ["Berlin",'Humburg','Nashik'],
},

]

def add_travel_log(country , times_visited , cities_visited):
    new_country  = {};
    new_country["country"] = country;
    new_country["visited"] = times_visited;
    new_country["cities"] = cities_visited;
    travel_log.append(new_country);

add_travel_log(country="Russia",times_visited= 3 , cities_visited=["Moscow","paris"]);

print(travel_log);
