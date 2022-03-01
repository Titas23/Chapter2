

# print("hello", "world", sep = "**")
# print("hello", "world", sep = "\n")
# print("1", "two", 3, sep = " ")


# print("hello", end= "\n")
# print("world")

# print("01234567890123456")
# print("\"a\tb\tc\"")
# print("a\tb\tc".expandtabs(5))
# print("Nudge, \tnudge, \nwink, \twink.".expandtabs(11))

# print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
# print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
# print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
# print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")

# for i in range (10):
#     i = i+1
#     print(i)

# str1 = "There is a {0}% probability that the stock market will crash tomorrow and a {1}% that it will rally!"
# print(str1.format(10, 50))
# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))


# print("{0:10,.3%} / {0:10,.3%}".format(12.34569, 13.495950))

# print("The area of {0:s} is {1:,d} square miles.".format("Texas", 268820))

# str2= "The population of {0:s} is {1:.2%} of the U.S. population"
# print(str2.format("Texas", 26448000 / 309000000))

str3 = "Of the total U.S. population, {0:.2%} of househoulds resides in {1:s}"

print(str3.format(26448000 / 309000000, "Texas"))