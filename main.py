# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400
IsLeapYear = False
divisible_by_four = year % 4 
divisible_by_hundred = year % 100
divisible_by_four_hundred = year % 400
#divisible by 4, no:not a leap year; yes, check /100.
#/100: no,leap year; yes, check /400
#/400: yes, leap year; no, not leap year

if divisible_by_four == 0:
  IsLeapYear = True
  #if it's divbisble by 4, but not divisible by 100, it's still not a leap year
  if divisible_by_hundred == 0:
    IsLeapYear = False
    #if it's divisible by 4, and not divisible by 100, but divisible by 400, it's still a leap year
    if divisible_by_four_hundred == 0:
      IsLeapYear = True
    else:
      IsLeapYear = False

if IsLeapYear == False:
  print("Not a leap year")
else:
  print("Leap Year")
  



