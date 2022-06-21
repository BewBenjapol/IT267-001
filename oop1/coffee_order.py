class coffee_order:
    def  __init__(self,menu_type:str) -> None:
        self.menu_type = menu_type

    def total(self):
        print(f"Hi, {self.menu_type}")

    def customer_name(self):
        print(f"Benjapol, {self.menu_type}")

    def menu(self):
        print(f"Cafe Mocha, {self.menu_type}")

    def num(self):
        print(f"")

    