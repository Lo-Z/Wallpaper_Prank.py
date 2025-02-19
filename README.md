# Wallpaper_Prank.py
A Python script that can be converted into a windows .exe that changes the desktop wallpaper to whatever .jpg from the internet that you wish.

------------------------------------------------------------------~-~ Ω <(-.-)> Ω ~-~-------------------------------------------------------------------

 This python script will change the wallpaper of a windows PC using an HTTP URL and requires internet access. 

 To convert this .py to an .exe file for windows so that python is not needed to run use the following command
 
-   pyinstaller --onefile --noconsole --hidden-import=requests Wallpaper_Prank.py

 The current HTTPS link will change the wallpaper of the PC to a my little pony picture. After the .exe is created then you can rename it to whatever you want

 This was originally created as a prank for a coworker "Hey, can you check if this tool works on your machine? IT wants feedback. -> SalaryAdjustment2025.exe"

 I am not responsible for the misuse of this script. 

------------------------------------------------------------------~-~ Ω <(-.-)> Ω ~-~-------------------------------------------------------------------

# Bonus Fun

If you want to change the icon of the .exe to match that of a known app, you'll need an .ico file

You can find some images of icons here [Icon Archive](https://iconarchive.com/) or here [Icons8](https://icons8.com/) 

Icons8 has more realistic icons IMO

Once you've downloaded an icon, you'll need to convert it to an .ico if it's not already in that format. Coverter Here [IcoConverter](https://icoconvert.com/)

Once you have your desired .ico file recomile the python script with the below command

-  pyinstaller --onefile --noconsole --icon="C:\File\Path\To\icon.ico" --hidden-import=requests Wallpaper_Prank.py

Your new .exe file will be inside the dist/ folder in whatever folder you compiled the original .py script in.

again I am not responsible for the misuse of this script. 

------------------------------------------------------------------~-~ Ω <(-.-)> Ω ~-~-------------------------------------------------------------------
