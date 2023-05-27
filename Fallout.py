hours_filled =0
foods = []
cleaned_foods =[]
cleaned_clothes =[]
drinkss = []
clothess = []
money = 500
def first_choice():
  print("Time to do the to-do list: ")
  print("1. Food")
  print("2. Drinks")
  print("3. Clothes")
  print("4. Cleaning the foods")
  print("5. Cleaning the clothes")
  print("6. Story of the disaster")
  print("7. Credit")
  print("8. Finish")
  needs_choice = int(input("Enter what you need: "))
  if needs_choice == 1:
   food()
  elif needs_choice == 2:
   drinks()
  elif needs_choice == 3:
   clothes()
  elif needs_choice == 4:
    cleaning_foods()
  elif needs_choice == 5:
    cleaning_clothes()
  elif needs_choice ==6:
    story_disaster()
  elif needs_choice == 7:
    credit()
  elif needs_choice == 8:
    finish()
  else:
   print("Choose an actual need!")

def finish():
  if hours_filled >= 120:
    print("You succeeded!")
    if money <= 100:
     print("You are good at saving money")
    elif money <= 200:
     print("You are great at saving money!")
    elif money <= 300 or money < 400:
     print("You are a fantastic person for saving money!")
  else:
    print("You didn't succeed. Try to manage your money problems.")

def cleaning_foods():
  print(foods)
  cleaning_choice = input("Which option do you want to do: ")
  if cleaning_choice == "Cow meat" or cleaning_choice == "cow meat":
     print("You picked the cow meat!")
     foodcleanse = input("Do you want to clean the cow meat?y/n")
     if foodcleanse == "y":
       print("You cleaned the cow meat!")
       foods.remove("Cow meat")
       cleaned_foods.append("Cow meat")
     elif foodcleanse == "n":
       cleaning_foods()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "Salmon" or cleaning_choice == "salmon":
     print("You picked the salmon")
     foodcleanse = input("Do you want to clean the salmon?y/n")
     if foodcleanse == "y":
       print("You cleaned the salmon!")
       foods.remove("Salmon")
       cleaned_foods.append("Salmon")
     elif foodcleanse == "n":
       cleaning_foods()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "Sweet Potatoes" or cleaning_choice == "sweet potatoes":
     print("You picked the salmon")
     foodcleanse = input("Do you want to clean the salmon?y/n")
     if foodcleanse == "y":
       print("You cleaned the salmon!")
       foods.remove("Salmon")
       cleaned_foods.append("Salmon")
     elif foodcleanse == "n":
       cleaning_foods()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "Nuts" or cleaning_choice == "nuts":
     print("You picked the nuts")
     foodcleanse = input("Do you want to clean the nuts?y/n")
     if foodcleanse == "y":
       print("You cleaned the nuts!")
       foods.remove("Nuts")
       cleaned_foods.append("Nuts")
     elif foodcleanse == "n":
       cleaning_foods()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "back" or cleaning_choice == "Back":
    first_choice()
  else:
    print("Write an actual response!")

def cleaning_clothes():
  print(clothess)
  cleaning_choice = input("Which option do you want to do: ")
  if cleaning_choice == "Shirt" or cleaning_choice == "shirt":
     print("You picked the shirt!")
     clothcleanse = input("Do you want to clean the shirt?y/n")
     if clothcleanse == "y":
       print("You cleaned the shirt!")
       clothess.remove("Shirt")
       cleaned_clothes.append("Shirt")
       ccchoice = input("Back? y/n")
       if ccchoice == "y":
         first_choice()
       else:
         print("ok")
     elif clothcleanse == "n":
       cleaning_clothes()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "Pants" or cleaning_choice == "pants":
     print("You picked the pants!")
     clothcleanse = input("Do you want to clean the pants?y/n")
     if clothcleanse == "y":
       print("You cleaned the pants!")
       clothess.remove("Pants")
       cleaned_clothes.append("Pants")
       ccchoice = input("Back? y/n")
       if ccchoice == "y":
         first_choice()
       else:
         print("ok")
     elif clothcleanse == "n":
       cleaning_clothes()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "Sandals" or cleaning_choice == "sandals":
     print("You picked the sandals!")
     clothcleanse = input("Do you want to clean the sandals?y/n")
     if clothcleanse == "y":
       print("You cleaned the sandals!")
       clothess.remove("Sandals")
       cleaned_clothes.append("Sandals")
       ccchoice = input("Back? y/n")
       if ccchoice == "y":
         first_choice()
       else:
         print("ok")
     elif clothcleanse == "n":
       cleaning_clothes()
     else:
       print("Please, write an actual response")
  elif cleaning_choice == "back" or cleaning_choice == "Back":
    first_choice()
  else:
    print("Write an actual response!")


def credit():
  print(money)

def story_disaster():
  print("                               Welcome to nuclear town")
  print("Story:A nuclear bomb has detonated to your specific location due toby angering north korea")
  print("Fortunately. You survived thanks to a basement that you built incase of a catastrophic disaster")
  print("However, now you have to live in this contaminated place for 1 week . Since you can skip for 2 days, you have 5 days left. You only have a special radioactive suit as well as a flashlight. you also have around 500 $")
  choice = input("Back? y/n")
  if choice == "y":
    first_choice()
  if choice == "n":
    print("Okay then")


def food():
  
  global money
  global hours_filled
  global foods
  print("1. Cow meat(Not Cleaned)")
  print("2. Salmon(Not Cleaned)")
  print("3. Sweet Potatoes(Not Cleaned)")
  print("4. Nuts(Not Cleaned)")
  print("5. back to choose")
  food_choice = int(input("Pick which food: "))

  
  if food_choice == 1:
    print("You chose cow meat that is not cleaned and has a radioactive dose of 12%.")
    print("The price is 8$")
    food_choice1 = input("Do you want to take this meat(yes) or choose another food(back)")
    if food_choice1 == "yes":
      print("Congratulations! you got a new meat!")
      money -= 8
      foods.append("Cow meat")
      hours_filled += 3.5
      food_choice2 = input("Do you still want to more foods(food) or buy other essential needs(needs)?")
      if food_choice2 == "needs":
        first_choice()
      elif food_choice2 == "food":
        food()
    elif food_choice1 == "back":
        food()

  
  elif food_choice == 2:
    print("You chose salmon that is not cleaned and has a radioactive dose of 8%.")
    print("The price is 11$")
    food_choice1 = input("Do you want to take this fish(yes) or choose another food(back)")
    if food_choice1 == "yes":
      print("Congratulations! you got a new fish meat!")
      money -= 11
      foods.append("Salmon")
      hours_filled += 2
      food_choice2 = input("Do you still want to buy more foods(food) or buy other essential needs(needs)?")
      if food_choice2 == "needs":
        first_choice()
      elif food_choice2 == "food":
        food()
    elif food_choice1 == "back":
        food()

  
  elif food_choice == 3:
    print("You chose sweet potatos that is not cleaned and has a radioactive dose of 13%.")
    print("The price is 2$")
    food_choice1 = input("Do you want to take this potato(yes) or choose another food(back)")
    if food_choice1 == "yes":
      print("Congratulations! you got a new potato!")
      money -= 2
      foods.append("sweet potato")
      hours_filled += 0.8
      food_choice2 = input("Do you still want to buy more foods(food) or buy other essential needs(needs)?")
      if food_choice2 == "needs":
        first_choice()
      elif food_choice2 == "food":
        food()
    elif food_choice1 == "back":
        food()

  elif food_choice == 4:
    print("You chose Nuts that is not cleaned and has a radioactive dose of 9%.")
    print("The price is 3$")
    food_choice1 = input("Do you want to take these nuts(yes) or choose another food(back)")
    if food_choice1 == "yes":
      print("Congratulations! you got new nuts!")
      money -= 3
      foods.append("Nuts")
      hours_filled += 1.6
      food_choice2 = input("Do you still want to buy more foods(food) or buy other essential needs(needs)?")
      if food_choice2 == "needs":
        first_choice()
      elif food_choice2 == "food":
        food()
    elif food_choice1 == "back":
        food()

def drinks():
  print("1. Glass of Water")
  print("2. Cup of Tea")
  print("3. Glass of Milk")
  print("4. Orange Juice")
  print("5. back to choose")

  drink_choice = int(input("Pick which drink: "))
  global money
  global drink
  global hours_filled
  if drink_choice == 1:
    print("You chose water that is filtered and has a radioactive dose of 1%.")
    print("The price is 1$")
    drink_choice1 = input("Do you want to take this water(yes) or choose another drink(back)")
    if drink_choice1 == "yes":
      print("Congratulations! you got a new water!")
      money -= 1
      drinkss.append("Water")
      hours_filled += 0.5
      drink_choice2 = input("Do you still want to buy more drinks(drinks) or buy other essential needs(needs)?")
      if drink_choice2 == "needs":
        first_choice()
      elif drink_choice2 == "drinks":
        drinks()
    elif drink_choice1 == "back":
        drinks()


  elif drink_choice == 2:
     print("You chose tea that is from pretty clean water and has a radioactive dose of 3%.")
     print("The price is 13$")
     drink_choice1 = input("Do you want to take this tea(yes) or choose another drink(back)")
     if drink_choice1 == "yes":
      print("Congratulations! you got a new tea!")
      money -= 13
      drinkss.append("Tea")
      hours_filled += 0.2
      drink_choice2 = input("Do you still want to buy more drinks(drinks) or buy other essential needs(needs)?")
      if drink_choice2 == "needs":
        first_choice()
      elif drink_choice2 == "drinks":
        drinks()
     elif drink_choice1 == "back":
        drinks()


  elif drink_choice == 3:
     print("You chose milk that is from a well fed and protected cow and has a radioactive dose of 5%.")
     print("The price is 5$")
     drink_choice1 = input("Do you want to take this milk(yes) or choose another drink(back)")
     if drink_choice1 == "yes":
      print("Congratulations! you got a new milk!")
      money -= 5
      drinkss.append("Milk")
      hours_filled += 1.5
      drink_choice2 = input("Do you still want to buy more drinks(drinks) or buy other essential needs(needs)?")
      if drink_choice2 == "needs":
        first_choice()
      elif drink_choice2 == "drinks":
        drinks()
     elif drink_choice1 == "back":
        drinks()
  elif drink_choice == 4:
     print("You chose orange juice that is good and has a radioactive dose of 4%.")
     print("The price is 11$")
     drink_choice1 = input("Do you want to take this orange juice(yes) or choose another drink(back)")
     if drink_choice1 == "yes":
      print("Congratulations! you got a new orange juice!")
      money -= 11
      drinkss.append("orange juice")
      hours_filled += 1.1
      drink_choice2 = input("Do you still want to buy more drinks(drinks) or buy other essential needs(needs)?")
      if drink_choice2 == "needs":
        first_choice()
      elif drink_choice2 == "drinks":
        drinks()
     elif drink_choice1 == "back":
        drinks()
  else:
    first_choice()
def clothes():
  print("1. Shirt(Not Cleaned)")
  print("2. Pants(Not Cleaned)")
  print("3. Sandals(Not Cleaned)")
  print("4. back to choose")

  cloth_choice = int(input("Pick which clothes: "))
  global money
  
  if cloth_choice == 1:
    print("You chose a shirt that is not cleaned and has a radioactive dose of 4%.")
    print("The price is 6$")
    cloth_choice1 = input("Do you want to take this shirt(yes) or choose another clothes(back)")
    if cloth_choice1 == "yes":
      print("Congratulations! you got a new shirt!")
      money -= 6
      clothess.append("Shirt")
      cloth_choice2 = input("Do you still want to buy more shirt(shirt) or buy other essential needs(needs)?")
      if cloth_choice2 == "needs":
        first_choice()
      elif cloth_choice2 == "shirt":
        clothes()
    elif cloth_choice1 == "back":
        clothes()
  elif cloth_choice == 2:
    print("You chose pants that are not cleaned and has a radioactive dose of 4%.")
    print("The price is 8$")
    cloth_choice1 = input("Do you want to take these pants(yes) or choose another clothes(back)")
    if cloth_choice1 == "yes":
      print("Congratulations! you got new pants!")
      money -= 6
      clothess.append("Pants")
      cloth_choice2 = input("Do you still want to buy more pants(pants) or buy other essential needs(needs)?")
      if cloth_choice2 == "needs":
        first_choice()
      elif cloth_choice2 == "pants":
        clothes()
    elif cloth_choice1 == "back":
        clothes()

  elif cloth_choice == 3:
    print("You chose sandals that are not cleaned and has a radioactive dose of 5%.")
    print("The price is 3$")
    cloth_choice1 = input("Do you want to take these sandals(yes) or choose another clothes(back)")
    if cloth_choice1 == "yes":
      print("Congratulations! you got new sandals!")
      money -= 3
      clothess.append("Sandals")
      cloth_choice2 = input("Do you still want to buy more sandals(sandals) or buy other essential needs(needs)?")
      if cloth_choice2 == "needs":
        first_choice()
      elif cloth_choice2 == "sandals":
        clothes()
    elif cloth_choice1 == "back":
        clothes()
  else:
    first_choice()
    
first_choice()
