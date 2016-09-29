import csv
import menu
import menu_type
import refresh_index
import refresh_menu
import tool
import sys
import os.path
import time
import wx
import order_form

########### Check of input data ######################

tool.show_message("Check INPUT",
                  "Hello, for running this program, we need several csv files placed under /data/ folder which contain restaurants & lunch menus data :" +
                  "\n - menu_hamburger_data.csv" +
                  "\n - menu_salad_data.csv" +
                  "\n - menu_sandwich_data.csv" +
                  "\n - menu_sushi_data.csv" +
                  "\n - resto_data.csv"
                  "\nDo you want to continue?",
                  1)
    
print "Checking input csv files..."

if tool.check_menu_data("salad") == True:
    print "menu_salad_data.csv OK!"
else:
    sys.exit()

if tool.check_menu_data("sandwich") == True:
    print "menu_sandwich_data.csv OK!"
else:
    sys.exit()

if tool.check_menu_data("hamburger") == True:
    print "menu_hamburger_data.csv OK!"
else:
    sys.exit()

if tool.check_menu_data("sushi") == True:
    print "menu_sushi_data.csv OK!"
else:
    sys.exit()

if tool.check_resto_data() == True:
    print "resto_data.csv OK!"
else:
    sys.exit()

########### Create index page ########################

salad_menu = menu_type.MenuType("Salad menu",
                                "Bring you the cool of summer",
                                "img/salad.jpg")

sandwich_menu = menu_type.MenuType("Sandwich menu",
                                   "Wonderful balance of bread &amp; vegetables",
                                   "img/sandwich.jpg")

sushi_menu = menu_type.MenuType("Sushi menu",
                                "Want the oriental delicay ?",
                                "img/sushi.jpg")

hamburger_menu = menu_type.MenuType("Hamburger menu",
                                    "Let's be American !",
                                    "img/hamburger.jpg")

menu_types_list = [salad_menu, sandwich_menu, sushi_menu, hamburger_menu]
refresh_index.open_index_page(menu_types_list)

print "Create index page OK!"

############ Create menu pages ##########################
salad_menus_list = []
sandwich_menus_list = []
hamburger_menus_list = []
sushi_menus_list = []

# Read menu info from data csv files & create the menu pages
# -- salad menus page
if tool.read_menu_data("salad", salad_menus_list) == True:
    refresh_menu.open_menu_page("salad", salad_menus_list)
    print "Create salad menus page OK!"
# -- sandwich menus page
if tool.read_menu_data("sandwich", sandwich_menus_list) == True:
    refresh_menu.open_menu_page("sandwich", sandwich_menus_list)
    print "Create sandwich menus page OK!"
# -- hamburger menus page
if tool.read_menu_data("hamburger", hamburger_menus_list) == True:
    refresh_menu.open_menu_page("hamburger", hamburger_menus_list)
    print "Create hamburger menus page OK!"
# -- sushi menus page
if tool.read_menu_data("sushi", sushi_menus_list) == True:
    refresh_menu.open_menu_page("sushi", sushi_menus_list)
    print "Create sushi menus page OK!"

print "All generated HTML pages are stored under /html/ folder."

########### Start a timer ################################

# Sleep for 30 seconds
time.sleep(30)
# Prompt to ask if the user has decided which menu to order
go_order = tool.show_message("Ordering", "Already decided? \nGo to order form now!", 4)

while True:
    if go_order == 6:
        # Exit the while loop
        break
    else:
        # Sleep for 30 seconds
        time.sleep(30)
        # Re ask the question
        go_order = tool.show_message("Ordering", "Already decided? \nGo to order form now!", 4)


########## Create order form ##########################

menus_list=[salad_menus_list, sandwich_menus_list, hamburger_menus_list, sushi_menus_list]

# Create the wx application
app = wx.App()
# Instantiate the order form with all menus info
order_form.OrderForm(None, title="Order Form", all_menus_list=menus_list)
# Enter into mainloop to listen to events
app.MainLoop()


        





                
                    

        
        
    















