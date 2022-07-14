'''
MIT License
Copyright (c) 2022 Juan Carlos Bindez
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


Author: www.github.com/JuanBindez
License: https://github.com/JuanBindez/PyLockDir/blob/main/LICENSE
Description: change file and directory permissions
Python Version: 3.10
year: 2022
Local: Brazil
OS: Linux
'''



def header_menu():
    print(
        '''
                             ____        _               _    ____  _      
                            |  _   _   _| |    ___   ___| | _|  _  (_)_ __ 
                            | |_) | | | | |   / _ \ / __| |/ / | | | | '__|
                            |  __/| |_| | |__| (_) | (__|   <| |_| | | |   
                            |_|     __, |_____ ___/  ___|_| _ ____/|_|_|   
                                   |___/                              
        
                               [ Ctrl + C ]  Para Encerrar o Programa

        '''
    )


def header_choices():
    print(

        '''



                            [1]  ---------  000        [6]  rw-rw-rw-  666
                            [2]  r--------  400        [7]  rwx------  700
                            [3]  r--r--r--  444        [8]  rwxr-x---  750
                            [4]  rw-------  600        [9]  rwxr-xr-x  755
                            [5]  rw-r--r--  644        [10] rwxrwxrwx  777
        
        
        '''
    )
