# PySide 6 & Qt Learning Path

Hello!

This is my personal journey of learning how to create desktop applications with Qt and its Python module, PySide6. 

It mostly follows the [freeCodeCamp tutorial](https://youtu.be/Z1N9JzNax2k) and the Daniel Gakwaya [repository](https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-) (same tutorial files), which I found to be great resources to understand the library, the essential components and how they interact with each other to make a functional GUI desktop app.

Each lecture of this repo presents either one of the following:
- A new GUI component and how it is configured inside the working window
- A non-GUI module to extend an existing GUI object functionality

Almost by default, all lecture folders have a `main.py` and a `widget.py` files. The first one is used solely to run the application, and the other contains the relevant code for the lecture. As advised in the tutorials (and some previous experience with GUI libraries), it uses an OOP structure to manage and contain pieces of code.

As I learn a new topic included in the tutorial, or from another source, I will commit the the folder with its respective files.

Although it is a personal learning path, it might be of use to you, dear reader. If thats the case, go ahead, clone the repo and run the scripts in the lecture folders! I strongly advise creating a virtual environment in your working directory and installing the latest version of PySide inside of it, like this (in Windows):

```
python -m venv .venv
.\.venv\Scripts/activate.bat
pip install pyside6
```

For other OS installations, more tutorials, and API, its best to use the official [PySide6 documentation](https://doc.qt.io/qtforpython-6/index.html).
