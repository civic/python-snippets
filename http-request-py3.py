
def http_get():
    import urllib.request
    response = urllib.request.urlopen('http://www.example.com')
    print(response.getcode())
    html = response.read()
    print(html.decode('utf-8'))


def http_post():
    import urllib.request
    import urllib.parse

    data = urllib.parse.urlencode({'foo': 'bar'}).encode('utf-8')
    request = urllib.request.Request('http://www.example.com', data)
    response = urllib.request.urlopen(request)
    print(response.getcode())
    html = response.read()
    print(html.decode('utf-8'))

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


http_get()
http_post()
http_get_requests()
http_post_requests()
