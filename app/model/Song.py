#!/usr/bin/python

import pymongo

class SongDAO(object):
  
  def __init__(self, database):
    self.database = database
    self.songs = database.songs

  def get_song(self, identifier):
    return self.songs.find_one({"_id": identifier})

  def get_songs(self, album):
    return self.songs.find({"album": album})

  def get_songs(self, artist):
    return self.songs.find({"artists": artist})
          
