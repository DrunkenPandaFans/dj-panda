# -*- coding: utf-8 -*-


class PlaylistException(Exception):
    pass


class Playlist(object):

    def __init__(self):
        self._playlist = []
        self._current_song = None

    def add_song(self, song_path):
        if not song_path:
            raise PlaylistException("Song path is empty.")

        if not self.playlist:
            self._current_song = song_path
            self._playlist.append(song_path)
        else:
            self._playlist.append(song_path)

    def add_song_to_top(self, song_path):
        if not song_path:
            raise PlaylistException("Song path is empty.")

        self._playlist.insert(0, song_path)
        self._current_song = song_path

    def add_song_to_index(self, i, song_path):
        if not song_path:
            raise PlaylistException("Song path is empty.")

        self._playlist.insert(i, song_path)

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
            try:
                self._current_song = self.playlist[0]
            except (IndexError):
                self._current_song = None
                raise PlaylistException("Playlist is empty")
        else:
            self._current_song = None
