from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_remove_product(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_first_product_to_cart()

    cart = CartPage(page)
    cart.open()
    cart.remove_product()

    assert page.locator(".cart_item").count() == 0



def test_product_in_cart(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")  
    
    page.get_by_role("button", name="Login").click() 
    page.locator(".inventory_item").first.get_by_role("button", name="Add to cart").click()

    page.locator(".shopping_cart_link").click()
    
    assert page.get_by_text("Sauce Labs Backpack").is_visible()
