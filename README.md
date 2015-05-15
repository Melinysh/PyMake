# PyMake
## A basic makefile generator

Pymake generates a Makefile for the files of the current working directory. Currently works with C/C++ files. You can declare your compiler or pymake will try to detect gcc or g++ for the compiler. 

#### What's New
* Support for 'make install'
* Support for 'make uninstall'
* Restructured Makefile to support variables


####Usage: pymake.py  \[-c Compiler -d Source Directory -f "Flags" -i Install Directory -o Output File\]  

Options:  

  --version  
show program's version number and exit  

  -h, --help  
show this help message and exit   
 
  -c compiler, --compiler=compiler	
Set compiler to use. If not set, pymake will look at your files and guess  

-d directory, --directory=directory  
Directory for pymake to create Makefile in. Default is ./   

  -f Flags, --flags=Flags  
Extra flags for the compiler. Typed within quotes. For example, "-Wall"    

-i installPath, --install-dir=installPath  
Directory for 'make install'. Default is /usr/local/bin  

  -o outputFile, --output=outputFile  
Output file name from compiler. Default is a.out    

  
  



