# The Wine Society*

This website is a specialist shop, with a wine club. A place for wine enthusiast. The shop will sell wine from different parts of the world, and will encourage customers to join the club to access extra customer benefits.

## Table of Contents

- Introduction
- Business Model
- Preparation
	 - Wireframe
	 - Agile / Github issues and projects
- Features
	 - Homepage
	 - Shop
	 - blog
	 - Site management
- Technologies
	 - Django
	 - SQL Database
	 - Stripe
	 - Heroku
	 - AWS
- Marketing
- Testing
- Deployment
- Bugs
- Credits
- Acknowledgements

## Introduction

## Business Model

This a business to customer business, B to C model, built around a community. The site will offer a traditional retail experience, with the goal of engaging customers who are interested in the product and want to learn more about its background, attend tastings, and hear talks from winemakers and other industry specialists. The wine club will produce informative and engaging blog posts, host wine tasting events, and offer member discounts and monthly wine samples curated around themes and events.  The club will offer a subscription service to provide customers with a convenient and hassle-free way to discover and enjoy new wines. The business will also offer products related to wine, including wine glasses, decanters, wine opener, and other related products.  

## Preparation

### Wireframes

Before using Balsamiq to layout my design, I prefer to utilize simple hand drawn sketches to develop my websites. To have a better understanding of the design and functionality, I took some time to examine and dissect other websites that I found enjoyable.

<details>

### Product Page

![product Page](/media/readme_images/product.png)

 ### Shop
![product Page](/media/readme_images/Shop.png)

### Basket
![product Page](/media/readme_images/basket.png)
</details>

### Agile Development

In the development of this e-commerce Django site, Agile methodologies were employed. The project was organised into various Tasks, contributing to overarching Epics that represented large-scale features and goals. To track the progress and ensure that stages were achieved, milestones were set at key points throughout the project timeline.

User Stories were created and divided between the site owner and the customer to represent the different requirements and positions of these two groups. User Stories covered issues like customer management and inventory control for the website owner. The focus for the customer, was on enhancing user experience through seamless navigation, efficient checkouts, and intuitive search functionalities. By combining Agile practices with clearly defined milestones, the I was able to prioritise work, adapt to changes, and hopefully produce a functional ecommerce website.

### Agile User Stories
![product Page](/media/readme_images/agile.png)

## Features

### Homepage

The homepage will feature a large hero image, with the title of the business. The image will take up 100% of the viewport. The shop link will be prominently displayed on the page. The website owner will be able to use this landing page to create a theme for the site, either to promote a product, an event, or a season.

As the user scrolls down, they will see bold images with links to different sections of the shop. For example, a "Bold Reds" image would bring the user to a curated selection of red wines. The homepage will also contain links to the blog and wine club, with information about upcoming events.

![Home page](media/readme_images/homepage.png)

## Shop

### Product Page

<details>

<summary>Product Page</summary>

![Product page](media/readme_images/product_page.png)

</details>

### Product detail

<details>
<summary>Product Details</summary>

![Product page](media/readme_images/product_details.png)

</details>

### Shopping bag

<details>
<summary>Shopping Bag</summary>

![Product page](media/readme_images/shopping_bag.png)

</details>

### Checkout

<details>
<summary>Checkout</summary>

![Product page](media/readme_images/checkout_site.png)

</details>


## Technologies*

### Languages

- HTML
- CSS
- JavaScript
- Python

### Programs, Libraires and Programs

- Django
- Django Allauth
- Codeanywhere
- Heroku
- Elephant SQL
- Amazon Web Services
- Stripe


## Marketing
Leveraging both Facebook and a dedicated blog, I aim to create a dynamic online presence for my wine shop. Facebook is invaluable for real-time engagement, where the I can post daily updates on new arrivals, special promotions, and upcoming tasting events.
<details>
  <summary>Facebook page screenshots</summary>

  ### Facebook
  
  ![facebook Screenshot 1](media/readme_images/facebook_bus.png)
  ![facebook Screenshot 1](media/readme_images/facebook_bus_2.png)
</details>

### Blog

The blog, on the other hand, serves as a platform for more in-depth content, including wine pairing guides and interviews with vineyard owners. Together, these platcforms not only attract new customers but also build a community of wine enthusiasts.

A wine blog can be used to populate other marketing channels, such as Facebook and Instagram, with engaging and informative content. Additionally, Google places higher ranking on authoritative sources, so a regularly updated blog can assist the overall business with SEO rankings.

<details>
  <summary>blog page screenshots</summary>

### Blog
  
  ![blog Screenshot 1](media/readme_images/blog_cover.png)
  ![blog Screenshot 2](media/readme_images/blog_details.png)
</details>


## Testing

The website was tested for markup and CSS validation along with javascript, responsive design.

The python code was run through Code Institute's Pep8 Linter to check for errors. It passed with no errors expect for line length.
- Products models
Results:
50: E501 line too long (91 > 79 characters)
96: E501 line too long (85 > 79 characters)
98: E501 line too long (84 > 79 characters)

- Checkout Webhook and webhook handler
81: E501 line too long (80 > 79 characters)
82: E501 line too long (80 > 79 characters)
83: E501 line too long (80 > 79 characters)
111: E501 line too long (89 > 79 characters)
119: E501 line too long (107 > 79 characters)
163: E501 line too long (93 > 79 characters)

- Checkout models
15: E501 line too long (122 > 79 characters)
26: E501 line too long (94 > 79 characters)
27: E501 line too long (93 > 79 characters)
28: E501 line too long (92 > 79 characters)
30: E501 line too long (86 > 79 characters)
65: E501 line too long (113 > 79 characters)
66: E501 line too long (91 > 79 characters)
68: E501 line too long (113 > 79 characters)
74: E501 line too long (109 > 79 characters)

As they do not impact the website, I have left them in place to avoid creating issues.

- HTML W3C
-![W3C HTML Result](./media/readme_images/w3org.png)
    - This validator showed several errors in relation to li items as children of nav element. Unfortunately, I was unable to locate the shown errors in the code in order to fix them before submission. 
    - I was able to fix the error casued by a gap in the URL using urlencode to replace the gap with %20.
  - Error: Duplicate ID user-options. I was unable to locate the duplication before deployment. It has not impacted the functionality of the site

- CSS W3C
-![W3C CSS Result](./media/readme_images/css_error.png)
   -  Two error which one which I corrected, the second issue was not resolved before deployment.

I manually tested the site, dicovering and resolving a number of bugs. I used prints statements and console log as my main tools for fixing the the issues. I with statments I would be able see each step and indentify the issues.

## Deployment

1.	Set a repository on GitHub using the CI template from code institute.  
2.	Set up workspace within Codeanywhere by using GitHub repository.
3.	Once workspace has been created, install Django, pip3 install ‘django<4’
4.	Create a new project, use django-admin startproject the_wine_society
5.	Create gitignore file, touch .gitignore and add *.pyc,*.sqlite3, _pycahe_
6.	Run the project using django3 manage.py runserver
7.	Add to ‘8000-shane-bath-ecommerce-pp5-g3jop36yi6.us2.codeanyapp.com’ to ALLOWED_HOSTS = [] settings.py
8.	Once you have confirmed that the server is working, stop the server and complete you first migration. Run python3 manage.py migrate
9.	Create a super user, run python3 manange.py createsuperuser and create as username with password
10.	Commit changes to the github repository, run git add . , git commit -m “initial commit”. Git push
11.	Create a databasae, I used ElephantSQL, create a new database using the tiny turtle level. Name you database, select the region closes to you and create new instance
12.	Deploy the app to Heroku, select create new app, name the app and select Europe. Create the app.
13.	Configure the database in Heroku, go to settings, select revel config vars. Add DATABASE_URL and paste in the postgres URL from ElephantSQL. Click add.
14.	Inistall dj_database_ url and psycoppd2, run pip3 install dj_database_url==0.5.0 psycopg2 in the terminal
15.	Add the packages to requirements.txt run pip3 freeze > requirements.txt
16.	In settings.py add import os and import dj_database_url
17.	Add the new elephantSQL database url to env.py:
DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
18.	Install gunicorn, run pip3 install gunicorn
19.	Add the gunicorn to requirements.txt run pip3 freeze > requirements.txt
20.	In the Heroku app disable STATIC file, in the reveal config section under setting add: DISABLE_COLLLECTSTATIC and 1. Click add
21.	In Heroku reveal config section, add SECRET_KEY and add a password
22.	Add PORT and 8000 to Heroku config var section
23.	In settings.py replace the SECRET_KEY with the following, SECRET_KEY = os.environ.get(‘SECRET_KEY, ‘ ‘)
24.	In settings.py change debug from TRUE to 'DEVELOPMENT' in os.environ
25.	In settings.py add if os.path.isfile('env.py'): import env
26.	Run python manage.py migrate to migrate to the ElephantSQL database
27.	Created and  deployed AWS bucket added keys to the Heroku config files

The live site canbe found here: https://the-wine-society-01e133d06325.herokuapp.com/
## Bugs

I have discovered 10 minutes before deployment  that my small screen media css is not working on the deployed app. It working on my development side. To late to fix it.

<details>

![Small screen ](/media/readme_images/ccs_codeanywhere.png)

</details>

## Credits

The basis of the code come from the Code Institue "Boutique Ado"

## Acknowledgements

A big thank you to Dasiy Mcgirr
