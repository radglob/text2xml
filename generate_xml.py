# This script will take generated text files and compile them into a single xml file.
# NOTE: It is advised that you check all of your text files first.

import os
from lxml import etree
import re

TEXTS_PATH = os.path.dirname(os.path.realpath(__file__)) + "/text/"
XML_HEADER = '<?xml version="1.0" encoding="utf-8"?>'

def generate_xml():
    # Start XML tree
    root = etree.Element('document')

    os.chdir(TEXTS_PATH)
    files = os.listdir(".")
    for file in files:
        # Ignore meta files
        if not ".meta" in file:
            text = parseFile(file)
            # Generate three parts from text
            group = etree.Element('group')
            
            title = etree.SubElement(group, 'title')
            title.text = text[0].decode('unicode-escape')
            
            subtitle = etree.SubElement(group, 'subtitle')
            subtitle.text = text[1].decode('unicode-escape')
            
            content = etree.SubElement(group, 'content')
            content.text = "\n\n".join(text[2:]).decode('unicode-escape')
            
            # Add to tree
            root.append(group)
            
    treeString = etree.tostring(root, pretty_print=True)
    os.chdir("..")

    # Write to file
    xml_file = open("text.xml", "w")
    xml_file.write(XML_HEADER + "\n")
    xml_file.write(treeString)
    xml_file.close()

    print "XML generated."

def parseFile(file):
    with open(file, "r") as openFile:
        text = openFile.read().split("\n\n")
        return text
    return None

def main():
    generate_xml()

main()
