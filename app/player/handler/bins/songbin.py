# -*- coding: utf-8 -*-

import gst
import gtk


class SongBin(gst.Bin):

    def __init__(self, song_path):
        gst.Bin.__init__(self)

        self.source = gst.element_factory_make("filesrc", "file-source")
        self.decoder = gst.element_factory_make("mad", "mp3-decoder")
        self.conv = gst.element_factory_make("audioconvert", "converter")

        self.source.set_property("location", song_path)

        self.add(self.source, self.decoder, self.conv)
        gst.element_link_many(self.source, self.decoder, self.conv)

        self.src_pad = gst.GhostPad("src", self.conv.get_pad("src"))
        self.add_pad(self.src_pad)
