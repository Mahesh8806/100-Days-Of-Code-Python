from posixpath import split


height = input("Input a list of strudent height\n").split();

# print(height);
# print(type(height))

for i in range(0, len(height)):
    height[i] = int(height[i]);

# print(height);
total_height = 0 ;
for i in height:
    total_height += i;

# print(total_height)
number_of_height = 0 ;
for i in height:
    number_of_height += 1;

avg = total_height/number_of_height;

print("The Average Height is:"+str(round(avg)));