# This script will go through all images in a directory and pull the text from the images
# using the Tesseract OCR engine.

import os
import subprocess
import lxml

BASEDIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_PATH = BASEDIR + "/About Text"
TEXTS_PATH = BASEDIR + "/text/"
COMMAND = "tesseract"

def read_image(filename):
    # Get the name of the new text file (Tesseract automatically appends a .txt extension)
    textName = "../text/" + filename.split(".png")[0]
    # Compose command with relevant filenames.
    command = COMMAND + " " + filename + " " + textName

    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)

def generate_text():
    os.chdir(IMAGES_PATH)
    files = os.listdir(".")
    for filename in files:
        if not ".meta" in filename:
            if not "@2x" in filename:
                read_image(filename)

    print "Text generated."

def generate_xml():
    os.chdir(TEXTS_PATH)
    files = os.listdir(".")
    for file in files:
        with open(file, "r") as openFile:
            text = openFile.read().split("\n\n")
            print len(text)

    print "XML generated."

def test():
    print IMAGES_PATH
    print TEXTS_PATH

def main():
    generate_text()

main()
