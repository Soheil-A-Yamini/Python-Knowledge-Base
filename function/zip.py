"""
🎮 Python Example: Using zip() and unzip (*)

This script demonstrates:
1. How to combine multiple lists into a single list of tuples using zip()
2. How to "unzip" the data back into separate sequences
"""

# ------------------------------------
# Example inventory data
# ------------------------------------
item_names   = ['Sword', 'Wooden Shield', 'Metal']
item_rarity  = [66, 45, 12]     # Higher = rarer
item_weights = [3.3, 5.6, 7.0]  # Weight in kg

# ------------------------------------
# Combine lists with zip()
# Each element at the same position is grouped into a tuple
# ------------------------------------
inventory = list(zip(item_names, item_rarity, item_weights))
print("📦 Zipped Inventory (list of tuples):")
print(inventory)

# Output:
# [('Sword', 66, 3.3), ('Wooden Shield', 45, 5.6), ('Metal', 12, 7.0)]

# ------------------------------------
# Unzip inventory back into separate sequences
# zip(*) unpacks the zipped tuples
# ------------------------------------
names, rarity, weights = zip(*inventory)
print("\n🔓 Unzipped Data (tuples):")
print("Names:  ", names)
print("Rarity: ", rarity)
print("Weights:", weights)

# Output:
# Names:   ('Sword', 'Wooden Shield', 'Metal')
# Rarity:  (66, 45, 12)
# Weights: (3.3, 5.6, 7.0)

