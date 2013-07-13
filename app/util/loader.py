# -*- coding: utf-8 -*-

import os


class Loader(object):
    """
    class for load directory with audio files
    and prepare them to insert in database
    """

    def __init__(self):
        self.songs = []

    def load_audio_files_from_dir(self, path):
        """
        Examine files from path

        @param path: path to directory
        """

        for item in os.walk(path):
            for name in item[2]:
                self.songs.append(item[0] + '/' + name)

    def get_audio_files(self):
        """
        Get list of songs

        @return: list of songs
        """
        return self.songs
