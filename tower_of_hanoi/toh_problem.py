"""
Tower of Hannoi implementation by Vineeth.Aljapur
A stack-moving puzzle game.
"""

import copy
import sys
from urllib import response

TOTAL_DISKS = 5

# Start with all disks on tower A
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    """Runs a single game of the toh"""
    print ("""Tower of Hannoi
    Move the tower of disks, one disk at a time, to another tower.
    Larger disks cannot rest on top of smaller disks
    """)

    towers = {
        "A": [5, 4, 3, 2, 1], 
        "B": [],
        "C": []
    }

    while True:
        # Display the towers and disks
        displayTowers(towers)

        # Ask the user for a move
        fromTower, toTower = getPlayerMove(towers)

        # Move the top disks from fromTower to toTower
        disk  = towers[fromTower].pop()
        towers[toTower].append(disk)

        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)
            print ("Congrats! You have solved the TOH")
            sys.exit()

def getPlayerMove(towers):
    """Asks the player for the move"""

    while True: # Keep asking until they make valid move
        print("Enter the letters of 'from' and 'to' towers, or 'QUIT'.")
        print("(e.g. AB moves top disk of tower A to tower B)")
        print()

        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # make sure the user entered valid response
        if response not in ("AB", "AC", "BA", "CA", "BC", "CB"):
            print("Enter one of AB, AC, BA, CA, BC, CB")
            continue

        # Use more descriptive variable names
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            print("You have selected tower with no disks")
            continue
        elif len(towers[toTower]) == 0:
            # Any disk can be moved to empty tower
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller disks")
            continue
        else:
            # It is a valid move
            return fromTower, toTower 

def displayTowers(towers):
    """Displays the three towers and the disks"""
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0) # Display the bare pole with no disk
            else:
                displayDisk(tower[level])
        print ()

    # Display tower labels
    emptySpace = " " * TOTAL_DISKS
    print (f"{emptySpace} A{emptySpace}{emptySpace} B{emptySpace}{emptySpace} C\n")

def displayDisk(width):
    """Display disk of given width. Width 0 means no disk"""
    emptySpace = " " * (TOTAL_DISKS -width)

    if width == 0:
        # Display pole with no width
        print(f"{emptySpace}||{emptySpace}", end="")

    else:
        # Display the disk
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

# If this program is run instead of imported, run the game
if __name__=="__main__":
    main()
