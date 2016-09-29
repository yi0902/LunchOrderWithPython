import wx
import resto
import re
import smtplib
import gmail

# Define a windows form for ordering
class OrderForm(wx.Frame):

    def __init__(self, parent, title, all_menus_list):
        super(OrderForm, self).__init__(parent, title=title, size=(550, 600))
        self.menu_list = all_menus_list
        self.InitUI()
        self.Centre()
        self.Show()    

    def InitUI(self):
        # Create a panel & sizer
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(12, 5)
        # Add client info label
        lb_client_info = wx.StaticText(panel, label="Client Information")
        sizer.Add(lb_client_info, pos=(0, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        # Add first name label
        lb_first_name = wx.StaticText(panel, label="First Name")
        sizer.Add(lb_first_name, pos=(1, 0), flag=wx.LEFT, border=5)
        # Add first name text filed
        self.tc_first_name = wx.TextCtrl(panel)
        sizer.Add(self.tc_first_name, pos=(1, 1), span=(1, 1), flag=wx.LEFT|wx.TOP|wx.EXPAND)
        # Add last name label
        lb_last_name = wx.StaticText(panel, label="Last Name")
        sizer.Add(lb_last_name, pos=(1, 3), flag=wx.LEFT, border=5)
        # Add last name text filed
        self.tc_last_name = wx.TextCtrl(panel)
        sizer.Add(self.tc_last_name, pos=(1, 4), span=(1, 1), flag=wx.LEFT|wx.TOP|wx.EXPAND)
        # Add email label
        lb_email = wx.StaticText(panel, label="Email")
        sizer.Add(lb_email, pos=(2, 0), flag=wx.LEFT|wx.TOP, border=5)
        # Add email text filed
        self.tc_email = wx.TextCtrl(panel)
        sizer.Add(self.tc_email, pos=(2, 1), span=(1, 4), flag=wx.TOP|wx.EXPAND, border=5)
        # Add split line
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(3, 0), span=(1, 5), flag=wx.TOP|wx.EXPAND|wx.BOTTOM, border=5)
        # Add order info label
        lb_order_info = wx.StaticText(panel, label="Order Information")
        sizer.Add(lb_order_info, pos=(4, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        # Add menu type label
        lb_menu_type = wx.StaticText(panel, label="Menu Type")
        sizer.Add(lb_menu_type, pos=(5, 0), flag=wx.LEFT|wx.TOP, border=5)
        # Add menu type combo box
        options = ['Salad menu', 'Sandwich menu', 'Hamburger menu', 'Sushi menu']
        combo_menu_type = wx.ComboBox(panel, choices=options, style=wx.CB_READONLY)
        sizer.Add(combo_menu_type, pos=(5, 1), span=(1, 4), flag=wx.TOP|wx.EXPAND, border=5)
        combo_menu_type.Bind(wx.EVT_COMBOBOX, self.OnSelect_MenuType)
        # Add menu name label
        lb_menu_name = wx.StaticText(panel, label="Menu Name")
        sizer.Add(lb_menu_name, pos=(6, 0), flag=wx.LEFT|wx.TOP, border=5)
        # Add menu name combo box
        options_names = []
        self.combo_menu_name = wx.ComboBox(panel, choices=options_names, style=wx.CB_READONLY)
        sizer.Add(self.combo_menu_name, pos=(6, 1), span=(1, 4), flag=wx.TOP|wx.EXPAND, border=5)
        self.combo_menu_name.Bind(wx.EVT_COMBOBOX, self.OnSelect_MenuName)
        # Add menu price label
        lb_menu_price = wx.StaticText(panel, label="Menu Price")
        sizer.Add(lb_menu_price, pos=(7, 0), flag=wx.LEFT|wx.TOP, border=5)
        # Add price
        self.lb_price = wx.StaticText(panel, label='')
        sizer.Add(self.lb_price, pos=(7, 1), flag=wx.LEFT|wx.TOP, border=5)
        # Add provider restaurant information
        sb = wx.StaticBox(panel, label="Provided by restaurant")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.lb_resto_name = wx.StaticText(panel, label="")
        boxsizer.Add(self.lb_resto_name, flag=wx.LEFT|wx.TOP, border=5)
        self.lb_resto_address = wx.StaticText(panel, label="")
        boxsizer.Add(self.lb_resto_address,flag=wx.LEFT, border=5)
        self.lb_resto_telephone = wx.StaticText(panel, label="")
        boxsizer.Add(self.lb_resto_telephone, flag=wx.LEFT|wx.BOTTOM, border=5)
        self.lb_resto_opentime = wx.StaticText(panel, label="")
        boxsizer.Add(self.lb_resto_opentime, flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(8, 0), span=(1, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)
        # Add pickup time label
        lb_pickup_time = wx.StaticText(panel, label="Pick-up Time")
        sizer.Add(lb_pickup_time, pos=(9, 0), flag=wx.LEFT|wx.TOP, border=5)
        # Add pickup time combo box
        options_pickup = ['11h45 - 12h00','12h00 - 12h15','12h15 - 12h30','12h30 - 12h45',
                          '12h45 - 13h00','13h00 - 13h15','13h15 - 13h30','13h30 - 13h45']
        self.combo_pickup_time = wx.ComboBox(panel, choices=options_pickup, style=wx.CB_READONLY)
        sizer.Add(self.combo_pickup_time, pos=(9, 1), span=(1, 4), flag=wx.TOP|wx.EXPAND, border=5)
        # Add confirm button
        button_ok = wx.Button(panel, label="Confirm")
        sizer.Add(button_ok, pos=(11, 3))
        button_ok.Bind(wx.EVT_BUTTON, self.OnClick_ButtonOK)
        # Add cancel button
        button_cancel = wx.Button(panel, label="Cancel")
        sizer.Add(button_cancel, pos=(11, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=5)
        button_cancel.Bind(wx.EVT_BUTTON, self.OnClick_ButtonCancel)
        
        panel.SetSizer(sizer)

    def OnSelect_MenuType(self, e):
        # Get the selected menu type
        selected_menu_type = e.GetString()
        # Get the corresponding menu list
        if selected_menu_type == "Salad menu":
            self.selected_menu_list= self.menu_list[0]
        elif selected_menu_type == "Sandwich menu":
            self.selected_menu_list = self.menu_list[1]
        elif selected_menu_type == "Hamburger menu":
            self.selected_menu_list = self.menu_list[2]
        elif selected_menu_type == "Sushi menu":
            self.selected_menu_list = self.menu_list[3]
        # Pass menus names to menu name combobox choices
        names = []
        self.combo_menu_name.Clear()
        for menu in self.selected_menu_list:
            names.append(menu.name)
        self.combo_menu_name.AppendItems(names)

    def OnSelect_MenuName(self, e):
        # Get the selected menu name
        selected_menu_name = e.GetString()
        # Get the menu object from menu list
        for menu in self.selected_menu_list:
            if menu.name == selected_menu_name:
                self.selected_menu = menu
                break
        # Set the price label
        self.lb_price.SetLabel(self.selected_menu.price + " EUR")
        # Get the resto object
        self.restaurant = self.selected_menu.get_resto_info()
        # Set resto labels
        self.lb_resto_name.SetLabel(self.restaurant.name)
        self.lb_resto_address.SetLabel(self.restaurant.address)
        self.lb_resto_telephone.SetLabel(self.restaurant.telephone)
        self.lb_resto_opentime.SetLabel(self.restaurant.opentime)
        
    def OnClick_ButtonCancel(self, e):
        # Exit the form
        self.Close(True)

    def OnClick_ButtonOK(self, e):
        # Check names
        first_name = self.tc_first_name.GetValue()
        last_name = self.tc_last_name.GetValue()
        if first_name != "" and last_name != "":
            # Check email address validation
            email_addr = self.tc_email.GetValue()
            if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email_addr) != None:
                # Check selected menu name
                if self.combo_menu_name.GetValue() != "":
                    # Check selected pick-up time
                    pickup_time = self.combo_pickup_time.GetValue()
                    if pickup_time != "":
                        # Create confirmation email
                        title = "Confirmation of your order on Defecto lunch booking system"
                        body =("Dear " + first_name + " " + last_name + ",\n\n" 
                               "We are pleased to inform you that your order of menu <" + self.selected_menu.name + "> is confirmed !\n\n" 
                               "======================================\n" 
                               "The detail of your order : \n" 
                               " - Menu name : " + self.selected_menu.name + "\n" 
                               " - Menu price : " + self.selected_menu.price + " EUR\n" 
                               " - Provided by : \n" 
                               "     " + self.restaurant.name + "\n" 
                               "     " + self.restaurant.address + "\n" 
                               "     " + self.restaurant.telephone + "\n" 
                               "     " + self.restaurant.opentime + "\n" 
                               " - Your pick-up time : " + pickup_time + "\n"
                               "======================================\n"
                               "Thank you again for ordering on our lunch booking system ! We wish you an excellent lunch time !")
                        gmail_server = gmail.GmailServer(email_addr, title, body)
                        # Send email to client
                        if gmail_server.send_email() == True:
                            # Prompt email sent message
                            wx.MessageBox("Thank you for ordering!\nThe confirmation email has been sent to your email address!", "Confirmed", wx.OK | wx.ICON_INFORMATION)
                            # Exit the form
                            self.Close(True)
                        else:
                            wx.MessageBox("Sorry, there is an error in sending confirmation email to your email address!", "ERROR", wx.OK | wx.ICON_INFORMATION)
                    else:
                        wx.MessageBox("Sorry, you haven't selected a pick-up time", "ERROR", wx.OK | wx.ICON_INFORMATION)
                else:
                    wx.MessageBox("Sorry, you haven't selected a menu", "ERROR", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox("Sorry, the email address you entered is not valid, please check", "ERROR", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Sorry, you haven't entered your name information, please check", "ERROR", wx.OK | wx.ICON_INFORMATION)
        

        

        
