# 1st method to open file and read

file = open("new_file.txt", mode="w")
file.write("Its Mahesh Bro...")

# 2nd method to open file and read

# By default the mode of file is set to the read ...
# At the time of Writing into file if file does not exists then python automaticaly create one
with open("new_file.txt", mode="w") as file:
    file.write("\nIts Rahul Bro...")
    

