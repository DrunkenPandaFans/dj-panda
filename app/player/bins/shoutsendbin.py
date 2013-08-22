# -*- coding: utf-8 -*-

import gst


class ShoutsendBin(gst.Bin):

    def __init__(self,caps,args):
        gst.Bin.__init__(self)
        capsfilter = gst.element_factory_make("capsfilter", None)
        audioconvert = gst.element_factory_make("audioconvert", None)
        audioresample = gst.element_factory_make("audioresample", None)
        queue = gst.element_factory_make("queue", None)
        shout2send = gst.element_factory_make("shout2send", None)

        capsfilter.set_property("caps", caps)
        queue.set_property("min-threshold-buffers", 10)

        # TODO: I should do something when gethostbyname fails

        shout2send.set_property("protocol", args["protocol"])
        shout2send.set_property("ip", args["host"])
        shout2send.set_property("port", args["port"])
        shout2send.set_property("mount", args["mount"])


        if args["encoding"] == "mp3":
            lame = gst.element_factory_make("lame", None)

            if args["quality"] == None:
                lame.set_property("bitrate", args["bitrate"])
            else:
                quality = 10 - args["quality"]
                lame.set_property("quality", quality)

            self.add(capsfilter, audioconvert, audioresample, lame, queue, shout2send)
            gst.element_link_many(capsfilter, audioconvert, audioresample, lame, queue, shout2send)

        else:
            vorbisenc = gst.element_factory_make("vorbisenc", None)
            oggmux = gst.element_factory_make("oggmux", None)

            if args["quality"] == None:
                vorbisenc.set_property("bitrate", args["bitrate"])
            else:
                quality = args["quality"] / 10.0
                vorbisenc.set_property("quality", quality)

            self.add(capsfilter, audioconvert, audioresample, queue, vorbisenc, oggmux, shout2send)
            gst.element_link_many(capsfilter, audioconvert, audioresample, queue, vorbisenc, oggmux, shout2send)

        self.add_pad(gst.GhostPad("sink", capsfilter.get_pad("sink")))