# Ecommerce Store with Django
This is an Ecommerce store based on `Django 2.2` and `python 3.6`


## Features
* Categorizing products by adding categories and subcategories
* Adding Products with details and pictures
* OAuth including Google
* Payment with [stripe](www.stripe.com)
* User Review for products
* Searching for Products
* User favorite list
* Saving user addresses

## Installation
1. Clone the repository and navigate to the directory:

    ```
    git clone https://github.com/fatemehkarimi/ecommerce_store.git
    cd ecommerce_store
    ```
1. Setup virtual env and install dependancies:

    ```
    pipenv shell
    pipenv sync
    ```
1. Build dockerfile:

    ```
    sudo docker build .
    ```
1. migrate django project:

    ```
    sudo docker-compose exec web python3 manage.py migrate
    ```
1. run docker image:

    ```
    sudo docker-compose up -d
    ```
1. Navigate to [localhost](http://localhost:8000) to see the homepage
1. Admin dashboard is available at [localhost/admin](http://localhost:8000/admin). to access the dashboard, first create a superuser:

    ```
    sudo docker-compose exec web python3 manage.py createsuperuser
    ```
1. to use payment of website, add your stripe account public and private keys to file `conffidentials.py` in `ecommerce_store` subdirectory.

    ```
    STRIPE_TEST_PUBLISHABLE_KEY = 'YOUR_PUBLIC_KEY'
    STRIPE_TEST_SECRET_KEY = 'YOUR_PRIVATE_KEY'
    ```
