#!/usr/bin/env python3
"""
Object-Oriented Programming in Python: Classes and Inheritance
This script demonstrates OOP concepts with practical examples.
"""

# ============================================================================
# BASIC CLASS DEFINITION
# ============================================================================

print("=" * 60)
print("BASIC CLASS DEFINITION")
print("=" * 60)

class Person:
    """A simple class representing a person"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age, city):
        """Constructor method - called when creating a new instance"""
        self.name = name      # Instance variable
        self.age = age        # Instance variable
        self.city = city      # Instance variable
        self._private_var = "This is private"  # Convention for private
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name}, {self.age} years old from {self.city}"
    
    def have_birthday(self):
        """Method that modifies instance state"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old"
    
    def get_info(self):
        """Return person information as dictionary"""
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "species": self.species
        }
    
    @classmethod    
    def create_anonymous(cls):
        """Class method - creates a person with default values"""
        return cls("Anonymous", 0, "Unknown")
    
    @staticmethod
    def is_adult(age):
        """Static method - doesn't need instance or class"""
        return age >= 18
    
    def __str__(self):
        """String representation of the object"""
        return f"Person({self.name}, {self.age}, {self.city})"
    
    def __repr__(self):
        """Detailed string representation for debugging"""
        return f"Person(name='{self.name}', age={self.age}, city='{self.city}')"

# Creating instances
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "Los Angeles")

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Introduction: {person1.introduce()}")
print(f"Birthday: {person1.have_birthday()}")
print(f"Info: {person1.get_info()}")

# Using class method
anonymous = Person.create_anonymous()
print(f"Anonymous person: {anonymous}")

# Using static method
print(f"Is 20 adult? {Person.is_adult(20)}")
print(f"Is 15 adult? {Person.is_adult(15)}")

# ============================================================================
# INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("INHERITANCE")
print("=" * 60)

class Employee(Person):
    """Employee class inheriting from Person"""
    
    def __init__(self, name, age, city, employee_id, salary, department):
        # Call parent class constructor
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
    
    def introduce(self):
        """Override parent method"""
        base_intro = super().introduce()
        return f"{base_intro}. I work in {self.department} department."
    
    def get_salary_info(self):
        """New method specific to Employee"""
        return f"Employee ID: {self.employee_id}, Salary: ${self.salary:,.2f}"
    
    def give_raise(self, percentage):
        """Method to give raise"""
        self.salary *= (1 + percentage / 100)
        return f"Raise given! New salary: ${self.salary:,.2f}"
    
    def __str__(self):
        return f"Employee({self.name}, {self.department}, ${self.salary:,.0f})"

class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name, age, city, student_id, major, gpa):
        super().__init__(name, age, city)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.courses = []
    
    def add_course(self, course):
        """Add a course to student's schedule"""
        self.courses.append(course)
        return f"Added course: {course}"
    
    def get_academic_info(self):
        """Get academic information"""
        return {
            "student_id": self.student_id,
            "major": self.major,
            "gpa": self.gpa,
            "courses": self.courses
        }
    
    def introduce(self):
        """Override parent method"""
        base_intro = super().introduce()
        return f"{base_intro}. I'm studying {self.major} with GPA {self.gpa}."

# Testing inheritance
employee = Employee("Charlie", 28, "San Francisco", "EMP001", 75000, "Engineering")
student = Student("Diana", 20, "Boston", "STU001", "Computer Science", 3.8)

print(f"Employee: {employee}")
print(f"Employee intro: {employee.introduce()}")
print(f"Salary info: {employee.get_salary_info()}")
print(f"After raise: {employee.give_raise(10)}")

print(f"\nStudent: {student}")
print(f"Student intro: {student.introduce()}")
print(f"Added course: {student.add_course('Python Programming')}")
print(f"Added course: {student.add_course('Data Structures')}")
print(f"Academic info: {student.get_academic_info()}")

# ============================================================================
# MULTIPLE INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("MULTIPLE INHERITANCE")
print("=" * 60)

class Contact:
    """Mixin class for contact information"""
    
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
    
    def get_contact_info(self):
        return f"Email: {self.email}, Phone: {self.phone}"

class Address:
    """Mixin class for address information"""
    
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"

class Customer(Person, Contact, Address):
    """Customer class with multiple inheritance"""
    
    def __init__(self, name, age, email, phone, street, city, state, zip_code):
        # Initialize all parent classes
        Person.__init__(self, name, age, city)
        Contact.__init__(self, email, phone)
        Address.__init__(self, street, city, state, zip_code)
        self.orders = []
    
    def place_order(self, order):
        """Place a new order"""
        self.orders.append(order)
        return f"Order placed: {order}"
    
    def get_customer_info(self):
        """Get complete customer information"""
        return {
            "personal": self.get_info(),
            "contact": self.get_contact_info(),
            "address": self.get_full_address(),
            "orders": self.orders
        }

# Testing multiple inheritance
customer = Customer(
    "Eve", 35, "eve@email.com", "555-0123",
    "123 Main St", "Chicago", "IL", "60601"
)

print(f"Customer: {customer}")
print(f"Contact: {customer.get_contact_info()}")
print(f"Address: {customer.get_full_address()}")
print(f"Order: {customer.place_order('Laptop')}")
print(f"Order: {customer.place_order('Mouse')}")
print(f"Customer info: {customer.get_customer_info()}")

# ============================================================================
# ABSTRACT CLASSES AND INTERFACES
# ============================================================================

print("\n" + "=" * 60)
print("ABSTRACT CLASSES AND INTERFACES")
print("=" * 60)

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def describe(self):
        """Concrete method - can be used by all subclasses"""
        return f"A {self.color} shape with area {self.area():.2f} and perimeter {self.perimeter():.2f}"

class Circle(Shape):
    """Circle class implementing Shape"""
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle class implementing Shape"""
    
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Testing abstract classes
circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)

print(f"Circle: {circle.describe()}")
print(f"Rectangle: {rectangle.describe()}")

# ============================================================================
# ENCAPSULATION AND PROPERTIES
# ============================================================================

print("\n" + "=" * 60)
print("ENCAPSULATION AND PROPERTIES")
print("=" * 60)

class BankAccount:
    """Bank account with encapsulation"""
    
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder  # Protected attribute
        self._balance = initial_balance        # Protected attribute
        self._transactions = []                # Protected attribute
    
    @property
    def balance(self):
        """Property to get balance (read-only)"""
        return self._balance
    
    @property
    def account_holder(self):
        """Property to get account holder (read-only)"""
        return self._account_holder
    
    @property
    def transactions(self):
        """Property to get transactions (read-only)"""
        return self._transactions.copy()  # Return copy to prevent modification
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposit: +${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrawal: -${amount:.2f}")
            return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
    
    def get_statement(self):
        """Get account statement"""
        return {
            "account_holder": self._account_holder,
            "balance": self._balance,
            "transactions": self._transactions.copy()
        }

# Testing encapsulation
account = BankAccount("Frank", 1000)
print(f"Account holder: {account.account_holder}")
print(f"Initial balance: ${account.balance:.2f}")

print(f"Deposit: {account.deposit(500)}")
print(f"Withdraw: {account.withdraw(200)}")
print(f"Withdraw: {account.withdraw(2000)}")  # Should fail
print(f"Deposit: {account.deposit(100)}")

print(f"Statement: {account.get_statement()}")

# ============================================================================
# POLYMORPHISM
# ============================================================================

print("\n" + "=" * 60)
print("POLYMORPHISM")
print("=" * 60)

class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Base speak method"""
        return "Some sound"
    
    def move(self):
        """Base move method"""
        return "Some movement"

class Dog(Animal):
    """Dog class"""
    
    def speak(self):
        return f"{self.name} says: Woof!"
    
    def move(self):
        return f"{self.name} runs on four legs"

class Cat(Animal):
    """Cat class"""
    
    def speak(self):
        return f"{self.name} says: Meow!"
    
    def move(self):
        return f"{self.name} walks gracefully"

class Bird(Animal):
    """Bird class"""
    
    def speak(self):
        return f"{self.name} says: Tweet!"
    
    def move(self):
        return f"{self.name} flies through the air"

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

print("Animal sounds:")
for animal in animals:
    print(f"  {animal.speak()}")

print("\nAnimal movements:")
for animal in animals:
    print(f"  {animal.move()}")

# Function that works with any animal
def make_animal_speak(animal):
    """Function demonstrating polymorphism"""
    return animal.speak() # the speak method is different for each animal but the function is the same

print(f"\nPolymorphic function: {make_animal_speak(Dog('Rex'))}")

# ============================================================================
# PRACTICAL EXAMPLE: LIBRARY MANAGEMENT SYSTEM
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)

class Book:
    """Book class"""
    
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False
        self.borrower = None
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({status})"

class LibraryMember(Person):
    """Library member class"""
    
    def __init__(self, name, age, city, member_id):
        super().__init__(name, age, city)
        self.member_id = member_id
        self.borrowed_books = []
        self.fines = 0.0
    
    def borrow_book(self, book):
        """Borrow a book"""
        if not book.is_borrowed:
            book.is_borrowed = True
            book.borrower = self
            self.borrowed_books.append(book)
            return f"Successfully borrowed '{book.title}'"
        else:
            return f"'{book.title}' is already borrowed"
    
    def return_book(self, book):
        """Return a book"""
        if book in self.borrowed_books:
            book.is_borrowed = False
            book.borrower = None
            self.borrowed_books.remove(book)
            return f"Successfully returned '{book.title}'"
        else:
            return f"You haven't borrowed '{book.title}'"
    
    def get_borrowed_books(self):
        """Get list of borrowed books"""
        return [book.title for book in self.borrowed_books]

class Library:
    """Library class"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
        return f"Added '{book.title}' to the library"
    
    def add_member(self, member):
        """Add a member to the library"""
        self.members.append(member)
        return f"Added member {member.name} to the library"
    
    def search_books(self, query):
        """Search for books by title or author"""
        results = []
        query = query.lower()
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results
    
    def get_available_books(self):
        """Get all available books"""
        return [book for book in self.books if not book.is_borrowed]
    
    def get_borrowed_books(self):
        """Get all borrowed books"""
        return [book for book in self.books if book.is_borrowed]

# Testing the library system
library = Library("Central Library")

# Add books
books = [
    Book("Python Programming", "John Smith", "1234567890", 2020),
    Book("Data Science", "Jane Doe", "0987654321", 2021),
    Book("Machine Learning", "Bob Johnson", "1122334455", 2019),
    Book("Web Development", "Alice Brown", "5566778899", 2022)
]

for book in books:
    library.add_book(book)

# Add members
members = [
    LibraryMember("Charlie Wilson", 25, "New York", "M001"),
    LibraryMember("Diana Davis", 30, "Los Angeles", "M002")
]

for member in members:
    library.add_member(member)

# Test the system
print(f"Library: {library.name}")
print(f"Total books: {len(library.books)}")
print(f"Available books: {len(library.get_available_books())}")

# Search for books
search_results = library.search_books("python")
print(f"\nSearch results for 'python': {[book.title for book in search_results]}")

# Borrow books
member = members[0]
print(f"\n{member.borrow_book(books[0])}")
print(f"{member.borrow_book(books[1])}")

print(f"Borrowed books: {member.get_borrowed_books()}")
print(f"Available books: {len(library.get_available_books())}")

# Return a book
print(f"{member.return_book(books[0])}")
print(f"Borrowed books after return: {member.get_borrowed_books()}")

print("\n" + "=" * 60)
print("END OF OBJECT-ORIENTED PROGRAMMING")
print("=" * 60) 