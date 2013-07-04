# -*- coding: utf-8 -*-

import os

class Loader(object):
    """class for load directory with audio files
        and prepare them to insert in database"""

    def __init__(self,path):
        self.songs = []
        self.load_songs_from_dir(path)

    def load_dir(self, path):
        """
        Load direcotry
        @param path: path to directory

        @return: return 3-tuple, consist of dir path, sub dir, list of files
        """
        return os.walk(path)

    def load_songs_from_dir(self, path):
        """Examine files from path
        @param path: path to directory

        @return: return path to files in directory
        """
        for item in self.load_dir(path):
            for name in item[2]:
                self.songs.append(item[0] + '/' + name)

    def get_songs(self):
        return self.songs

d = Loader('/home/paynes/mp3')
print(d.get_songs())
