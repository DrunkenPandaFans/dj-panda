# -*- coding: utf-8 -*-

import unittest
from app.player.playlist import *


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist()
        self.song_one = "../good_audio.mp3"
        self.song_two = "../good_audio.ogg"

    def test_add_song(self):
        self.playlist.add_song(self.song_one)

        self.assertEqual(1, len(self.playlist.playlist))

    def test_add_none_song(self):
        def add():
            self.playlist.add_song(None)

        self.assertRaises(WrongSongException, add)

    def test_add_song_to_top(self):
        self.playlist.add_song_to_top(self.song_one)

        self.assertEqual(self.song_one, self.playlist.playlist[0])

    def test_add_none_song_to_top(self):
        def add():
            self.playlist.add_song_to_top(None)

        self.assertRaises(WrongSongException, add)

    def test_add_song_to_index(self):
        self.playlist.add_song(self.song_one)
        self.playlist.add_song_to_index(1, self.song_two)

        self.assertEqual(self.song_two, self.playlist.playlist[1])

    def test_add_none_song_to_index(self):
        self.playlist.add_song(self.song_one)

        def add():
            self.playlist.add_song_to_index(1, None)

        self.assertRaises(WrongSongException, add)

    def test_get_current_song(self):
        self.playlist.add_song(self.song_one)
        song = self.playlist.current_song

        self.assertEqual(self. song_one, song)

    def test_get_playlist(self):
        self.playlist.add_song(self.song_one)

        self.assertEqual(1, len(self.playlist.playlist))

    def test_set_current_song_to_index(self):
        self.playlist.add_song(self.song_one)
        self.playlist.add_song(self.song_two)
        self.playlist.add_song(self.song_one)

        self.playlist.set_current_song_to_index(1)

        self.assertEqual(self.song_two, self.playlist.current_song)
        self.assertEqual(2, len(self.playlist.playlist))

    def test_next_song(self):
        self.playlist.add_song(self.song_one)
        self.playlist.add_song(self.song_two)

        self.assertEqual(self.song_one, self.playlist.current_song)

        self.playlist.next_song()

        self.assertEqual(self.song_two, self.playlist.current_song)
