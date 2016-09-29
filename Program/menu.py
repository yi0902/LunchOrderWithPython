import resto
import csv
import tool

# Define parent class Menu
class Menu():

    def __init__(self, menu_provider, menu_name, menu_ingredient_list,
                 net_weight, associated_dessert, associated_drink,
                 menu_price, menu_photo_url):
        self.provider = menu_provider
        self.name = menu_name
        self.ingredient_list = menu_ingredient_list
        self.weight = net_weight
        self.dessert = associated_dessert
        self.drink = associated_drink
        self.price = menu_price
        self.photo_url = menu_photo_url

    # Function to return a restaurant object
    def get_resto_info(self):
        # Set resto found flag
        resto_found = False
        # Parse resto csv file
        with open("data/resto_data.csv", 'rb') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Skip the header line
            next(csv_reader)
            # Loop on each line
            for row in csv_reader:
                if row[0] == self.provider:
                    # Set resto found flag to TRUE
                    resto_found = True
                    # Instantiate and return the resto object
                    return resto.Resto(row[0], row[1], row[2], row[3], row[4])
        if resto_found == False:
            tool.show_message("ERROR", "Can't find " + self.provider + " in resto_data.csv, please check data file!", 1)
            sys.exit()

# Define child class SaladMenu inherited from Menu
class SaladMenu(Menu):

    def __init__(self, menu_provider, menu_name, menu_ingredient_list,
                 net_weight, associated_dessert, associated_drink,
                 menu_price, menu_photo_url, salad_sauce):
        Menu.__init__(self, menu_provider, menu_name, menu_ingredient_list,
                      net_weight, associated_dessert, associated_drink,
                      menu_price, menu_photo_url)
        self.sauce = salad_sauce
		
# Define child class SandwichMenu inherited from Menu
class SandwichMenu(Menu):

    def __init__(self, menu_provider, menu_name, menu_ingredient_list,
                 net_weight, associated_dessert, associated_drink,
                 menu_price, menu_photo_url, type_of_sandwich):
        Menu.__init__(self, menu_provider, menu_name, menu_ingredient_list,
                      net_weight, associated_dessert, associated_drink,
                      menu_price, menu_photo_url)
        self.sandwich_type = type_of_sandwich

# Define child class HamburgerMenu inherited from Menu
class HamburgerMenu(Menu):

    def __init__(self, menu_provider, menu_name, menu_ingredient_list,
                 net_weight, associated_dessert, associated_drink,
                 menu_price, menu_photo_url, type_of_bread, hamburger_sauce):
        Menu.__init__(self, menu_provider, menu_name, menu_ingredient_list,
                      net_weight, associated_dessert, associated_drink,
                      menu_price, menu_photo_url)
        self.bread_type = type_of_bread
	self.sauce = hamburger_sauce

# Define child class SushiMenu inherited from Menu
class SushiMenu(Menu):

    def __init__(self, menu_provider, menu_name, menu_ingredient_list,
                 net_weight, associated_dessert, associated_drink,
                 menu_price, menu_photo_url, nb_of_pieces):
        Menu.__init__(self, menu_provider, menu_name, menu_ingredient_list,
                      net_weight, associated_dessert, associated_drink,
                      menu_price, menu_photo_url)
        self.pieces_nb = nb_of_pieces
        

    

    
        
        
