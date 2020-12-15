CREATE TABLE Users (
    userId int IDENTITY(1,1) NOT NULL  PRIMARY KEY,
    username varchar(50) NOT NULL,
	firstname varchar(50) NOT NULL,
	lastname varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
    password varchar(50) NOT NULL,
    phone varchar(50) NOT NULL
);



CREATE TABLE Products (
    productId int IDENTITY(1,1) NOT NULL  PRIMARY KEY,
    productname varchar(50) NOT NULL,
	status varchar(50) NOT NULL
);

CREATE TABLE Orders (
    orderId int IDENTITY(1,1) NOT NULL,
    userId int NOT NULL FOREIGN KEY REFERENCES Users(userId),
    productId int NOT NULL FOREIGN KEY REFERENCES Products(productId),
    status varchar(50) NOT NULL,
	isComplete bit NOT NULL
);
