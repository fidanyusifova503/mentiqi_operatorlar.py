# Mentiqi operatorlar --> and, or , not 
# 1. And - mentiqi vurma 
# True = beli = 1, False = yox = 0
num1, num2=5,9
# True and True ==> True 
print(1, num1 > 3 and num2 < 10 )

# False and False ==> False 
print(2,num1 > 13 and num2 <= num1)

#True and False ==> False
print(3,13 > 5 and 7 <= num1)

# False and True ==> False
print(4,13 >= 13 and 10 <= 20)

# 2. or - mentiqi toplama

num3, num4 =10 -5
# # True and True ==> True 
print( 5, num1 < 25  or  num4 ! < 6 )


# False and True ==> False
print(6 ,14 == 18 or 25  >= num4)


#True and True ==> True 
print(7, 16 ! = 25 or  num3 > num4 )


#3. not = mentiqi inkar 
# not True = False
# not False = True
print(not 25 < 13)
print(not num4 < 25)




