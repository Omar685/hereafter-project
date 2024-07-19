CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT ,
  name VARCHAR(255) NOT NULL,
  username VARCHAR(255) ,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  logo VARCHAR(255) DEFAULT "/static/images/one.jpg",
  age VARCHAR(100),
  location VARCHAR(255),
  PRIMARY KEY(id, username)
)

-- INSERT INTO users(name, username, email, password, age, location)
-- VALUES ("Omar", "Omar332", "omar@gmail.com", "123123", "16", "Egypt")

-- UPDATE users
-- SET status = ""
-- WHERE 1;

-- ALTER TABLE users
-- ALTER COLUMN status VARCHAR(50) DEFAULT '';