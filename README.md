PyQt5_stylesheetssheet
==================
skin include:
style_blue
style_black
style_Classic
style_Dark
style_DarkOrange
style_gray
style_navy


these stylesheet for Qt applications (PyQt5).


License
===========

This project is licensed under the MIT license.


Installation
==============

Python
-----------

Install ``PyQt5_stylesheets`` package using the *setup* script or using *pip*:

```bash
python setup.py install
```

or

```bash
pip install PyQt5_stylesheets
```

Usage
============
```Python

import PyQt5_stylesheets
app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_black"))
```
```Python

import PyQt5_stylesheets
class yourDialog(QDialog):
    def __init__(self,parent=None):
      supper(QDialog,self).__init__(parent):
      self.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_black"))
      ...
      ...
```

style Include
============
`style_blue`
`style_black`
`style_Classic`
`style_Dark`
`style_DarkOrange`
`style_gray`
`style_navy`


Contact information:
=========================

  - Maintainer: 13693421942@163.com
  - Homepage: https://github.com/xiongbigboss/PyQt5_stylesheets.git


Snapshots
=================

Here are a few snapshots:

![alt text](/screenshots/example.png "example")
![alt text](/screenshots/example1.png "example1")
![alt text](/screenshots/example2.png "example2")
![alt text](/screenshots/example3.png "example3")
![alt text](/screenshots/example4.png "example4")
![alt text](/screenshots/example5.png "example5")

