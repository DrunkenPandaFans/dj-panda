# -*- coding: utf-8 -*-

import mutagen.mp3
import mutagen.oggvorbis


class MetaDataLoader(object):

    def __init__(self):
        self.metadata = []
        self.load = {'mp3': self.load_mp3_metadata,
                     'wav': self.load_wav_metadata,
                     'ogg': self.load_ogg_metadata}

    def load_ogg_metadata(self, _file):
        """
        Ogg metadata loader

        @param _file: ogg file

        @return: return metadata (path, album, genre, length, artist, title)
        """
        metadata = {}
        metadata['path'] = _file

        info = mutagen.oggvorbis.Open(_file)

        if info.tags.get('album') is not None:
            metadata['album'] = info.tags['album'][0]
        if info.tags.get('genre') is not None:
            metadata['genre'] = info.tags['genre'][0]

        metadata['length'] = info.info.length

        if info.tags.get('artist') is not None:
            metadata['artist'] = info.tags['artist'][0]
        if info.tags.get('title') is not None:
            metadata['title'] = info.tags['title'][0]

        return metadata

    def load_mp3_metadata(self, _file):
        """
        Mp3 metadata loader

        @param _file: mp3 file

        @return: return metadata (path, album, genre, length, artist, title)
        """
        metadata = {}
        metadata['path'] = _file

        info = mutagen.mp3.Open(_file)

        if info.tags.get('TALB') is not None:
            metadata['album'] = info.tags['TALB']
        if info.tags.get('TCON') is not None:
            metadata['genre'] = info.tags['TCON']

        metadata['length'] = info.info.length

        if info.tags.get('TPE1') is not None:
            metadata['artist'] = info.tags['TPE1']
        if info.tags.get('TIT2') is not None:
            metadata['title'] = info.tags['TIT2']

        return metadata

    def extract_metadata(self, audio_files):
        """
        Iterate audio files and load metadata from different audio files

        @param audio_files: list of audio files
        """
        for _file in audio_files:
            try:
                audio_type = _file[_file.rfind('.') + 1:]
                self.metadata.append(self.load[audio_type](_file))
            except mutagen.mp3.HeaderNotFoundError:
                print(_file + " Header is empty ")
            except mutagen.oggvorbis.OggVorbisHeaderError:
                print(_file + "Header is wrong")
            except KeyError:
                print(_file + " Not supported audio format")

    def get_metadata(self):
        """
        Get a list of songs metadata

        @return: return list
        """
        return self.metadata

