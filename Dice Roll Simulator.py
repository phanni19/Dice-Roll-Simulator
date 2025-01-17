#● ┌ ─ ┐ │ └ ┘
import random

"┌────────┐"
"│        │"
"│        │"
"│        │"
"└────────┘"

dice_art = {
     1: ("┌────────┐",
         "│        │",
         "│    ●   │",
         "│        │",
         "└────────┘"),
     2: ("┌────────┐",
         "│ ●      │",
         "│        │",
         "│      ● │",
         "└────────┘"),
     3: ("┌────────┐",
         "│ ●      │",
         "│    ●   │",
         "│      ● │",
         "└────────┘"), 
     4: ("┌────────┐",
         "│ ●    ● │",
         "│        │",
         "│ ●    ● │",
         "└────────┘"), 
     5: ("┌────────┐",
         "│ ●    ● │",
         "│    ●   │",
         "│ ●    ● │",
         "└────────┘"),
     6: ("┌────────┐",
         "│ ●    ● │",
         "│ ●    ● │",
         "│ ●    ● │",
         "└────────┘")                     
}

dice = []
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):  
        print(line)

print(dice)
