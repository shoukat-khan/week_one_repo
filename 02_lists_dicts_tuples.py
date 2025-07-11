#!/usr/bin/env python3
"""
Python Data Structures: Lists, Dictionaries, and Tuples
This script demonstrates advanced operations on Python's core data structures.
"""

# ============================================================================
# LISTS - Mutable, Ordered Collections
# ============================================================================

print("=" * 60)   
print("LISTS - MUTABLE, ORDERED COLLECTIONS")
print("=" * 60)

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"Fruits: {fruits}")

# List operations
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")
print(f"Slice [::2]: {fruits[::2]}")  # Every second element
print(f"Length: {len(fruits)}")

# List methods
print("\n--- List Methods ---")

# Adding elements
fruits.append("fig")
print(f"After append('fig'): {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")

fruits.extend(["grape", "honeydew"])
print(f"After extend(['grape', 'honeydew']): {fruits}")

# Removing elements
removed_fruit = fruits.pop()
print(f"Popped: {removed_fruit}, List: {fruits}")

removed_fruit = fruits.pop(2)
print(f"Popped index 2: {removed_fruit}, List: {fruits}")

# Note: banana was already removed in previous operations
print(f"Current fruits list: {fruits}")

# Searching and counting
print(f"\nIndex of 'cherry': {fruits.index('cherry')}")
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"'grape' in fruits: {'grape' in fruits}")

# Sorting
fruits.sort()
print(f"Sorted fruits: {fruits}")

fruits.sort(reverse=True)
print(f"Reverse sorted: {fruits}")

# List comprehension examples
print("\n--- List Comprehensions ---")

# Basic comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Comprehension with condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
print(f"3x3 matrix: {matrix}")

# String manipulation with comprehension
word_lengths = [len(word) for word in fruits]
print(f"Word lengths: {word_lengths}")

# ============================================================================
# DICTIONARIES - Mutable, Key-Value Pairs
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARIES - MUTABLE, KEY-VALUE PAIRS")
print("=" * 60)

# Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice Johnson",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "employed": True
}

# Nested dictionary
company = {
    "name": "TechCorp",
    "employees": {
        "alice": {"name": "Alice", "role": "Developer", "salary": 75000},
        "bob": {"name": "Bob", "role": "Manager", "salary": 90000},
        "charlie": {"name": "Charlie", "role": "Designer", "salary": 65000}
    },
    "departments": ["Engineering", "Marketing", "Sales"]
}

print(f"Person: {person}")
print(f"Company: {company}")

# Dictionary operations
print(f"\nPerson's name: {person['name']}")
print(f"Person's skills: {person['skills']}")
print(f"Alice's role: {company['employees']['alice']['role']}")

# Safe access with get()
print(f"Person's phone: {person.get('phone', 'Not provided')}") # if the key is not found, it will return the default value
print(f"Person's age: {person.get('age', 'Not provided')}")

# Dictionary methods
print("\n--- Dictionary Methods ---")

# Keys, values, items
print(f"Keys: {list(person.keys())}") # returns a list of the keys in the dictionary
print(f"Values: {list(person.values())}") # returns a list of the values in the dictionary
print(f"Items: {list(person.items())}") # returns a list of tuples, each containing a key-value pair

# Adding and updating
person["email"] = "alice@email.com"
print(f"After adding email: {person}")

person.update({"age": 26, "experience": 3})
print(f"After update: {person}")

# Removing items
removed_value = person.pop("email") # removes the key-value pair and returns the value
print(f"Popped email: {removed_value}, Person: {person}")

# Dictionary comprehension
print("\n--- Dictionary Comprehensions ---")

# Basic comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dictionary: {square_dict}")

# Comprehension with condition
even_square_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even square dictionary: {even_square_dict}")

# From existing data
word_length_dict = {word: len(word) for word in fruits}
print(f"Word length dictionary: {word_length_dict}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged dictionaries: {merged}")

# ============================================================================
# TUPLES - Immutable, Ordered Collections
# ============================================================================

print("\n" + "=" * 60)
print("TUPLES - IMMUTABLE, ORDERED COLLECTIONS")
print("=" * 60)

# Creating tuples
empty_tuple = ()
single_element = (42,)  # Note the comma
coordinates = (40.7128, -74.0060) # latitude and longitude of New York City
rgb_color = (255, 128, 0) # red, green, blue
person_tuple = ("Alice", 25, "New York")

print(f"Empty tuple: {empty_tuple}")
print(f"Single element: {single_element}")
print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Person tuple: {person_tuple}")

# Tuple operations
print(f"\nFirst coordinate: {coordinates[0]}") # latitude
print(f"Last coordinate: {coordinates[-1]}") # longitude
print(f"Slice [0:1]: {coordinates[0:1]}") # latitude
print(f"Length: {len(coordinates)}") # 2

# Tuple unpacking
x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

name, age, city = person_tuple
print(f"Unpacked person: name={name}, age={age}, city={city}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# Tuple methods
print(f"\nIndex of 255 in RGB: {rgb_color.index(255)}")
print(f"Count of 128 in RGB: {rgb_color.count(128)}")

# Named tuples (from collections module)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) # creates a new class called Point inside the bracket the Point shows that the 
p1 = Point(10, 20) # creates a new instance of the Point class with x=10 and y=20 the namedtuple('Point', ['x', 'y']) 'Point' shows the name of the class and ['x', 'y'] shows the names of the attributes
p2 = Point(30, 40) # creates a new instance of the Point class

print(f"\nNamed tuple Point: {p1}")
print(f"Point x: {p1.x}, Point y: {p1.y}")
print(f"Point as dict: {p1._asdict()}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Student Grade Management System
print("\n--- Student Grade Management System ---")

students = [
    {"name": "Alice", "grades": [85, 92, 78, 96, 88]},
    {"name": "Bob", "grades": [75, 82, 78, 85, 80]},
    {"name": "Charlie", "grades": [65, 70, 68, 72, 69]},
    {"name": "Diana", "grades": [95, 98, 92, 96, 94]}
]

def calculate_average(grades):
    return sum(grades) / len(grades)

def get_grade_letter(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

# Process students
for student in students:
    avg = calculate_average(student["grades"])
    grade = get_grade_letter(avg)
    student["average"] = avg
    student["letter_grade"] = grade

# Sort by average (highest first)
students.sort(key=lambda x: x["average"], reverse=True)

print("Student Rankings:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}: {student['average']:.1f} ({student['letter_grade']})")

# Example 2: Inventory Management System
print("\n--- Inventory Management System ---")

inventory = {
    "laptop": {"quantity": 10, "price": 999.99, "category": "electronics"},
    "mouse": {"quantity": 50, "price": 25.99, "category": "electronics"},
    "notebook": {"quantity": 100, "price": 5.99, "category": "stationery"},
    "pen": {"quantity": 200, "price": 1.99, "category": "stationery"},
    "headphones": {"quantity": 15, "price": 89.99, "category": "electronics"}
}

def get_total_value(inventory):
    return sum(item["quantity"] * item["price"] for item in inventory.values())

def get_items_by_category(inventory, category):
    return {k: v for k, v in inventory.items() if v["category"] == category}

def get_low_stock_items(inventory, threshold=20):
    return {k: v for k, v in inventory.items() if v["quantity"] < threshold}

print(f"Total inventory value: ${get_total_value(inventory):.2f}")
print(f"Electronics: {list(get_items_by_category(inventory, 'electronics').keys())}")
print(f"Low stock items: {list(get_low_stock_items(inventory).keys())}")

# Example 3: Data Processing Pipeline
print("\n--- Data Processing Pipeline ---")

# Simulate data from a CSV file
raw_data = [
    ("Alice", "Engineering", 75000, "New York"),
    ("Bob", "Marketing", 65000, "Los Angeles"),
    ("Charlie", "Engineering", 80000, "San Francisco"),
    ("Diana", "Sales", 60000, "Chicago"),
    ("Eve", "Engineering", 85000, "Seattle")
]

# Process data into structured format
employees = []
for name, department, salary, location in raw_data:
    employees.append({
        "name": name,
        "department": department,
        "salary": salary,
        "location": location
    })

# Analysis
departments = {}
for emp in employees:
    dept = emp["department"]
    if dept not in departments:
        departments[dept] = {"count": 0, "total_salary": 0}
    departments[dept]["count"] += 1
    departments[dept]["total_salary"] += emp["salary"]

print("Department Analysis:")
for dept, data in departments.items():
    avg_salary = data["total_salary"] / data["count"]
    print(f"{dept}: {data['count']} employees, avg salary: ${avg_salary:.0f}")

# Find highest paid employee
highest_paid = max(employees, key=lambda x: x["salary"])
print(f"\nHighest paid employee: {highest_paid['name']} (${highest_paid['salary']})")

print("\n" + "=" * 60)
print("END OF LISTS, DICTIONARIES, AND TUPLES")
print("=" * 60) 