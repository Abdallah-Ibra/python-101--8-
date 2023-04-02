from playwright.sync_api import Playwright, sync_playwright, expect
from colorama import Fore

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10000)
    username = "standard_user"
    password= "secret_sauce"
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(300)
    page.wait_for_load_state('domcontentloaded')
    page.locator("[data-test=\"username\"]").click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("[data-test=\"username\"]").fill(username)
    page.wait_for_load_state('domcontentloaded')
    page.locator("[data-test=\"password\"]").click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("[data-test=\"password\"]").fill(password)
    page.wait_for_load_state('domcontentloaded')
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_timeout(500)
    page.wait_for_load_state('domcontentloaded')
    # if 'data-test="error"' in page.inner_html('*'):
    #     print(Fore.RED+f'[-] Invalid Credits: {username}|{password}!'+Fore.RESET)
    # else:
    # #     print(Fore.LIGHTGREEN_EX+f'[+] Login Successfully: {username}|{password}!'+Fore.RESET)
    # if page.url == 'https://www.saucedemo.com/inventory.html':
    #     print(Fore.LIGHTGREEN_EX+f'[+] Login Successfully: {username}|{password}!'+Fore.RESET)
    #     page.wait_for_timeout(300)
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("a:has-text(\"Sauce Labs Backpack\")").click()
    #     page.wait_for_url("https://www.saucedemo.com/inventory-item.html?id=4")
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("a:has-text(\"1\")").click()
    #     page.wait_for_url("https://www.saucedemo.com/cart.html")
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"checkout\"]").click()
    #     page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"firstName\"]").click()
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"firstName\"]").fill("Alex")
    #     page.locator("[data-test=\"lastName\"]").click()
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"lastName\"]").fill("Matt")
    #     page.locator("[data-test=\"postalCode\"]").click()
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"postalCode\"]").fill("00972")
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"continue\"]").click()
    #     page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    #     page.wait_for_load_state('domcontentloaded')
    #     page.locator("[data-test=\"finish\"]").click()
    #     if '/checkout-complete.html' in page.url:
    #         print(Fore.CYAN+'[#] Your Order Completed!'+Fore.RESET)
    # else:
    #     print(Fore.RED+f'[-] Invalid Credits: {username}|{password}!'+Fore.RESET)
    img = page.locator('img[alt="Sauce Labs Backpack"]').screenshot(type='png')
    with open('SauceLabsBackPack/img1.png','wb') as f:
        f.write(img)
    body = page.locator('#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.inventory_item_label > div').text_content()
    price = page.locator('#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div').text_content()
    print('[#] Title: Sauce Labs Backpack')
    print('='*30)
    print(f'[#] Body:\n{body}')
    print('='*30)
    print(f'[#] Price: {price}')
    
    # page.get_by_role("heading", name="Thank you for your order!").click()
    page.pause()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as p:
    run(p)

