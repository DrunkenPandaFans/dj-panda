# -*- coding: utf-8 -*-


import mutagen.mp3
from loader import Loader


class MetaDataLoader(object):

    def __init__(self):
        self.metadata = {}
        self.load = {'mp3': self.load_mp3_metadata}

    def load_mp3_metadata(self, _file):
        """
        Mp3 metadata loader

        @param _file: mp3 file

        @return: return metadata (album, genre, length, artist, title)
        """
        info = mutagen.mp3.Open(_file)
        metadata = []
        for item in info.keys():
            #TODO
            #metadata.append(info.tags['TALB'].text[0])
            pass

        return metadata

    def extract_metadata(self, audio_files):
        """
        Iterate audio files and load metadata from different audio files

        @param audio_files: list of audio files

        @return: return dictionary, key is audio file path,
                 value is list of metadata
        """
        for _file in audio_files:
            try:
                audio_type = _file[_file.rfind('.') + 1:]
                self.metadata[_file] = self.load[audio_type](_file)
            except mutagen.mp3.HeaderNotFoundError:
                print(_file + " Header is empry ")
            except KeyError:
                print(_file + " Not supported audio format")

    def get_metadata(self):
        """
        Get dictionary

        @return: return dictionary
        """
        return self.metadata
