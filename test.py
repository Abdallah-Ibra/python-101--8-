from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.amazon.com/")

    page.get_by_placeholder("Search Amazon").click()

    page.get_by_placeholder("Search Amazon").fill("macbook")

    page.get_by_placeholder("Search Amazon").press("Enter")
    page.wait_for_url("https://www.amazon.com/s?k=macbook&crid=N10P98QNN9AJ&sprefix=macbook%2Caps%2C475&ref=nb_sb_noss_1")

    page.get_by_role("link", name="Apple 2022 MacBook Pro Laptop with M2 chip: 13-inch Retina Display, 8GB RAM, 256GB ​​​​​​​SSD ​​​​​​​Storage, Touch Bar, B...").click()
    page.wait_for_url("https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C5HNXJ/ref=sr_1_1?crid=N10P98QNN9AJ&keywords=macbook&qid=1679412519&sprefix=macbook%2Caps%2C475&sr=8-1")

    page.get_by_role("listitem", name="Click to select 16 GB RAM").get_by_role("link").click()
    page.wait_for_url("https://www.amazon.com/dp/B0B8TGK8W6/ref=twister_B0BB52CWDX")
    page.pause()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
