# -*- coding: utf-8 -*-
import gst
import gtk
import gobject

import logging

from playlist import *
from bins.sourcebin import SourceBin
from bins.outputbin import OutputBin
from bins.silencebin import SilenceBin


class Player:

    def __init__(self):
        #pozriet sa na toto este
        self.caps = gst.caps_from_string("audio/x-raw-int, channels=2, rate=44100, width=16, depth=16")

        self.playlist = Playlist()

        self.pipeline = gst.Pipeline("player")
        self.status = None
        self.now_playing = None

        #create adder and tee
        self.adder = gst.element_factory_make("adder", "adder")
        self.__adder_sink = None
        self.tee = gst.element_factory_make("tee", "tee")

        self.pipeline.add(self.adder, self.tee)

        adder_src = self.adder.get_pad("src")
        adder_src.link(self.tee.get_pad("sink"))

        outputbin = OutputBin()
        self.pipeline.add(outputbin)
        tee_src = self.tee.get_request_pad("src%d")
        tee_src.link(outputbin.get_pad("sink"))

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.on_message)

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

        self.status = "Streaming"

        return True

    def stream_off(self):
        #nastavit STATE_NULL a unlinknut vsetky bins
        self.pipeline.set_state(gst.STATE_NULL)

    def play(self):
        if not self.now_playing:
            if self.now_playing == self.playlist.current_song:
                logging.warning("Player::play(): Song is Playing")
                return False

        if not self.link():
            logging.warning("Player::play(): Source was not linked")
            return False

        self.pipeline.set_state(gst.STATE_PLAYING)

        return True

    def play_next(self):
        try:
            self.playlist.next_song()

            if not self.play():
                logging.warning("Player::play_next(): Could not play next song")
                return False

            return True

        except PlaylistException as err:
            print(err)
            return False

    def play_song_at_index(self, i):
        try:
            self.playlist.set_current_song_at_index(i)

            if not self.play():
                logging.warning("Player::play_song_at_index(): Could not play song")
                return False

            return True

        except EmptySongPathException as err:
            print(err)
            return False

    def play_song(self, song):
        try:
            self.playlist.add_song_at_top(song)

            if not self.play():
                logging.warning("Player::play_song(): Could not play song")
                return False

            return True

        except EmptySongPathException as err:
            print(err)
            return False

    def on_message(self, bus, message):
        if message.type is gst.MESSAGE_EOS:
            if not self.play_next():
                logging.warning("Player::on_message(): Could not play next song")

                self.unlink()

                return False

            return True

    def link(self):
        if self.__adder_sink:
            if not self.unlink():
                logging.warning("Player::link(): Unlink failed")
                return False

        if not self.playlist.current_song:
            logging.warning("Player::link(): Current song is None")
            return False

        self.pipeline.set_state(gst.STATE_NULL)
        self.song_source = SourceBin(self.playlist.current_song)
        print(self.playlist.current_song)
        self.pipeline.add(self.song_source)

        self.__adder_sink = self.adder.get_request_pad("sink%d")
        self.song_source.get_pad("src").link(self.__adder_sink)

        self.now_playing = self.playlist.current_song

        return True

    def unlink(self):
        #self.link_silence()

        if not self.__adder_sink:
            logging.warning("Player::unlink(): Adder sink is None")
            return False

        if not self.song_source:
            logging.warning("Player::unlink(): Song source is None")
            return False

        self.song_source.set_state(gst.STATE_NULL)

        self.__adder_sink.get_parent().release_request_pad(self.__adder_sink)
        self.song_source.get_pad("src").unlink(self.__adder_sink)
        self.pipeline.remove(self.song_source)

        self.__adder_sink = None
        self.now_playing = None
        self.bus = None

        return True

    def link_silence(self):
        print("link silence")
        self.silence = SilenceBin()

        self.pipeline.add(self.silence)

        self.__adder_sink_silence = self.adder.get_request_pad("sink%d")

        self.silence.get_pad("src").link(self.__adder_sink_silence)

        self.silence.set_state(gst.STATE_PLAYING)

    def unlink_silence(self):
        self.silence.set_state(gst.STATE_NULL)

        self.__adder_sink_silence.get_parent().release_request_pad(self.__adder_sink_silence)

        self.silence.get_pad("src").unlink(self.__adder_sink_silence)

        self.pipeline.remove(self.silence)