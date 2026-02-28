#Prompt: You can guess it
def questionSix():
  turingVar = "t123u123r123i123n123g"
  output = ""
  
  for stupidName in range(len(turingVar)):
      if turingVar[stupidName] == "t" or turingVar[stupidName] == "u" or turingVar[stupidName] == "r" or turingVar[stupidName] == "i" or turingVar[stupidName] == "n" or turingVar[stupidName] == "g":
          #or say if turingVar[stupidName] in "turing":
              output += turingVar[stupidName]
  
  print(output)

#Prompt: assign a list to the values [1, 2, 3, 4, 5]. Calculate (we've decided on calculating the average), then output the list backwards.
def questionSeven():
  myList = [1, 2, 3, 4, 5]
  myListAverage = sum(myList) / len(myList)


  print(myListAverage)
  print(myList[::-1])


#Prompt: assign a variable to the string "seven." Output the string with 1 of the first letter followed by 2 of the second letter...5 of the fifth letter.
def questionEight():
  myVar = "seven"
  for i in range(len(myVar)):
    print(myVar[i] * (i + 1))

#Prompt: declare a var, assign it to "froglizardfroglizard," and output True if "frog" and lizard appear the same number of times. If last condition is not true, output False.
def questionTen():
  myVar = "froglizardfroglizard"
  frogCount = 0
  lizardCount = 0


  for i in range(len(myVar)):
    if myVar[i:i+4] == "frog":
        frogCount += 1
    if myVar[i:i+6] == "lizard":
        lizardCount += 1

  if frogCount == lizardCount:
    print(True)
  else:
    print(False)

def questionNine():
  my_var = 5
  rmdr = my_var % 7
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  print(days[rmdr])

def questionEleven():
  weirdList = [8, 6, 2, 8, 7, 5, 2]
  weirdListSum = 0
  
  for v in weirdList:
      if v != 8 and v!= 2:
          weirdListSum += v
  
  print(weirdListSum)

def questionTwelve():
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  dict1 = {}
  
  for i in range(len(list1)):
      dict1[list1[i]] = list2[i]
      
  print(dict1)

def questionTwelveAlt():
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  dict1 = dict(zip(list1, list2))
  
  
  print(dict1)

#I did number 13, but deleted it :(

def questionFifteen():
  '''Declare a string and assign it to "135246ABCzyx". Output the sorted version of the string using these rules. 1: Sorted uppercase letters are ahead of lowercase letters. 2: Sorted lowercase letters are ahead of digits. 3: Sorted odd digits are ahead of sorted even digits. NOTE: Values will be changed when grading.'''
  
  #This only works if one assumes that each group of characters are already sorted
  #remember to use dir() on strings; it's useful
  #Yes, endRestult was a typo, but I kept it
  painfulVar = "135246ABCzyx"
  uppercase = ""
  lowercase = ""
  odd = ""
  even = ""
  endRestult = ""
  #endRestult would be uppercase + lowercase + odd + even (endRestultt += u/l/o/e)
  
  for i in range(len(painfulVar)):
      if painfulVar[i].isalpha():
          if painfulVar[i].isupper():
              uppercase += painfulVar[i]
          else:
              lowercase += painfulVar[i]
      elif painfulVar[i].isnumeric():
          if int(painfulVar[i]) % 2 == 0:
              even += painfulVar[i]
          else:
              odd += painfulVar[i]
              
  endRestult += uppercase
  endRestult += lowercase
  endRestult += odd
  endRestult += even
  
  print(endRestult)
