mukesh = 'Simple Python Calculator by [MUKESH](https://t.me/itz_mst_boi)\n'

mukesh2 = mukesh.center(50)
print(mukesh2)


a = float(input('ENTER YOUR 1ST NUMBER dude:= '))

b = float(input('ENTER  YOUR 2ND NUMBER dude:='))

c = input(
    'Enter operation you want to calculate\n SUPPORTING OPERATION ARE : +,-,*,**,and /')

# to perform addition
if '+' in c:
    print('Addition of two  is', a+b)
    # to perform subtraction
elif '-' in c:
    print('Subtraction of two numbers is', a-b)
# to perform multiplication
elif '*' in c:
    print('Multiplication of two numbers is', a*b)
    # to perform division
elif '/' in c:
    print('Division of two numbers is', a/b)
    #  to get reminder

elif '%' in c:
    print('reminder of given number  is ', a % b)
#  to find power
elif '**' in c:
    print('power of given number is', a**b)
    #  else ur lol
else:
    print("wrong operator lol")
