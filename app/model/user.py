#!/usr/bin/python

class UserDAO(object):
  "Class to access users collection"

  def __init__(self, database):
    self.database = database
    self.users = database.users

  def save(self, nickname, token):
    if not nickname or not token:
      return

    user = {"_id": nickname,
            "token": token}
    
    #TODO catch exception
    self.users.insert(user)

  def update(self, nickname, token):
    if not identifier or not nickname or not token:
      return

    user = {"_id": nickname,
            "token": token}

    #TODO catch exception
    self.users.update({"_id": nickname}, user)

  def find(self, identifier):
    if not identifier:
      return None

    user = self.users.findById({"_id": identifier})
    return user

  def find_by_token(self, token):
    if not token:
      return None

    user = self.users.findOne({"token": token})
    return user
