# x=2
# if x>5:
#     print("X is greater than 5!")
# else:
#     print("X is less than 5!")
#     print("Multiple steps")

# a, b, c = "One", "Two", 1
# print(a)
# print(b)
# print(c)

# a = b = c = 1
# print(a)
# print(b)
# print(c)

#unpacking
# numbers = [1, 2, 3]
# a, b, c = numbers
# print(a)
# print(b)
# print(c)

#print(type(numbers))

#Casting
# x=5
# print(float(x))
# print(str(x))
# print(type(x))

# #Strings
# a = "Anna"
# print(a[0])
# print(a[1])

# for x in a:
#     print(x)

# print(len(a))

# #check for a value
# x = "12354"
# print("6" in x) #returns a boolean

# #negative indexing
# print(x[0]) #1
# print(x[-1]) #5
# print(x[-5])

# slicing, end number is not inclusive
# x = "12354"
# print(x[1:3])
# print(x[:3])
# print(x[1:])

# x = [1, 2, 3]
# list = [1, "apple", 7.5]
# # print(x)
# # print(list)

# x[0] = "o"
# print(x)

# list.insert(1, "inserted value")
# print(list)
# list.append("appended string")
# print(list)
# list.extend(x)
# print(list)

#Tupples
# tuple = (1, 2, 3)
# print(tuple[-1])

#Sets
#no duplicates
# set1 = {1, 2, 3, 3}
# print(set1)

# #only valid ways to access
# print(1 in set1)

# for x in set1:
#     print(x)

#Dictionary
# dic1 = {
#     "first": "Anna",
#     "last": "Young"
# }
# print(dic1)
# print(dic1["first"])

# list2 = [4, 5, 6]
# list1 = [1, 2, 3]

# print(list2 + list1)

#IF statements
# x=2
# if (x ==2) | (x <5):
#     print("true")

# if (x ==2) or (x <5):
#     print("true")

# #elif keyword
# if x >5:
#     print("x > 5")
# elif x==5:
#     print("x = 5")
# else:
#     print("x < 5")

#for/while loops
#i=0 i<6 i++
# for x in range(6):
#     print(x)
# else:
#     print("Done with for loop")

# i=0
# while i < 5:
#     print("i < 5")
#     i += 1

# def myFunc():
#     print("Inside myFunc")
#     #as many statments as you want
#     #
#     #
#     #

# #call the function  
# myFunc()

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def fullName(self):
        return(self.first + " " + self.last)


student1 = Student("Anna", "Young")
print(student1.fullName())
print(student1.first)
print(student1.last)