def panagram(s):
    char="abcdefghijklmnopqrstuvwxyz"
    for i in char:
        if i not in s:
            print("not a panagram")
            break
    else:
        print("panagram")
    



if __name__ == "__main__":
    n=input("Enter a string: ")
    panagram(n)
