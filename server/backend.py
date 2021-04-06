import tornado.web
import tornado.ioloop
import json


class UploadHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # This is to prevent the cross-origin CORS issue
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        msg = {"msg": "success", "code": 200}
        self.finish(json.dumps(msg))

    def post(self):
        files = self.request.files['files']

        for f in files:
            try:
                fhandler = open(f'./uploads/{f.filename}', 'wb')
                fhandler.write(f.body)
                fhandler.close()
                msg = {"msg": "success", "code": 200}
                self.finish(json.dumps(msg))
            except Exception as e:
                msg = {"msg": "An internal error occurred", "code": 500}
                self.finish(json.dumps(msg))


class indexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # This is to prevent the cross-origin CORS issue

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        # Sending an object, this will enable sharing infomation bwteeen frontend and backend easier

        cred = {
            "fname": "Anthony",
            "lname": "Ngayo",
            "profession": "SysAdmin",
            "age": 30
        }
        cred = json.dumps(cred)
        self.finish(cred)


if __name__ == "__main__":
    app = tornado.web.Application([
        ("/api/", indexHandler),
        ("/api/upload/", UploadHandler),
    ])
    app.listen(8000)
    print("App is listening on 8000 ... ")

    tornado.ioloop.IOLoop.instance().start()
