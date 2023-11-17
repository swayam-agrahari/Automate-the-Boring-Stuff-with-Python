def addToInventory(inventory, addedItems):
    # your code goes here
    count = {}

    for items in addedItems:
        count.setdefault(items, 0)
        count[items] = count[items]+1
    for keys, values in inventory.items():
        if (keys in count.keys()):
            count[keys] = count[keys] + inventory[keys]
        else:

            count[keys] = values

    return count


def displayInventory(my_dict):
    print("Inventory:")
    count = 0
    for keys, items in my_dict.items():
        print(f'{items} {keys}')
        count = count + items
    print("Total number of items:", count)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)