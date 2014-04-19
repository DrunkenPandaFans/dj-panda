# -*- coding: utf-8 -*-

import gtk
import gst
import gobject

import logging

from bins.silencebin import SilenceBin
from bins.songbin import SongBin


class InputHandler:
    """
    Class to handle link and unlink song bins
    """

    def __init__(self,player):
        self.player = player

    """
    Method creates song bin and links them into pipeline. Then unlinks silence bin
    """
    def link(self,song_path):
        #TODO aktualizovat po uprave playlistu
        self.player.song_bin = SongBin(song_path)

        self.player.pipeline.add(self.player.song_bin)
        self.player.adder_song_sink = self.player.adder.get_request_pad("sink%d")

        self.player.song_bin.get_pad("src").link(self.player.adder_song_sink)
        self.player.song_bin.set_state(gst.STATE_PLAYING)

        self._unlink_silence()

    """
    Method links silence bin and remove song bin from pipeline
    """
    def unlink(self):
        self._link_silence()

        self.player.song_bin.set_state(gst.STATE_NULL)

        self.player.song_bin.get_pad("src").unlink(self.player.adder_song_sink)
        self.player.pipeline.remove(self.player.song_bin)

        self.player.song_bin = None
        self.player.adder_song_sink = None

    """
    Method creates silence bin and links them into pipeline.
    """
    def _link_silence(self):
        if self.player.adder_silence_sink:
            pass

        self.player.silence_bin = SilenceBin()
        self.player.pipeline.add(self.player.silence_bin)

        self.player.adder_silence_sink = self.player.adder.get_request_pad("sink%d")

        self.player.silence_bin.get_pad("src").link(self.player.adder_silence_sink)
        self.player.silence_bin.set_state(gst.STATE_PLAYING)

        return True

    """
    Method unlinks silence bin
    """
    def _unlink_silence(self):
        if not self.player.adder_silence_sink:
            pass

        self.player.silence_bin.set_state(gst.STATE_NULL)

        self.player.silence_bin.get_pad("src").unlink(self.player.adder_silence_sink)
        self.player.pipeline.remove(self.player.silence_bin)

        self.player.silence_bin = None
        self.player.adder_silence_sink = None

