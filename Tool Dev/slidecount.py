#!/usr/bin/env python3
# A GUI version of SlideCount, using Tkinter for options and files.

import os
import re
import zipfile
import tkinter
from tkinter import filedialog, messagebox

def show_error(text):
    tkinter.messagebox.showerror('Error', text)

def show_results(text):
    tkinter.messagebox.showinfo("Results", text)

def count(files):
    # Declare a dictionary to hold the [deck name, slide count]
    decks = {}
    results = ""

    # Iterate through the files.
    for file in files:
        # If the file ends with ".pptx", add it to the decks dictionary with an initial count of 0 slides.
        if os.path.abspath(file).endswith('.pptx'):
                decks[(os.path.abspath(file))] = 0
        # If the file ends with something other than ".pptx", ignore it and print a message.
        else:
            show_error("The file %s is not a .pptx file and will be ignored." % (file))

    # Iterate through the items in the decks dictionary.
    for deck, count in decks.items():
        try:
            # Attempt to read the file as a zip archive.
            archive = zipfile.ZipFile(deck, 'r')
            # Use the file's list of included files instead of fully decompressing the file to disk.
            contents = archive.namelist()
        # If there was an error reading a file, leave its slide count at 0 and print a message.
        except Exception as e:
            show_error("Error reading %s (%s). Count will be 0." % (os.path.basename(deck), e))
        else:
            # Iterate through each item in the zip file's namelist.
            for fileentry in contents:
                    # If a file entry matches a name we know to be a slide, increment the count of slides for that deck by 1.
                    if(re.findall("ppt/slides/slide", fileentry)):
                            decks[deck] += 1

    results += ("Slides\tDeck\n")

    # Iterate through a sorted version of the decks dictionary, and print out the slide count and name of each deck.
    for deck, count in sorted(decks.items()):
        results += ("%s\t%s\n" % (count, os.path.basename(deck)))

    # If the user has requested a summary, print it.
    if (show_summary.get()):
        results += ("- - - - -\n")
        total = 0
        # Iterate through the values in the decks dictionary and add up all of the counts.
        for count in decks.values():
            total += count
        results += ("%s total slides in %s decks." % (total, len(decks)))

    show_results(results)

# Create the Tkinter interface.
app = tkinter.Tk()
app.geometry('275x175')
app.title("SlideCount")

# Open the file picker and send the selected files to the count() function.
def clicked():
    t = tkinter.filedialog.askopenfilenames()
    count(t)

# Create the window header.
header = tkinter.Label(app, text="Welcome to SlideCount!", fg="blue", font=("Arial Bold", 16))
header.pack(side="top", ipady=10)

# Add the descriptive text.
text = tkinter.Label(app, text="Select some .pptx files, and the\n app will count how many slides\n are contained within them.")
text.pack()

# Display the button to enable a summary view.
show_summary = tkinter.BooleanVar()
show_summary.set(True)
summary = tkinter.Checkbutton(app, text="Show summary", var=show_summary)
summary.pack(ipady=10)

# Draw the button that opens the file picker.
open_files = tkinter.Button(app, text="Choose decks...", command=clicked)
open_files.pack(fill="x")

# Initialize Tk window.
app.mainloop()