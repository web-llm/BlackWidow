from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import argparse

from Classes import *

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument("--debug", action='store_true',  help="Dont use path deconstruction and recon scan. Good for testing single URL")
parser.add_argument("--url", help="Custom URL to crawl")
parser.add_argument("--remote", help="Remote WebDriver URL")
args = parser.parse_args()

# Clean form_files/dynamic
root_dirname = os.path.dirname(__file__)
dynamic_path = os.path.join(root_dirname, 'form_files', 'dynamic')
if os.path.exists(dynamic_path):
    for f in os.listdir(dynamic_path):
        os.remove(os.path.join(dynamic_path, f))
else:
    os.makedirs(dynamic_path)

WebDriver.add_script = add_script


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-xss-auditor")

# launch Chrome
if args.remote:
    driver = webdriver.Remote(command_executor=args.remote, options=chrome_options)
else:
    driver = webdriver.Chrome(options = chrome_options)



#driver.set_window_position(-1700,0)

# Read scripts and add script which will be executed when the page starts loading
## JS libraries from JaK crawler, with minor improvements
driver.add_script( open("js/lib.js", "r").read() )
driver.add_script( open("js/property_obs.js", "r").read() )
driver.add_script( open("js/md5.js", "r").read() )
driver.add_script( open("js/addeventlistener_wrapper.js", "r").read() )
driver.add_script( open("js/timing_wrapper.js", "r").read() )
driver.add_script( open("js/window_wrapper.js", "r").read() )
# Black Widow additions
driver.add_script( open("js/forms.js", "r").read() )
driver.add_script( open("js/xss_xhr.js", "r").read() )
driver.add_script( open("js/remove_alerts.js", "r").read() )

if args.url:
    url = args.url
    Crawler(driver, url).start(args.debug)
else:
    print("Please use --url")




