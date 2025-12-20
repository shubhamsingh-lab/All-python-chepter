a = int(input("Enter your age"))

#if statement no: 1
if(a%2 ==0):
    print("a is even")
else:
    print('a is odd')

#if statement no: 2
if  (a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print('you are entring and invalid age')

else:
    print("you are below the age of consent")
print('end of program')