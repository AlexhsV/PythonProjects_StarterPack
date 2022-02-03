from urllib.request import Request, urlopen
import json
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})

data = urlopen(req).read()

data = data.decode()

datajs=json.loads(data)

latest_round = list(datajs.values())[0]
print('The latest round is:', latest_round )
print("\nGive me a second...")

hex_randomness20 = ''
for i in range(20):
    round = latest_round - i
    url = "https://drand.cloudflare.com/public/{0}".format(round)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})

    data = urlopen(req).read()

    data = data.decode()

    datajs=json.loads(data)

    randomness = list(datajs.values())[1]  #getting the second value which is the randomness

    an_integer = int(randomness, 16)
    hex_randomness = hex(an_integer)

    hex_randomness20+=randomness

def entropy(string):
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy

print("\nThe entropy of the last 20 hexademical numbers combined is:",entropy(hex_randomness20))
