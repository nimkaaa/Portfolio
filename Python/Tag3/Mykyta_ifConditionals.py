import datetime

CURRENT_MONTH = int(datetime.datetime.now().strftime("%m"))
CURRENT_YEAR = int(datetime.datetime.now().strftime("%Y"))

#=====================Functions=========================

def isLegit(country):
   return country == "yes"

def isAdult(month, year):
   years = CURRENT_YEAR - year
   if years > 18:
      return True
   elif years == 18:
      return month <= CURRENT_MONTH
   else:
      return False

def isHorror(wish):
   return wish == "yes"

#=====================START=========================

user_country = input("Is it considered 18 years in your country to age?\n(yes/no)\n")

if isLegit(user_country):
   print("All right, let's proceed. ...")
   user_month = int(input("In which month were you born? (give as digits)\n"))
   user_year = int(input("In which year were you born?\n"))
   if isAdult(user_month, user_year):
      print("All right, let's proceed. ...")
      user_wish = input("Do you wanna watch horror movie (18+)?\n(yes/no)\n")
   else:
      print("Thanks for answering! Have a nice childhood! Bye!")
else:
   print("Thanks for answering! Have a nice childhood! Bye!")

# arbeite noch dran...

