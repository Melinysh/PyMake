##### PyMake
#### A basic makefile generator

Pymake generates a Makefile for the files of the current working directory. Currently works with C and C++ files and can use gcc or g++ for the compiler. 

## Current version: 0.1.1 

## Usage: pymake.py [-f "Flags" -o Output File -d Directory]  

## Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -f Flags, --flags=Flags  
                        Extra flags for the compiler. Typed within quotes. For
                        example, "-Wall". Default is "-o [fileName]"  
  -o outputFile, --output=outputFile  
                        Output file name from compiler. Default is a.out 
  -d directory, --directory=directory
                          Directory for pymake to create Makefile for. Default
						  is ./
