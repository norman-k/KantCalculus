#!/usr/bin/env python

import cgi
import cgitb
import urllib #a python module that allows me to fetch the content from certain url's
import re #a python module that helps you look for specific instances of text in strings

cgitb.enable()

def quote(stock):
    url = 'http://finance.google.com/finance?q=' #generic url used by google finance
    snippet = re.search('id="ref_"*?.*?>(.*?)<', urllib.urlopen(url + stock).read()) #This is what google calls before outputting certain stock info. '*?' is just any text in the specified fashion
    try:
        stocks = snippet.group(1) #assigns the first matched value
    except:
        stocks = '<br>' + 'Nothing available for: ' + '<br>' + stock
    return stocks

print "Content-type: text/html\n";
print "<br>"
print "Here is Google's latest stock info: "
print "<br>"
print quote('goog')
print "<br>"
print "Here is Apple's latest stock info: "
print "<br>"
print quote('aapl')
print "<br>"
print "Here is Barclay High Yield's latest stock info: "
print "<br>"
print quote('jnk')
print "<br>"
print "Would you like to look up any stocks of your own?"
print "<br>"
print "Enter a quote: "
print '''<form action="stocks.py" method="GET">
      <input type="text" name="stocks">
      <input type="submit" value="Submit form">'''
form_data = cgi.FieldStorage()
keys = form_data.keys()
for key in keys:
    print quote(form_data[key].value)
