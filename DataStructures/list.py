import random

def roll_dice(sides=6, count=1):
    """Roll 'count' dice each with 'sides' sides. Returns list of individual rolls."""
    if sides < 2:
        raise ValueError("sides should be >= 2")
    if count < 1:
        raise ValueError("count should be >= 1")
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls

if __name__ == "__main__":
    print("Single roll (6-sided):", roll_dice())
    print("Three rolls (6-sided):", roll_dice(count=3))
    print("One roll (20-sided):", roll_dice(sides=20))