
def http_get():
    import urllib2
    response = urllib2.urlopen('http://www.example.com')
    print(response.getcode())
    html = response.read()
    print(html)


def http_post():
    import urllib
    import urllib2

    data = urllib.urlencode({'foo': 'bar'})
    request = urllib2.Request('http://www.example.com', data)
    response = urllib2.urlopen(request)
    print(response.getcode())
    html = response.read()
    print(html)

def http_get_requests():
    import requests
    
    response = requests.get('http://www.example.com')
    print(response.status_code)
    print(response.text)

def http_post_requests():
    import requests
    
    response = requests.post('http://www.example.com', data={'foo': 'bar'})
    print(response.status_code)
    print(response.text)


#http_get()
#http_post()
http_get_requests()
http_post_requests()
