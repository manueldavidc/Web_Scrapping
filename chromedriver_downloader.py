import os
import platform
import zipfile
import urllib.request

def download_chromedriver():
    # Get the appropriate download URL for ChromeDriver based on the OS
    system = platform.system()
    
    if system == "Linux":
        url = "https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip"
    elif system == "Darwin":  # macOS
        url = "https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_mac64.zip"
    elif system == "Windows":
        url = "https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip"
    else:
        raise Exception(f"Unsupported system: {system}")

    # Define the path to store the driver
    chromedriver_zip = "chromedriver.zip"

    # Download the zip file
    print(f"Downloading ChromeDriver from {url}")
    urllib.request.urlretrieve(url, chromedriver_zip)

    # Extract the zip file
    with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
        zip_ref.extractall(".")
    
    # Clean up
    os.remove(chromedriver_zip)
    print(f"ChromeDriver downloaded and extracted.")

download_chromedriver()
