#!/usr/bin/env python3
import os
from optparse import OptionParser
from configparser import ConfigParser 

## Global variables
VERSION = "0.6.2"
flags = ""
outputFile = ""
directory = ""
compiler = ""
installPath = ""
builddir = ""
srcdir = ""
configFile = ""
fileType = ""
verbose = False

def debugPrint(*args):
    if verbose:
        for a in args:
            print((a), end=' ')
        print("")

def parseCommandline():
    global flags, outputFile, directory, compiler, installPath, builddir, srcdir, configFile, verbose, fileType
    # Get commandline arguments
    parser = OptionParser(usage="Usage: pymake.py [ -bcdfihostvx ]", version="PyMake Version " + VERSION)
    parser.add_option("-b", "--build-dir", dest="builddir", help="set build directory for project to use. Default: .", default=".")
    parser.add_option("-c", "--compiler", dest="compiler", help="set compiler to use. Default: PyMake will look at your files and guess, if it can't then it will use gcc", default="")
    parser.add_option("-d", "--directory", dest="directory", help="directory for pymake to create Makefile for. Default: .", default=".")
    parser.add_option("-f", "--flags", dest="flags", help="flags for the compiler and typed within quotes", default="")
    parser.add_option("-i", "--install-dir", dest="installPath", help="directory for 'make install'. Default: /usr/local/bin", default="/usr/local/bin")
    parser.add_option("-o", "--output-target", dest="outputFile", help="output file name from compiler. Default: a.out", default="a.out")
    parser.add_option("-s", "--source-dir", dest="srcdir", help="set source directory for project to use. Default: .", default=".")
    parser.add_option("-t", "--file-type", dest="fileType", help="the file type of your source files (ex. c, cpp, go). Default: pymake will look at your files and guess", default = "")
    parser.add_option("-v", dest="verbose", help="enable verbose output", action="store_true")
    parser.add_option("-x", "--config-file", dest="configFile", help="path to pymake config file. Default: ~/.pymake.cfg", default="~/.pymake.cfg")

    (options, args) = parser.parse_args()
    outputFile = options.outputFile
    flags = options.flags
    directory = options.directory
    compiler = options.compiler
    installPath = options.installPath
    builddir = options.builddir
    srcdir = options.srcdir
    configFile = options.configFile
    verbose = options.verbose
    fileType = options.fileType

def parseConfig(fileType):
    global flags, compiler, installPath
    conf = ConfigParser()
    f = conf.read(os.path.expanduser(configFile))
    if len(f) == 0:
        debugPrint("Unable to find config file at " + configFile)
        return False
    debugPrint("Config file found at " + configFile)
    confFlags = confCompiler = confInstallDir = ""
    try:
      confFlags = conf.get(fileType, "flags")
    except:
        pass
    try:
        confCompiler = conf.get(fileType, "compiler")
    except:
        pass
    try:
        confInstallDir = conf.get(fileType, "installPath")
    except:
        pass
    if len(confFlags) != 0 :
        flags = confFlags
    if len(confCompiler) != 0:
        compiler = confCompiler
    if len(confInstallDir) != 0:
        installPath = confInstallDir
    return True


def files():
    print((os.getcwd()))
    allFiles = [f for f in os.listdir(os.getcwd() + "/" + srcdir) if os.path.isfile(srcdir + "/" +f)]
    sourceFiles = []
    for f in allFiles:
        if "." in f and isSourceFile(f):
            sourceFiles.append(f.lower())
    return sourceFiles

# Checks to see if the file extention should be included in file list for compiler
def isSourceFile(fileName):
    if fileName.startswith("."):
        return False
    elif fileName.split(".")[-1] in ["c", "cc", "cpp", "cxx", "cp", "go", "f", "f90", "f95", "f03", "f15", "for", "s", "asm"]:
        return True
    return False

def typeOfFile(fileName):
    return fileName[(fileName.index('.'))+1:]

def baseFileName(fileName):
    return fileName[:(fileName.index('.'))]

def setCompiler(fileType):
    global compiler
    if compiler != "":
        return
    if fileType in ["c", "s", "asm"]:
        compiler = "gcc"
    elif fileType in ["cc", "cpp", "cxx", "cp"]:
        compiler = "g++"
    elif fileType in ["f", "f90", "f95", "f03", "f15", "for"]:
        compiler = "gfortran"
    elif fileType == "go":
        compiler = "go build"
    else:
        print(("File type '" + fileType + "' not supported yet. Defaulting to gcc."))
        compiler = "gcc"

def flagsForCompiler(compilerName):
    compilerVarName = ""
    compilerFlagsName = ""

    if compilerName == "g++":
        compilerVarName = "CXX"
        compilerFlagsName = "CXXFLAGS"
    elif compilerName == "gfortran":
        compilerVarName = "FF"
        compilerFlagsName = "FFLAGS"
    elif compilerName == "go build":
        compilerVarName = "GC"
        compilerFlagsName = "GCFLAGS"
    else:
        # Default to gcc with C setup
        compilerVarName = "CC"
        compilerFlagsName = "CFLAGS"

    flagVars =  compilerVarName + " := " + compilerName + "\n"
    flagVars += compilerFlagsName + " := " + flags + "\n"
    ## Use PYMAKE_COMPILER_FLAGS and PYMAKE_COMPILER to keep it track of compiler and flags for internal use
    flagVars += "PYMAKE_COMPILER := $(" + compilerVarName + ")\n"
    flagVars += "PYMAKE_COMPILER_FLAGS := $(" + compilerFlagsName + ")\n"
    return flagVars


def generateFileContents(fileType, compilerName):
    fileContents = "# Generated by pymake version " + VERSION + "\n# PyMake was written by Stephen Melinyshyn | github.com/Melinysh/PyMake\n\n"

    # Compiler specific variables
    fileContents += flagsForCompiler(compilerName)
    fileContents += "SRCEXT := " + fileType + "\n"
    fileContents += "SRCDIR := " + srcdir + "\n"
    fileContents += "BUILDDIR := " + builddir + "\n"
    fileContents += "INSTALL_PATH := " + installPath + "\n"
    fileContents += "TARGET := " + outputFile + "\n"
    fileContents += "SOURCES := $(wildcard $(SRCDIR)/*.$(SRCEXT))\n"
    fileContents += "OBJECTS := $(patsubst $(SRCDIR)/%.o,$(BUILDDIR)/%.o,$(SOURCES:.$(SRCEXT)=.o))\n"

    fileContents += "\n\nall: $(TARGET)\n\n"

     # Main compilation
    fileContents += "$(TARGET): " + ("\n" if fileType == "go" else "$(OBJECTS)\n")
    fileContents += "\t$(PYMAKE_COMPILER) " + ("$(PYMAKE_COMPILER_FLAGS) " if fileType == "go" else "") + "-o $(TARGET) " + ("$(SOURCES)" if fileType == "go" else "$^") + "\n\n"

    # Object files
    if fileType != "go":
        fileContents += "$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)\n"
        fileContents +="\t$(PYMAKE_COMPILER) $< $(PYMAKE_COMPILER_FLAGS) -c -o $@\n"

    ## Clean
    fileContents += "\n"
    fileContents += "clean:" + "\n"
    fileContents += "\t" + "-rm $(TARGET) " + ("" if fileType == "go" else "$(OBJECTS)") + "\n"

    ## Run
    fileContents += "\n"
    fileContents += "run: all\n"
    fileContents += "\t./$(TARGET)\n"

    ## Install
    fileContents += "\n"
    fileContents += "install: $(TARGET)\n"
    fileContents += "\tinstall $(TARGET) $(INSTALL_PATH)\n"

    ## Uninstall
    fileContents += "\n"
    fileContents += "uninstall:\n"
    fileContents += "\t-rm $(INSTALL_PATH)/$(TARGET)\n"


    return fileContents

def writeToMakefile(fileContents):
    makefile = open("Makefile", 'w')
    makefile.write(fileContents)
    makefile.close()


def guessFileType(files):
    global fileType
    if len(files) == 0:
        print("Whoops! PyMake can't find any files that would belong in a Makefile.")
        print("Are you sure you're in the right directory?")
        exit(1)
    fileType = typeOfFile(files[0])


def start():
    parseCommandline()
    os.chdir(directory)
    fileList = files()
    debugPrint("Files found in src directory ",srcdir," : ", fileList)
    if fileType == "":
        guessFileType(fileList)
    debugPrint("Pymake believes the filetype is " + fileType)
    setCompiler(fileType)
    debugPrint("Compiler is set to " + compiler)

    parseConfig(fileType)

    fileContents = generateFileContents(fileType, compiler)
    writeToMakefile(fileContents)
    debugPrint("Successfully generated Makefile.")

    exit(0)

start()
