#!/usr/bin/python

import json
import requests


class GitHub(object):

  __API_URL = "https://api.github.com/"

  def __init__(self, client_id, client_secret):
    self.client_id = client_id
    self.client_secret = client_secret


  def get_user_info(self, access_token):
    if not access_token:
      return {}
    headers = self._prepare_headers()
    url = self.__API_URL + "user"

    params = {"access_token": access_token}

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
      print "response code is %d" % response.status_code
      return {}

    result = response.json()
    return result
  
  def _prepare_headers(self):
    return {"Accept": "application/json"}


class GitHubAuthenticator(object):
    """ Class provides OAuth authentization via GitHub API"""

    def __init__(self, client_id, client_secret, access_token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token_url = access_token_url

    def retrieve_access_token(self, code):
        """ 
        Method retrieves access token to GitHub API
        for provided code.

        @param code: code sent by GitHub after user granted
         access privileges to application
        @type code: str
        @return: access token, that can be used to 
          access GitHub profile of user
        @rtype: str| None
        """

        if not code:
            #TODO raise exception here
            return ""
    
        params = {"client_id": self.client_id,
                  "client_secret": self.client_secret,
                  "code": code }
        paramsJson = json.dumps(params)

        headers = {"Content-Type": "application/json",
                   "Accept": "application/json" }

        access_response = requests.post(self.access_token_url,
            data=paramsJson, headers=headers)
        if access_response.status_code != 200:
            #TODO raise exception
            return ""

        respondJson = access_response.json()
        return respondJson["access_token"]
