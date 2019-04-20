#appearance of vending machine
vendingMachine = [["A2","A3","A4","A5"],["B2","B3","B4","B5"],["C2","C3","C4","C5"],["D2","D3","D4","D5"]]

print('\nPrinting vending machine. . .')

#printing elements in array
for row in range(len(vendingMachine)):
  print("\n")
  for col in range(len(vendingMachine[row])):
    print(vendingMachine[row][col],end=' ')

print("\n")

#each row in vending machine
#snacks
secA = {2:"cheetos",3:"popcorn",4:"chips",5:"cookies"}
#candy bars
secB = {2:"snickers",3:"payday",4:"kitkat",5:"skittles"}
#gum flavors
secC = {2:"mint gum",3:"bubble gum",4:"fruit gum",5:"orange gum"}
#gummies
secD = {2:"gummy frogs",3:"gummy sharks",4:"gummy bears",5:"gummy snakes"}

#getting row from user
def userChoiceLett():
  choiceLett = input("Enter a letter: ")
  if choiceLett.lower() == 'a':
    return secA
  elif choiceLett.lower() == 'b':
    return secB
  elif choiceLett.lower() == 'c':
    return secC
  elif choiceLett.lower() == 'd':
    return secD
  else:
    print('ERROR:INVALID INPUT')
    return choiceLett()

#getting column from user
def userChoiceNum(array):
  choiceNum = input("Enter a number: ")
  if choiceNum == '2':
    return('You bought '+choiceRow[0]+'!')
  elif choiceNum == '3':
    return('You bought '+choiceRow[1]+'!')
  elif choiceNum == '4':
    return('You bought '+choiceRow[2]+'!')
  elif choiceNum == '5':
    return('You bought '+choiceRow[3]+'!')
  else:
    print("ERROR: INVALID INPUT")
    return userChoiceNum()

#setting user's choice to a variable
choiceRow = userChoiceLett()
print('. . .')
#setting user's choice to a variable
choiceCol = userChoiceNum(choiceRow)
print(choiceCol)


