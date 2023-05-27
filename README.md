# computer_program_virus

To make the script run at startup on both Windows and macOS, you can follow the instructions below:


On Windows:


Save your script with a .pyw extension instead of .py (e.g., script.pyw). The .pyw extension indicates that the script should run as a "Windows" application without displaying a console window.


Press Win + R to open the Run dialog.


Type shell:startup and press Enter. This will open the Startup folder for the current user.

Move or create a shortcut to your script into this Startup folder. To create a shortcut, right-click in the folder, select "New," and then "Shortcut." In the "Location" field, provide the path to your Python executable (e.g., C:\Python\python.exe) followed by the path to your script (e.g., C:\Path\to\script.pyw). Click "Next" and follow the instructions to create the shortcut.

Restart your computer, and your script should automatically run at startup without displaying a console window.


On macOS:

Save your script with a .py extension (e.g., script.py).

Open a terminal.

Run the following command to open the user's Login Items settings:


"open -b com.apple.systempreferences /System/Library/PreferencePanes/Accounts.prefPane"


In the "Login Items" tab, click the "+" button to add a new item.

Locate and select your script (script.py) in the file selection dialog.

Click "Add" to add the script to the Login Items.

Restart your computer, and your script should automatically run at startup.

Please note that the specific steps may vary slightly depending on the version of Windows or macOS you are using. Additionally, keep in mind that running scripts at startup might require administrative privileges on some systems.
