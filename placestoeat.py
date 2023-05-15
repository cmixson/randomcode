import random
print("Have you been asked what you want to eat today and dont know? Generate it.")
print("Pick a place: Selma or Montgomery?")
choice = input()
 
places = [["selma", "China Wok","Burger King", "Dominos", "Mcdonalds", "Wendys", "Lannie's", "Subway", "Jack's","Sonics", "Taco Bell", "Hardees", "Popeyes", "American Deli", "Captain D's", "Huddle House", "Church's", "Zaxby's"],
       ["montgomery", "Burger King", "Dominos", "Mcdonalds", "Wendys", "Starbucks", "Subway", "Jack's","Sonics", "Taco Bell", "Hardees", "Popeyes", "American Deli", "Captain D's", "Chick-fil-A", "Church's", "Zaxby's", "Arbys", "WhattaBurger", "Five Guys", "Panda Express", "Moon's BBQ", "Wingmasters"]]

for items in places:
    if items[0] == str.lower(choice):
        place = random.choice(items)
        if place == choice:
            place = random.choice(items)
        print("Let's go to " + place + ".")
