This was a coding test given to me pre-interview.

I was supposed to ask if I had any questions, but
the definition of the task was clear enough.  However
I was marked down because I did not ask how I was
supposed to deploy this code into a production
environment and my directions to pull it from git
and start it were not sufficient.

I don't think it would have been avery good fit anyways
since they were very suprised at how many tests I 
had written, even though I plainly list on my resume
that I wouls prefer working in an environment open
to TDD.  It also would explain why their production
code seemed to have an unusual number of problems
everytime they launched a new feature.


Fibonacci API

Service runs on port 8080

Requests take the form of http://server:8080/fibo/<n>
where <n> is the number of terms you would like to 
have returned.

Invalid requests return "404 Not Found"

Service may be started by pulling repository into
destination directory and running:

    python fiboapi.py 2>&1 >/dev/null

Service is WSGI and may be installed under a HTTP
server such as nginx or Apache, or may be run as
standalone as above.

Depends on Python web and json modules.
