class Book:

  def __init__(self, title, author, num_copies):
    self.title = title
    self.author = author
    self.num_copies = num_copies

  def check_in(self):
    self.num_copies += 1

  def check_out(self):
  	if self.num_copies > 0:
  		self.num_copies -= 1
  		return True
  	return False