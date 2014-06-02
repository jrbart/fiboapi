Fibonacci API

Service runs on port 8080

Requests take the form of http://server:8080/fibo/<n>
where <n> is the number of terms you would like to 
have returned.

Invalid requests return "404 Not Found"

Service may be started by pulling repository into
destination directory and running:

    python fiboapi.py 2>&1 >/dev/null

Service is WSCGI and may be installed under a HTTP
server such as nginx or Apache, or may be run as
standalone as above.
