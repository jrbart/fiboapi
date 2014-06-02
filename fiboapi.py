import web
import json
from mymath.fibo import fibo

urls = ( "/",          "index", 
         "/fibo/(.*)", "myfibo",  )

class index:
    def GET(self):
        return 1

class myfibo:
    def GET(self,val):
        web.header('Content-Type', 'application/json')
        return json.dumps(fibo(int(val)))

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
