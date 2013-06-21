#!/bin/bash

#
# Script to setup your ultimate jukebox.
#

echo "Welcome to DJ Panda."
echo "Playing only the best music."
echo "Sponsored by nobody. :)"
echo ""

echo "But first you have to do little bit of work."
echo ""

#
# Do some magic setup here.
#

#
# Check for python deps
#
if test ! $(which pip)
then
  echo " x You need to install pip. If you are on Ubuntu, run this:"
  echo "   easy_install install pip"
  exit
else
  echo " + Pip was found."
fi

if test ! $(which virtualenv)
then
  echo " x You need to install virtualenv. Run this:"
  echo "   pip install virtualenv"
  exit
else
  echo " + VirtualEnv found."
fi

#
# Create virtual envinroment for project
#

echo "Creating virtual environment for project"
virtualenv env
echo " + Virtual environment created in env directory"

echo "Activating virtual environment"
source env/bin/activate
echo " + Virtual environment activated"


echo "Instaling python libraries"
pip install -r requirements.txt
if [ $? != 0 ]
then
  echo " x Python libraries were not installed. Please check your access privileges"
  exit
else
  echo " + Python Libraries were installed"
fi

#
# Good job. Panda is ready to play.
#
echo "Good Job! Panda is ready."
