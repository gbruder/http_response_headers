# http-response-headers

python script to get reponse headers from 2 URLS and display / compare.

# Requirements

* Python 2.7
* pip install requests[security]

## Python Modules

* sys
* requests[security]
* optparse

# Install

You can download the latest version clicking [here](https://github.com/gbruder/http_response_headers/archive/master.zip)

# Usage

```
$ ./response_headers_get.py 
Usage: response_headers_get.py  --url1 <URL> --url2 <URL> --verify || --noverify [-v] [-q]

Options:
  -h, --help     show this help message and exit
  --url1=URL1    first URL to get response headers for
  --url2=URL2    second URL to get response headers for
  --verify       verify the SSL certificate
  --noverify     ignore verifying the SSL certificate
  -v, --verbose
  -q, --quiet
```

# Example

```
$ ./response_headers_get.py  --url1 http://www.georgebruder.com --url2 https://georgebruder.com --verify

---------------------------------------------------------------------------------
URL:    http://www.georgebruder.com
Response Header:
    Date: Sun, 08 Apr 2018 20:44:17 GMT
    Content-Type: text/html
    Transfer-Encoding: chunked
    Connection: keep-alive
    Set-Cookie: __cfduid=d177c2e7a2e39ff124d6d251c554c6d121523220257; expires=Mon, 08-Apr-19 20:44:17 GMT; path=/; domain=.georgebruder.com; HttpOnly
    Cf-Railgun: direct (starting new WAN connection)
    Last-Modified: Sat, 07 Apr 2018 04:07:49 GMT
    Strict-Transport-Security: max-age=0
    Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
    Server: cloudflare
    CF-RAY: 4087922e7b716dd2-SJC
    Content-Encoding: gzip
---------------------------------------------------------------------------------


---------------------------------------------------------------------------------
URL:    https://georgebruder.com
Response Header:
    Date: Sun, 08 Apr 2018 20:44:17 GMT
    Content-Type: text/html
    Transfer-Encoding: chunked
    Connection: keep-alive
    Set-Cookie: __cfduid=d61eae6367a9c60fcf3a7467c26c7403f1523220257; expires=Mon, 08-Apr-19 20:44:17 GMT; path=/; domain=.georgebruder.com; HttpOnly
    Cf-Railgun: direct (starting new WAN connection)
    Last-Modified: Sat, 07 Apr 2018 04:07:49 GMT
    Strict-Transport-Security: max-age=0
    Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
    Server: cloudflare
    CF-RAY: 4087922fa92e6e50-SJC
    Content-Encoding: gzip
---------------------------------------------------------------------------------
```
