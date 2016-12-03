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
PyQt5_stylesheets is a darks stylesheet for python qt applications
"""
from setuptools import setup, find_packages
from PyQt5_stylesheets import __version__

setup(
    name='PyQt5_stylesheets',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/xiongbigboss/PyQt5_stylesheets.git',
    license='MIT',
    author='xiongbigboss',
    author_email='13693421942@163.com',
    description='A dark stylesheet for PyQt5 applications',
    long_description="""
This package provides a dark style sheet for PyQt5 applications.

All you have to do is the following::

    import PyQt5_stylesheets
    app = QtGui.QApplication().instance()

    # PyQt5
    app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_black"))

""",
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications :: Qt5',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Application Frameworks'])
