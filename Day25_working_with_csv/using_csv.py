import csv

with open("weather_data.csv",mode='r') as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        # print(row[1])
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
        
