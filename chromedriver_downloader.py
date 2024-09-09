import os
import platform
import zipfile
import urllib.request
import stat

def download_chromedriver():
    # Get the appropriate download URL for ChromeDriver based on the OS
    system = platform.system()
    
    if system == "Linux":
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip"
    elif system == "Darwin":  # macOS
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_mac64.zip"
    elif system == "Windows":
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_win32.zip"
    else:
        raise Exception(f"Unsupported system: {system}")

    # Define the path to store the driver
    chromedriver_zip = "chromedriver.zip"
    chromedriver_dir = os.path.join(os.path.expanduser("~"), ".local", "bin")

    # Ensure the directory exists
    os.makedirs(chromedriver_dir, exist_ok=True)

    # Download the zip file
    print(f"Downloading ChromeDriver from {url}")
    urllib.request.urlretrieve(url, chromedriver_zip)

    # Extract the zip file to the desired directory
    with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
        zip_ref.extractall(chromedriver_dir)
    
    # Clean up the zip file
    os.remove(chromedriver_zip)

    # Make the ChromeDriver executable
    chromedriver_path = os.path.join(chromedriver_dir, "chromedriver")
    os.chmod(chromedriver_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

    print(f"ChromeDriver downloaded and extracted to {chromedriver_dir}.")

download_chromedriver()

