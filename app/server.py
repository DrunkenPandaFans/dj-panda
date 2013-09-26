#!/usr/bin/python

from model.user import UserDAO
from util.github import GitHub, GitHubAuthenticator
from bottle import redirect, request, response, route, run
from pymongo import MongoClient

import json

@route('/login')
def login():
  url = "https://github.com/login/oauth/authorize?client_id=%s" % CONFIG['github_client_id']
  redirect(url)


@route('/login/callback')
def login_callback():
  code = request.query['code']
  token = AUTHENTICATOR.retrieve_access_token(code)
  user = GITHUB_API.get_user_info(token)
  orgs = GITHUB_API.get_user_orgs(token)
  for org in orgs:
    if org['login'] == CONFIG['github_org']:
      USER_DAO.save(user['login'], token)
      response.set_cookie('login', user['login'])
      break

  return "Hello %s!! Your access token is %s" % (user["login"], token)


def load_config():
  config_file = open('config/config.json')
  config = json.load(config_file)
  config_file.close()
  return config


def prepare_authenticator():
  client_id = CONFIG['github_client_id']
  client_secret = CONFIG['github_client_secret']
  access_url = "https://github.com/login/oauth/access_token"
  return GitHubAuthenticator(client_id, client_secret, access_url)

CONFIG = load_config()

client = MongoClient(CONFIG['mongo_url'], CONFIG['mongo_port'])

USER_DAO = UserDAO(client.test)
AUTHENTICATOR = prepare_authenticator()
GITHUB_API = GitHub(CONFIG['github_client_id'], CONFIG['github_client_secret'])
run(host='localhost', port='9080')
