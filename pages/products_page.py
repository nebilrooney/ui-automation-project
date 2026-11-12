class ProductsPage:

    def __init__(self,page):
        self.page = page


    def add_first_product_to_cart(self):

       self.page.locator(".inventory_item").first.get_by_role("button", name="Add to cart").click()     