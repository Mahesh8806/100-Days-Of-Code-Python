scores = input("Enter Numbers\n").split(); 

for i in range(0, len(scores)):
    scores[i] = int(scores[i]);

max  =  0;

for score in scores:
    if(score>max):
        max  = score;

print(f"The heighest score in class is{max}");
