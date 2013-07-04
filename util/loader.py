# -*- coding: utf-8 -*-

import os


class Loader(object):
    """
    class for load directory with audio files
    and prepare them to insert in database
    """

    def __init__(self, path):
        self.songs = self.load_audio_files_from_dir(path)

    @classmethod
    def load_dir(self, path):
        """
        Load directory
        @param path: path to directory

        @return: return 3-tuple, consist of dir path, sub dir, list of files
        """
        return os.walk(path)

    @classmethod
    def load_audio_files_from_dir(self, path):
        """
        Examine files from path
        @param path: path to directory

        @return: return path to files in directory
        """
        songs = []
        for item in self.load_dir(path):
            for name in item[2]:
                songs.append(item[0] + '/' + name)

        return songs

    def get_audio_files(self):
        """
        Get list of songs
        @return: list of songs
        """
        return self.songs
