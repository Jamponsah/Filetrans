#working with strings
print("my name is john")
# defining your variables
law= ('happy birthdaay tom you all')
print(len(law))
# moditying strings
b = 'We Are Learning Python Data Types For The Our Session'
print(b.lower())

 # string concatenation
a= 'Beautiful'
b = 'Day'
c= a + " " + b
print(c)

# list data type
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
print(students)

# access list items
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
print(students[0])
print(students[3])

# ranges of list
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
print(students[2:5])
print(students[:4])
print(students[4:])

#change list items
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
students[1] = 'Gustava'
print(students)

# insert items
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
students.insert (9,'Amponsah')
print(students)

# add to list
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
students.append('Micah')
print(students)
# remove
students = ['John', 'Sharon', 'Nasir', 'Mac', 'Samuel', 'Rahab', 'Brian', 'Jackline']
students.remove('Jackline')
print(students)