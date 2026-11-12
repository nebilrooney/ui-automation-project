class CartPage:


    def __init__(self, page):
         self.page = page


    def open(self):

         self.page.locator(".shopping_cart_link").click()

    def remove_product(self):
         self.page.get_by_role("button", name="Remove").click()


    def checkout(self):
         self.page.get_by_role("button", name="Checkout").click()          