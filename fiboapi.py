import web
import json

urls = ( "/",          "index", 
         "/fibo/(.*)", "fibo",  )

class index:
    def GET(self):
        return 1

class fibo:
    def GET(self,val):
        web.header('Content-Type', 'application/json')
        return json.dumps([0])

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
