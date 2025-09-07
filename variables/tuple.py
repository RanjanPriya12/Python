fruits = ('banana','apple','kiwi')
#for x in fruits:
   # print(x)

#for i in range(len(fruits)):
    #print(fruits[i])

i=0;
while i<len(fruits):
   print(fruits[i])
   i=i+1;

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
#print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

#print(mytuple)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#And
#The and keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or
#The or keyword is a logical operator, and is used to combine conditional statements
if a > b or a > c:
  print("At least one of the conditions is True")

#Not
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement
if not a > b:
  print("a is NOT greater than b")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in 
#the pass statement to avoid getting an error.
if b > a:
  pass