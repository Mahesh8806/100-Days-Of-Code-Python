import pandas

data = pandas.read_csv("weather_data.csv")

dict_data = data.to_dict()
print(dict_data)

# Convert to list...
temp_list = data['temp'].to_list()
print(temp_list)

# ---------I hade done this way ....

# sum = 0
# avg=0
# for temp in temp_list:
#     sum += temp

# avg = sum / len(temp_list)
# print(avg)

# -----------------Second way to calculate mean or average...

# s_avg = sum(temp_list)/len(temp_list)
# print(s_avg)

#----------------- Third Easiest way to calculate mean or average is...

#This functions work on series data only
print(data['temp'].mean())

#----------------------Calculate max temp from Temperature
print(data['temp'].max())


# To print data where day is equal to monday...

row = data[data['day']=='Monday']
print(row)


# Print the row where temperature is high....
print("\nThe row where temperature is high...")
high_temp_row = data[data['temp'] == data['temp'].max()]

print(high_temp_row)