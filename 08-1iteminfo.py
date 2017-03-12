class ITEMINFO:
    ICode=0
    Item=''
    Price=0
    Qty=0
    Netprice=0
    Discount=0
    def __init__(self):
        self.ICode=0
        self.Item=''
        self.Price=0
        self.Qty=0
        self.Netprice=0
        self.Discount=0
    def Buy(self,ICode,Item,Price,Qty):
        self.ICode=ICode
        self.Item=Item
        self.Price=Price
        self.Qty=Qty
        self.Netprice=0
        self.FindDisc()
    def FindDisc(self):
        if self.Qty>=20:
            self.Discount=20
        if self.Qty>=11 and self.Qty<20:
            self.Discount=15
        if self.Qty<11:
            self.Discount=0
        self.Net()
    def Net(self):
        total=self.Price*self.Qty
        self.Netprice=total-(total*self.Discount/100)
    def ShowAll(self):
        print('''\
Item Code : %s
Item Name : %s
Price of each item : %s
Quantity in stock : %s
Discount percentage on the item : %s
Final Price : %s\
'''%(self.ICode,self.Item,self.Price,self.Qty,self.Discount,self.Netprice))
mall=ITEMINFO()
mall.Buy(1,'dsf',324,14)
mall.ShowAll()
