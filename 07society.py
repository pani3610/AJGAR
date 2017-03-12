class society:
    society_name=''
    house_no=0
    no_of_members=0
    flat=''
    income=0
    def __init__(self):
        self.society_name="Surya Apartments"
        self.house_no=20
        self.no_of_members=3
        self.flat="A Type"
        self.income=25000
    def Inputdata(self,society,house_no,no_of_members,income):
        self.society_name=society
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.income=income
        self.allocate_flat()
    def allocate_flat(self):
        if self.income>=25000:
            self.flat='A Type'
        if self.income>=20000 and self.income<25000:
            self.flat='B Type'
        if self.income>=15000 and self.income<20000:
            self.flat='C Type'
        if self.income<15000:
            self.flat='D Type'
    def Showdata(self):
        print('Society Name : %s\nHouse no. : %s\nNo. of members : %s\nFlat : %s\nIncome : %s'%(self.society_name,self.house_no,self.no_of_members,self.flat,self.income))
surya=society()
surya.Inputdata("Surya Apartments",15,4,17000)
surya.Showdata()
