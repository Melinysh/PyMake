#!/usr/bin/env python
import os
from optparse import OptionParser

## Global variables
flags = ""
outputFile = ""
directory = ""

def parseCommandline():
    global flags, outputFile, directory 
    # Get commandline arguments
    parser = OptionParser(usage="Usage: pymake.py [-f \"Flags\" -o Output File -d Directory]", version="PyMake Version 0.1.2")
    parser.add_option("-f", "--flags", dest="flags", help="Extra flags for the compiler. Typed within quotes. For example, \"-Wall\". Default is \"-o [fileName]\"", default="", metavar="Flags")
    
    parser.add_option("-o", "--output", dest="outputFile", help="Output file name from compiler. Default is a.out", default="a.out", metavar="outputFile") 
    parser.add_option("-d", "--directory", dest="directory", help="Directory for pymake to create Makefile for. Default is ./", default="./", metavar="directory") 
    (options, args) = parser.parse_args()
    outputFile = options.outputFile
    flags = options.flags
    directory = options.directory

def files():
    allFiles = [f for f in os.listdir('.') if os.path.isfile(f)]
    sourceFiles = []
    for f in allFiles:
        if "." in f:
            sourceFiles.append(f)
    return sourceFiles

def typeOfFile(fileName):
    return fileName[(fileName.index('.'))+1:]

def baseFileName(fileName):
    return fileName[:(fileName.index('.'))]

def compiler(fileType):
    if fileType == "c":
        return "gcc"
    elif fileType == "cpp":
        return "g++"
    else:
        print("File type '" + fileType + "' not supported yet. Defaulting to gcc.")
        return "gcc"

def generateFileContents(fileNames, compilerName):
    global flags, outputFile ## From commandline
    fileContents = ""
    fileContents += outputFile + ": " + fileNames
    fileContents += "\n" + "\t"
    fileContents += compilerName
    if len(flags) != 0: # The user has defined flags, so use those instead.
        fileContents += " " + flags + " -o " + outputFile + " " + fileNames
    else:
        fileContents += " -o " + outputFile + " " + fileNames
    ## Clean
    fileContents += "\n\n"
    fileContents += "clean:" + "\n"
    fileContents += "\t" + "$(RM) " + outputFile
    return fileContents 

def writeToMakefile(fileContents):
    makefile = open("Makefile", 'w')
    makefile.write(fileContents)
    makefile.close()


def start():
    parseCommandline()
    os.chdir(directory)
    fileList = files()
    fileNames = ""
    for f in fileList:
        fileNames += f + " "
    fileContents = generateFileContents(fileNames, compiler(typeOfFile(fileList[0]))) # Take the file type of the first file
    writeToMakefile(fileContents)
    print("Makefile created.")
    exit(0)

start()
