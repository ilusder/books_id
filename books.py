import time

import requests as req
from config import API_ID
import csv
import json

books = []

with open('books.list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        place = row['place'] if row['place'] != "" else place
        row_n = row['row'] if row['row'] != "" else row_n
        book = {'place': place,
                'row': row_n,
                'ibsn': row['ibsn']}


        h = {'Authorization': API_ID}
        resp = req.get("https://api2.isbndb.com/book/{}".format(row['ibsn']), headers=h)
        resp_json = resp.json()
        book["authors"] = \
            resp_json['book']['authors'][0] if 'book' in resp_json \
                                               and 'authors' in resp_json['book'] \
                                               and len(resp_json['book']['authors']) else ""
        book["title"] = resp_json['book']['title'] if 'book' in resp_json else ""
        books.append(book)
        time.sleep(1)

with open('out.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=book.keys())
    writer.writeheader()
    writer.writerows(books)


