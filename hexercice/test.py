#!/usr/bin/python

from uuid import uuid4
from random import randint
from hashlib import sha256


mot_client = str(uuid4())
mot_server = str(uuid4())

tirage_client = randint(0, 1)
tirage_server = randint(0, 1)

def f(a, b, c):
	return sha256(' '.join([a,b,str(c)]).encode('utf8')).hexdigest()


function1 = f(mot_client, mot_server, tirage_server)
function2 = f(mot_client, mot_server, tirage_client)


print(function1)
print(function2)
