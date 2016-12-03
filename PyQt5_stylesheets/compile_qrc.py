#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
Utility scripts to compile the qrc file. The script will
attempt to compile the qrc file using the following tools:
    - rcc
    - pyside-rcc
    - pyrcc4

Delete the compiled files that you don't want to use 
manually after running this script.
"""
import os


def compile_all():
    """
    Compile style.qrc using rcc, pyside-rcc and pyrcc4
    """
    print("Compiling for PyQt5: style_Dark.qrc -> pyqt5_style_Dark_rc.py")
    os.system("pyrcc5 style_Dark.qrc -o pyqt5_style_Dark_rc.py")

    print("Compiling for PyQt5: style_DarkOrange.qrc -> pyqt5_style_DarkOrange_rc.py")
    os.system("pyrcc5 style_DarkOrange.qrc -o pyqt5_style_DarkOrange_rc.py")

    print("Compiling for PyQt5: style_Classic.qrc -> pyqt5_style_Classic_rc.py")
    os.system("pyrcc5 style_Classic.qrc -o pyqt5_style_Classic_rc.py")

    print("Compiling for PyQt5: style_black.qrc -> pyqt5_style_black_rc.py")
    os.system("pyrcc5 style_black.qrc -o pyqt5_style_black_rc.py")

    print("Compiling for PyQt5: style_blue.qrc -> pyqt5_style_blue_rc.py")
    os.system("pyrcc5 style_blue.qrc -o pyqt5_style_blue_rc.py")

    print("Compiling for PyQt5: style_gray.qrc -> pyqt5_style_gray_rc.py")
    os.system("pyrcc5 style_gray.qrc -o pyqt5_style_gray_rc.py")

    print("Compiling for PyQt5: style_navy.qrc -> pyqt5_style_navy_rc.py")
    os.system("pyrcc5 style_navy.qrc -o pyqt5_style_navy_rc.py")


if __name__ == "__main__":
    compile_all()
