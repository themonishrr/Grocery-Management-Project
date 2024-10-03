import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='7327',
    database='dbms_miniproject'
)
cursor = conn.cursor()

st.title("Grocery Store Management System")

# Function to add a customer
def add_customer():
    st.subheader("Add Customer")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    address = st.text_input("Address")
    
    if st.button("Submit"):
        cursor.execute("INSERT INTO Customers (name, email, phone_number, address) VALUES (%s, %s, %s, %s)", (name, email, phone_number, address))
        conn.commit()
        st.success("Customer added successfully")

# Function to add a product
def add_product():
    st.subheader("Add Product")
    name = st.text_input("Name")
    category = st.text_input("Category")
    price = st.text_input("Price")
    stock_quantity = st.text_input("Stock Quantity")
    
    if st.button("Submit"):
        cursor.execute("INSERT INTO Products (name, category, price, stock_quantity) VALUES (%s, %s, %s, %s)", (name, category, price, stock_quantity))
        conn.commit()
        st.success("Product added successfully")

# Function to add an order
def add_order():
    st.subheader("Add Order")
    customer_id = st.text_input("Customer ID")
    order_date = st.text_input("Order Date")
    total_amount = st.text_input("Total Amount")
    
    if st.button("Submit"):
        cursor.execute("INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)", (customer_id, order_date, total_amount))
        conn.commit()
        st.success("Order added successfully")

# Function to add a supplier
def add_supplier():
    st.subheader("Add Supplier")
    name = st.text_input("Name")
    contact_number = st.text_input("Contact Number")
    email = st.text_input("Email")
    address = st.text_input("Address")
    
    if st.button("Submit"):
        cursor.execute("INSERT INTO Suppliers (name, contact_number, email, address) VALUES (%s, %s, %s, %s)", (name, contact_number, email, address))
        conn.commit()
        st.success("Supplier added successfully")

# Function to update customer details
def update_customer():
    st.subheader("Update Customer")
    customer_id = st.text_input("Customer ID")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    address = st.text_input("Address")
    
    if st.button("Submit"):
        cursor.execute("UPDATE Customers SET name = %s, email = %s, phone_number = %s, address = %s WHERE customer_id = %s", (name, email, phone_number, address, customer_id))
        conn.commit()
        st.success("Customer details updated successfully")

# Function to delete a customer
def delete_customer():
    st.subheader("Delete Customer")
    customer_id = st.text_input("Customer ID")
    
    if st.button("Submit"):
        cursor.execute("DELETE FROM Customers WHERE customer_id = %s", (customer_id,))
        conn.commit()
        st.success("Customer deleted successfully")

# Function to view the customer table
def view_customer():
    st.subheader("View Customers")
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    
    for customer in customers:
        st.write(customer)

# Function to view the orders table
def view_orders():
    st.subheader("View Orders")
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    
    for order in orders:
        st.write(order)

# Function to view the supplier table
def view_supplier():
    st.subheader("View Suppliers")
    cursor.execute("SELECT * FROM Suppliers")
    suppliers = cursor.fetchall()
    
    for supplier in suppliers:
        st.write(supplier)

# Streamlit sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a function", ["Add Customer", "Add Product", "Add Supplier", "Update Customer", "Delete Customer", "View Customers",  "View Suppliers"])

if option == "Add Customer":
    add_customer()
elif option == "Add Product":
    add_product()
# elif option == "Add Order":
#     add_order()
elif option == "Add Supplier":
    add_supplier()
elif option == "Update Customer":
    update_customer()
elif option == "Delete Customer":
    delete_customer()
elif option == "View Customers":
    view_customer()
elif option == "View Orders":
    view_orders()
elif option == "View Suppliers":
    view_supplier()
