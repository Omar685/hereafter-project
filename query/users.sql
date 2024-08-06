CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  username VARCHAR(255) UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  logo VARCHAR(255) DEFAULT "/static/images/one.jpg",
  cover VARCHAR(255) DEFAULT "/static/images/tow.jpg",
  age VARCHAR(10),
  location VARCHAR(255),
  followers INT,
  following INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id, username)
)
