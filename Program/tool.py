import ctypes
import os.path
import csv
import menu

# Function to prompt up a message box
def show_message(title, text, style):
    return ctypes.windll.user32.MessageBoxA(0, text, title, style)

# Function to check if the menu csv file exists and contains good data
def check_menu_data(menu_type):
    file_path = "data/menu_" + menu_type + "_data.csv"
    # Check if file exists
    if os.path.exists(file_path):
        # Open the file to check its fileds
        with open(file_path, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Skip the header line
            next(csv_reader)
            # Set the data ok flag
            is_data_ok = True
            # Loop on each line
            for row in csv_reader:
                # Check each filed
                # -- check for number filed (price)
                try:
                    float(row[6])
                except ValueError:
                    show_message("ERROR",
                                 "File %s, line %d : The price in this line is not digital, please check the data file" % (file_path, csv_reader.line_num),
                                 0)
                    is_data_ok = False
                # -- check for non empty filed
                for filed in row:
                    if filed == '':
                        show_message("ERROR",
                                     "File %s, line %d : There is an empty filed, please check the data file" % (file_path, csv_reader.line_num),
                                     0)
                        is_data_ok = False
                        break
                if is_data_ok == False:
                    return False
            return True
    else:
        show_message("ERROR",
                     "File %s doesn't exsit, please check the data file" % (file_path),
                     0)
        return False

# Function to read the content of menu csv file and instantiate menu objects
def read_menu_data(menu_type, menu_list):
    file_path = "data/menu_" + menu_type + "_data.csv"
    with open(file_path, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Skip the header line
        next(csv_reader)
        # Loop on each line
        for row in csv_reader:
            # Initialize the menu object with the row info
            if menu_type == "salad":
                current_menu = menu.SaladMenu(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            elif menu_type == "sandwich":
                current_menu = menu.SandwichMenu(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            elif menu_type == "hamburger":
                current_menu = menu.HamburgerMenu(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            elif menu_type == "sushi":
                current_menu = menu.SushiMenu(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            else:
                show_message("ERROR","The menu type " + menu_type + " is not pre-defined", 0)
                return False
            # Add the object to the list
            menu_list.append(current_menu)
    return True

# Function to check if the resto csv file exists and contains good data
def check_resto_data():
    file_path = "data/resto_data.csv"
    # Check if file exists
    if os.path.exists(file_path):
        # Open the file to check its fileds
        with open(file_path, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Skip the header line
            next(csv_reader)
            # Loop on each line
            for row in csv_reader:
                # Check for non empty filed
                for filed in row:
                    if filed == '':
                        show_message("ERROR",
                                     "File %s, line %d : There is an empty filed, please check the data file" % (file_path, csv_reader.line_num),
                                     0)
                        return False
            return True
    else:
        show_message("ERROR",
                     "File %s doesn't exsit, please check the data file" % (file_path),
                     0)
        return False

