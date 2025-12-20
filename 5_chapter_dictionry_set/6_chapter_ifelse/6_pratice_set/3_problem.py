p1 = 'make a lot of money'
p2 = 'by now'
p3 = 'subsribe this'
p4 = 'click this'

message = input('Enter your message: ')

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print('This message is spam ')
else:
    print('This message is not spam')