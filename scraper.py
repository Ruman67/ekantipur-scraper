from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ekantipur.com/", wait_until="domcontentloaded")
        print("Website loaded successfully")
        browser.close()

if __name__ == "__main__":
    run()