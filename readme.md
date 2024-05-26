# Rentify

Rentify is a Django web application that allows users to register as buyers or sellers and manage property listings. Sellers can post, update, and delete their property listings, while buyers can view and express interest in properties. Additionally, users can like properties, and email notifications are sent to the sellers when a buyer expresses interest.

## Features

- User registration and authentication (buyers and sellers)
- Sellers can post, update, and delete property listings
- Buyers can view property listings and express interest
- Buyers and sellers receive email notifications when interest is expressed
- Property listing with filtering options
- Like functionality for properties

## Installation

### Create a virtual environment and install dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt


Set up the database:
python manage.py makemigrations
python manage.py migrate


Create a superuser:
python manage.py createsuperuser

Create a .env file in the root directory and add the following variables:
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password


Run the development server:
python manage.py runserver




Open your browser and go to http://127.0.0.1:8000/.

Usage
User Registration
URL: /register/
Method: GET, POST
Description: Allows users to register as either a buyer or seller.
User Login
URL: /login/
Method: GET, POST
Description: Allows users to log in with their username or email and password.
User Logout
URL: /logout/
Method: GET
Description: Logs the user out and redirects to the homepage.
Seller Dashboard
URL: /seller_dashboard/
Method: GET
Description: Displays the logged-in seller's properties.
Buyer Dashboard
URL: /buyer_dashboard/
Method: GET
Description: Displays all property listings with pagination and filtering options.
Post Property
URL: /post_property/
Method: GET, POST
Description: Allows sellers to post a new property.
Update Property
URL: /update_property/<property_id>/
Method: GET, POST
Description: Allows sellers to update their property details.
Delete Property
URL: /delete_property/<property_id>/
Method: GET, POST
Description: Allows sellers to delete their property.
Property Detail
URL: /property_detail/<property_id>/
Method: GET
Description: Displays detailed information about a property.
Express Interest
URL: /express_interest/<property_id>/
Method: POST
Description: Allows buyers to express interest in a property. Sends email notifications to the seller and the buyer.
Like Property
URL: /like_property/<property_id>/
Method: POST
Description: Allows buyers to like or unlike a property.
```
