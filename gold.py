#!/usr/bin/python

import urllib, json
import argparse


troy_ounce = 31.1034768


def get_current_gold_price():
    url = "http://api.nbp.pl/api/cenyzlota"
    response = urllib.urlopen(url)
    return json.loads(response.read())[0]['cena']


def compute(params, current_gold_price):
    real_price = params['weight'] * params['fineness']/1000 * current_gold_price
    spread = (params['price'] - real_price) / real_price

    return {
        'real_price': real_price,
        'spread_price': params['price'],
        'weight': params['weight'],
        'spread': "{0:.2f}".format(spread*100) + '%',
        'gold_price_in_pln/oz': current_gold_price * troy_ounce
    }


current_gold_price = get_current_gold_price()



parser = argparse.ArgumentParser()
parser.add_argument('-weight', type=float, help='weight of coin')
parser.add_argument('-fineness', type=int, help='fineness of coin')
parser.add_argument('-price', type=float, help='required price')

args = parser.parse_args()


params = {
    'weight': args.weight,
    'fineness': args.fineness,
    'price': args.price
}

print compute(params, current_gold_price)