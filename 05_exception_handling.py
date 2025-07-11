#!/usr/bin/env python3
"""
Exception Handling in Python: Error Management and Debugging
This script demonstrates various exception handling techniques and best practices.
"""

import sys
import traceback
from typing import Union, List, Dict, Any

# ============================================================================
# BASIC EXCEPTION HANDLING
# ============================================================================

print("=" * 60)
print("BASIC EXCEPTION HANDLING")
print("=" * 60)

def basic_exception_example():
    """Demonstrate basic try-except blocks"""
    
    # Example 1: Division by zero
    print("--- Division by Zero ---")
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero - {e}")
    
    # Example 2: File not found
    print("\n--- File Not Found ---")
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    
    # Example 3: Type conversion
    print("\n--- Type Conversion ---")
    try:
        number = int("abc")
        print(f"Number: {number}")
    except ValueError as e:
        print(f"Error: Invalid conversion - {e}")
    
    # Example 4: Index out of range
    print("\n--- Index Out of Range ---")
    numbers = [1, 2, 3, 4, 5]
    try:
        value = numbers[10]
        print(f"Value: {value}")
    except IndexError as e:
        print(f"Error: Index out of range - {e}")

basic_exception_example()

# ============================================================================
# MULTIPLE EXCEPTION TYPES
# ============================================================================

print("\n" + "=" * 60)
print("MULTIPLE EXCEPTION TYPES")
print("=" * 60)

def multiple_exceptions_example():
    """Handle multiple types of exceptions"""
    
    # Example 1: Multiple except blocks
    print("--- Multiple Except Blocks ---")
    
    def process_data(data):
        try:
            if isinstance(data, str):
                return int(data)
            elif isinstance(data, list):
                return data[0]  # returns the first element of the list
            elif isinstance(data, dict):
                return data["key"]
            else:
                return data / 2
        except ValueError as e:
            print(f"ValueError: {e}")
            return None
        except IndexError as e:
            print(f"IndexError: {e}")
            return None
        except KeyError as e:
            print(f"KeyError: {e}")
            return None
        except TypeError as e:
            print(f"TypeError: {e}")
            return None
    
    # Test different scenarios
    test_cases = ["123", "abc", [1, 2, 3], [], {"key": "value"}, {}, 10, "hello"]  # 1st is a string, 2nd is a string, 3rd is a list, 4th is an empty list, 5th is a dictionary, 6th is an empty dictionary, 7th is an integer, 8th is a string
    
    for test_case in test_cases:
        print(f"Processing {test_case}: ", end="")
        result = process_data(test_case)
        print(f"Result = {result}")
    
    # Example 2: Single except block with multiple exception types
    print("\n--- Single Except with Multiple Types ---")
    
    def safe_operation(operation_type, data):
        try:
            if operation_type == "divide":
                return 100 / data
            elif operation_type == "index":
                return data[5]
            elif operation_type == "convert":
                return int(data)
        except (ZeroDivisionError, IndexError, ValueError) as e:
            print(f"Operation failed: {e}")
            return None
    
    print(f"Divide by 0: {safe_operation('divide', 0)}")
    print(f"Index [1,2,3][5]: {safe_operation('index', [1, 2, 3])}")
    print(f"Convert 'abc': {safe_operation('convert', 'abc')}")

multiple_exceptions_example()

# ============================================================================
# ELSE AND FINALLY CLAUSES
# ============================================================================

print("\n" + "=" * 60)
print("ELSE AND FINALLY CLAUSES")
print("=" * 60)

def else_finally_example():
    """Demonstrate else and finally clauses"""
    
    # Example 1: Using else clause
    print("--- Else Clause ---")
    
    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None 
        else:              # if no exception is raised, the else block is executed
            print("Division successful!")
            return result
    
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print(f"10 / 0 = {divide_numbers(10, 0)}")
    
    # Example 2: Using finally clause
    print("\n--- Finally Clause ---")
    
    def file_operation(filename):
        file = None
        try:
            file = open(filename, "w")
            file.write("Hello, World!")
            print("File written successfully")
        except IOError as e:
            print(f"IO Error: {e}")
        finally:            # finally block is executed regardless of whether an exception is raised or not
            if file:
                file.close()
                print("File closed (finally block)")
    
    file_operation("test_file.txt")
    
    # Example 3: Using both else and finally
    print("\n--- Else and Finally Together ---")
    
    def process_user_input():
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
        except ValueError:
            print("Invalid input - not a number")
            return None
        except KeyboardInterrupt:
            print("\nInput cancelled by user")
            return None
        else:
            print("Input processed successfully")
            return number
        finally:
            print("Input processing completed (finally block)")
    
    # Uncomment to test interactive input
    # result = process_user_input()
    # print(f"Result: {result}")

else_finally_example()

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)

# Define custom exception classes
class ValidationError(Exception):
    """Base class for validation errors"""
    pass

class AgeValidationError(ValidationError):
    """Raised when age validation fails"""
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.age}"

class EmailValidationError(ValidationError):
    """Raised when email validation fails"""
    def __init__(self, email, message="Invalid email format"):
        self.email = email
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.email}"

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds. Balance: ${balance}, Required: ${amount}"
        super().__init__(self.message)

# Example using custom exceptions
def custom_exceptions_example():
    """Demonstrate custom exception usage"""
    
    # Example 1: Age validation
    def validate_age(age):
        if not isinstance(age, int):
            raise ValidationError(f"Age must be an integer, got {type(age)}")
        if age < 0:
            raise AgeValidationError(age, "Age cannot be negative")
        if age > 150:
            raise AgeValidationError(age, "Age seems unrealistic")
        return True
    
    # Example 2: Email validation
    def validate_email(email):
        if not isinstance(email, str):
            raise ValidationError(f"Email must be a string, got {type(email)}")
        if "@" not in email or "." not in email:
            raise EmailValidationError(email)
        return True
    
    # Example 3: Bank account
    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance
        
        def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            return amount
    
    # Test custom exceptions
    print("--- Testing Custom Exceptions ---")
    
    # Test age validation
    test_ages = [25, -5, 200, "twenty"]
    for age in test_ages:
        try:
            validate_age(age)
            print(f"Age {age} is valid")
        except AgeValidationError as e:
            print(f"Age validation failed: {e}")
        except ValidationError as e:
            print(f"Validation error: {e}")
    
    # Test email validation
    test_emails = ["user@example.com", "invalid-email", "user@", 123]
    for email in test_emails:
        try:
            validate_email(email)
            print(f"Email {email} is valid")
        except EmailValidationError as e:
            print(f"Email validation failed: {e}")
        except ValidationError as e:
            print(f"Validation error: {e}")
    
    # Test bank account
    account = BankAccount(100)
    try:
        print(f"Withdrawing $50: {account.withdraw(50)}")
        print(f"Withdrawing $100: {account.withdraw(100)}")
    except InsufficientFundsError as e:
        print(f"Bank error: {e}")

custom_exceptions_example()

# ============================================================================
# EXCEPTION HIERARCHY AND INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("EXCEPTION HIERARCHY AND INHERITANCE")
print("=" * 60)

def exception_hierarchy_example():
    """Demonstrate exception hierarchy and inheritance"""
    
    # Example 1: Catching base exception types
    print("--- Catching Base Exception Types ---")
    
    def process_data_safely(data):
        try:
            if isinstance(data, str):
                return int(data)
            elif isinstance(data, list):
                return data[0]
            elif isinstance(data, dict):
                return data["key"]
        except (ValueError, IndexError, KeyError) as e:
            print(f"Specific error: {e}")
            return None
        except Exception as e:
            print(f"General error: {e}")
            return None
    
    # Example 2: Exception hierarchy in practice
    print("\n--- Exception Hierarchy in Practice ---")
    
    class DataProcessor:
        def __init__(self):
            self.data = {}
        
        def add_item(self, key, value):
            try:
                if not isinstance(key, str):
                    raise TypeError("Key must be a string")
                if key in self.data:
                    raise KeyError(f"Key '{key}' already exists")
                self.data[key] = value
                return True
            except (TypeError, KeyError) as e:
                print(f"Data processing error: {e}")
                return False
            except Exception as e:
                print(f"Unexpected error: {e}")
                return False
        
        def get_item(self, key):
            try:
                return self.data[key]
            except KeyError:
                print(f"Key '{key}' not found")
                return None
        
        def process_numeric_data(self, key):
            try:
                value = self.data[key]
                if isinstance(value, (int, float)):
                    return value * 2
                else:
                    return float(value) * 2
            except (KeyError, ValueError) as e:
                print(f"Error processing numeric data: {e}")
                return None
    
    # Test the data processor
    processor = DataProcessor()
    
    print(f"Add item 'name': {processor.add_item('name', 'Alice')}")
    print(f"Add item 'age': {processor.add_item('age', 25)}")
    print(f"Add item 'name': {processor.add_item('name', 'Bob')}")  # Duplicate key
    print(f"Add item 123: {processor.add_item(123, 'invalid')}")    # Invalid key type
    
    print(f"Get 'name': {processor.get_item('name')}")
    print(f"Get 'nonexistent': {processor.get_item('nonexistent')}")
    
    print(f"Process 'age': {processor.process_numeric_data('age')}")
    print(f"Process 'name': {processor.process_numeric_data('name')}")

exception_hierarchy_example()

# ============================================================================
# CONTEXT MANAGERS AND EXCEPTION HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS AND EXCEPTION HANDLING")
print("=" * 60)

def context_manager_example():
    """Demonstrate context managers with exception handling"""
    
    # Example 1: Custom context manager
    class DatabaseConnection:
        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.connection = None
        
        def __enter__(self):
            print(f"Connecting to {self.host}:{self.port}")
            # Simulate connection
            self.connection = f"Connection to {self.host}:{self.port}"
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"Closing connection to {self.host}:{self.port}")
            self.connection = None
            if exc_type is not None:
                print(f"Connection closed due to error: {exc_val}")
            return False  # Don't suppress the exception
    
    # Example 2: Using context manager
    print("--- Database Connection Example ---")
    
    try:
        with DatabaseConnection("localhost", 5432) as db:
            print(f"Using connection: {db.connection}")
            # Simulate some operation
            raise ValueError("Simulated database error")
    except ValueError as e:
        print(f"Caught error: {e}")
    
    # Example 3: File processing with context manager
    print("\n--- File Processing Example ---")
    
    class FileProcessor:
        def __init__(self, filename):
            self.filename = filename
            self.file = None
        
        def __enter__(self):
            try:
                self.file = open(self.filename, "w")
                return self
            except IOError as e:
                print(f"Failed to open file: {e}")
                raise
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
                print(f"File {self.filename} closed")
            if exc_type is not None:
                print(f"File processing error: {exc_val}")
            return False
        
        def write_data(self, data):
            if self.file:
                self.file.write(data)
                print(f"Data written to {self.filename}")
    
    try:
        with FileProcessor("output.txt") as processor:
            processor.write_data("Hello, World!\n")
            processor.write_data("This is a test file.\n")
    except Exception as e:
        print(f"File processing failed: {e}")

context_manager_example()

# ============================================================================
# DEBUGGING AND TRACEBACK
# ============================================================================

print("\n" + "=" * 60)
print("DEBUGGING AND TRACEBACK")
print("=" * 60)

def debugging_example():
    """Demonstrate debugging and traceback handling"""
    
    # Example 1: Basic traceback
    print("--- Basic Traceback ---")
    
    def function_a():
        return function_b()
    
    def function_b():
        return function_c()
    
    def function_c():
        raise ValueError("Error in function_c")
    
    try:
        function_a()
    except ValueError as e:
        print(f"Error: {e}")
        print("Traceback:")
        traceback.print_exc()
    
    # Example 2: Custom error reporting
    print("\n--- Custom Error Reporting ---")
    
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero")
            print(f"Arguments: a={a}, b={b}")
            print("Stack trace:")
            traceback.print_exc()
            return None
        except TypeError as e:
            print(f"Error: Invalid types - {e}")
            print(f"Arguments: a={a} (type: {type(a)}), b={b} (type: {type(b)})")
            return None
    
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"'10' / 2 = {safe_divide('10', 2)}")
    
    # Example 3: Exception chaining
    print("\n--- Exception Chaining ---")
    
    def process_user_data(user_id):
        try:
            # Simulate database lookup
            if user_id == 0:
                raise ValueError("Invalid user ID")
            
            # Simulate data processing
            if user_id == 1:
                raise RuntimeError("Data processing failed")
            
            return f"User {user_id} processed successfully"
        
        except (ValueError, RuntimeError) as e:
            # Chain the exception with additional context
            raise Exception(f"Failed to process user {user_id}") from e
    
    for user_id in [0, 1, 2]:
        try:
            result = process_user_data(user_id)
            print(result)
        except Exception as e:
            print(f"Error processing user {user_id}: {e}")
            if e.__cause__:
                print(f"Caused by: {e.__cause__}")

debugging_example()

# ============================================================================
# PRACTICAL EXAMPLE: DATA VALIDATION SYSTEM
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: DATA VALIDATION SYSTEM")
print("=" * 60)

class DataValidationSystem:
    """A comprehensive data validation system with exception handling"""
    
    def __init__(self):
        self.validation_rules = {}
        self.validation_errors = []
    
    def add_validation_rule(self, field_name, rule_func, error_message):
        """Add a validation rule for a field"""
        if field_name not in self.validation_rules:
            self.validation_rules[field_name] = []
        self.validation_rules[field_name].append((rule_func, error_message))
    
    def validate_field(self, field_name, value):
        """Validate a single field"""
        if field_name not in self.validation_rules:
            return True
        
        for rule_func, error_message in self.validation_rules[field_name]:
            try:
                if not rule_func(value):
                    raise ValidationError(f"{field_name}: {error_message}")
            except Exception as e:
                self.validation_errors.append(str(e))
                return False
        return True
    
    def validate_data(self, data):
        """Validate all fields in the data"""
        self.validation_errors.clear()
        is_valid = True
        
        for field_name, value in data.items():
            if not self.validate_field(field_name, value):
                is_valid = False
        
        return is_valid
    
    def get_errors(self):
        """Get all validation errors"""
        return self.validation_errors.copy()

def practical_example():
    """Demonstrate the data validation system"""
    
    # Create validation system
    validator = DataValidationSystem()
    
    # Add validation rules
    validator.add_validation_rule("name", 
                                 lambda x: isinstance(x, str) and len(x.strip()) > 0,
                                 "Name must be a non-empty string")
    
    validator.add_validation_rule("age",
                                 lambda x: isinstance(x, int) and 0 <= x <= 150,
                                 "Age must be an integer between 0 and 150")
    
    validator.add_validation_rule("email",
                                 lambda x: isinstance(x, str) and "@" in x and "." in x,
                                 "Email must be a valid email address")
    
    validator.add_validation_rule("salary",
                                 lambda x: isinstance(x, (int, float)) and x >= 0,
                                 "Salary must be a non-negative number")
    
    # Test data
    test_cases = [
        {
            "name": "Alice Johnson",
            "age": 25,
            "email": "alice@example.com",
            "salary": 75000
        },
        {
            "name": "",
            "age": 200,
            "email": "invalid-email",
            "salary": -5000
        },
        {
            "name": "Bob Smith",
            "age": "thirty",
            "email": "bob@company.com",
            "salary": 65000
        }
    ]
    
    # Validate each test case
    for i, test_data in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Data: {test_data}")
        
        try:
            if validator.validate_data(test_data):
                print("✅ Validation passed")
            else:
                print("❌ Validation failed")
                print("Errors:")
                for error in validator.get_errors():
                    print(f"  - {error}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

practical_example()

print("\n" + "=" * 60)
print("END OF EXCEPTION HANDLING")
print("=" * 60) 