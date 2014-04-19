# -*- coding: utf-8 -*-
import gst
import gtk
import gobject

import logging

from playlist import *
from handler.bins.outputbin import AlsaOutputBin
from handler.inputhandler import InputHandler

class Player:

    def __init__(self,listener):
        #pozriet sa na toto este
        self.caps = gst.caps_from_string("audio/x-raw-int, channels=2, rate=44100, width=16, depth=16")

        self.init(listener)

        self.adder_song_sink = None
        self.adder_silence_sink = None
        self.tee_sto_sink = None
        self.tee_stream_sink = None

    def init(self, listener):
        #vytvorime si handler, ktory ma nastarosti prilinkovanie a odlinkovanie pesnicky
        self._inputhandler = InputHandler(self)

        #ulozime si predaneho listenera, ktory zabezpecuje komunikaciu medzi playerom a playlistom
        self._listener = listener

        #vytvorime si pipeline
        self.pipeline = gst.Pipeline("player")

        #nastavime si status playera
        self.status = None

        #vytvorime si jednotlive elementy pipeline a vlozime ich do nej
        self.adder = gst.element_factory_make("adder", "adder")
        self.tee = gst.element_factory_make("tee", "tee")
        self.pipeline.add(self.adder, self.tee)

        #prepojime vstupny element s vystupnym
        adder_src = self.adder.get_pad("src")
        adder_src.link(self.tee.get_pad("sink"))

        #vytvorime vystupny bin a pripojime ho do pipeline
        outputbin = AlsaOutputBin()
        self.pipeline.add(outputbin)

        #vystupny bin prilinkujeme k vystupnemu elementu
        tee_src = self.tee.get_request_pad("src%d")
        tee_src.link(outputbin.get_pad("sink"))

        #ziskame z pipeline bus, ktory zachytava udalosti pipeline
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.on_message)

    """
    Metoda
    """
    def stream_on(self):
        st = self.pipeline.get_state()
        if st[1] == gst.STATE_PLAYING:
            logging.warning("Player::stream_on(): Pipeline's state is Playing'")
            return False

        st = self.pipeline.set_state(gst.STATE_PLAYING)
        if st == gst.STATE_CHANGE_FAILURE:
            logging.warning("Player::stream_on(): Could not change pipeline state to Playing")
            return False

        st = self.pipeline.get_state(gst.CLOCK_TIME_NONE)
        if st == gst.STATE_CHANGE_FAILURE:
            logging.warning("Player::stream_on(): Pipeline's state was not changed to Playing'")
            return False

        self.status = status.STREAMING

        return True

    def stream_off(self):
        #nastavit STATE_NULL a unlinknut vsetky bins
        self.pipeline.set_state(gst.STATE_NULL)

    def play(self, song_path):
        if self.status is status.STREAMING or self.status is status.STOPPED:
            self._inputhandler.link(song_path)
        else:
            logging.warning("Player::play(): Player has not \"Streaming\" status")

    def stop(self):
        self._inputhandler.unlink()

    def on_message(self, bus, message):
        if message.type is gst.MESSAGE_EOS:
            self._listener.change_song()

class status:
    PLAYING = "Playing"
    STREAMING = "Streaming"
    STOPPED = "Stopped"