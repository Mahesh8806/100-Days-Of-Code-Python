import pandas

data_dict = {
    "students": ["Rahul","Varsha","Mahesh"],
    "scores": [76,90,95],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# It will return the row from 0 to 2. including row 2
data_list = data[:2]
print(data_list)