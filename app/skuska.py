# -*- coding: utf-8 -*-

from player import Player
from player.playlist import Playlist
from player.playerlistener import PlayerListener


if __name__ == "__main__":
    listener = PlayerListener()

    player = Player(listener)

    playlist = Playlist(listener)
    playlist.add_song("")
    playlist.add_song("")

    listener.set_player(player)
    listener.set_playlist(playlist)

