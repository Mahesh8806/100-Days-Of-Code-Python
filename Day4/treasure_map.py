from matplotlib.ft2font import HORIZONTAL


row1 = ["🖽","🖽","🖽"]
row2 = ["🖽","🖽","🖽"]
row3 = ["🖽","🖽","🖽"]


map = [row1 , row2 , row3];

print(f"{row1}\n{row2}\n{row3}");

position = input("Where do you want to put Treasure? RowColumn\n");

row = int(position[0]);
coloumn = int(position[1]);

map[row - 1][coloumn - 1] =  "💰";
print(f"{row1}\n{row2}\n{row3}");
