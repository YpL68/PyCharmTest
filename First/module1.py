# Test game
from random import randint

cols_count = int(input("Map size x: "))
rows_count = int(input("Map size y: "))
x = int(input("Character x: "))
y = int(input("Character y: "))

portal_x = randint(0, cols_count - 1)
portal_y = randint(0, rows_count - 1)

direction = "initial"

print(f"Genarating map {cols_count} x {rows_count}....")

while True:
    word_map = ""
    for i in range(rows_count):
        row = ""
        for j in range(cols_count):
            cell = "| "
            if j == x and i == y:
                print(f"Moving character {direction} to {x} : {y}")
                cell = "|X"
            elif j == portal_x and i == portal_y:
                cell = "|O"
            row += cell
        row += "|\n"
        word_map += row
    print(word_map)

    if x == portal_x and y == portal_y:
        print("Ты победил!!!!")
        break

    action = input("Action: ")
    if action == "move":
        direction = input("Direction: ")
        if direction == "up" and y > 0:
            y -= 1
        elif direction == "down" and y < rows_count - 1:
            y += 1
        elif direction == "left":
            x = rows_count - 1 if x == 0 else x - 1
        elif direction == "right":
            x = 0 if x == cols_count - 1 else x + 1
        else:
            print("Wrong direction. Please try again.")
    elif action == "exit":
        break
    else:
        print("Wrong action. Please try again.")

print("Game over")