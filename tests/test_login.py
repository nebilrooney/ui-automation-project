from pages.login_page import LoginPage

def test_login_with_pom(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert page.url.endswith("inventory.html")


def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com/") 

    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("wrong123") 

    page.get_by_role("button", name="Login").click() 

    print(page.url)

    print(page.locator("[data-test='error']").inner_text())
