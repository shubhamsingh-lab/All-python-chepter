#write a program to find out wheather a student has passed or fail.if it requried a total  of 40% and and atleast 30% in each subject to pass. assume 3 subject and take marks as user input

marks1 = int(input('Enter the marks1: '))
marks2 = int(input('Enter the marks2: '))
marks3 = int(input('Enter the marks3: '))

#check for total percentages

total_percentage = (100)*(marks1 +marks2 +marks3)/300

if (total_percentage>=40):
    print('you are passed: ', total_percentage)
else:
    print('you are fail try again next year: ', total_percentage)   


