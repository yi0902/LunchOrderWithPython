import webbrowser
import os
import re

# Styles and scripting for the page
index_page_head = '''
<!DOCTYPE html>
<html lang="en">
	<head>
        <meta charset="utf-8" />
        <title>Order menu online at LA DEFENSE</title>
	<link rel="stylesheet" type="text/css" href="css/style.css" />
	<link rel="stylesheet" type="text/css" href="css/base.css" />
	<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
	<script type="text/javascript" charset="utf-8">
		$(document).on('click', '.promoBG1', function (event) {
			var menuType = decodeURI($(this).attr('menu-type')).split(" ")[0].toLowerCase();
			var absolutePath = $(this).attr('menu-path');
			var srcURL= absolutePath + "/menu_"+ menuType + ".html";
			window.location.href = srcURL;
		});
	</script>
	<style type="text/css" media="screen">
                .media:hover {
                        background-color: #EEE;
			cursor: pointer;
		}
	</style>
    </head>
'''

# The index page layout and logo bar
index_page_content = '''
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
		<!-- title -->    
		<div class="l-grid">
			<div class="l-col l-size1of1">
				<h2 class="f-display mbl"> Order your lunch menu here &amp; Get it without waiting </h2>
			</div>
		</div>
		<!-- lunch menu -->
		<div class="l-grid">
			<ul class="list-media promos">
				{menu_type_content}
			</ul>
		</div>
	</div>
  </body>
</html>
'''

# A single menu type html template
menu_type_content = '''
<li class="l-col l-size1of4 media promo1">
	<div class="promoBG1" menu-type="{menu_type_name}" menu-path="{menu_path}">
		<div class="img">
			<img src="{menu_type_image}">
		</div>
		<div class="bd">
			<h2 class="mbs f-alt">{menu_type_name}</h2>
			<div class="promo-text">
				{menu_type_description}
			</div>
		</div>
	</div>
</li>
'''

def create_menu_type_content(index_file, menu_types):
    # Get the parent folder of index page
    url = 'file://' + os.path.abspath(os.path.dirname(index_file.name))
    # The HTML content for this section of the page
    content = ''
    for type in menu_types:
        # Append each type with its content filled in
        content += menu_type_content.format(
	    menu_path=url,
            menu_type_name=type.name,
            menu_type_image=type.image_url,
            menu_type_description=type.description
        )
    return content

def open_index_page(menu_types):
  # Create or overwrite the index file
  index_file = open("html/index.html", 'w')

  # Replace the placeholder for the menu types with the actual dynamically generated content
  rendered_content = index_page_content.format(menu_type_content=create_menu_type_content(index_file, menu_types))

  # Output the file
  index_file.write(index_page_head + rendered_content)
  index_file.close()

  # open the output file in the browser
  url = os.path.abspath(index_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
