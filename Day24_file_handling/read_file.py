print("# 1st method to open file and read")
file = open("my_file.txt", mode="r")
content = file.read()
print(content)


print("# 2nd method to open file and read")

# By default the mode of file is set to the read ...

with open("my_file.txt", mode="r") as file:
    text = file.read()
    print(text)



    