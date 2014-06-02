import web
import json
from mymath.fibo import *

urls = ( "/",          "index", 
         "/fibo/(.*)", "myfibo",  )

class index:
    def GET(self):
        return 1

class myfibo:
    def GET(self,val):
        web.header('Content-Type', 'application/json')
        try:
            res = fibo(int(val))
        except RangeError:
            raise web.notfound("Exception: RangeError")
        return json.dumps(res)

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
