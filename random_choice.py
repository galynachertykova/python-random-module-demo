"""Pick and print a random item from a list of strings."""

import random

items = ["apple", "banana", "cherry", "date", "elderberry"]
selection = random.choice(items)
print(f"Random choice: {selection}")
