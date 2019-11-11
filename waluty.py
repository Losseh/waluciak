#!/usr/bin/python

import urllib, json


def load_rates(currency, timespan):
    url = "http://api.nbp.pl/api/exchangerates/rates/a/" + currency + "/last/" + timespan + "/?format=json"
    response = urllib.urlopen(url)
    return json.loads(response.read())


def get_rate_value(rate):
    return rate[u'mid']


def get_rates(currency):
    rates = load_rates(currency, "100")['rates']
    pure_rates = map(get_rate_value, rates)

    current_rate = pure_rates[-1]
    avg_rate100 = sum(pure_rates) / len(pure_rates)
    avg_rate30 = sum(pure_rates[-30:]) / 30

    percent100 = 100 * (current_rate - avg_rate100) / avg_rate100
    percent100 = "{:2.2f}%".format(percent100)

    percent30 = 100 * (current_rate - avg_rate30) / avg_rate30
    percent30 = "{:2.2f}%".format(percent30)

    return {
        'current': current_rate,
        'avg100': "{:2.3f}".format(avg_rate100),
        'avg30': "{:2.3f}".format(avg_rate30),
        'rel_diff100': percent100,
        'rel_diff30': percent30,
        'currency': currency
    }


print get_rates('eur')
print get_rates('usd')
