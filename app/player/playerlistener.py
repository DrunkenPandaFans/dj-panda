# -*- coding: utf-8 -*-

"""
Trieda zaistujuca komunikaciu medzi playlistom a playerom
"""
class PlayerListener:

    def __init__(self):
        self._player = None
        self._playlist = None


    def set_player(self, player):
        self._player = player

    def set_playlist(self, playlist):
        self._playlist = playlist

    def get_player(self):
        return self._player

    def get_playlist(self):
        return self._playlist

    def change_song(self):
        if self._playlist:
            self._playlist.next_song()
            if self._playlist.current_song():
                self._player.play()

    def changed_song(self):
        if self._player:
            self._player.play()

