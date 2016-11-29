import argparse
import logging
from handler import Handler
import boto3
import os
import json
import time

PARSER = argparse.ArgumentParser(description='Client message processor')
PARSER.add_argument('API_token', help="the individual API token given to your team")
PARSER.add_argument('API_base', help="the base URL for the game API")

ARGS = PARSER.parse_args()
API_BASE = ARGS.API_base

logger = logging.getLogger()

QUEUE_NAME = os.environ.get('QUEUE_NAME', "unicorn-dogs-input")
sqs = boto3.resource('sqs', region_name='eu-central-1')

handler = Handler(ARGS.API_token, ARGS.API_base, logger)

class SQSPoller(object):
    def __init__(self):
        self.queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
        print self.queue

    def poll(self):
        for message in self.queue.receive_messages():
            msg = json.loads(message.body)
            print msg['Id']
            handler.process_message(msg)
            print "Handled message part"
            message.delete()
        print "poll finished"

if __name__ == "__main__":

    poller = SQSPoller()
    while True:
        poller.poll()
        time.sleep(0.1)
