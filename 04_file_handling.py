#!/usr/bin/env python3
"""
File Handling in Python: Reading, Writing, and Data Processing
This script demonstrates various file operations and data formats.
"""

import os
import json  
import csv  
import pickle 
import shutil  
from pathlib import Path

# ============================================================================
# BASIC FILE OPERATIONS
# ============================================================================

print("=" * 60)
print("BASIC FILE OPERATIONS")
print("=" * 60)

# Create a sample directory for our files
sample_dir = Path("sample_files")
sample_dir.mkdir(exist_ok=True)

# Writing text files
print("--- Writing Text Files ---")

# Method 1: Using 'with' statement (recommended)
with open(sample_dir / "sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("We can write various types of content here.\n")

print("Created sample.txt")

# Method 2: Using file object directly
file = open(sample_dir / "sample2.txt", "w", encoding="utf-8")
file.write("This is another way to write files.\n")
file.write("But using 'with' statement is preferred.\n")
file.close()

print("Created sample2.txt")

# Reading text files
print("\n--- Reading Text Files ---")

# Method 1: Read entire file
with open(sample_dir / "sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Full content:")
    print(content)

# Method 2: Read line by line
print("\nLine by line:")
with open(sample_dir / "sample.txt", "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.rstrip()}")

# Method 3: Read all lines into a list
with open(sample_dir / "sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"\nAll lines as list: {lines}")

# Appending to files
print("\n--- Appending to Files ---")

with open(sample_dir / "sample.txt", "a", encoding="utf-8") as file:
    file.write("\nThis line was appended later.\n")
    file.write("Appending is useful for logs and data collection.\n")

print("Appended content to sample.txt")

# Reading the updated file
with open(sample_dir / "sample.txt", "r", encoding="utf-8") as file:
    print("Updated content:")
    print(file.read())

# ============================================================================
# CSV FILE HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("CSV FILE HANDLING")
print("=" * 60)

# Writing CSV files
print("--- Writing CSV Files ---")

# Sample data
employees = [
    ["Name", "Age", "Department", "Salary"],
    ["Alice Johnson", 25, "Engineering", 75000],
    ["Bob Smith", 30, "Marketing", 65000],
    ["Charlie Brown", 28, "Engineering", 80000],
    ["Diana Davis", 35, "Sales", 70000],
    ["Eve Wilson", 27, "Engineering", 78000]
]

# Method 1: Using csv.writer
with open(sample_dir / "employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print("Created employees.csv using csv.writer")

# Method 2: Using csv.DictWriter (more structured)
employee_data = [
    {"Name": "Frank Miller", "Age": 32, "Department": "HR", "Salary": 60000},
    {"Name": "Grace Lee", "Age": 29, "Department": "Engineering", "Salary": 82000},
    {"Name": "Henry Taylor", "Age": 31, "Department": "Marketing", "Salary": 68000}
]

with open(sample_dir / "employees_dict.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "Department", "Salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row
    writer.writerows(employee_data)

print("Created employees_dict.csv using csv.DictWriter")

# Reading CSV files
print("\n--- Reading CSV Files ---")

# Method 1: Using csv.reader
with open(sample_dir / "employees.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("CSV content using csv.reader:")
    for row in reader:
        print(f"  {row}")

# Method 2: Using csv.DictReader
with open(sample_dir / "employees_dict.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\nCSV content using csv.DictReader:")
    for row in reader:
        print(f"  {row}")

# Processing CSV data
print("\n--- Processing CSV Data ---")

with open(sample_dir / "employees.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    
    # Calculate average salary
    salaries = []
    engineering_employees = []
    
    for row in reader:
        name, age, dept, salary = row
        salaries.append(float(salary))
        if dept == "Engineering":
            engineering_employees.append(name)
    
    avg_salary = sum(salaries) / len(salaries)
    print(f"Average salary: ${avg_salary:,.2f}")
    print(f"Engineering employees: {engineering_employees}")

# ============================================================================
# JSON FILE HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("JSON FILE HANDLING")
print("=" * 60)

# Writing JSON files
print("--- Writing JSON Files ---")

# Sample data structure
company_data = {
    "company_name": "TechCorp",
    "founded": 2010,
    "employees": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "position": "Senior Developer",
            "skills": ["Python", "JavaScript", "SQL"],
            "salary": 85000,
            "active": True
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "position": "Product Manager",
            "skills": ["Product Management", "Agile", "Analytics"],
            "salary": 95000,
            "active": True
        },
        {
            "id": 3,
            "name": "Charlie Brown",
            "position": "Designer",
            "skills": ["UI/UX", "Figma", "Adobe Creative Suite"],
            "salary": 75000,
            "active": False
        }
    ],
    "departments": ["Engineering", "Product", "Design", "Marketing"],
    "location": {
        "city": "San Francisco",
        "state": "CA",
        "country": "USA"
    }
}

# Write JSON with pretty formatting
with open(sample_dir / "company.json", "w", encoding="utf-8") as file:
    json.dump(company_data, file, indent=2, ensure_ascii=False) # indent=2 is for pretty formatting, ensure_ascii=False is to avoid encoding issues

print("Created company.json")

# Reading JSON files
print("\n--- Reading JSON Files ---")

with open(sample_dir / "company.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("Loaded JSON data:")
print(f"Company: {loaded_data['company_name']}")
print(f"Founded: {loaded_data['founded']}")
print(f"Location: {loaded_data['location']['city']}, {loaded_data['location']['state']}")
print(f"Number of employees: {len(loaded_data['employees'])}")

# Processing JSON data
print("\n--- Processing JSON Data ---")

# Find active employees
active_employees = [emp for emp in loaded_data['employees'] if emp['active']]
print(f"Active employees: {len(active_employees)}")

# Calculate average salary
salaries = [emp['salary'] for emp in loaded_data['employees']]
avg_salary = sum(salaries) / len(salaries)
print(f"Average salary: ${avg_salary:,.2f}")

# Find employees with Python skills
python_developers = [emp for emp in loaded_data['employees'] if 'Python' in emp['skills']]
print(f"Python developers: {[emp['name'] for emp in python_developers]}")

# ============================================================================
# BINARY FILE HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("BINARY FILE HANDLING")
print("=" * 60)

# Writing binary files
print("--- Writing Binary Files ---")

# Sample binary data
sample_data = b"Hello, this is binary data!\nIt can contain any bytes.\n"

with open(sample_dir / "sample.bin", "wb") as file:
    file.write(sample_data)

print("Created sample.bin")

# Reading binary files
with open(sample_dir / "sample.bin", "rb") as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"Decoded content: {binary_content.decode('utf-8')}")

# Pickle for Python object serialization
print("\n--- Pickle Serialization ---")

# Sample Python object
python_object = {
    "numbers": [1, 2, 3, 4, 5],
    "text": "Hello from pickle!",
    "nested": {"key": "value", "list": [10, 20, 30]}
}

# Serialize object
with open(sample_dir / "data.pickle", "wb") as file:
    pickle.dump(python_object, file)

print("Serialized object to data.pickle")

# Deserialize object
with open(sample_dir / "data.pickle", "rb") as file:
    loaded_object = pickle.load(file)

print(f"Deserialized object: {loaded_object}")

# ============================================================================
# FILE AND DIRECTORY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("FILE AND DIRECTORY OPERATIONS")
print("=" * 60)

# File information
print("--- File Information ---")

sample_file = sample_dir / "sample.txt"
print(f"File exists: {sample_file.exists()}")
print(f"File size: {sample_file.stat().st_size} bytes")
print(f"File path: {sample_file.absolute()}")
print(f"File name: {sample_file.name}")
print(f"File extension: {sample_file.suffix}")

# Directory operations
print("\n--- Directory Operations ---")

# List files in directory
print("Files in sample_files directory:")
for item in sample_dir.iterdir():
    if item.is_file():
        print(f"  File: {item.name} ({item.stat().st_size} bytes)")
    elif item.is_dir():
        print(f"  Directory: {item.name}")

# Create subdirectories
subdir = sample_dir / "subfolder"
subdir.mkdir(exist_ok=True)

# Copy files
shutil.copy2(sample_dir / "sample.txt", subdir / "sample_copy.txt")
print(f"Copied sample.txt to {subdir / 'sample_copy.txt'}")

# Move files
shutil.move(sample_dir / "sample2.txt", subdir / "sample2_moved.txt")
print(f"Moved sample2.txt to {subdir / 'sample2_moved.txt'}")

# ============================================================================
# PRACTICAL EXAMPLE: LOG FILE PROCESSOR
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: LOG FILE PROCESSOR")
print("=" * 60)

# Create a sample log file
log_content = """2024-01-15 10:30:15 INFO User login successful - user_id: 12345
2024-01-15 10:32:22 ERROR Database connection failed - retry_count: 3
2024-01-15 10:35:10 INFO User logout - user_id: 12345
2024-01-15 11:15:30 WARNING High memory usage detected - usage: 85%
2024-01-15 11:20:45 INFO User login successful - user_id: 67890
2024-01-15 11:25:12 ERROR File not found - path: /data/config.json
2024-01-15 12:00:00 INFO Daily backup completed - files: 1500
2024-01-15 12:15:30 WARNING Disk space low - available: 2.5GB
2024-01-15 13:45:22 INFO User login successful - user_id: 11111
2024-01-15 14:20:15 ERROR Network timeout - duration: 30s
"""

with open(sample_dir / "app.log", "w", encoding="utf-8") as file:
    file.write(log_content)

print("Created sample log file: app.log")

# Log file processor
class LogProcessor:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.logs = []
    
    def load_logs(self):
        """Load and parse log entries"""
        with open(self.log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    self.logs.append(self.parse_log_entry(line))
    
    def parse_log_entry(self, line):
        """Parse a single log entry"""
        try:
            # Split by first two spaces to separate timestamp and level
            parts = line.split(" ", 2)
            timestamp = f"{parts[0]} {parts[1]}"
            remaining = parts[2]
            
            # Extract log level and message
            if " INFO " in remaining:
                level, message = "INFO", remaining.split(" INFO ", 1)[1]
            elif " ERROR " in remaining:
                level, message = "ERROR", remaining.split(" ERROR ", 1)[1]
            elif " WARNING " in remaining:
                level, message = "WARNING", remaining.split(" WARNING ", 1)[1]
            else:
                level, message = "UNKNOWN", remaining
            
            return {
                "timestamp": timestamp,
                "level": level,
                "message": message
            }
        except Exception as e:
            return {"timestamp": "", "level": "PARSE_ERROR", "message": line}
    
    def get_logs_by_level(self, level):
        """Get all logs of a specific level"""
        return [log for log in self.logs if log["level"] == level]
    
    def get_error_count(self):
        """Get count of error logs"""
        return len(self.get_logs_by_level("ERROR"))
    
    def get_warning_count(self):
        """Get count of warning logs"""
        return len(self.get_logs_by_level("WARNING"))
    
    def export_summary(self, output_file):
        """Export log summary to JSON"""
        summary = {
            "total_logs": len(self.logs),
            "error_count": self.get_error_count(),
            "warning_count": self.get_warning_count(),
            "info_count": len(self.get_logs_by_level("INFO")),
            "errors": self.get_logs_by_level("ERROR"),
            "warnings": self.get_logs_by_level("WARNING")
        }
        
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=2)
        
        return summary

# Process the log file
processor = LogProcessor(sample_dir / "app.log")
processor.load_logs()

print(f"Total log entries: {len(processor.logs)}")
print(f"Error count: {processor.get_error_count()}")
print(f"Warning count: {processor.get_warning_count()}")

# Export summary
summary = processor.export_summary(sample_dir / "log_summary.json")
print(f"Log summary exported to log_summary.json")

# Display errors
print("\nError logs:")
for error in processor.get_logs_by_level("ERROR"):
    print(f"  {error['timestamp']}: {error['message']}")

# ============================================================================
# CLEANUP
# ============================================================================

print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

# List all created files
print("Files created in this session:")
for item in sample_dir.rglob("*"):
    if item.is_file():
        print(f"  {item.relative_to(sample_dir)}")

print("\n" + "=" * 60)
print("END OF FILE HANDLING")
print("=" * 60)