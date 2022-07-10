class juiceorder:
    def  __init__(self,menu,size,price) -> None:
        self.menu = menu
        self.size = size
        self.price = price

    def show(self,OJ,AJ,WJ,PJ):
        self.OJ = 25
        self.AJ = 25 
        self.WJ = 30
        self.PJ = 30
    
    def check(self,check_menu,compute_price,display_order):
        self.check_menu = check_menu
        self.compute_price = compute_price
        self.display_order = display_order

    def show_detail(self):
        print(f'==== OJ*25 ====')
        print(f'==== AJ*25 ====')
        print(f'==== WJ*25 ====')
        print(f'==== PJ*25 ====')
        print(f'juiceorder: {self.name}\n {self.compute_price:,}\ngdp: {self.gdp:,}')
        

    




    

        
    


