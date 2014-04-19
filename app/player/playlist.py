# -*- coding: utf-8 -*-


class PlaylistException(Exception):
    pass


class EmptySongPathException(Exception):
    pass


class Playlist(object):

    """
    TODO pridat zoznam hranych pesniciek a pridat metody, ktore budu presuvat pesnicky medzi aktualnym playlistom a uz hranymi.

    """
    def __init__(self,listener):
        self._playlist = []
        self._current_song = None
        self._listener = listener

    def add_song(self, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        if not self.playlist:
            self.current_song = song_path
            self._playlist.append(song_path)
        else:
            self._playlist.append(song_path)

    def add_song_at_top(self, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        self._playlist.insert(0, song_path)
        self.current_song = song_path

    def add_song_at_index(self, i, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        self._playlist.insert(i, song_path)

    def set_current_song_at_index(self, i):
        song = self.playlist[i]
        while(song is not self.current_song):
            self.next_song()

    @property
    def playlist(self):
        return self._playlist

    @property
    def current_song(self):
        return self._current_song

    @current_song.setter
    def current_song(self, song_path):
        self._current_song = song_path
        if self._current_song:
            self._listener.changed_song()

    def next_song(self):
        if self._playlist:
            self._playlist.pop(0)
            try:
                self.current_song = self.playlist[0]
            except IndexError:
                self.current_song = None
        else:
            self.current_song = None
