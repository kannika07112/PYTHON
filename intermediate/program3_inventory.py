# Program 3: Inventory using dictionary

inventory = {"apple": 10, "banana": 20, "orange": 15}

def add_item(item, qty):
    inventory[item] = inventory.get(item, 0) + qty

def remove_item(item, qty):
    if item in inventory and inventory[item] >= qty:
        inventory[item] -= qty
    else:
        print("Not enough stock")

add_item("apple", 5)
remove_item("banana", 5)
print(inventory)
