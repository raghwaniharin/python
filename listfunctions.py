"""
AUTHOR HARIN HARISH
FILE IS A PREVIEEW OF ALL THE BASIC FUNCTIONS OF LISTS
EDX COURSE
"""
list1=[1,1,2,3,4]
list2=[10,9,8,7]
print(list1)
print(list2)
list3=list1+list2
print(list3)
list3.extend([5,6])
print(list3)
list4=list3
print("list 4 is: " + str(list4))
print("\n")
print('del')
#del removes item in index 5
del(list4[5])
print(list4)
#pop removes last item from list same as stack pop is a function so it returns value which is now stored
# in a variable
print("\n")
print("pop")
x=list4.pop()
print("value popped out is:" + str(x))
print("\n")
print("remove")
#remove is a also  function which will find the value and remove it from the list
list4.remove(1)
print(list4)


