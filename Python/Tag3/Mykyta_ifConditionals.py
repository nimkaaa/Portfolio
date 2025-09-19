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
   elif years == 18 and legal_age:
      return month <= CURRENT_MONTH
   else:
      return False

def isHorror(wish):
   return wish == "yes"

def calculateMonths(month, year):
   user_months = (CURRENT_YEAR - year - 1) * 12 + month #узнаем кол-во месяцев
   return 216 - user_months

#=====================START=========================

user_country = input("Is it considered 18 years in your country to be legal age?\n(yes/no)\n")

legal_age = isLegit(user_country)

user_month = int(input("In which month were you born? (give as digits)\n"))
user_year = int(input("In which year were you born?\n"))

if isAdult(user_month, user_year):
   print("All right, let's proceed. ...")
   user_wish = input("Do you wanna watch horror movie (18+) or something else?\n(horror/another movie)\n")
else:
   print(f"Sorry, yor are too young, but you can come back in {calculateMonths(user_month, user_year)} months")