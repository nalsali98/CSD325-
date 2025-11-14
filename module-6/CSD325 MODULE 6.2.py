"""
Forest Fire Sim for CSD-325 Module 6.2
Modified by Noor Al Salihi
-----------------------------------------------------------
ADDED IN THIS VERSION:
- Lake feature placed roughly in the center of the display
- Lake uses BLUE "~" character
- Water does NOT change over time (cannot grow trees or burn)
- Fire cannot cross or overwrite water (water acts as firebreak)
-----------------------------------------------------------
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module.')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New lake symbol

# Colors
WATER_COLOR = 'blue'

# Simulation settings
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    addLake(forest)  # NEW: Add lake after forest creation
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):

                # Do not modify water tiles at all
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                # EMPTY → TREE
                if (forest[(x, y)] == EMPTY) and (random.random() <= GROW_CHANCE):
                    nextForest[(x, y)] = TREE

                # TREE → FIRE (lightning)
                elif (forest[(x, y)] == TREE) and (random.random() <= FIRE_CHANCE):
                    nextForest[(x, y)] = FIRE

                # FIRE spreads
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):

                            # Skip water: fire CANNOT cross it
                            if forest.get((x + ix, y + iy)) == WATER:
                                continue

                            # Fire spreads to nearby trees
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    # Fire burns out → becomes empty
                    nextForest[(x, y)] = EMPTY

                else:
                    # Otherwise, copy tile as-is
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Creates initial random forest."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def addLake(forest):
    """
    Adds a lake to the center of the forest.
    Lake is a rectangular block approximately in the middle.
    Water cannot burn or transform.
    """

    lake_width = 15
    lake_height = 6

    start_x = (WIDTH // 2) - (lake_width // 2)
    start_y = (HEIGHT // 2) - (lake_height // 2)

    for x in range(start_x, start_x + lake_width):
        for y in range(start_y, start_y + lake_height):
            forest[(x, y)] = WATER


def displayForest(forest):
    """Displays forest contents with colors."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):

            tile = forest[(x, y)]

            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')

            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            elif tile == WATER:
                bext.fg(WATER_COLOR)
                print(WATER, end='')

            elif tile == EMPTY:
                print(' ', end='')

        print()

    bext.fg('reset')
    print(f"Grow chance: {GROW_CHANCE * 100}%  ", end='')
    print(f"Lightning chance: {FIRE_CHANCE * 100}%  ", end='')
    print("Press Ctrl-C to quit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
