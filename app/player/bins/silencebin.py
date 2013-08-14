# -*- coding: utf-8 -*-

import gst


class SilenceBin(gst.Bin):

    def __init__(self):
        gst.Bin.__init__(self)

        self.silencesrc = gst.element_factory_make("audiotestsrc", "silencesrc")
        self.silenceconv = gst.element_factory_make("audioconvert", "silenceconv")

        self.silencesrc.set_property("wave", 4)

        self.add(self.silencesrc, self.silenceconv)
        gst.element_link_many(self.silencesrc, self.silenceconv)

        silence_src = gst.GhostPad("src", self.silenceconv.get_pad("src"))
        self.add_pad(silence_src)