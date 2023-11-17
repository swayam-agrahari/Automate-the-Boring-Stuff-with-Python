def commaSeparation(spam):
   if not spam:
      print("The list is empty.")
   else:
      for i, item in enumerate(spam):
         if i == len(spam)-1 and len(spam) != 1:
            print("and", end=' ')
         print(item, end="")
         if i < len(spam)-1:
            print(", ", end='')

spam = ['apples', 'bananas', 'tofu', 'cats']
commaSeparation(spam)
