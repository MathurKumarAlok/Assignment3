my_str = input("Enter a string : ")
reverse = ""
for i in range(len(my_str),0,-1):
    reverse =reverse + my_str[i-1]
    print(my_str[i-1])