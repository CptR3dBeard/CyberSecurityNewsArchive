
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this ok
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 11270233
#    Student name: Lane Travis Nash
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [1C2202]
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from cgitb import html, text
from email import message
from gettext import find
from glob import glob
from turtle import onclick
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen, open_new_tab

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd, listdir
 
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime
from click import command

from requests import head

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#
# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
from web_doc_downloader import download
from tkinter import messagebox

# defining our window parameters
tk = Tk()
# setting gui title
tk.title("Cyber Secruity News Archive")
# setting gui geometry
tk.geometry('400x400')
# setting background image
img = PhotoImage(file='hackerlogo.png')
# setting our frame size
frame = Frame(tk, width=50, height=50)
# packing frame to GUI
frame.pack()
# creating our Label
label = Label(frame, image = img)
# packing Label to GUI
label.pack()

# required variables
internet_archive = 'InternetArchive'

# display the html file
def display_html():
    webopen(f"file://' + '/Users/lane/Documents/GitHub/Portfolio2ITD104/thearchivedfile.html")
    

# extract news from web archive html docs
def extract_news():
    """ This function intends to extract the correct news information
    from existing news articles that have been archived and display them approriatly
    in a HTML document."""
    
    # process selection as an integer not a tuple
    users_selection = int(selection_box.curselection()[0])
    # check the users file choice
    file_name = options[users_selection]


    # open specified file and search for key tags
    with open(f'InternetArchive/{file_name}' ,mode='r') as root:
        # save html content as string
        html_to_text = str(root.readlines())

        # save each article heading
        headings = findall('home-title\'>(.*?)</h2>', html_to_text)
        # save pop title
        #pop_title = findall('<div class=\'pop-title\'>(.*?)</div>',html_to_text)

        # save each article picture
        picture_refs = findall("loading=\'lazy\' src=\'https://thehackernews.com/new-images/img/b/R29vZ2xl(.*?)\'",html_to_text)

        # save each popup picture
        #pop_picture_refs = findall("height =\'72\' src=\'https://thehackernews.com/new-images/img/b/R29vZ2xl(.*?)\'.jpeg",html_to_text)
        
        # save each article synposis
        synopsis = findall('home-desc\'>(.*?)</div>',html_to_text)
        
    
    # basic design of our HTML document for web archive generation
    html_template = f"""<!DOCTYPE html>
    <html>

    <style>
    body {{
        background-image: linear-gradient(#8CF4F9,#7D7DD1);
    }}
    h1 {{
        text-align: center;
    }}

    p {{
        text-align: center;
    }}
    </style>
    <body>
    <h1> Thank you for using the Cyber Archive </h1>
    <p> All images and articles are the intellectual property of </p>
    <a href='https://thehackernews.com/'><p>The Hacker News</p></a>

    <h1>{headings[0]}</h1>
    <p> <img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[0]}><br><br>{synopsis[0]}</p>

    <h1>{headings[1]}</h1>
    <p> <img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[1]}><br><br>{synopsis[1]}</p>

    <h1>{headings[2]}</h1>
    <p><img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[2]}><br><br>{synopsis[2]}</p>

    <h1>{headings[3]}</h1>
    <p><img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[3]}><br><br>{synopsis[3]}</p>

    <h1>{headings[4]}</h1>
    <p><img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[4]}><br><br>{synopsis[4]}</p>

    <h1>{headings[5]}</h1>
    <p><img src =https://thehackernews.com/new-images/img/b/R29vZ2xl{picture_refs[5]}><br><br>{synopsis[5]}</p>

    </body>
    </html>"""

    # create the generated news document and write to it using html template
    open('thearchivedfile.html',mode='w').write(html_template)

    

# scrape cyber security news and archive contents
def scrape_news_and_archive():
    # call imported web document downloader
    download('https://thehackernews.com/')
    
    


def options_menu_data():
    # setting global variables to be used in other functions
    global options
    global selection_box
    # empty options list
    options = []

    # check for html files within the InternetArchive
    for files in listdir('InternetArchive'):
        if files.endswith('2022.html'):
            # save html file names to options list
            options.append(files)
    print(options)

    # creating our list box
    selection_box = Listbox(tk)
    # checking file options
    for option in options:
        # insert option into list box
        selection_box.insert(END, option)
    # insert latest option
    selection_box.insert(END, 'Latest')

# !!!Beginning of Instruction menu functions!!!
def how_to_use():
    messagebox.showinfo(instructions_window,message='1. Firstly you must select a news article from our menu\n\
    2. You must hit extract from news archive button which is located below our file selection box\n\
    3. Lastly you then hit Display news article and you will be directed to an offline generated document containing the news.')

def purpose_message_box():
    messagebox.showinfo(instructions_window,message='The purpose of this program is to to safely and legally archive news articles\
    that have been posted online. In addition, allowing users to retrieve newly generated webpages from specific dates and view the events\
    of the day')

def instructons_gui_menu():
    """ The purpose of this function is create an easy intelligble
    GUI to give instructions and example to users, the purpose of this program
    and how to use it effectively for archiving and retrieving news articles"""
    global instructions_window
    # defining a pop-up gui interface to store instructions on the program
    instructions_window = Toplevel(tk)
    instructions_window.geometry('200x200')
    instructions_Label =  Label(instructions_window,text='What do you need assistance with?')
    purpose_button = Button(instructions_window,text='What is the purpose of this program?',command=purpose_message_box)
    how_to_use_button = Button(instructions_window,text='How do i use this program?',command=how_to_use)
    # using place method to position the Labels and Buttons of instructions menu
    instructions_Label.place(x=20,y=20)
    purpose_button.place(x=20,y=40)
    how_to_use_button.place(x=20,y=80)


# !!!Ending of Instruction Menu Functions!!!

# All Function calls
options_menu_data()


# defining our buttons
# extract information from news archive
extract_html_news_file = Button(tk,text='Extract News Article From Archive',command= extract_news)
# submit confirmation button to finalise decision
submit_button = Button(tk,text='Display News Article',command= display_html)
# label to instruct user on what to do
our_label = Label(tk,text='Which News Document do you wish to view?')
# defining a help button
help_me = Button(tk,text='Help me!',command=instructons_gui_menu)

#placing our buttons on screen
extract_html_news_file.place(x=20,y=212)
selection_box.place(x=20,y=40)
submit_button.place(x=20,y=240)
our_label.place(x=20,y=18)
help_me.place(x=150,y=280)


# main event loop
tk.mainloop()

