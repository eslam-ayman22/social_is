#!/usr/bin/env python
# coding: utf-8

# In[9]:


string= 'Hello'
integar = 16

print(string)
print(integar)


# In[3]:


#########conditionals

number_of_orange = 5

if number_of_orange < 1:
    print('You have no orange')
elif number_of_orange == 1:
    print('You have one orange')
elif number_of_orange < 4:
    print('You have a few orange')
else:
    print('You have many orange!')


# In[13]:


##############################list
student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[1]


# In[11]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[0]


# In[14]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[-1]


# In[15]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[0:2]


# In[16]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[:2]


# In[17]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[3:]


# In[18]:


#########################loop

student = ['Alice', 'Bob', 'Carol', 'Dave']

for student in student_names:
    print('Hello ' + student + '!')


# In[19]:


# Initialize an empty list and add to it the
# student names containing more than four characters
long_names = []
for student in student:
    # This is our criterion
    if len(student) > 4:
        long_names.append(student_name)

long_names


# In[21]:


#################################
#lested loop

student_names = ['eslam', 'ali', 'ahmed', 'Diaa']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[23]:


student_names = ['eslam', 'ali', 'Diaa', 'Ahmed']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        # This is the criterion we added
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )

student_pairs


# In[24]:


################################3
#Tuples
student_grade = ('Alice', 'Spanish', 'A-')
student_grade


# In[25]:


student_grade = ('Alice', 'Spanish', 'A-')
student_grade[0]


# In[27]:


###############################3
#Unpacking

student = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student

print(student_name)
print(subject)
print(grade)


# In[29]:


student = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[30]:


######################################
#Compare this to the same code using indices:

for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])


# In[34]:


##############################
#Dictionaries
languages = {
    'A': 'Spanish',
    'B': 'French',
    'C': 'Italian',
    'D': 'Italian',
}
languages['D']


# In[37]:



languages = {
    'A': 'Spanish',
    'B': 'French',
    'C': 'Italian',
    'D': 'Italian',
}
##We can check if a particular key is in a dictionary with the in keyword:
'D' in languages


# In[38]:


# Add an entry that doesn't exist
languages['Esther'] = 'French'
languages


# In[40]:


# Delete an entry that exists
del languages['B']
languages


# In[41]:


# Change an entry that does exist
languages['Esther'] = 'Italian'
languages


# In[43]:


# Looping over dictionaries
for key in languages:
    value = languages[key]
    print(key, 'is taking', value)


# In[45]:


for key, value in languages.items():
    print(key, 'is taking', value)


# In[46]:


#Dictionaries as records
student_grade = ('Alice', 'Spanish', 'A')


# In[47]:


student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# In[48]:


record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# In[50]:


# List of tuples
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]
student_grades[1]


# In[52]:


#List of dictionaries
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[57]:


student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records
#Now each item in the list is a dictionary:
student_grade_records[1]


# In[59]:


student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records
#and we can work with the individual records as such:
student_grade_records[1]['grade']


# In[62]:


# Dictionary of dictionaries

language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    language_grades[student_name] = record
    
language_grades


# In[63]:


language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    language_grades[student_name] = record
    
language_grades
#Now we can refer to these by student name:
foreign_language_grades['Alice']


# In[64]:


language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    language_grades[student_name] = record
    
language_grades
#And we can get the individual data that we care about:
foreign_language_grades['Alice']['grade']


# In[65]:


#Dictionary with tuple keys
grades = {}
for student_name, subject, grade in student_grades:
    grades[student_name, subject] = grade
    
grades


# In[70]:


grades = {}
for student_name, subject, grade in student_grades:
    grades[student_name, subject] = grade
    
grades
#Now we can represent all of a student's grades:
grades['Alice', 'Math'] = 'A'
grades['Alice', 'History'] = 'B'
grades


# In[76]:


#Another dictionary of dictionaries
student_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_cards:
        student_cards[student_name] = {}
    student_cards[student_name][subject] = grade
student_cards


# In[80]:


student_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_cards:
        student_cards[student_name] = {}
    student_cards[student_name][subject] = grade
student_cards
#And we can easily fetch a student's "report card":
student_cards['Alice']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




