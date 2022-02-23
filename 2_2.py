

myvar = "Say it ain't so"

print(myvar)


var2 = "spam & eggs"

spam = "spam" 
eggs = "eggs" 

spam_and_eggs = spam + " & " + eggs

print("var2", var2)

print(var2[0])
print(var2[:])
print(var2.rfind('s'))
print(spam_and_eggs)

length = len(spam_and_eggs)

print(length)
print(spam_and_eggs.upper())
print(spam_and_eggs.lower())
print(spam_and_eggs.count("sp"))
print(spam_and_eggs.capitalize())
print(spam_and_eggs.title())
print(spam_and_eggs.strip())


praise = "Good Doggie"
count = praise.upper().count("G")

print("count : ", count)

town = input("Enter the name of your city: ")

full_name = input("Enter a full name: ")
n = full_name.rfind(" ")
print("Last name:", full_name[n+1: ])
print("First name(s): ", full_name[:n])