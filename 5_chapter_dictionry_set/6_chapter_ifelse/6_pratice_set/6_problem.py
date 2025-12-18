marks = int(input('Enter your marks: '))

if(marks<=100 and marks>=90):
    print('your are pass in EX grad :')
elif(marks<=90 and marks>=80):
    print('you are passed in A grad')
elif(marks<=80 and marks>=70):
    print('you are passed in  B grad')
elif(marks<=70 and marks>=60):
    print('you are passed in  C grad')
elif(marks<=60 and marks>=50):
    print('you are passed in  D grad')
elif(marks<=50):
    print('you are Fail')
