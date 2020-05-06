from tkinter import *
from datetime import date
import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text = "Password * ").pack()
    password_entry = Entry(screen1,textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", height = "1", width = "10", command = register_user).pack()


def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)


    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print("login success")
            login_success()
        else:
            print("Password has not been recognized")
    else:
        print("User not found")
        

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    
    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    
# Gives user the ability to either manual enter or use scanner
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Printer")
    screen3.geometry("300x250")
    Label(screen3, text = "\nWhat would you like to do?").pack()
    Label(screen3, text = "").pack()

    Button(screen3, text = "Manual Entry", width = 30, height = 2, command = manual_entry).pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Scanned Entry", width = 30, height = 2, command = scan_entry).pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Print Values", width = 30, height = 2, command = print_entries).pack()

# Manual entry of prodct
def manual_entry():
    global screen4
    screen4 = Toplevel(screen)
    screen4.geometry("300x250")
    print("manual entry")
    Label(screen4, text = "\nEnter Information Below").pack()
    Label(screen4, text = "").pack()
    
    global cost_entry
    global cost
    global brand_entry
    global brand
    global flavor_entry
    global flavor

    cost = StringVar()
    brand = StringVar()
    flavor = StringVar()
    
    Label(screen4, text = "Cost of Product").pack()
    cost_entry = Entry(screen4, textvariable = cost)
    cost_entry.pack()
    Label(screen4, text = "Brand of Product").pack()
    brand_entry = Entry(screen4, textvariable = brand)
    brand_entry.pack()
    Label(screen4, text = "Flavor of Product").pack()
    flavor_entry = Entry(screen4, textvariable = flavor)
    flavor_entry.pack()
    Button(screen4, text = "Apply Purchase", width = 30, height = 2, command = append_to_file1).pack()
    
# Add the purchase to the end of users file
def append_to_file1():
    cost_info = cost.get()
    brand_info = brand.get()
    flavor_info = flavor.get()

    today = date.today()
    d1 = today.strftime("%d/%m/%y")

    add_to_file = "\n" + cost_info+',' + brand_info+',' + flavor_info+','+d1
    
    with open(username1, "a") as user_file:
        user_file.write(add_to_file)
        user_file.close()

# Use scanner to enter product value
# Scan and data scrape from UPC website
# If any area comes back empty, then add an entry to gain user input then append to file
def print_entries():
    print("data entry")
    

# Add the purchase to the end of users file
def append_to_file2():
    cost_info = cost.get()
    brand_info = brand.get()
    flavor_info = flavor.get()

    today = date.today()
    d1 = today.strftime("%d/%m/%y")

    add_to_file = "\n" + cost_info+',' + brand_info+',' + flavor_info+','+d1
    
    with open(username1, "a") as user_file:
        user_file.write(add_to_file)
        user_file.close()


# Prin out the list of products bought and total spent(2/13/20)
def scan_entry():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("300x250")
    print("Scan entry")
    Label(screen5, text = "\nScan Barcode").pack()
    Label(screen5, text = "").pack()
    
    global cost_entry
    global cost
    global brand_entry
    global brand
    global flavor_entry
    global flavor
    global barcode
    global barcode_entry

    cost = StringVar()
    brand = StringVar()
    barcode = StringVar()
    flavor = StringVar()

    Label(screen5, text = "Barcode").pack()
    barcode_entry = Entry(screen5, textvariable = barcode)
    barcode_entry.pack()

    Button(screen5, text = "Get info", width = 30, height = 2, command =get_info).pack()
    
    '''Label(screen5, text = "Cost of Product").pack()
    cost_entry = Entry(screen5, textvariable = cost)
    cost_entry.pack()
    Label(screen5, text = "Brand of Product").pack()
    brand_entry = Entry(screen5, textvariable = brand)
    brand_entry.pack()
    Label(screen4, text = "Flavor of Product").pack()
    flavor_entry = Entry(screen5, textvariable = flavor)
    flavor_entry.pack()
    Button(screen4, text = "Apply Purchase", width = 30, height = 2, command = append_to_file1).pack()'''

def get_info():
    print("hello")
    print(barcode_entry)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Scanner 1.0")
    Label(text = "Scanner 1.0", bg ="gray", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()

main_screen()
 
