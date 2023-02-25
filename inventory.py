
class Shoe:

    country = ""
    code = ""
    product = ""
    cost = 0
    quantity = 0
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
       return self.cost

    def get_quantity(self):     
        return self.quantity

    def set_quantity(self, qty):     
        self.quantity = qty
        
    def __str__(self):
        print(f"Item country: {self.country}")
        print(f"Item code: {self.code}")
        print(f"Item product: {self.product}")
        print(f"Item cost: {self.cost}")
        print(f"Item quantity: {self.quantity}")

shoe_list = []

def read_shoes_data():
    try :
        with open("C:\\Education\\inventory.txt", "r+") as item_file:
            items_file = item_file.readlines()
            index = 0
            for line in items_file:
                if index > 0 :
                    country,code,product,cost,qt  = line.strip('\n').split (',')
                    shoes=Shoe(country,code,product,int(cost),int(qt))
                    #print(shoes.__str__())
                    shoe_list.append(shoes)
                index += 1
    except:
        print("something wrong")
   


def capture_shoes():
    pr_pos=-1
    item_code = input ("Please enter code")
    for index, p in enumerate (shoe_list):
        if p.code == item_code :
            pr_pos=index
    if pr_pos == -1:
        print(f'{item_code} was not found')
    else:
        quintity=int(input(f"Enter new Quantity for product {item_code}: "))
        shoe_list[pr_pos].set_quantity(quintity)
        update_file()

def update_file() :
    try :
        with open("C:\\Education\\inventory.txt",'w') as file:
            pass
        with open("C:\\Education\\inventory.txt", "w+") as item_file:
            item_file.write("Country,Code,Product,Cost,Quantity\n")
            for insdex, p in enumerate (shoe_list):
                 item_file.write(f"{p.country},{p.code},{p.product},{p.cost},{p.quantity}\n")
    except:
        print("something wrong")


def view_all():
    data_list = []
    top_row = "country\tcode\tproduct\tcost\tquantity"
    print(top_row)
    for p in shoe_list:
        print(f"{p.country}\t{p.code}\t{p.product}\t{p.cost}\t{p.quantity}")


def re_stock() :
    pr_pos=0
    try :
        minmium_qty = shoe_list[0].get_quantity()
        for index, p in enumerate (shoe_list):
            if p.get_quantity() < minmium_qty :
                pr_pos=index
                minmium_qty = p.get_quantity() 
        quintity=int(input(f"Enter new Quantity for product {shoe_list[pr_pos].code}: "))
        shoe_list[pr_pos].set_quantity(quintity)
        update_file()
    except :
        print("something wrong")


def seach_shoe():
    pr_pos=-1
    item_code = input ("Please enter code")
    for index, p in enumerate (shoe_list):
        if p.code == item_code :
            pr_pos=index
    if pr_pos == -1:
        print(f'{item_code} was not found')
    else:
        return shoe_list[pr_pos]

def value_per_item():
    for index, p in enumerate (shoe_list):
        value = int(p.get_cost()*p.get_quantity())
        print(f'{p.code} values is {value}')


def highest_qty():
    pr_pos=0
    try :
        miaximum_qty = shoe_list[0].get_quantity()
        for index, p in enumerate (shoe_list):
            if p.get_quantity() > miaximum_qty :
                pr_pos=index
                miaximum_qty = p.get_quantity() 
        return shoe_list[pr_pos]
    except :
        print("something wrong")

#==========Main Menu=============

read_shoes_data()
while True :      
    try:   
        sentence="Select one of the following Options below: \n vl - values\n h - highest qty\n s - search \n r - re-stock \n v - view all \n c - capture shoes \n e - Exit"
        print(sentence)
        menu=input("Enter your choice: ").lower()
        if menu == 'v': 
            view_all()      
        elif menu == 'c':
            capture_shoes()
        elif menu == 'e':    
            print('Goodbye!!!')
            exit()
        elif menu == 'r':
            re_stock()
        elif menu == 'vl':
            value_per_item()
        elif menu == 's':
            item = seach_shoe()
            print(item.__str__())
        elif menu == 'h':
            item = highest_qty()
            print(item.__str__())
        else:
            print('Incorrect option')
    except :
        exit()

