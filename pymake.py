#!/usr/bin/env python
import os
from optparse import OptionParser

## Defaults
flags = ""
outputFile = ""

def parseCommandline():
    global flags, outputFile 
    # Get commandline arguments
    parser = OptionParser(usage="Usage: pymake.py [-f \"Flags\" -o Output File]", version="0.1")
    parser.add_option("-f", "--flags", dest="flags", help="Extra flags for the compiler. Typed within quotes. For example, \"-Wall\". Default is \"-o [fileName]\"", default="", metavar="Flags")
    parser.add_option("-o", "--output", dest="outputFile", help="Output file name from compiler. Default is a.out", default="a.out", metavar="outputFile") 
    (options, args) = parser.parse_args()
    outputFile = options.outputFile
    flags = options.flags

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
    return fileContents 

def writeToMakefile(fileContents):
    makefile = open("Makefile", 'w')
    makefile.write(fileContents)
    makefile.close()


def start():
    parseCommandline()
    fileList = files()
    fileNames = ""
    for f in fileList:
        fileNames += f + " "
    fileContents = generateFileContents(fileNames, compiler(typeOfFile(fileList[0])))
    writeToMakefile(fileContents)
    print("Makefile created.")
    exit(0)

start()
