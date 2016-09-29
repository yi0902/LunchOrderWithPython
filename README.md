# LunchOrderWithPython
This is an express-lunch booking tool written in Python

Working at La Défense (Europe's largest purpose-built business district), a good relaxed lunch break becomes something luxurious. More and more people intend to make a quick stop at some express restaurants to grab something, return back to their desks and eat there, so am I. 

However, I always find it difficult to buy the express food in this business district during the lunch peak time. There are always very long queues before each sandwich store, salad bar or other types of express restaurants. We have to wait for around 15-30 min to get served for buying a simple sandwich. The worse is that when it’s finally our turn, food that we want is running out of stock…

So to improve this situation, I propose to create an express-lunch booking system just dedicated for La Défense. All restaurants in this district that offer takeout can register in the system. People
-	Browse the web page
-	Select the lunch menu they want
-	Fix the pick-up time
-	Pay on Internet by a credit card or on site by using the restaurant tickets (a quick French payment dedicated for lunch)
-	Finally go to the express restaurant to take their food at the time they defined. 

Of course, the restaurant should open a pick-up window for these people who have booked online. In this way, we can save much of our time and we will rarely have the bad surprise of out of stock.

It sounds like an ambitious project? Yes, so in my project, I will make things simple. 

I will just try to simulate the client side (web pages + order form) by using python, without going further to the database and server side. As there is no server, web pages can’t call directly python functions, I decide to realize the booking functionalities by a window form. Also, I will skip the payment part as it’s sensitive and not plays much in the project prototype. So finally, the functionalities that I will implement on my system are:  
-	Visualization of different lunch menus on web site
-	Prompt to ask client whether they have decided to pass order
-	Client order procedure via a windows form
-	Order confirmation by email

To run this program, you need:

- have wxPython (http://www.wxpython.org/download.php#msw) properly installed
- go to Program folder and execute main.py.

Now you can have a try!

