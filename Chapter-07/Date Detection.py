import re
def dateValidation(d,m,y):
   y=int(y)
   validDate = False
   month={'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
   if(y % 2 == 0 and y % 400 == 0 and y % 100 != 0):
      for key,value in month.items():
         if((m == key and int(d) <= value) or (m == '02' and int(d)<= 29)):
            validDate = True

   for key,value in month.items():
       if((m == key and int(d) <= value)):
          validDate = True
   return validDate

date=re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo = date.search('THe date is 07/05/2004')
day = mo.group(1)
month= mo.group(2)
year= mo.group(3)
if(dateValidation(day,month,year)):
   print("Its a valid date.")
else:
   print("Its not a valid date.")



