import requests as req



isbn_number = '9785171184841'
h = {'Authorization': API_ID}
resp = req.get("https://api2.isbndb.com/book/{}".format(isbn_number), headers=h)
print(resp.json())