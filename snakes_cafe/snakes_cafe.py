print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type \"quit\" **")
print("**************************************")
print("\nAppetizers \n---------- \nWings \nCookies \nSpring Rolls")
print("\nEntrees \n------- \nSalmon \nSteak \nMeat Tornado \nA Literal Garden \n\nDesserts \n-------- \nIce Cream \nCake \nPie \n\nDrinks \n------ \nCoffee \nTea \nUnicorn Tears")
print("\n*********************************** \n** What would you like to order? ** \n***********************************")
response = input(">")
oder =[]
while response != "quit":
  oder.append(response)
  print(f"{oder.count(response)} order of {response} have been added to your meal **")
  response = input(">")
  
  
    