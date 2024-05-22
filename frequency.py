def frequency(string):
  dictionary = {} #create an empty dictionary
  for char in string:
     if char in dictionary: #checks wheather i is in the dictionary
        dictionary[char] += 1 # increment the dictionary by 1
     else:
        dictionary[char] =1 # else adds i by value 1
  print(dictionary) 
     
if __name__ == "__main__":
    n=input("Enter a string: ")
    frequency(n)
