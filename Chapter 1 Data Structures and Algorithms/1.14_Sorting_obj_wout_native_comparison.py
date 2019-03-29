class User:
  def __init__(self, user_id):
    self.user_id = user_id
  
  def __repr__(self):
    return f"User({self.user_id})"

users = [User(23), User(3), User(99)]
print(users)
# print(sorted(users)) # Ошибка

from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

print(max(users, key=attrgetter('user_id')))
print(min(users, key=attrgetter('user_id')))
