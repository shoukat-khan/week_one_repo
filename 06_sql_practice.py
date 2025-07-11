#!/usr/bin/env python3
"""
PostgreSQL and SQL Practice with Python
This script demonstrates connecting to PostgreSQL, reading CSV files, and performing SQL operations.
"""

import os
import csv
import json
import shutil
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from psycopg2 import Error, IntegrityError

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# DATABASE CONNECTION SETUP
# ============================================================================

print("=" * 60)
print("POSTGRESQL AND SQL PRACTICE WITH ENV VARIABLES")
print("=" * 60)

def get_db_connection(database_name=None):
    """Create database connection using environment variables"""
    try:
        # Use provided database name or default from environment
        db_name = database_name or os.getenv('DB_NAME', 'postgres')
        
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            database=db_name,
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD')
        )
        print(f"✅ Successfully connected to PostgreSQL database: {db_name}")
        return connection
    except Error as e:
        print(f"❌ Error connecting to PostgreSQL database '{db_name}': {e}")
        return None

def create_database_if_not_exists():
    """Create the target database if it doesn't exist and return connection to it"""
    try:
        # First, connect to default postgres database to create target database
        admin_connection = get_db_connection()  # Uses default DB_NAME (postgres)
        if not admin_connection:
            return None
        
        admin_connection.autocommit = True
        cursor = admin_connection.cursor()
        
        # Get target database name from environment
        target_db = os.getenv('TARGET_DB_NAME', 'python_learning')
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (target_db,))
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {target_db}")
            print(f"✅ Database '{target_db}' created successfully")
        else:
            print(f"✅ Database '{target_db}' already exists")
        
        cursor.close()
        admin_connection.close()
        
        # Now connect to the target database using the same function
        return get_db_connection(target_db)
        
    except Error as e:
        print(f"❌ Error creating database: {e}")
        return None

# ============================================================================
# ENVIRONMENT VALIDATION
# ============================================================================

def validate_environment():
    """Validate that all required environment variables are set"""
    required_vars = ['DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("Please check your .env file and ensure all variables are set.")
        return False
    
    print("✅ All required environment variables are loaded")
    return True

# ============================================================================
# FILE CLEANUP
# ============================================================================

def cleanup_files():
    """Remove all generated files and directories"""
    print("\n🧹 Cleaning up files...")
    
    # Remove data_files directory
    data_dir = Path("data_files")
    if data_dir.exists():
        shutil.rmtree(data_dir)
        print("✅ Removed data_files directory")
    
    # Remove sample_files directory
    sample_dir = Path("sample_files")
    if sample_dir.exists():
        shutil.rmtree(sample_dir)
        print("✅ Removed sample_files directory")
    
    # Remove individual files
    files_to_remove = [
        "test_file.txt",
        "output.txt",
    ]
    
    for file_path in files_to_remove:
        if Path(file_path).exists():
            Path(file_path).unlink()
            print(f"✅ Removed {file_path}")

# ============================================================================
# DATA FILE CREATION
# ============================================================================

def create_sample_data_files():
    """Create sample data files for practice"""
    
    # Create data directory
    data_dir = Path("data_files")
    data_dir.mkdir(exist_ok=True)
    
    # Sample employee data
    employees_data = [
        {"id": 1, "name": "Alice Johnson", "age": 25, "department": "Engineering", "salary": 75000, "city": "New York"},
        {"id": 2, "name": "Bob Smith", "age": 30, "department": "Marketing", "salary": 65000, "city": "Los Angeles"},
        {"id": 3, "name": "Charlie Brown", "age": 28, "department": "Engineering", "salary": 80000, "city": "San Francisco"},
        {"id": 4, "name": "Diana Davis", "age": 35, "department": "Sales", "salary": 70000, "city": "Chicago"},
        {"id": 5, "name": "Eve Wilson", "age": 27, "department": "Engineering", "salary": 78000, "city": "Seattle"},
        {"id": 6, "name": "Frank Miller", "age": 32, "department": "HR", "salary": 60000, "city": "Boston"},
        {"id": 7, "name": "Grace Lee", "age": 29, "department": "Engineering", "salary": 82000, "city": "Austin"},
        {"id": 8, "name": "Henry Taylor", "age": 31, "department": "Marketing", "salary": 68000, "city": "Denver"}
    ]
    
    # Sample product data
    products_data = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99, "stock": 50},
        {"id": 2, "name": "Mouse", "category": "Electronics", "price": 25.99, "stock": 100},
        {"id": 3, "name": "Notebook", "category": "Stationery", "price": 5.99, "stock": 200},
        {"id": 4, "name": "Pen", "category": "Stationery", "price": 1.99, "stock": 500},
        {"id": 5, "name": "Headphones", "category": "Electronics", "price": 89.99, "stock": 30},
        {"id": 6, "name": "Coffee Mug", "category": "Kitchen", "price": 12.99, "stock": 75},
        {"id": 7, "name": "T-Shirt", "category": "Clothing", "price": 19.99, "stock": 150}
    ]
    
    # Sample order data
    orders_data = [
        {"id": 1, "employee_id": 1, "product_id": 1, "quantity": 1, "total_price": 999.99, "order_date": "2024-01-15"},
        {"id": 2, "employee_id": 1, "product_id": 2, "quantity": 2, "total_price": 51.98, "order_date": "2024-01-16"},
        {"id": 3, "employee_id": 2, "product_id": 3, "quantity": 5, "total_price": 29.95, "order_date": "2024-01-17"},
        {"id": 4, "employee_id": 3, "product_id": 4, "quantity": 10, "total_price": 19.90, "order_date": "2024-01-18"},
        {"id": 5, "employee_id": 4, "product_id": 5, "quantity": 1, "total_price": 89.99, "order_date": "2024-01-19"},
        {"id": 6, "employee_id": 5, "product_id": 6, "quantity": 3, "total_price": 38.97, "order_date": "2024-01-20"},
        {"id": 7, "employee_id": 6, "product_id": 7, "quantity": 2, "total_price": 39.98, "order_date": "2024-01-21"}
    ]
    
    # Write employees to CSV
    with open(data_dir / "employees.csv", "w", newline="", encoding="utf-8") as file:
        if employees_data:
            fieldnames = employees_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees_data)
    
    # Write products to CSV
    with open(data_dir / "products.csv", "w", newline="", encoding="utf-8") as file:
        if products_data:
            fieldnames = products_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products_data)
    
    # Write orders to CSV
    with open(data_dir / "orders.csv", "w", newline="", encoding="utf-8") as file:
        if orders_data:
            fieldnames = orders_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders_data)
    
    print("✅ Sample data files created successfully")
    print(f"📁 Files created in: {data_dir}")
    print("   - employees.csv")
    print("   - products.csv") 
    print("   - orders.csv")
    
    return data_dir

# ============================================================================
# TABLE CREATION
# ============================================================================

def create_tables(connection):
    """Create sample tables for practice"""
    try:
        cursor = connection.cursor()
        
        # Create employees table
        create_employees_table = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER CHECK (age >= 0),
            department VARCHAR(50) NOT NULL,
            salary DECIMAL(10,2) CHECK (salary >= 0),
            city VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Create products table
        create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            category VARCHAR(50),
            price DECIMAL(10,2) CHECK (price >= 0),
            stock INTEGER DEFAULT 0 CHECK (stock >= 0),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Create orders table
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER REFERENCES employees(id),
            product_id INTEGER REFERENCES products(id),
            quantity INTEGER CHECK (quantity > 0),
            total_price DECIMAL(10,2) CHECK (total_price >= 0),
            order_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Execute table creation
        cursor.execute(create_employees_table)
        cursor.execute(create_products_table)
        cursor.execute(create_orders_table)
        
        connection.commit()
        print("✅ Tables created successfully")
        cursor.close()
        
    except Error as e:
        print(f"❌ Error creating tables: {e}")

# ============================================================================
# DATA INSERTION FROM FILES
# ============================================================================

def insert_data_from_files(connection, data_dir):
    """Insert data from CSV files into PostgreSQL tables"""
    try:
        # First, clear existing data to avoid duplicates
        cursor = connection.cursor()
        print("\n🧹 Clearing existing data...")
        cursor.execute("TRUNCATE TABLE orders, products, employees RESTART IDENTITY CASCADE")
        connection.commit()
        print("✅ Existing data cleared")
        
        # Insert employees
        print("\n📥 Inserting employees data...")
        successful_employees = 0
        with open(data_dir / "employees.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cursor.execute("""
                        INSERT INTO employees (id, name, age, department, salary, city)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (int(row['id']), row['name'], int(row['age']), row['department'], float(row['salary']), row['city']))
                    successful_employees += 1
                except IntegrityError as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    if "duplicate key" in str(e):
                        print(f"⚠️  Duplicate employee ID {row['id']}: {row['name']} - Skipping")
                    else:
                        print(f"❌ Error inserting employee {row['name']}: {e}")
                except Error as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    print(f"❌ Error inserting employee {row['name']}: {e}")
        
        connection.commit()
        print(f"✅ Inserted {successful_employees} employees")
        
        # Insert products
        print("📥 Inserting products data...")
        successful_products = 0
        with open(data_dir / "products.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cursor.execute("""
                        INSERT INTO products (id, name, category, price, stock)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (row['id'], row['name'], row['category'], row['price'], row['stock']))
                    successful_products += 1
                except IntegrityError as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    if "duplicate key" in str(e):
                        print(f"⚠️  Duplicate product ID {row['id']}: {row['name']} - Skipping")
                    else:
                        print(f"❌ Error inserting product {row['name']}: {e}")
                except Error as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    print(f"❌ Error inserting product {row['name']}: {e}")
        
        connection.commit()
        print(f"✅ Inserted {successful_products} products")
        
        # Insert orders
        print("📥 Inserting orders data...")
        successful_orders = 0
        with open(data_dir / "orders.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cursor.execute("""
                        INSERT INTO orders (id, employee_id, product_id, quantity, total_price, order_date)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (row['id'], row['employee_id'], row['product_id'], row['quantity'], row['total_price'], row['order_date']))
                    successful_orders += 1
                except IntegrityError as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    if "duplicate key" in str(e):
                        print(f"⚠️  Duplicate order ID {row['id']} - Skipping")
                    else:
                        print(f"❌ Error inserting order {row['id']}: {e}")
                except Error as e:
                    connection.rollback()  # Rollback the failed transaction
                    cursor = connection.cursor()  # Get a new cursor
                    print(f"❌ Error inserting order {row['id']}: {e}")
        
        connection.commit()
        print(f"✅ Inserted {successful_orders} orders")
        print("✅ Data insertion completed successfully")
        cursor.close()
        
    except Error as e:
        print(f"❌ Error inserting data: {e}")
        connection.rollback()

def insert_data_with_upsert(connection, data_dir):
    """Insert data using UPSERT (INSERT ... ON CONFLICT) for better duplicate handling"""
    try:
        cursor = connection.cursor()
        
        print("\n📥 Inserting data using UPSERT approach...")
        
        # Insert employees with UPSERT
        print("📥 Upserting employees data...")
        with open(data_dir / "employees.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                    INSERT INTO employees (id, name, age, department, salary, city)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        age = EXCLUDED.age,
                        department = EXCLUDED.department,
                        salary = EXCLUDED.salary,
                        city = EXCLUDED.city
                """, (row['id'], row['name'], row['age'], row['department'], row['salary'], row['city']))
        
        print("✅ Employees upserted successfully")
        
        # Insert products with UPSERT
        print("📥 Upserting products data...") #means insert or update if the id already exists
        with open(data_dir / "products.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                    INSERT INTO products (id, name, category, price, stock)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        category = EXCLUDED.category,
                        price = EXCLUDED.price,
                        stock = EXCLUDED.stock
                """, (row['id'], row['name'], row['category'], row['price'], row['stock']))
        
        print("✅ Products upserted successfully")
        
        # Insert orders with UPSERT
        print("📥 Upserting orders data...")
        with open(data_dir / "orders.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                    INSERT INTO orders (id, employee_id, product_id, quantity, total_price, order_date)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        employee_id = EXCLUDED.employee_id,
                        product_id = EXCLUDED.product_id,
                        quantity = EXCLUDED.quantity,
                        total_price = EXCLUDED.total_price,
                        order_date = EXCLUDED.order_date
                """, (row['id'], row['employee_id'], row['product_id'], row['quantity'], row['total_price'], row['order_date']))
        
        print("✅ Orders upserted successfully")
        
        connection.commit()
        print("✅ All data upserted successfully using ON CONFLICT")
        cursor.close()
        
    except Error as e:
        print(f"❌ Error in upsert operation: {e}")
        connection.rollback()

# ============================================================================
# DATA VERIFICATION
# ============================================================================

def verify_data_insertion(connection):
    """Verify that data was inserted correctly"""
    try:
        cursor = connection.cursor()
        
        print("\n" + "=" * 60)
        print("DATA VERIFICATION")
        print("=" * 60)
        
        # Check employees table
        cursor.execute("SELECT COUNT(*) FROM employees")
        emp_count = cursor.fetchone()[0]
        print(f"📊 Employees table: {emp_count} records")
        
        if emp_count > 0:
            cursor.execute("SELECT id, name, department, salary FROM employees LIMIT 3")
            sample_employees = cursor.fetchall()
            print("   Sample employees:")
            for emp in sample_employees:
                print(f"     ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Salary: ${emp[3]:,.0f}")
        
        # Check products table
        cursor.execute("SELECT COUNT(*) FROM products")
        prod_count = cursor.fetchone()[0]
        print(f"📊 Products table: {prod_count} records")
        
        if prod_count > 0:
            cursor.execute("SELECT id, name, category, price FROM products LIMIT 3")
            sample_products = cursor.fetchall()
            print("   Sample products:")
            for prod in sample_products:
                print(f"     ID: {prod[0]}, Name: {prod[1]}, Category: {prod[2]}, Price: ${prod[3]:.2f}")
        
        # Check orders table
        cursor.execute("SELECT COUNT(*) FROM orders")
        order_count = cursor.fetchone()[0]
        print(f"📊 Orders table: {order_count} records")
        
        if order_count > 0:
            cursor.execute("SELECT id, employee_id, product_id, quantity, total_price FROM orders LIMIT 3")
            sample_orders = cursor.fetchall()
            print("   Sample orders:")
            for order in sample_orders:
                print(f"     ID: {order[0]}, Employee: {order[1]}, Product: {order[2]}, Qty: {order[3]}, Total: ${order[4]:.2f}")
        
        # Check referential integrity
        cursor.execute("""
            SELECT COUNT(*) FROM orders o
            WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.id = o.employee_id)
               OR NOT EXISTS (SELECT 1 FROM products p WHERE p.id = o.product_id)
        """)
        orphan_orders = cursor.fetchone()[0]
        
        if orphan_orders == 0:
            print("✅ All foreign key relationships are valid")
        else:
            print(f"⚠️  Found {orphan_orders} orders with invalid references")
        
        cursor.close()
        return emp_count > 0 and prod_count > 0
        
    except Error as e:
        print(f"❌ Error verifying data: {e}")
        return False

# ============================================================================
# SQL QUERIES DEMONSTRATION
# ============================================================================

def demonstrate_sql_queries(connection):
    """Demonstrate various SQL queries"""
    try:
        cursor = connection.cursor()
        
        print("\n" + "=" * 60)
        print("SQL QUERIES DEMONSTRATION")
        print("=" * 60)
        
        # 1. Basic SELECT queries
        print("\n--- Basic SELECT Operations ---")
        
        # SELECT * FROM employees LIMIT 3
        cursor.execute("SELECT id, name, department, salary FROM employees LIMIT 3")
        employees = cursor.fetchall()
        print("First 3 employees:")
        for emp in employees:
            print(f"  ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Salary: ${emp[3]:,.0f}")
        
        # SELECT with WHERE clause
        cursor.execute("SELECT name, salary FROM employees WHERE department = 'Engineering'")
        engineering_employees = cursor.fetchall()
        print(f"\nEngineering employees ({len(engineering_employees)} rows):")
        for emp in engineering_employees:
            print(f"  {emp[0]}: ${emp[1]:,.0f}")
        
        # SELECT with ORDER BY
        cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3")
        top_earners = cursor.fetchall()
        print(f"\nTop 3 earners:")
        for emp in top_earners:
            print(f"  {emp[0]}: ${emp[1]:,.0f}")
        
        # 2. JOIN operations
        print("\n--- JOIN Operations ---")
        
        cursor.execute("""
            SELECT e.name, p.name as product, o.quantity, o.total_price
            FROM orders o
            JOIN employees e ON o.employee_id = e.id
            JOIN products p ON o.product_id = p.id
            ORDER BY o.total_price DESC
        """)
        order_details = cursor.fetchall()
        print("Order details with employee and product info:")
        for order in order_details[:5]:  # Show first 5
            print(f"  {order[0]} ordered {order[2]}x {order[1]} for ${order[3]:.2f}")
        
        # 3. Aggregation queries
        print("\n--- Aggregation Operations ---")
        
        # GROUP BY department
        cursor.execute("""
            SELECT department, 
                   COUNT(*) as employee_count, 
                   AVG(salary) as avg_salary,
                   SUM(salary) as total_salary
            FROM employees 
            GROUP BY department
            ORDER BY avg_salary DESC
        """)
        dept_stats = cursor.fetchall()
        print("Department statistics:")
        for dept in dept_stats:
            print(f"  {dept[0]}: {dept[1]} employees, avg salary: ${dept[2]:,.0f}")
        
        # 4. UPDATE operations
        print("\n--- UPDATE Operations ---")
        
        # Show current state
        cursor.execute("SELECT name, salary FROM employees WHERE department = 'Engineering'")
        current_salaries = cursor.fetchall()
        print("Current Engineering salaries:")
        for emp in current_salaries:
            print(f"  {emp[0]}: ${emp[1]:,.0f}")
        
        # Give 10% raise to Engineering department
        cursor.execute("""
            UPDATE employees 
            SET salary = salary * 1.1 
            WHERE department = 'Engineering'
        """)
        print(f"✅ Updated {cursor.rowcount} Engineering employees with 10% raise")
        
        # Show updated state
        cursor.execute("SELECT name, salary FROM employees WHERE department = 'Engineering'")
        updated_salaries = cursor.fetchall()
        print("Updated Engineering salaries:")
        for emp in updated_salaries:
            print(f"  {emp[0]}: ${emp[1]:,.0f}")
        
        # Additional UPDATE examples
        print("\n--- More UPDATE Examples ---")
        
        # Update specific employee's department
        cursor.execute("""
            UPDATE employees 
            SET department = 'Senior Engineering', salary = salary * 1.15
            WHERE name = 'Alice Johnson'
        """)
        print(f"✅ Promoted Alice Johnson to Senior Engineering with 15% raise")
        
        # Update products with low stock
        cursor.execute("SELECT name, stock FROM products WHERE stock < 100")
        low_stock = cursor.fetchall()
        print(f"Products with low stock (< 100):")
        for prod in low_stock:
            print(f"  {prod[0]}: {prod[1]} units")
        
        cursor.execute("""
            UPDATE products 
            SET stock = stock + 50 
            WHERE stock < 100
        """)
        print(f"✅ Restocked {cursor.rowcount} products with low inventory")
        
        # Update orders older than a certain date
        cursor.execute("""
            UPDATE orders 
            SET total_price = total_price * 0.9 
            WHERE order_date < '2024-01-18'
        """)
        print(f"✅ Applied 10% discount to {cursor.rowcount} older orders")
        
        # Conditional UPDATE with CASE
        cursor.execute("""
            UPDATE employees 
            SET salary = CASE 
                WHEN age > 30 THEN salary * 1.05
                WHEN age > 25 THEN salary * 1.03
                ELSE salary * 1.02
            END
        """)
        print(f"✅ Applied age-based salary increases to all employees")
        
        # 5. DELETE operations
        print("\n--- DELETE Operations ---")
        
        # Show current orders
        cursor.execute("SELECT COUNT(*) FROM orders")
        order_count = cursor.fetchone()[0]
        print(f"Current order count: {order_count}")
        
        # Show orders that will be deleted
        cursor.execute("SELECT id, quantity, total_price FROM orders WHERE quantity < 3")
        orders_to_delete = cursor.fetchall()
        print("Orders with quantity < 3 (to be deleted):")
        for order in orders_to_delete:
            print(f"  Order ID: {order[0]}, Qty: {order[1]}, Price: ${order[2]:.2f}")
        
        # Delete orders with low quantity (less than 3)
        cursor.execute("DELETE FROM orders WHERE quantity < 3")
        print(f"✅ Deleted {cursor.rowcount} orders with quantity < 3")
        
        # Show updated order count
        cursor.execute("SELECT COUNT(*) FROM orders")
        new_order_count = cursor.fetchone()[0]
        print(f"Updated order count: {new_order_count}")
        
        # Additional DELETE examples
        print("\n--- More DELETE Examples ---")
        
        # Delete products with zero stock
        cursor.execute("SELECT COUNT(*) FROM products WHERE stock = 0")
        zero_stock_count = cursor.fetchone()[0]
        if zero_stock_count > 0:
            cursor.execute("DELETE FROM products WHERE stock = 0")
            print(f"✅ Deleted {cursor.rowcount} products with zero stock")
        else:
            print("📊 No products with zero stock found")
        
        # Delete employees from a specific city (if any)
        cursor.execute("SELECT COUNT(*) FROM employees WHERE city = 'Boston'")
        boston_emp_count = cursor.fetchone()[0]
        if boston_emp_count > 0:
            # First show which employees will be affected
            cursor.execute("SELECT name, department FROM employees WHERE city = 'Boston'")
            boston_employees = cursor.fetchall()
            print(f"Employees in Boston (to be relocated):")
            for emp in boston_employees:
                print(f"  {emp[0]} from {emp[1]}")
            
            # Instead of deleting, let's relocate them
            cursor.execute("""
                UPDATE employees 
                SET city = 'Remote' 
                WHERE city = 'Boston'
            """)
            print(f"✅ Relocated {cursor.rowcount} Boston employees to Remote work")
        
        # Delete old orders (older than 2024-01-16) - but keep at least one for demo
        cursor.execute("""
            DELETE FROM orders 
            WHERE order_date < '2024-01-17' 
            AND id NOT IN (SELECT MIN(id) FROM orders)
        """)
        print(f"✅ Deleted {cursor.rowcount} old orders (keeping the oldest one for demo)")
        
        # Cascading DELETE example (delete employee and their orders)
        print("\n--- Cascading DELETE Example ---")
        
        # First, show orders for a specific employee
        cursor.execute("""
            SELECT o.id, e.name, p.name, o.quantity 
            FROM orders o
            JOIN employees e ON o.employee_id = e.id
            JOIN products p ON o.product_id = p.id
            WHERE e.name = 'Henry Taylor'
        """)
        henry_orders = cursor.fetchall()
        if henry_orders:
            print("Henry Taylor's orders:")
            for order in henry_orders:
                print(f"  Order {order[0]}: {order[2]} (qty: {order[3]})")
            
            # Delete Henry's orders first (due to foreign key constraint)
            cursor.execute("DELETE FROM orders WHERE employee_id = (SELECT id FROM employees WHERE name = 'Henry Taylor')")
            deleted_orders = cursor.rowcount
            
            # Then delete Henry
            cursor.execute("DELETE FROM employees WHERE name = 'Henry Taylor'")
            deleted_employees = cursor.rowcount
            
            print(f"✅ Deleted {deleted_orders} orders and {deleted_employees} employee (Henry Taylor)")
        else:
            print("📊 No orders found for Henry Taylor")
        
        # 6. Complex DELETE with subqueries
        print("\n--- Complex DELETE Examples ---")
        
        # Delete products that have never been ordered
        cursor.execute("""
            DELETE FROM products 
            WHERE id NOT IN (
                SELECT DISTINCT product_id 
                FROM orders 
                WHERE product_id IS NOT NULL
            )
        """)
        print(f"✅ Deleted {cursor.rowcount} products that were never ordered")
        
        # Final counts
        print("\n--- Final Record Counts ---")
        cursor.execute("SELECT COUNT(*) FROM employees")
        final_emp_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM products")
        final_prod_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM orders")
        final_order_count = cursor.fetchone()[0]
        
        print(f"📊 Final counts: {final_emp_count} employees, {final_prod_count} products, {final_order_count} orders")
        
        connection.commit()
        cursor.close()
        
    except Error as e:
        print(f"❌ Error in SQL queries: {e}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all PostgreSQL examples"""
    print("🚀 Starting PostgreSQL and SQL Practice with Environment Variables")
    
    # Cleanup files first
    cleanup_files()
    
    try:
        # Validate environment variables
        if not validate_environment():
            print("❌ Cannot proceed with missing environment variables")
            return
        
        # Create database and connect
        connection = create_database_if_not_exists()
        if not connection:
            print("❌ Cannot proceed without database connection")
            return
        
        # Create tables
        create_tables(connection)
        
        # Create sample data files
        data_dir = create_sample_data_files()
        
        # Insert data from files (using UPSERT for better duplicate handling)
        insert_data_with_upsert(connection, data_dir)
        
        # Verify data insertion
        if not verify_data_insertion(connection):
            print("❌ Data verification failed")
            return
        
        # Demonstrate SQL queries
        demonstrate_sql_queries(connection)
        
        # Cleanup files after processing
        cleanup_files()
        
        print("\n" + "=" * 60)
        print("✅ POSTGRESQL PRACTICE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
    except Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            print("🔌 Database connection closed")

if __name__ == "__main__":
    main()