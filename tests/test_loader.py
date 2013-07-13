# -*- coding: utf-8 -*-

import unittest
from app.util.loader import Loader


class TestLoader(unittest.TestCase):

    def setUp(self):
        self.path = "tests/data/"
        self.loader = Loader()

    def test_load_audio_files_from_dir(self):
        self.loader.load_audio_files_from_dir(self.path)

        self.assertEqual(2, len(self.loader.songs))

    def test_get_audio_files(self):
        audio_files = self.loader.get_audio_files()
        self.assertEqual(0, len(audio_files))