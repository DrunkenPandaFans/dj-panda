#!/bin/bash

CONFIG_FILE="config/config.json"

#
# Script to setup your ultimate jukebox.
#

echo "Welcome to DJ Panda."
echo "Playing only the best music."
echo "Sponsored by nobody. :)"
echo ""

echo "But first you have to do little bit of work."
echo ""

if [ -f $CONFIG_FILE ]
then
  echo " + Panda is already configured. You can find your configuration in $CONFIG_FILE" 
  exit 0
fi

#
# Do some magic setup here.
#

#
# Check for Mongo.
#
if test ! $(which mongodb)
then
  echo " x You need to install MongoDB. If you are on Ubuntu, run this:"
  echo "   apt-get install mongodb-10gen"
  echo " Otherwise check this site for more details: http://www.mongodb.org/downloads"
  echo ""
else
  echo " + MongoDB was found."
fi

echo "What is your Mongo login?"
read MONGO_LOGIN
echo "What is your Mongo password?"
read MONGO_PASSWORD
echo " + Mongo settings saved."


#
# Check for python deps
#
echo ""
if test ! $(which pip)
then
  echo " x You need to install pip. If you are on Ubuntu, run this:"
  echo "   apt-get install python-pip"
  exit
else
  echo " + Pip was found."
fi

echo ""
if test ! $(which virtualenv)
then
  echo " x You need to install virtualenv. Run this:"
  echo "   pip install virtualenv"
  exit
else
  echo " + VirtualEnv found."
fi


#
# You need to provide GitHub API credentials.
#
echo ""
echo "Please provide GitHub API credentials."
echo "If you do not have them. Please register application to your GitHub account"
echo "at https://github.com/settings/applications"
echo ""
echo "Your API key will be used for authentication of users"
echo ""

echo "Your GitHub client id:"
read GITHUB_CLIENT_ID

echo "Your GitHub client secret:"
read GITHUB_CLIENT_SECRET

echo "Do you want to log in users from your organization?[Y/n]"
read LOG_ORG

if [ "$LOG_ORG" = "y" ] || [ "$LOG_ORG" = "Y" ]
then 
  echo "What is name of your organization?"
  read GITHUB_ORG
fi


#
# Create virtual envinroment for project
#

echo "Creating virtual environment for project"
echo ""
virtualenv env
echo " + Virtual environment created in env directory"
echo ""

echo "Activating virtual environment"
echo ""
source env/bin/activate
echo " + Virtual environment activated"
echo ""


echo "Instaling python libraries"
pip install -r requirements.txt
if [ $? != 0 ]
then
  echo " x Python libraries were not installed. Please check your access privileges"
  exit -1
else
  echo " + Python Libraries were installed"
fi


#
# Write configuration to file
#
echo ""
echo "Saving application configuration..."

echo "{" >> $CONFIG_FILE
echo "'github_client_id': '$GITHUB_CLIENT_ID'," >> $CONFIG_FILE
echo "'github_client_secret': '$GITHUB_CLIENT_SECRET'," >> $CONFIG_FILE
echo "'github_org': '$GITHUB_ORG'," >> $CONFIG_FILE

echo "'mongo_login': '$MONGO_LOGIN'," >> $CONFIG_FILE
echo "'mongo_password': '$MONGO_PASSWORD'," >> $CONFIG_FILE
echo "'mongo_url': 'localhost',"  >> $CONFIG_FILE
echo "'mongo_port': 27017" >> $CONFIG_FILE
echo "}" >> $CONFIG_FILE

if [ $? -eq 0 ]
then
  echo ""
  echo " + Application configuration was saved to 'config/config.json"
  echo ""
else
  echo ""
  echo " x We could not write your configuration to config file :("
  exit -1
fi


#
# Good job. Panda is ready to play.
#
echo "Good Job! Panda is ready to dj."
