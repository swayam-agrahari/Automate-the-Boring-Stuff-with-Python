def  displayInventory(my_dict) :
   print("Inventory:")
   count = 0
   for keys,items in my_dict.items():
      print(f'{items} {keys}')
      count = count + items
   print("Total number of items:",count)  


my_dict = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(my_dict)