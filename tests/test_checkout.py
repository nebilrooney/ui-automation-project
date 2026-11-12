from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect


def test_checkout_success(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_first_product_to_cart()

    cart = CartPage(page)
    cart.open()
    cart.checkout()

    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Smith")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")

    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
