# PyMake
## A Makefile Generator 

PyMake generates a Makefile for the files of the current working directory or the specified directory. Currently works with C, C++, Fortran and Go files. You can declare your compiler or PyMake will try to detect `gcc`, `g++`, `gfortran` or `go build` for the compiler.  PyMake builds a Makefile that uses variables, so you don't have to rerun PyMake to modify your Makefile.


###Usage: pymake.py [ -c Compiler ] [ -d Source Directory ] [ -f "Flags" ] [ -i Install Directory ] [ -o Output File ] 

#####Options:  
--version  
show program's version number and exit  

-h, --help  
show this help message and exit   

-f FLAGS, --flags=FLAGS  
flags for the compiler and typed within quotes  

-o OUTPUTFILE  
output file name from compiler. Default: a.out  

-d DIRECTORY, --directory=DIRECTORY  
  directory for pymake to create Makefile for. Default: ./  

-c COMPILER, --compiler=COMPILER  
  set compiler to use. Default: PyMake will look at your files and guess  

-i INSTALLPATH, --install-dir=INSTALLPATH  
directory for 'make install'. Default: /usr/local/bin  


###License 
The MIT License (MIT)

Copyright (c)  2015 Stephen Melinyshyn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
  



