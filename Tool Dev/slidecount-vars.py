# A command-line version of SlideCount, using pre-defined variables.

import os
import re
import sys
import zipfile

# Define or gather the options and files to use
provide_summary = True
deck_dir = "/path/to/decks"
files = os.listdir(os.path.abspath(deck_dir))
# Or...
# files = ["/path/to/decks/deck1.pptx", "/path/to/decks/deck2.pptx", ...]

# Declare a dictionary to hold the [deck name, slide count]
decks = {}

# Iterate through the files.
if(files):
    for file in files:
        # If the file ends with ".pptx", add it to the decks dictionary with an initial count of 0 slides.
        if os.path.abspath(file).endswith('.pptx'):
                decks[(os.path.abspath(file))] = 0
        # If the file ends with something other than ".pptx", ignore it and print a message.
        else:
            print("The file %s is not a .pptx file and will be ignored." % (file))

# Iterate through the items in the decks dictionary.
for deck, count in decks.items():
    try:
        # Attempt to read the file as a zip archive.
        archive = zipfile.ZipFile(deck, 'r')
        # Use the file's list of included files instead of fully decompressing the file to disk.
        contents = archive.namelist()
    # If there was an error reading a file, leave its slide count at 0 and print a message.
    except Exception as e:
        print("Error reading %s (%s). Count will be 0." % (os.path.basename(deck), e))
    else:
        # Iterate through each item in the zip file's namelist.
        for fileentry in contents:
                # If a file entry matches a name we know to be a slide, increment the count of slides for that deck by 1.
                if(re.findall("ppt/slides/slide", fileentry)):
                        decks[deck] += 1

print("Slides\tDeck")

# Iterate through a sorted version of the decks dictionary, and print out the slide count and name of each deck.
for deck, count in sorted(decks.items()):
    print("%s\t%s" % (count, os.path.basename(deck)))

#If the user has requested a summary, print it.
if provide_summary:
    print("- - - - -")
    total = 0
    # Iterate through the values in the decks dictionary and add up all of the counts.
    for count in decks.values():
        total += count
    print("%s total slides in %s decks." % (total, len(decks)))