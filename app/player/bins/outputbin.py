# -*- coding: utf-8 -*-

import gst


class AlsaOutputBin(gst.Bin):

    def __init__(self):
        gst.Bin.__init__(self)

        self.sink = gst.element_factory_make("autoaudiosink", "std-output")

        self.add(self.sink)

        self.add_pad(gst.GhostPad("sink", self.sink.get_pad("sink")))