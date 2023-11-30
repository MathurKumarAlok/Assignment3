sentence = input("Enter a sentence :")
uppercase =0
lowercase= 0
for i in sentence:
    if (i>="a"and i<="z"):
        lowercase = lowercase+1
    if (i>="A" and i<="Z"):
        uppercase = uppercase+1

print("count lower case :",lowercase)
print("count upper case :",uppercase)


