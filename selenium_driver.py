from selenium import webdriver
import os

CURRENT_DIR = os.getcwd()


def get_driver(download_dir=None):
    if download_dir is None:
        download_dir = os.path.join(CURRENT_DIR, 'data')

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
      "download.default_directory": download_dir,
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True,
      "plugins.always_open_pdf_externally": True
    })
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options)

    # prevent bugs due to elements not loading properly in headless mode
    driver.set_window_size(1440, 900)
    return driver