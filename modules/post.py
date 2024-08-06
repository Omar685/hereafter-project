from enum import Enum



class Post(object):
  def __init__(self, id, user_id, content, image=None):
    self.id = id
    self.user_id = user_id
    self.content = content
    self.image = image
  
  def create_post(self, user_id):
    sql = "SELECT * FROM posts WHERE user_id = ?"
    value = user_id
    self.fetchone(sql, value)
    