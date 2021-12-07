import re
CoursesData = """101 COM Computers
                205 MAT Mathematics
                189 ENG English"""
# Extract all course numbers
Course_numbers = re.findall('[0-9]+', CoursesData)
print(Course_numbers)
# Extract all course codes
Course_codes = re.findall('[A-Z]{3}', CoursesData)
print(Course_codes)
# Extract all course names
Course_names = re.findall('[A-Za-z]{4,}', CoursesData)
print(Course_names)
