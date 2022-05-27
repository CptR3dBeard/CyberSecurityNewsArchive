
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
from dataclasses import replace
from distutils.file_util import move_file
from email import message
from fileinput import filename
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
from os import getcwd, listdir, rename
 
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

from click import option
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
# varibale containing current time
dt = datetime.today()
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
    """This function will open the HTML document after
    news has been written extracted and written to it"""
    # open webpage news document
    webopen(f"file://' + '/Users/lane/Documents/GitHub/Portfolio2ITD104/Webarchivepage/main_page.html")
    

# extract news from web archive html docs
def extract_news():
    """ This function intends to extract the correct news information
    from existing news articles that have been archived and display them approriatly
    in a HTML document."""
    # making variables global
    #global publish_and_download_date,headings,picture_refs,synopsis

    # process selection as an integer not a tuple
    users_selection = int(selection_box.curselection()[0]) 
    # check the users file choice
    file_name = options[users_selection]


    # open specified file and search for key tags
    with open(f'InternetArchive/{file_name}' , mode= 'r') as root:
        # saving the archive and publish dates of the file
        publish_and_download_date = findall('(.*?).html', file_name)

        # save html content as string
        html_to_text = str(root.readlines())

        # save each article heading
        headings = findall('home-title\'>(.*?)</h2>', html_to_text)

        # save each article picture
        picture_refs = findall("loading=\'lazy\' src=\'https://thehackernews.com/new-images/img/b/R29vZ2xl(.*?)\'",html_to_text)
        
        # save each article synposis
        synopsis = findall('home-desc\'>(.*?)</div>',html_to_text)
        create_archived_html(publish_and_download_date,headings,picture_refs,synopsis)

 
def create_archived_html(date,titles,pictures,descriptions):
    """This function's purpose to to design out webpage to contain the news of
    the file used from the InternetArchive folder. This is be presented by using Headers
    Pictures and the synposis of each news subject."""
    # basic design of our HTML document for web archive generation
    html_template2 = f"""
     <!DOCTYPE html>
 <html>
 <title> 📰 Articles 📰</title>
 <style>
body {{
        background-image: linear-gradient(#8CF4F9,#7D7DD1);
}}
p {{
    text-align: center;
}}
h1 {{
    text-align: center;
    margin-top: 100px;
}}
/* Add a black background color to the top navigation */
.topnav {{
  position: relative;
  background-color: rgb(2, 19, 117);
  overflow: hidden;
}}

/* Style the links inside the navigation bar */
.topnav a {{
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}}

/* Change the color of links on hover */
.topnav a:hover {{
  background-color: #ddd;
  color: black;
}}

/* Add a color to the active/current link */
.topnav a.active {{
  background-color: #010708;
  color: white;
}}

/* Centered section inside the top navigation */
.topnav-centered a {{
  float: none;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}}

/* Right-aligned section inside the top navigation */
.topnav-right {{
  float: right;
}}
.body {{
        background-image: linear-gradient(#8CF4F9,#7D7DD1);
}}
 </style>
<!-- Top navigation -->
<div class="topnav">

    <!-- Center of screen link -->
    <div class="topnav-centered">
      <a href="main_page.html">Home</a>
    </div>
  
    <!-- Left Side Links-->
    <a href="CyberSecurityEventsPage.html" class='active'>Cyber Security Events</a>
  
    <!-- Right Side Links -->
    <div class="topnav-right">
      <a href="about_page.html">About</a>
      <a href="#"></a>
    </div>
</div>
<div class ="mainbody">
    <body>
    <p> These news articles were published and archived on the {str(date)} </p> 
    <h1>1. {titles[0]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[0]}><br><br>{descriptions[0]}....</p>

    <h1>2. {titles[1]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[1]}><br><br>{descriptions[1]}....</p>

    <h1>3. {titles[2]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[2]}><br><br>{descriptions[2]}....</p>

    <h1>4. {titles[3]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[3]}><br><br>{descriptions[3]}....</p>

    <h1>5. {titles[4]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[4]}><br><br>{descriptions[4]}....</p>

    <h1>6. {titles[5]}</h1>
    <p> <img style="border:10px solid black;" src =https://thehackernews.com/new-images/img/b/R29vZ2xl{pictures[5]}><br><br>{descriptions[5]}....</p>

    </body>
</div>

    """
   
    # create the generated news document and write to it using html template
    open('Webarchivepage/CyberSecurityEventsPage.html',mode='w').write(html_template2)

    

# scrape cyber security news and archive contents
def scrape_news_and_archive():
    """This function is to scrape the latest news articles and save them
    to the InternetArchiveFolder """
    date = dt.date()
    # call imported web document downloader
    download('https://thehackernews.com/',f'{date}','html')
    # check internet archive if file exists
    if f'{date}.html' not in listdir('InternetArchive'):
        # move file to internet archive
        move_file(src= f'{date}.html' , dst= 'InternetArchive')
        # append new file to list box options
        options.append(f'{date}.html')
        # reload options menu data
        selection_box.insert(END,f'{date}.html')
    else:
         print('---- File Already Exists ----')


def options_menu_data():
    """This function records and displays the data
    within a tkinter listbox, for the user to select the
    desired document."""
    # setting global variables to be used in other functions
    global options
    global selection_box
    # empty options list
    options = []
    # check for html files within the InternetArchive
    for files in listdir('InternetArchive'):
        if files.endswith('.html'):
            # save html file names to options list
            options.append(files)
    print(options)

    # creating our list box
    selection_box = Listbox(tk)
    # checking file options
    for option in options:
        # insert option into list box
        selection_box.insert(END, option)

# !!!START of Instruction menu functions!!!
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
    # window varibale to make sure the help gui is infront of base gui
    instructions_window = Toplevel(tk)
    # setting the window geometry
    instructions_window.geometry('300x300')
    # creating our label and buttons
    instructions_Label =  Label(instructions_window,text='What do you need assistance with?')
    purpose_button = Button(instructions_window,text='What is the purpose of this program?',command=purpose_message_box)
    how_to_use_button = Button(instructions_window,text='How do i use this program?',command=how_to_use)
    # using place method to position the Labels and Buttons of instructions menu
    instructions_Label.place(x=20,y=20)
    purpose_button.place(x=20,y=40)
    how_to_use_button.place(x=20,y=80)


# !!!End of Instruction Menu Functions!!!
def main():
    # All Function calls
    options_menu_data()


    # defining our buttons
    # extract information from news archive
    extract_html_news_file = Button(tk,text='Extract News Article From Archive',command= extract_news)
    # submit confirmation button to finalise decision
    submit_button = Button(tk,text='Display News Article',command= display_html)
    # label to instruct user on what to do
    our_label = Label(tk,text='Which News Document do you wish to view?')
    # button for archiving the latest news
    archive_latest = Button(tk,text='Archive Latest News', command= scrape_news_and_archive)
    # defining a help button
    help_me = Button(tk,text='Help me!',command= instructons_gui_menu)

    #placing our buttons on screen
    extract_html_news_file.place(x=20,y=212)
    selection_box.place(x=20,y=40)
    submit_button.place(x=20,y=240)
    our_label.place(x=20,y=18)
    help_me.place(x=178,y=240)
    archive_latest.place(x=20,y=268)

    # main event loop
    tk.mainloop()

#refresh interface
def refresh_listbox():
    """Purpose of this function is to reload the GUI interface
    where neccesary, example would be to update the InternetArchive
    and list box."""
    selection_box.update()

main()
