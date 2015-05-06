# PyMake
## A basic makefile generator

Pymake generates a Makefile for the files of the current working directory. Currently works with C/C++ files. You can declare your compiler or pymake will try to detect gcc or g++ for the compiler. 

#### Current version: 0.1.3


####Usage: pymake.py [-f "Flags" -o Output File -d Directory -c Compiler]   

Options:  

  --version  
show program's version number and exit  

  -h, --help  
show this help message and exit   
 
  -f Flags, --flags=Flags  
Extra flags for the compiler. Typed within quotes. For example, "-Wall". Default is "-o [fileName]"  

  -o outputFile, --output=outputFile  
Output file name from compiler. Default is a.out    

  -d directory, --directory=directory  
Directory for pymake to create Makefile in. Default is ./  
  
  -c compiler, --compiler=compiler	
Set compiler to use. If not set, pymake will look at your files and guess.  


