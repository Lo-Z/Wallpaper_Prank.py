#------------------------------------------------------------------~-~ Ω <(-.-)> Ω ~-~-------------------------------------------------------------------
#
# This python script will change the wallpapaer of a windows PC using a .jpg image via HTTP and requires internet access. 
#
# To convert this .py to an .exe file for windows so that python is not needed to run use -> pyinstaller --onefile --noconsole --hidden-import=requests Wallpaper_Prank.py
#
# The current HTTPS link will change the wallpaper of the PC to a my little pony picture. After the .exe is created then you can rename it to whatever you want
#
# This was originally created as a prank for a coworker "Hey, can you check if this tool works on your machine? IT wants feedback. -> SalaryAdjustment2025.exe"
#
# I am not responsible for the misuse of this script. 
#
#------------------------------------------------------------------~-~ Ω <(-.-)> Ω ~-~-------------------------------------------------------------------

import ctypes
import os
import requests
import shutil
from pathlib import Path

# Function to set the wallpaper ------------------------------------------------------------------------------------------------------------------------
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014                           # Windows system command to change the wallpaper
    SPIF_UPDATEINIFILE = 0x01                               # Updates the system's INI file (Windows registry setting)
    SPIF_SENDCHANGE = 0x02                                  # Broadcasts the change to all applications
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

# Function to download an image from a URL and save it locally -----------------------------------------------------------------------------------------
def download_image(url, save_path):                          
    response = requests.get(url, stream=True)                # Send an HTTP GET request to the given URL, streaming the response to handle large files efficiently
    if response.status_code == 200:                          # Check if the request was successful (HTTP status code 200 means "OK")
        with open(save_path, 'wb') as file:                  # Open a new file at the specified save path in write-binary ('wb') mode
            shutil.copyfileobj(response.raw, file)           # Copy the downloaded content (raw data) into the file
        return save_path                                     # Return the path of the saved image
    else:
        return None                                          # Return None if the download failed

# Main prank function ----------------------------------------------------------------------------------------------------------------------------------
def prank():
    funny_image_url = "https://wallpapercat.com/w/full/0/0/5/2004525-2048x1152-desktop-hd-my-little-pony-a-new-generation-wallpaper-photo.jpg"      # URL of .jpg image to use as wallpaper
    temp_dir = Path(os.getenv("TEMP"))                       # Get the Windows temp folder path
    funny_image_path = temp_dir / "funny_wallpaper.jpg"      # Set the file path for saving the downloaded image


  # Download funny image -------------------------------------------------------------------------------------------------------------------------------
    downloaded_path = download_image(funny_image_url, funny_image_path)  # Try to download the image and save it

    if not downloaded_path:                                  # Check if the download failed
        print("Failed to download the image. Exiting prank.")  # Print error message if download was unsuccessful
        return                                               # Exit the function to prevent errors

    # Set funny wallpaper ------------------------------------------------------------------------------------------------------------------------------
    set_wallpaper(str(funny_image_path))                     # Change the desktop wallpaper to the downloaded funny image

# Run prank --------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":                                   # Ensure the script runs only when executed directly
    prank()                                                  # Call the prank function to change the wallpaper
