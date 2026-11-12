from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from playwright.sync_api import expect


def test_add_product_to_cart(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_first_product_to_cart()

    assert page.locator(".shopping_cart_link").inner_text() == "1"


def test_products_page(page):
    page.goto("https://www.saucedemo.com/") 


    page.get_by_placeholder("Username").fill("standard_user") 
    page.get_by_placeholder("Password").fill("secret_sauce") 

    page.get_by_role("button", name="Login").click() 

    expect(page.get_by_text("Products")).to_be_visible() 


def test_products_count(page):
    page.goto("https://www.saucedemo.com/") 

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click() 

    products = page.locator(".inventory_item") 

    expect(products).to_have_count(6) 


def test_product_name(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click() 

    product = page.get_by_text("Sauce Labs Backpack") 

    expect(product).to_be_visible() 



