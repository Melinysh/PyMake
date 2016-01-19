# PyMake
## A Makefile Generator 

PyMake generates a Makefile for the files of the current working directory or the specified directory. Currently works with C, C++, Fortran and Go files. You can declare your compiler or PyMake will try to detect `gcc`, `g++`, `gfortran` or `go build` for the compiler.  PyMake builds a Makefile that uses variables, so you don't have to rerun PyMake to modify your Makefile. In version 0.3, PyMake started supporting configuration files and to learn more, see the section below.  

### Usage
```
Usage: pymake.py [ -cdfihotvx ]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c COMPILER, --compiler=COMPILER
                        set compiler to use. Default: PyMake will look at your
                        files and guess, if it can't then it will use gcc
  -d DIRECTORY, --directory=DIRECTORY
                        directory for pymake to create Makefile for. Default:
                        ./
  -f FLAGS, --flags=FLAGS
                        flags for the compiler and typed within quotes
  -i INSTALLPATH, --install-dir=INSTALLPATH
                        directory for 'make install'. Default: /usr/local/bin
  -o OUTPUTFILE, --output-target=OUTPUTFILE
                        output file name from compiler. Default: a.out
  -t FILETYPE, --file-type=FILETYPE
                        the file type of your source files (ex. c, cpp, go).
                        Default: pymake will look at your files and guess
  -v                    enable verbose output
  -x CONFIGFILE, --config-file=CONFIGFILE
                        path to pymake config file. Default: ~/.pymake.cfg
```

### Recent updates
#### Version 0.4:
- Support for partial recompilation  (Yay!)
- Support for verbose output 
- Support for specifying the path to a config file

#### Version 0.4.2:
- Added `-t` flag for specifying your source file type

### Using the configuration file
Since version 0.3, PyMake supports reading a configuration file. This file, `.pymake.cfg`, can be placed in your home directory or specified with the `-x` flag. If found, PyMake will use the configuration options (compiler, flags, installation directory) over passed commandline options. The file should be formatted similar to a `.ini` file with sections named after the file extension of that programming language (ex. `c`, `cpp`). See the sample configuration file for an example. Future revisions to PyMake will increase the flexibility of the use of a configuration file. 


###License 
The MIT License (MIT)

Copyright (c)  2016 Stephen Melinyshyn

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
  
  



