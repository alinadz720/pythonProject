CREATE TABLE users (
    userId INT UNIQUE,
    username VARCHAR,
    firstname VARCHAR,
    lastname VARCHAR,
    email VARCHAR,
    password VARCHAR,
    phone VARCHAR
);

CREATE TABLE products (
    productId INT UNIQUE,
    name VARCHAR PRIMARY KEY,
    status VARCHAR
);

CREATE TABLE orders (
    orderId INT UNIQUE,
    userId INT,
    productId INT,
    status VARCHAR,
    is_complete BIT,
    FOREIGN KEY (userId) REFERENCES users (userId),
    FOREIGN KEY (productId) REFERENCES products (productId)
);