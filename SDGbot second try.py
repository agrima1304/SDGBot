# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:20:36 2022

@author: Agrima
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1March@2004',
    database = 'sdg_bot'
    )

mycursor = mydb.cursor()


import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import webbrowser

root = tk.Tk()

def setup_window():

    root.title('SDGbot')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("%dx%d" % (width, height))
    root['bg'] = '#A3C893'
    root.iconbitmap('C:\\Users\\Agrima\\OneDrive - Doha College\\Computer science\\YEAR 13\\EPQ - SDGbot\\SDG-Wheel_Transparent_WEB-Copy.ico')

    
setup_window()

#message_bubble = tk.PhotoImage(file = 'C:\\Users\\Agrima\\OneDrive - Doha College\\Computer science\\YEAR 13\\EPQ - SDGbot\\message bubble.png')
#small_bubble = message_bubble.subsample(10,10)

message_box = ScrolledText(root, bd = 4, height = 8, width = 77, wrap = tk.WORD, font = 'Times 25', bg = '#FFDAD8', foreground= '#010057')
message_box.grid(row = 0, column = 0, columnspan=6, padx= 5, pady= 5)
message_box.tag_configure('tag_right', justify= 'right')
message_box.insert('1.0' , 'Hey there! I am the SDGBot, what would you like to learn about today?')
#message_box.image_create('1.0', image = small_bubble)
sdg_general_info_icon = tk.PhotoImage(file='C:\\Users\\Agrima\\OneDrive - Doha College\\Computer science\\YEAR 13\\EPQ - SDGbot\\SDG transparent logo.png')
smaller = sdg_general_info_icon.subsample(4,4)
back_button_image = tk.PhotoImage(file = 'C:\\Users\\Agrima\\OneDrive - Doha College\\Computer science\\YEAR 13\\EPQ - SDGbot\\back.png')
back_button_smaller = back_button_image.subsample(32,32)

button_style = ttk.Style()
button_style.configure("General.TButton", background = 'pink', font = 'Times 25', foreground= '#010057')
resource_button_style = ttk.Style()
resource_button_style.configure('Resource.TButton', font = 'Times 25', foreground= '#010057')
back_button_style = ttk.Style()
back_button_style.configure ('Back.TButton', font = 'Times 15', foreground = 'black')

array = []
   
def sdg_info():
    sql = 'SELECT description FROM info WHERE sdg_no = 0'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        description = x[0]
    message_box['state'] = 'normal'
    message_box.insert(tk.INSERT, '\n'+'\n'+'What are the Sustainable Development Goals?', 'tag_right')
    message_box.insert(tk.INSERT, '\n'+'\n'+description)
    message_box['state'] = 'disabled'
    message_box.see(tk.END)
    

def specific_sdg():
    if specific_sdg_button:
        specific_sdg_button.destroy()
    if general_info_button:
        general_info_button.destroy()
    if how_to_help_button:
        how_to_help_button.destroy()
    global resources_button
    resources_button = ttk.Button(root, text = 'General' +'\n'+'Resources', style = 'Resource.TButton', command= general_resources)
    resources_button.grid(row=2, column = 0, ipady = 10, ipadx= 5)
    global back_button2
    back_button2 = ttk.Button(root, text = ' Back', image = back_button_smaller, compound= tk.LEFT, style = 'Back.TButton', command = home_screen)
    back_button2.grid(row = 1, column = 0)
    for x in range(1,18):
        create_specific_sdg(x)
        array.append(button_sdg_no)

def create_specific_sdg(sdg_no):
    global button_sdg_no
    image = tk.PhotoImage(file=f'C:\\Users\\Agrima\\OneDrive - Doha College\\Computer science\\YEAR 13\\EPQ - SDGbot\\SDG Icons 2019_WEB\\E-WEB-Goal-{sdg_no}.png')
    smaller = image.subsample(13, 13)
    button_sdg_no = ttk.Button(root, image = smaller, command= lambda: insert_sdg_info(sdg_no))
    button_sdg_no.image = smaller
    row = sdg_no%3 + 1
    column = sdg_no // 3
    button_sdg_no.grid(row = row+1, column = column)

    
def home_screen():
    for x in array:
        x.destroy()
    global back_button2
    global resources_button
    back_button2.destroy()
    resources_button.destroy()
    global general_info_button
    global specific_sdg_button
    global how_to_help_button
        
    general_info_button = ttk.Button(
        root,
        style = 'General.TButton',
        image = smaller,
        text = 'What are the ',
        compound = tk.BOTTOM,
        command = lambda: sdg_info()
        )
        
    general_info_button.grid(row = 1, column = 0, padx = 5, pady = 75, columnspan= 2)

    specific_sdg_button = ttk.Button(
        root,
        style = 'General.TButton',
        text = 'I want to learn more!',
        command = specific_sdg
        )

    specific_sdg_button.grid(row = 1, column = 2, padx = 5, columnspan= 2)

    how_to_help_button = ttk.Button(
        root,
        style = 'General.TButton',
        text = 'How can I help in achieving the SDGs?',
        command = deeds_4_the_sdgs
        )
    how_to_help_button.grid(row = 1, column = 4, padx = 5, columnspan= 2)
    
    
def insert_sdg_info(sdg_no):
    for item in array:
        item.destroy()
    sql = f'''
    SELECT description FROM info WHERE sdg_no = {sdg_no}
    '''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        description = x[0]
    message_box['state'] = 'normal'
    message_box.insert(tk.INSERT, '\n'+'\n'+'What is Goal '+str(sdg_no)+'?', 'tag_right')
    message_box.insert( tk.INSERT, '\n'+'\n'+description)
    message_box['state'] = 'disabled'
    message_box.see(tk.END)
    create_specific_resources(sdg_no)

    
def create_specific_resources(sdg_no):
    for x in array:
        x.destroy()
    global resources_button
    resources_button.destroy()
    global back_button1
    back_button1 = ttk.Button(root,text = ' Back', image = back_button_smaller, compound= tk.LEFT, style = 'Back.TButton', command = back_from_resources)
    back_button1.grid(row = 1, column = 0)
    global button_sdg_no
    sql = f'''
    SELECT description, primary_key
    FROM resources
    WHERE sdg_no = {sdg_no}
    '''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    row = 2
    column = 0
    for x in range(len(result)):
        create_resources_button(result[x][0], result[x][1], row, column)
        array.append(button)
        row += 1
        if row % 6 == 0:
            column += 1
            
def back_from_resources():
    for x in array:
        x.destroy()
    global back_button1
    if back_button1:
        back_button1.destroy()
    specific_sdg()
    
    
def general_resources():
    for x in array:
        x.destroy()
    global resources_button
    resources_button.destroy()
    global back_button1
    back_button1 = ttk.Button(root, text = ' Back', image = back_button_smaller, compound= tk.LEFT, style = 'Back.TButton', command = back_from_resources)
    back_button1.grid(row = 1, column = 0)
    sql = '''
    SELECT description, primary_key
    FROM resources
    WHERE sdg_no = 0
    '''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    row = 2
    column = 0
    for x in range(len(result)):
        create_resources_button(result[x][0], result[x][1], row, column)
        array.append(button)
        row += 1
        if row % 6 == 0:
            column += 1
    
    
def create_resources_button(description, primary_key, row, column):
    global button
    button = ttk.Button(root, text = description, style = 'General.TButton', command = lambda: insert_link(primary_key))
    button.grid(row = row, column = column, columnspan= 6, ipady = 5, pady = 10, ipadx = 10)
            

def insert_link(primary_key):
    sql = f'''
    SELECT link
    FROM resources
    WHERE primary_key = {primary_key}
    '''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    try:
        webbrowser.open_new_tab(result[0][0])
    except:
        message_box.insert(tk.INSERT, '\n'+'\n'+result[0][0])
        
def deeds_4_the_sdgs():
    webbrowser.open_new_tab('https://100kdeeds.org/')

general_info_button = ttk.Button(
    root,
    style = "General.TButton",
    image = smaller,
    text = 'What are the ',
    compound = tk.BOTTOM,
    command = lambda: sdg_info(),
    )
    
general_info_button.grid(row = 1, column = 0, padx = 5, pady = 75, columnspan= 2)

specific_sdg_button = ttk.Button(
    root,
    style = 'General.TButton',
    text = 'I want to learn more!',
    command = specific_sdg,
    )

specific_sdg_button.grid(row = 1, column = 2, padx = 5, columnspan= 2, ipadx= 20, ipady= 50)

how_to_help_button = ttk.Button(
    root,
    style= "General.TButton",
    text = '''How can I help in achieving the
Sustainable Development Goals?''',
    command = deeds_4_the_sdgs
    )
how_to_help_button.grid(row = 1, column = 4, padx = 5, columnspan= 2, ipadx= 20, ipady= 20)


root.mainloop()