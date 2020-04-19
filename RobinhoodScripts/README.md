# Robinhood Scripts
This Python project includes scripts that interact with the Robinhood API

## Installation

### Windows 10
Download Python 3.8 (or newer) and make sure it is selected as your active environment.

#### Download
In Windows 10, downloading the Windows Store version of Python will install it under the Packages directory (C:\Users\<USER>\AppData\Local\Packages)
which is where all UWP applications are registered for the current user.

Installing it via the traditional .exe installer  [Python 3.8.2](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe) will install it by default
in the user's Programs directory (C:\Users\<USER>\AppData\Local\Programs)

#### Selecting Python Environment in Visual Studio
Within the project RobinhoodScripts, Python Environments should expand to show you the current active environment.
If it has none, or it is pointing to the wrong location (you can tell by right clicking on it, going to properties, and checking the path)
right click on Python Environments and select `Add/Remove Python Environments...`.  This should give you a check box selection of currently installed instances of Python.
