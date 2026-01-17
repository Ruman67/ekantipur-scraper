from playwright.sync_api import sync_playwright
import json
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://ekantipur.com/", wait_until="domcontentloaded")
        print("Website loaded successfully")
#for clsoing of the ad
        page.wait_for_timeout(2000)
        try:
            close_btn = page.query_selector("i.icon-close[onclick=\"hide('roadblock-ad')\"]")
            if close_btn:
                close_btn.click()
                page.wait_for_timeout(1000)
                print("Ad closed successfully")
        except Exception as e:
            print(f"Could not close ad: {e}")

        browser.close()

if __name__ == "__main__":
    run()