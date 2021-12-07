import re

CoursesData = """101 COM Computers
    205 MAT Mathematics
    189 ENG English"""
# In[63]:  # define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4, })'
re.findall(course_pattern, CoursesData)
[('101', 'COM', 'Computers'),
 ('205', 'MAT', 'Mathematics'),
 ('189', 'ENG', 'English')]
print(re.findall('[a-zA-Z]+', CoursesData))
print(re.findall('[0-9]+', CoursesData))
