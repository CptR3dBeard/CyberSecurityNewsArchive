
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
from os import getcwd
 
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

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
internet_archive = 'InternetArchive'

# display the html file
def display_html():
    webopen(f'file://' + '/Users/lane/Documents/GitHub/Portfolio2ITD104/InternetArchive/testing.html')

# extract news from web archive html docs
def extract_news():
    """ This function intends to extract the correct news information
    from existing news articles that have been archived and display them approriatly
    in a HTML document."""

    # open specified file and search for key tags
    with open('InternetArchive/13may.html',mode='r') as root:
        # save html content to variable
        html_to_text = str(root.readlines())
        # find the heading of each article
        headings = findall('home-title\'>(.*?)</h2>',html_to_text)
        # find the referenced pictures attached to each article
        picture_refs = findall('src=\"https://thehackernews.com/new-images/img\"',html_to_text)
        # find the synopsis of each article
        synopsis = findall('home-desc\'>(.*?)</div>',html_to_text)
        
    
    # basic design of our HTML document for web archiving
    html_template = f"""<!DOCTYPE html>
    <html>

    <style>
    h1 {{
        text-align: center;
    }}
    p {{
        text-align: center;
    }}
    </style>
    <body>

    <h1>{headings[0]}</h1>
    <p> <img src =https://thehackernews.com/new-images/img{picture_refs[0]}><br>{synopsis[0]}</p>
    <h1>{headings[1]}</h1>
    <p> <img src =https://thehackernews.com/new-images/img{picture_refs[1]}><br>{synopsis[1]}</p>
    <h1>{headings[2]}</h1>
    <p> <br>{synopsis[2]}</p>
    <h1>{headings[3]}</h1>
    <p>123<br>{synopsis[3]}</p>
    <h1>{headings[4]}</h1>
    <p>123<br>{synopsis[4]}</p>
    <h1>{headings[5]}</h1>
    <p>123<br>{synopsis[5]}</p>
    <h1>{headings[6]}</h1>
    <p>123<br>{synopsis[6]}</p>

    </body>
    </html>"""

    open('InternetArchive/testing.html',mode='w').write(html_template)

    

# scrape cyber security news and archive contents
def scrape_news_and_archive():
    """ This functions purpose is to scrape the webcontents of 
    TheHackerNews.com and save the html document in a folder named
    InternetArchive """
    pass

# defining our window parameters
tk = Tk()
tk.title("Cyber Secruity News Archive")
tk.geometry('400x400')


# defining our buttons
extract_html_news_file = Button(tk,text='Extract HTML news file from archive',command= extract_news)
display_html_news_file = Button(tk,text='Display HTML news file',command= display_html)
archive_latest_news = Button(tk,text='Archive Latest News')

#placing our buttons on screen
extract_html_news_file.place(x=100,y=200)
display_html_news_file.place(x=100,y=170)
archive_latest_news.place(x=100,y=140)


# main event loop
tk.mainloop()

