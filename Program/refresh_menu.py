import os
import re

# Styles and scripting for the page
menu_page_head = '''
<!DOCTYPE html>
<html lang="en">
	<head>
        <meta charset="utf-8" />
        <title>Order menu online at LA DEFENSE</title>
		<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
		<link rel="stylesheet" type="text/css" href="css/style.css" />
		<link rel="stylesheet" type="text/css" href="css/base.css" />
		<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
		<script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
		<style type="text/css" media="screen">
			#detail .modal-dialog {
				margin-top: 200px;
				width: 400px;
				height: 500px;
			}
			.hanging-close {
				position: absolute;
				top: -12px;
				right: -12px;
				z-index: 9001;
			}
			.media:hover {
				background-color: #EEE;
				cursor: pointer;
			}
			.scale-menu {
				padding-bottom: 56.25%;
				position: relative;
			}
			.scale-menu iframe {
				border: none;
				height: 100%;
				position: absolute;
				width: 100%;
				left: 0;
				top: 0;
				background-image:url(https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS52YJKipQoQO0kemTJk0i8nqjVqqwO7OMJHajTvW_si-8IFcFi_A);
			}
		</style>
		<script type="text/javascript" charset="utf-8">
			// Clear the detail when the modal is closed
			$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
				$("#menu-detail-container").empty();
			});
			// Show the detail of the menu
			$(document).on('click', '.media', function (event) {
				var menu_ingredients = $(this).attr('menu-ingredients-id')
				var menu_weight = $(this).attr('menu-weight-id')
				var menu_dessert = $(this).attr('menu-dessert-id')
				var menu_drink = $(this).attr('menu-drink-id')
				var menu_other = $(this).attr('menu-other-id')
				var absolute_path = $(this).attr('menu-detail-path')
				var src_url = absolute_path+"?ingredients="+menu_ingredients+"&weight="+menu_weight+"&dessert="+menu_dessert+"&drink="+menu_drink+"&other="+menu_other
				$("#menu-detail-container").empty().append($("<iframe></iframe>", {
				  'id': 'menu-detail',
				  'src': src_url,
				  'type': 'text-html',
				  'frameborder': 0,
				  'scrolling': 'auto'
				}));
			});
		</script>
    </head>
'''


# The menu page layout and logo bar
menu_page_content = '''
  <body>
    <!-- Header part -->
    <div class="responsive-header">
		<div class="responsive-header-inner">
			<div class="responsive-header-logo">
				<a href="/">
					<img src="http://www.ladefense.fr/sites/all/themes/defacto/images/defacto_baseline.png" width="500" height="70" title="Defecto order lunch menu online">
				</a>
			</div>
		</div>
	</div>
    <!-- Main Content -->
	<div id="main" role="main">
		<div class="modal" id="detail">
			<div class="modal-dialog">
				<div class="modal-content">
					<a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
						<img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
					</a>
					<div class="scale-menu" id="menu-detail-container">
					</div>
				</div>
			</div>
		</div>
		<div class="l-grid">
			{menu_tiles}
		</div>
	</div>
	<div align="right">
		<a href="{index_path}" >
			<img src="http://www.charliepinder.com/images/back-01.png" width="80" height="80">
		</a>
	</div>
  </body>
</html>
'''

# A single menu html template
menu_content = '''
<div class="l-col l-size1of4 promo1">
	<div class="promoBG1">
		<div style="background-color:black;border:thick black solid" class="media" data-toggle="modal" data-target="#detail" menu-ingredients-id="{menu_ingredient}" menu-weight-id="{menu_weight}" menu-dessert-id="{menu_dessert}" menu-drink-id="{menu_drink}" menu-other-id="{menu_other}" menu-detail-path="{menu_path}" >
			<img src="{menu_image_url}" width="300" height="150">
		</div>
		<div class="bd" >
			<table>
				<tr>
					<td><h4 style="color:#C6051B"><b>{menu_title}</b></h4></td>
				</tr>
				<tr>
					<td><h5 style="color:#E8AB11;font-size:1.3em">Price : <b>{menu_price} &#128;</b></h5></td>
				</tr>
				<tr>
					<td>provided by <b>{menu_provider}</b></td>
				</tr>
			</table>
		</div>
	</div>
</div>
'''

# A single menu detail html template
menu_detail_content = '''
<html>
	<head>
		<script type="text/javascript" charset="utf-8">
			function render(){
				var queryDict = {}
				location.search.substr(1).split("&").forEach(function(item) {queryDict[item.split("=")[0]] = item.split("=")[1]})
				document.getElementById('ingredients').innerHTML =  decodeURI(queryDict["ingredients"]);
				document.getElementById('weight').innerHTML =  decodeURI(queryDict["weight"]);
				document.getElementById('dessert').innerHTML =  decodeURI(queryDict["dessert"]);
				document.getElementById('drink').innerHTML =  decodeURI(queryDict["drink"]);
				document.getElementById('other').innerHTML =  decodeURI(queryDict["other"]);
			}
		</script>
	</head>
	<body onload="render()">
		<div >
		 <ui>
			<li style="font-family:Georgia"><b> Ingredients : </b></li>
			<li id="ingredients"></li>
			<br>
			<li style="font-family:Georgia"><b> Net weight : </b></li>
			<li id="weight"></li>
			<br>
			<li style="font-family:Georgia"><b> Dessert : </b></li>
			<li id="dessert"></li>
			<br>
			<li style="font-family:Georgia"><b> Drink : </b></li>
			<li id="drink"></li>
			<br>
			<li style="font-family:Georgia"><b> Other : </b></li>
			<li id="other"></li>
		</ui>
	</body>
<html>
'''

def create_menu_content(menu_detail_file, menu_type, menu_list):
    # Get the detail page path
    url = 'file://' + os.path.abspath(menu_detail_file.name)
    content = ''
    for menu in menu_list:
        # Append each type with its content filled in
		if menu_type == "salad":
			content += menu_content.format(
				menu_path=url,
				menu_provider=menu.provider,
				menu_title=menu.name,
				menu_ingredient=menu.ingredient_list,
				menu_weight=menu.weight,
				menu_dessert=menu.dessert,
				menu_drink=menu.drink,
				menu_price=menu.price,
				menu_image_url=menu.photo_url,
				menu_other=menu.sauce
			)
		elif menu_type == "sandwich":
			content += menu_content.format(
				menu_path=url,
				menu_provider=menu.provider,
				menu_title=menu.name,
				menu_ingredient=menu.ingredient_list,
				menu_weight=menu.weight,
				menu_dessert=menu.dessert,
				menu_drink=menu.drink,
				menu_price=menu.price,
				menu_image_url=menu.photo_url,
				menu_other=menu.sandwich_type
			)
		elif menu_type == "hamburger":
			content += menu_content.format(
				menu_path=url,
				menu_provider=menu.provider,
				menu_title=menu.name,
				menu_ingredient=menu.ingredient_list,
				menu_weight=menu.weight,
				menu_dessert=menu.dessert,
				menu_drink=menu.drink,
				menu_price=menu.price,
				menu_image_url=menu.photo_url,
				menu_other=menu.bread_type
			)
		elif menu_type == "sushi":
			content += menu_content.format(
				menu_path=url,
				menu_provider=menu.provider,
				menu_title=menu.name,
				menu_ingredient=menu.ingredient_list,
				menu_weight=menu.weight,
				menu_dessert=menu.dessert,
				menu_drink=menu.drink,
				menu_price=menu.price,
				menu_image_url=menu.photo_url,
				menu_other=menu.pieces_nb
			)
    return content

def open_menu_page(menu_type, menu_list):
  
  # Create or overwrite the menu detial file
  menu_detial_file = open("html/menu_detail.html", 'w')

  # Output the menu detail file
  menu_detial_file.write(menu_detail_content)
  menu_detial_file.close()
  
  # Create or overwrite the menu detial file
  menu_page_file = open("html/menu_" + menu_type + ".html", 'w')
  
  # Get index page url
  index_url = 'file://' + os.path.abspath("html/index.html")

  # Replace the placeholder for the menu with the actual dynamically generated content
  rendered_content = menu_page_content.format(
						menu_tiles=create_menu_content(menu_detial_file, menu_type, menu_list),
						index_path=index_url)

  # Output the menu file
  menu_page_file.write(menu_page_head + rendered_content)
  menu_page_file.close()
  
 
