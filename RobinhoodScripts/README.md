# Robinhood Scripts
This Python project includes scripts that interact with the Robinhood API

## Installation

### Windows 10
Download Python 3.7 from the Windows Store and make sure it is selected as your active environment.

#### Download
In Windows 10, downloading the Windows Store version of Python will install it under the Packages directory (C:\Users\<USER>\AppData\Local\Packages)
which is where all UWP applications are registered for the current user.  I have not had success with Python 3.8 as, although this version seems to work,
there seems to be an issue with its version number (displays as 0.0 in Visual Studio) which creates issues when debugging.
Python 3.7 does not have the same issue with its version number. If installed via the Windows Store, check the App Execution Alias settings
and make sure that the toggles for `python.exe` (etc) are routed to Python 3.7.

Installing it via the traditional .exe installer [Python 3.8.2](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe) will install it by default
in the user's Programs directory (C:\Users\<USER>\AppData\Local\Programs).  The 1 major caveat to this is that Windows 10 has set the keyword `python`
as an execution alias for their Windows 10 UWP version of Python which will redirect you to the Windows store if you do not have that version installed.
IF INSTALLED VIA THIS METHOD, this needs to be untoggled via the App Execution Alias settings (it should show as redirecting python.exe and python3.exe to App Installer).
However, it might be a good idea to untoggle this anyway... seems weird to redirect `python` to the App Installer (very confusing).  Either way,
I have not had success with this method... it seems like this also yields the version issue in Visual Studio... but 3.7 probably works ok.

#### Selecting Python Environment in Visual Studio
Within the project RobinhoodScripts, Python Environments should expand to show you the current active environment.
If it has none, or it is pointing to the wrong location (you can tell by right clicking on it, going to properties, and checking the path)
right click on Python Environments and select `Add/Remove Python Environments...`.  This should give you a check box selection of currently installed instances of Python.
