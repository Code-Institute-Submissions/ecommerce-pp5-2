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
	 - Club / Blog
	 - Images
	 - Typgraphy
	 - Color Scheme
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

- HTML
-![W3C Markup Result](./media/readme_images/w3org.png)
    - This validator showed several errors in relation to li items as children of nav element. Unfortunately, I was unable to locate the shown errors in the code in order to fix them before submission. 
    - I was able to fix the error casued by a gap in the URL using urlencode to replace the gap with %20.
  - Error: Duplicate ID user-options. I was unable to locate the duplication before deployment. It has not impacted the functionality of the site
  
## Deployment

## Bugs

## Credits

## Acknowledgements
