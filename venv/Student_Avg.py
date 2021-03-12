sub1 = int(input("marks1="))
sub2 = int(input("marks2="))
sub3 = int(input("marks3="))
sub4 = int(input("marks4="))
sub5 = int(input("marks5="))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=75 ):
    print('A')
elif(avg>=65):
    print('B')
elif(avg>=55):
    print('C')
elif(avg>=50):
    print('D')
else:
    print("Fail")
