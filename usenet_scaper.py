# http://www.eternal-september.org/
# news.eternal-september.org Port 119
# List of Groups: http://www.eternal-september.org/hierarchies.php

# https://news.solani.org/

import nntplib
import configparser

config = configparser.ConfigParser()
config.read('usenet_server.cfg')
server_url = config['SERVER']['URL']

with nntplib.NNTP(server_url, user='Dieshe', password='tfhfnbifw') as n:
    resp, count, first, last, name = n.group('de.rec.misc')
    print('Group', name, 'has', count, 'articles.')

    

    first_article = True

    while True:

        print('------------------')

        if first_article:
            resp, number, message_id = n.stat(first)
            first_article = False
        else:
            resp, number, message_id = n.next()

        print("Article number:", number)

        resp, info = n.body(number)
        for line in info.lines:
            print(line.decode('iso-8859-1', "ignore"))

        if number >= last:
            break
