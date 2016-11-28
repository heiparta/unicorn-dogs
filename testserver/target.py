#!/usr/bin/env python
"""
Client which receives the requests

Args:
    API Token
    API Base (https://...)

"""
from flask import Flask, request
import logging
import argparse
import urllib2
import os

# logging.basicConfig(level=logging.DEBUG)

# parsing arguments
PARSER = argparse.ArgumentParser(description='Client message processor')
PARSER.add_argument('API_token', help="the individual API token given to your team")
PARSER.add_argument('API_base', help="the base URL for the game API")

ARGS = PARSER.parse_args()

# defining global vars
MESSAGES = {} # A dictionary that contains message parts
API_BASE = ARGS.API_base
# 'https://csm45mnow5.execute-api.us-west-2.amazonaws.com/dev'

APP = Flask(__name__)

# creating flask route for type argument
@APP.route('/<id>', methods=['GET', 'POST'])
def main_handler(id):
    """
    main routing for requests
    """
    print(id)
    return 'OK'

if __name__ == "__main__":

    # By default, we disable threading for "debugging" purposes.
    # This will cause the app to block requests, which means that you miss out on some points,
    # and fail ALB healthchecks, but whatever I know I'm getting fired on Friday.
    APP.run(host="0.0.0.0", port=os.environ.get("APP_PORT", "80"))

    # Use this to enable threading:
    # APP.run(host="0.0.0.0", port="80", threaded=True)
