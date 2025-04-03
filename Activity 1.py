string = input("Enter in a word: ")
character = input("Enter a character that you want to search in the word above: ")
i = 0
count = 0
while i<len(string):
    if string[i]== character:
        count = count + 1
    i = i + 1
print("The number of times ", character," has occured in ", string," is ", count,"  times ")