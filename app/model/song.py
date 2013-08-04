#!/usr/bin/python

import pymongo
import logging
import sys

class SongDAO(object):
  
  def __init__(self, database):
    self.database = database
    self.songs = database.songs
    self.logger = logging.getLogger(self.__class__.__name__)

  def get_song(self, identifier):
    return self.songs.find_one({"_id": identifier})

  def get_songs(self, album):
    return self.songs.find({"album": album})

  def get_songs(self, artist):
    return self.songs.find({"artists": artist})

  def save(self, name, album, artist, path):
    song = { "name": name,
             "album": album,
             "artist": artist,
             "path": path}

    try:
      self.songs.insert(song)
    except:
      msg = sys.exc_info()[0]
      self.logger.error("It wasn't possible to save song because of following exception: %s", msg)

  def remove(self, identifier):
    try:
      self.songs.delete({"_id": identifier})
    except:
      msg = sys.exc_info()[0]
      self.logger.error("It wasn't possible to remove song because of following exception: %s", msg)
          
