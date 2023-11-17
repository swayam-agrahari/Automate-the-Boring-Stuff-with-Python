import re
def passWordChecker(str):
   pattern_ucase= re.compile(r'[A-Z]')
   ucase=re.findall(pattern_ucase,str)
   pattern_lcase= re.compile(r'[a-z]')
   lcase=re.findall(pattern_lcase,str)
   pattern_digit =  re.compile(r'[0-9]')
   digit=re.findall(pattern_digit,str)
   length = len(str)
   if(len(ucase)>= 1 and len(lcase) >= 1 and len(digit) >= 1 and length >= 8):
      print("Password is strong")
   else:
      print("Password is weak")


str = input("Enter your passwword")
passWordChecker(str)

