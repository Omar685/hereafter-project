USE akhirah

CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  post_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  content VARCHAR(2000),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(post_id) REFERENCES posts(id),
  FOREIGN KEY(user_id) REFERENCES users(id)
);

-- SOURCE E:\2024\My Projects\continuous\venv\projects\hereafter-project\query\comments.sql