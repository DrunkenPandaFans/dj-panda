# -*- coding: utf-8 -*-

import unittest
from app.util.metadataloader import MetaDataLoader
from app.util.metadataloader import WrongHeaderException
from app.util.metadataloader import NotSupportedFileException


class TestMetaDataLoader(unittest.TestCase):

    def setUp(self):
        self.loader = MetaDataLoader()
        self.metadata = [{'path':'tests/data/good_audio.ogg',
                          'album':u'good_audio_album',
                          'title':u'good_audio',
                          'genre':u'good_audio_genre',
                          'artist':u'good_audio_artist',
                          'length':380.8130612244898},
                         {'path':'tests/data/good_audio.mp3',
                          'album':u'good_audio_album',
                          'title':u'good_audio',
                          'genre':u'good_audio_genre',
                          'artist':u'good_audio_artist',
                          'length':380.8130612244898}]
        self.good_ogg_file = "tests/data/good_audio.ogg"
        self.no_header_ogg_file = "tests/data/wrong_header_audio.ogg"
        self.good_mp3_file = "tests/data/good_audio.mp3"
        self.no_header_mp3_file = "tests/data/wrong_header_audio.mp3"
        self.no_supported_file = "tests/data/no_supported_audio_wma"

    def test_load_metadata(self):
        def load():
            self.loader.load_metadata(self.no_supported_file)

        self.assertRaises(NotSupportedFileException, load)

    def test_load_ogg_metadata(self):
        metadata = self.loader.load_ogg_metadata(self.good_ogg_file)

        self.assertEqual(self.metadata[0]['album'], metadata['album'])
        self.assertEqual(self.metadata[0]['artist'], metadata['artist'])
        self.assertEqual(self.metadata[0]['title'], metadata['title'])
        self.assertEqual(self.metadata[0]['genre'], metadata['genre'])
        self.assertEqual(self.metadata[0]['path'], metadata['path'])
        self.assertAlmostEqual(self.metadata[0]['length'],
                    metadata['length'], places=1)

    def test_load_ogg_with_no_header(self):
        def load_ogg():
            self.loader.load_ogg_metadata(self.no_header_ogg_file)

        self.assertRaises(WrongHeaderException, load_ogg)

    def test_load_mp3_metadata(self):
        metadata = self.loader.load_mp3_metadata(self.good_mp3_file)

        self.assertEqual(self.metadata[1]['album'], metadata['album'])
        self.assertEqual(self.metadata[1]['artist'], metadata['artist'])
        self.assertEqual(self.metadata[1]['title'], metadata['title'])
        self.assertEqual(self.metadata[1]['genre'], metadata['genre'])
        self.assertEqual(self.metadata[1]['path'], metadata['path'])
        self.assertAlmostEqual(self.metadata[1]['length'],
                 metadata['length'], places=1)

    def test_load_mp3__with_no_header(self):
        def load_mp3():
            self.loader.load_mp3_metadata(self.no_header_mp3_file)

        self.assertRaises(WrongHeaderException, load_mp3)

    def test_extract_metadata(self):
        self.loader.extract_metadata([self.good_ogg_file,
                    self.good_mp3_file])

        self.assertEqual(2, len(self.loader.metadata))

    def test_get_metadata(self):
        metadata = self.loader.get_metadata()
        self.assertEqual(0, len(metadata))