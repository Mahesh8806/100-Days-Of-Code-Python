enemies = 1;

# First way to increase local variab
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function:{enemies}")
increase_enemies();
print(f"Enemies Outside function:{enemies}")


def increase_enemies():
    print(f"Enemies inside function:{enemies}")
    return enemies + 1;

enemies = increase_enemies();
print(f"Enemies Outside function:{enemies}")