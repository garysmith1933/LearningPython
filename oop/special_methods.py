class Book():

  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

  #returns string version of object
  def __str__(self):
    return f"{self.title} by {self.author}"

  #returns length of the object
  def __len__(self):
    return self.pages

  #deletes object
  def __del__(self):
    print('A book object has been DELETED')

b = Book('Python rocks', 'Jose', 200)

print(b) # prints Python rocks by Jose

del b 
print(b) # will print b is not defined
