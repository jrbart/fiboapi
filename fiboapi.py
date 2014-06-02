import web

urls = ( "/",          "index", 
         "/fibo/(.*)", "fibo",  )

class index:
    def GET(self):
        return 1

class fibo:
    def GET(self,val):
        return 0

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
