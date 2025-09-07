fruits = ['banana','apple','grapes','guava','almonds'];
#for x in fruits:
   # print(x);

#for i in range(len(fruits)):
   # print(fruits[i]);

#i=0;
#while i<len(fruits):
   # print(fruits[i]);
   # i=i+1;

fruits.insert(2,'blackberry');
#print(fruits)

fruits.append('mango')
#print(fruits)

fruitList = ['Lichi','Coconut']
fruits.extend(fruitList)
#print(fruits)

fruits.remove('apple')
#print(fruits)

#print(fruits.pop(3))

del fruits[2]
#print(fruits)

#fruits.clear()
newList = [x for x in fruits if 'a' in x]
print(newList)

newList.reverse()
#print(newList)

newList.sort(key=str.lower)
#print(newList)

copyList1 = list(fruits)
copyList2 = newList.copy()
copyList3 = fruits[:]
print(copyList3)