# -*- coding: utf-8 -*-


class PlaylistException(Exception):
    pass


class EmptySongPathException(Exception):
    pass


class Playlist(object):

    def __init__(self):
        self.__playlist = []
        self.__current_song = None

    def add_song(self, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        if not self.playlist:
            self.current_song = song_path
            self.__playlist.append(song_path)
        else:
            self.__playlist.append(song_path)

    def add_song_at_top(self, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        self.__playlist.insert(0, song_path)
        self.current_song = song_path

    def add_song_at_index(self, i, song_path):
        if not song_path:
            raise EmptySongPathException("Song path is empty.")

        self.__playlist.insert(i, song_path)

    def set_current_song_at_index(self, i):
        song = self.playlist[i]
        while(song is not self.current_song):
            self.next_song()

    @property
    def playlist(self):
        return self.__playlist

    @property
    def current_song(self):
        return self.__current_song

    @current_song.setter
    def current_song(self, song_path):
        self.__current_song = song_path

    def next_song(self):
        if self.__playlist:
            self.__playlist.pop(0)
            try:
                self.current_song = self.playlist[0]
            except IndexError:
                self.__current_song = None
                raise PlaylistException("Playlist is empty")
        else:
            self.__current_song = None
