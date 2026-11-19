class User:
    def __init__(self,id,username,password,role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def user_details(self):
        return f'{self.id},{self.username},{self.password},{self.role}\n'

class Authentication:
    def register(self):
        id = int(input('Enter your ID: '))
        username = input('Enter your Username: ')
        password = input('Enter your Password: ')
        role = input('Enter your Role: ')
        user = User(id,username,password,role)

        with open('users.txt','r') as f:
            data = f.readlines()

        for line in data:
            details = line.strip().split(',')
            db_username = details[1]
            if db_username == username:
                print('User Already Exist!')
                return

        with open('users.txt','a') as f:
            data = user.user_details()
            f.write(data)
            print('Registration Successful!')

    def login(self):
        username = input('Enter Your Username: ')
        password = input('Enter Your Password: ')

        with open('users.txt','r') as f:
            data = f.readlines()

        is_found = False
        for line in data:
            details = line.strip().split(',')
            if username == details[1]:
                is_found = True
                if password == details[2]:
                    print('Login Success!')
                    return int(details[0]),details[-1] # (101,admin)
                else:
                    print('Invalid Credentials!')
                    return None
        if not is_found:
            print('User Not Found, First Create Your Account!')
            return None

class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def prod_details(self):
        return f'{self.id},{self.name},{self.price},{self.quantity}\n'

class Admin:
    def add_product(self):
        id = int(input('Enter Product ID: '))
        name = input('Enter Product Name: ')
        price = int(input('Enter Product Price: '))
        quantity = int(input('Enter Product Quantity: '))
        product = Product(id,name,price,quantity)

        with open('products.txt','r') as f:
            data = f.readlines()

        is_found = False
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                prod_name = details[1]
                if prod_name == name:
                    is_found = True
                    new_quantity = int(details[3])+quantity
                    f.write(f'{details[0]},{details[1]},{details[2]},{new_quantity}\n')
                else:
                    f.write(line)
        if not is_found:
            with open('products.txt','a') as f:
                prod_details = product.prod_details()
                f.write(prod_details)
                print('Product Added Successfully!')

    def delete_product(self):
        id = int(input('Enter Product ID: '))

        with open('products.txt','r') as f:
            data = f.readlines()

        is_found = False
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                if id == int(details[0]):
                    is_found = True
                else:
                    f.write(line)
        if is_found:
            print('Product Deleted Successfully!')
        else:
            print('Product Not Found!')

    def update_product(self):
        id = int(input('Enter Product ID: '))

        with open('products.txt','r') as f:
            data = f.readlines()

        is_found = False
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                if id == int(details[0]):
                    is_found = True
                    print('1) To Update Name')
                    print('2) To Update Price')
                    print('3) To Update Quantity')
                    print('4) To Update All')

                    choice = int(input('Enter Your Choice: '))
                    match choice:
                        case 1:
                            new_name = input('Enter New Name: ')
                            f.write(f'{details[0]},{new_name},{details[2]},{details[3]}\n')
                            print('New Name Updated Successfully!')
                        case 2:
                            new_price = input('Enter New Price: ')
                            f.write(f'{details[0]},{details[1]},{new_price},{details[3]}\n')
                            print('New Price Updated Successfully!')
                        case 3:
                            new_quantity = input('Enter New Quantity: ')
                            f.write(f'{details[0]},{details[1]},{details[2]},{new_quantity}\n')
                            print('New Quantity Updated Successfully!')
                        case 4:
                            new_name = input('Enter New Name: ')
                            new_price = input('Enter New Price: ')
                            new_quantity = input('Enter New Quantity: ')
                            f.write(f'{details[0]},{new_name},{new_price},{new_quantity}\n')
                            print('All Details Updated Successfully!')
                        case _:
                            f.write(line)
                            print('Invalid Choice!') 
                else:
                    f.write(line)
        if not is_found:
            print('Product Not Found!')

    def search_product(self):
        with open('products.txt','r') as f:
            data = f.readlines()
            if len(data) == 0:
                print('No Product Available!')
                return
            
        id = int(input('Enter Product ID: '))

        with open('products.txt','r') as f:
            data = f.readlines()

        for line in data:
            details = line.strip().split(',')
            if id == int(details[0]):
                print('-------------------------------------')
                print('|ID   |NAME      |PRICE  |QUANTITY  |')
                print('-------------------------------------')
                print(f'|{details[0]+' '*(5-len(details[0]))}|{details[1]+' '*(20-len(details[1]))}|{details[2]+' '*(20-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
                print('-------------------------------------')
                return
        print('Product Not Found!')

    def view_all_products(self):
        with open('products.txt','r') as f:
            data = f.readlines()
            if len(data) == 0:
                print('No Product Available!')
                return

        with open('products.txt','r') as f:
            data = f.readlines()

        print('-------------------------------------')
        print('|ID   |NAME      |PRICE  |QUANTITY  |')
        print('-------------------------------------')               
        for line in data:
            details = line.strip().split(',')
            print(f'|{details[0]+' '*(5-len(details[0]))}|{details[1]+' '*(20-len(details[1]))}|{details[2]+' '*(20-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
        print('-------------------------------------')

class Cart(Admin):
    def __init__(self,user_id):
        self.user_id = user_id

    def add_product_to_the_cart(self):
        prod_name = input('Enter Product Name: ')

        with open('products.txt','r') as f:
            data = f.readlines()

        is_found = False
        new_product = []
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                if prod_name == details[1] and int(details[-1]) > 0:
                    is_found = True
                    new_product = details
                    new_quantity = int(details[-1])-1
                    f.write(f'{details[0]},{details[1]},{details[2]},{new_quantity}\n')
                else:
                    f.write(line)

        if is_found:
            with open('cart.txt','r') as f:
                data = f.readlines()

            is_found = False
            with open('cart.txt','w') as f:
                for line in data:
                    details = line.strip().split(',')
                    if prod_name == details[2] and int(details[0]) == self.user_id:
                        is_found = True
                        new_quantity = int(details[-1])+1
                        f.write(f'{details[0]},{details[1]},{details[2]},{details[3]},{new_quantity}\n')
                    else:
                        f.write(line)
            if not is_found:            
                new_product.insert(0,str(self.user_id))
                new_product[-1] = '1'
                new_product = ','.join(new_product)+'\n'

                with open('cart.txt','a') as f:
                    f.write(new_product)
        else:
            print('Product Not Found!')

    def decrease_quantity(self):
        prod_name = input('Enter Product Name: ')

        with open('cart.txt','r') as f:
            data = f.readlines()

        is_found = False
        with open('cart.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                if prod_name == details[2] and int(details[0]) == self.user_id:
                    if int(details[-1]) > 0:
                        is_found = True
                        new_quantity = int(details[-1])-1
                        f.write(f'{details[0]},{details[1]},{details[2]},{details[3]},{new_quantity}\n')
                else:
                    f.write(line)
        if is_found:
            with open('products.txt','r') as f:
                data = f.readlines()

            with open('products.txt','w') as f:
                for line in data:
                    details = line.strip().split(',')
                    if prod_name == details[1]:
                        new_quantity = int(details[-1])+1
                        f.write(f'{details[0]},{details[1]},{details[2]},{new_quantity}\n')
                    else:
                        f.write(line)

    def view_cart(self):
        with open('cart.txt','r') as f:
            data = f.readlines()

        is_found = False
        for line in data:
            details = line.strip().split(',')
            if int(details[0]) == self.user_id:
                is_found = True
                break

        if is_found:
            total_amount = 0
            print('----------------------------------')
            print('|NAME      |PRICE     |QUANTITY  |')
            print('----------------------------------')
            for line in data:
                details = line.strip().split(',')
                if int(details[0]) == self.user_id:
                    print(f'|{details[2]+' '*(20-len(details[2]))}|{details[3]+' '*(20-len(details[3]))}|{details[4]+' '*(10-len(details[4]))}|')
                    total_amount += int(details[3]) * int(details[-1])
            print('----------------------------------')
            print(f'            Total Amount = {total_amount}/-')
        else:
            print('Cart is Empty!')

def admin_login():
    while True:
        print('\n1) To Add Product')
        print('2) To Delete Product')
        print('3) To Update Product')
        print('4) To Search Product')
        print('5) To View All Products')
        print('6) To Logout!')

        choice = int(input('Enter Your Choice: '))
        admin = Admin()
        match choice:
            case 1: admin.add_product()
            case 2: admin.delete_product()
            case 3: admin.update_product()
            case 4: admin.search_product()
            case 5: admin.view_all_products()
            case 6:
                print('Logged-out Successfully!')
                break
            case _: print('Invalid Choice!')


def user_login(user_id):
    while True:
        print('\n1) To Add Product To the Cart')
        print('2) To Decrease Quantity')
        print('3) To View All Products')
        print('4) TO Search Product')
        print('5) To View Cart')
        print('6) To Logout')

        choice = int(input('Enter Your Choice: '))
        cart = Cart(user_id)
        match choice:
            case 1: cart.add_product_to_the_cart()
            case 2: cart.decrease_quantity()
            case 3: cart.view_all_products()
            case 4: cart.search_product()
            case 5: cart.view_cart()
            case 6: 
                print('Logged-out Successfully!')
                break
            case _: print('Invalid Choice!')

print('<------- WELCOME TO ECOMMERCE WEBSITE ------->')

while True:
    print('\n1) To Register')
    print('2) To Login')
    print('3) To Exit')

    choice = int(input('Enter Your Choice: '))
    auth = Authentication()
    match choice:
        case 1:
            auth.register()
        case 2:
            user_details = auth.login()
            if user_details != None:
                if user_details[-1] == 'admin':
                    admin_login()
                else:
                    user_login(user_details[0])
        case 3: 
            print('Thank You, Visit Again!')
            break
        case _: print('Invalid Choice!')