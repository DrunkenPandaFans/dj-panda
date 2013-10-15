# -*- coding: utf-8 -*-

import gtk
import gst
import gobject

from bins.silencebin import SilenceBin


class InputHandler:

    def __init__(self,player):
        self.player = player

    def link(self):
        if not self.player.status:
            self._link_silence()

    def unlink(self):
        pass

    def _link_silence(self):
        if self.player.adder_silence_sink:
            return False

        self.player.silence_bin = SilenceBin()

        self.player.pipeline.add(self.silence_bin)

        self.player.adder_silence_sink = self.player.adder.get_request_pad("sink%d")

        self.player.silence_bin.get_pad("src").link(self.player.adder_silence_sink)

        self.player.silence_bin.set_state(gst.STATE_PLAYING)

        return True

    def _unlink_silence(self):
        if not self.player.adder_silence_sink:
            return False

        self.player.silence_bin.set_state(gst.STATE_NULL)

        self.player.silence_bin.get_pad("src").unlink(self.player.adder_silence_sink)
        self.player.pipeline.remove(self.player.silence_bin)

        self.player.silence_bin = None
        self.player.adder_silence_sink = None
