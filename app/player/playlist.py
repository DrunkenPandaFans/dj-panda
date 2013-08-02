# -*- coding: utf-8 -*-


class WrongSongException(Exception):
    pass


class Playlist(object):

    def __init__(self):
        self._playlist = []
        self._current_song = None

    def add_song(self, song):
        if not song:
            raise WrongSongException

        if not self.playlist:
            self._current_song = song
            self._playlist.append(song)
        else:
            self._playlist.append(song)

    def add_song_to_top(self, song):
        if not song:
            raise WrongSongException

        self._playlist.insert(0, song)
        self._current_song = song

    def add_song_to_index(self, i, song):
        if not song:
            raise WrongSongException

        self._playlist.insert(i, song)

    def set_current_song_to_index(self, i):
        song = self.playlist[i]
        while(song is not self.current_song):
            self.next_song()

    @property
    def playlist(self):
        return self._playlist

    @property
    def current_song(self):
        return self._current_song

    def next_song(self):
        if self._playlist:
            self._playlist.pop(0)
            self._current_song = self.playlist[0]
        else:
            self._current_song = None
