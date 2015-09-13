#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

from requests_oauthlib import OAuth1Session
import ujson
import unidecode

URL = "https://stream.twitter.com/1.1/statuses/filter.json"


def decode(string):
    return unidecode.unidecode(string)

def request_params(keys, language):
    parameter_keys = ','.join(keys)
    params = {
        'track': parameter_keys,
        #'language': language,
        'stall_warnings': True,
    }
    return params


def stream(consumer_key, consumer_secret, access_token, access_token_secret, 
           keys, language):

    # TODO: consider language

    keys = ','.join(keys[0].split())
    parameters = {'track': keys, 'stall_warnings': True}

    twitter = OAuth1Session(client_key=consumer_key,
                            client_secret=consumer_secret,
                            resource_owner_key=access_token,
                            resource_owner_secret=access_token_secret)

    r = twitter.post(URL, data=parameters, stream=True)

    for line in r.iter_lines():
        try:
            line = ujson.loads(line)
            print "{}\t{}\t{}".format(line['id'], decode(line['user']['name']), decode(line['text'].strip()))
        except Exception as e:
            print "\t\t\tError occurred!", e


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Streamer for Twitter', fromfile_prefix_chars='@')

    parser.add_argument('--language', default='en-US')
    parser.add_argument('--keys', nargs='+')
    parser.add_argument('--consumer-key', required=True)
    parser.add_argument('--consumer-secret', required=True)
    parser.add_argument('--access-token', required=True)
    parser.add_argument('--access-token-secret', required=True)


    args = parser.parse_args()
    stream(args.consumer_key, args.consumer_secret, args.access_token, args.access_token_secret, 
           args.keys, args.language)

