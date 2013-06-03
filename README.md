dj-panda
========

Server for sharing, listening and freaking out about music.

Where is actual source?
-----------------------

Well, sad thing is there is none yet. We plan to start hack on this during summer.
But we thought we publish README now.

Who have come up with this awesome thing?
-----------------------------------------

We actually didn't come up with this briliant idea. But we stole it from [Zach Holman](https://github.com/holman) and other GitHub folks. They built very similar thing as their 
free time hacking project and open-sourced it [here](https://github.com/play/play).
So go and check them out.

What is this?
-------------
This is your own music streaming server for your home, work, school radio or whenever you want.
Well, we probably wouldn't use it as school radio, but you' ve got idea. :)

We use VLC to play music on server and libvlc binding for controlling player via REST api.
We use GitHub organizations API and OAuth for authentication.

In future we would like to use Pusher for notifications and other useful stuff.

Why are you doing this, then?
-----------------------------

Problem is, they wrote it for Apple Mini and we don't have Apple machine.
So we decided to write our own for Linux. And we also wanted to learn Python and other awesome stuff.

Who the hell are we?
--------------------

We are bunch of friends, who study at Brno, Czech Republic. Our first app was school project
called [Drunken Panda](https://drunkenpanda-iref.rhcloud.com). I know very cool name. :)
It is simple (so far) app about beer. And after that we decided to work on other fun projects together and this is one of them.

And you can quite often meet us in different pubs around town.

How to set it up?
-----------------

Right now, there is not much to set up. But as projects grows up, we will try to add all 
configuration stuff to `script/bootstrap`. So you just run this script and you are good to go.

How to contribute?
------------------

Just sent us pull request or create issue.

@DrunkenPandaFans