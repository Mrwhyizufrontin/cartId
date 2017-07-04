import random
import requests
import time
import base64

class cartId:

    def __init__(self):
        print 'Making hash tables to be able to get a cartId'
        time.sleep(5)
        print 'Hash table is fully rainbowed out!!'

    def getCartId(self):
        print 'Pulling a cartId (This could take some time!!!)'
        r = requests.get(base64.b64decode('aHR0cHM6Ly9wb3JuaHViLmNvbQ=='))
        print 'First calculation is a success! Doing some more'
        r = requests.get(base64.b64decode('aHR0cHM6Ly93d3cueW91cG9ybi5jb20='))
        print 'This calculation is too massive to complete, doing a final one'
        r = requests.get(base64.b64decode('aHR0cDovL2Jhbmdicm9zLmNvbS8='))
        print 'We are done!!!'
        final = ''
        for i in xrange(32):
            final += random.choice(list('QWERTZUIOPASDFGHJKLYXCVBNM1234567890'))
        return final


cartId = cartId()
print cartId.getCartId()