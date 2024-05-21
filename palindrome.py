def palindrome(s):
   s=s.lower() #to convert upercase character to lowercase
   r=s[::-1] #to reverse the string
   if s==r: 
    print("palindrome")
   else:
    print("not a palindrome")



if __name__ == "__main__":
    n=input("Enter a string: ")
    palindrome(n)
