# -*- coding: utf-8 *-*

import vlc

class Player(object):

    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(unicode('a.mp3'))
        self.player.set_media(self.media)

    def Play(self):
        if (not self.player.is_playing()):
            self.player.play()

    def Pause(self):
        if (self.player.is_playing()):
            self.player.pause()

    def Stop(self):
        if (self.player.is_playing()):
            self.player.stop()

    def getVolume(self):
        return self.player.audio_get_volume()

    def setVolume(self, volume):
        self.player.audio_set_volume(volume)



if __name__ == "__main__":
    player = Player()
    player.Play()
    #player.setVolume(500)
    #print player.getVolume()
    #print player.player.audio_get_track()

    a = 100
    while(True):
        a = a - 1
     #   print player.player.audio_get_track()
    #    player.setVolume(300)
      #  print player.getVolume()
