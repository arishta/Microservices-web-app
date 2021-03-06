# Microservices-web-app

## Basic idea
The basic idea of this project is to show how various microservices, each independent of each other, communicate among themselves. There are three microservices: User, Product and Like. These microservices are independent of each other, are built on different frameworks and yet are still able to communicate with each other using the messaging service - RabbitMQ.

## Requirements
1. Python == 3.9.1
2. Django == 3.1.4
3. Flask == 1.1.2
4. MySQL == 5.7.32
5. Postman == 7.36.1
6. Docker

## Details about the microservices

It is a backend web application which consists of three microservices:

### User microservice:

This microservice is built on the Django framework.
It is concerned with storing, processing and retrieving information related to users. To store the information of the users, it uses a MySQL database called User. All the CRUD operations related to the users are performed by this microservice.

### Product microservice: 

This microservice is built on the Django framework.
It is concerned with storing, processing and retrieving information related to products. To store the information of the products, it uses a MySQL database called Product. All the CRUD operations related to the products are performed by this microservice.

### Likes microservice

This microservice is built on the Flask framework and is concerned with incrementing the likes on a product by a user. This microservice communicates with the Product and the User app to update the information in their respective databases.

## API Description

### User app 
There are 6 APIs made in this app: 
1. Get list: It lists all the users available in the database. 
2. Create a user: It creates a new user and feeds this information to the database. 
3. Retrieve user using id: It fetches the user corresponding to the given user id
4. Update user: It updates the information of the user corresponding to the given user id.
5. Delete user: It deletes the specified user id from the database.
6. Get random user: It generates the user id of any random user. 


### Products app 

There are 6 APIs made in this app: 
1. Get list: It lists all the products available in the database. 
2. Create a product: It creates a new product and feeds this information to the database. 
3. Retrieve product using id: It fetches the product corresponding to the given product id.
4. Update product: It updates the information of the product corresponding to the given product id.
5. Delete product: It deletes the specified product id from the database.
6. Get random product: It generates the product id of any random product. 

### Likes app 

This app has one API called - create likes. This generates a random user id and random product id and increases the likes count corresponding to this user and product. This API communicates with the user and product microservice via RabbitMQ.

## Screenshots

#### Create user API

![Create user](https://github.com/arishta/Microservices-web-app/blob/main/screenshots/create%20user.PNG)

#### Create product API
![Create product](https://github.com/arishta/Microservices-web-app/blob/main/screenshots/create%20product.PNG)

#### Create likes API
![Create likes](https://github.com/arishta/Microservices-web-app/blob/main/screenshots/create%20like.PNG)

#### Retrieve product id 
Increased likes count on product id 9
![Increased likes count on product](https://github.com/arishta/Microservices-web-app/blob/main/screenshots/increased%20likes%20in%20product%20id.PNG)

#### Retrieve user id 
(Increased likes count on user id 6)
![Increased likes count on user](https://github.com/arishta/Microservices-web-app/blob/main/screenshots/increased%20likes%20in%20user.PNG)



