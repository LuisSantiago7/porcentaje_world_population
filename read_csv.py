import csv


def obtain_porcentage_world(path):
    with open(path, 'r') as csvFile:
        reader = csv.DictReader(csvFile, delimiter = ',')
        country_porcentage_world = {}
        country_names = []
        for row in reader:
            country = row['Country/Territory']
            porcentage = float(row['World Population Percentage'])
        
            country_names.append(country)
            country_porcentage_world[country] = porcentage
        
        country_porcentage_world = dict(zip(country_names, country_porcentage_world.values()))
        return country_porcentage_world.keys(), country_porcentage_world.values()
                
