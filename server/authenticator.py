#!/usr/bin python3


# Python Authentication using JsonWebTokens

from tornado.ioloop import IOLoop
from tornado import gen
import tormysql
import jwt
import json

with open('cred.json', 'r') as f:
    cred = json.load(f)

pool = tormysql.ConnectionPool(
    max_connections = 20, #max open connections
    idle_seconds = 7200, #conntion idle timeout time, 0 is not timeout
    wait_connection_timeout = 3, #wait connection timeout
    host = cred['host'],
    user = cred['user'],
    passwd = cred['passwd'],
    db = cred['db'],
    charset = "utf8"
)


@gen.coroutine
def test():
    with (yield pool.Connection()) as conn:
        try:
            with conn.cursor() as cursor:
                yield cursor.execute("INSERT INTO test(id) VALUES(1)")
        except:
            yield conn.rollback()
        else:
            yield conn.commit()

        with conn.cursor() as cursor:
            yield cursor.execute("SELECT * FROM actor limit 10")
            datas = cursor.fetchall()

    print(datas)

    yield pool.close()



    # def get(self):
    #     # cur = self.conn.cursor()
    #     print( dir( self.conn ))
    #     # cur.execute('select * from actor')
    #     # for row in cur:
    #     #     results.append( row )
    #     # return results 
        


# class AuthHandler():

#     def get(self):
#         self.write('Auth!!')
#         self.finish()

#     def post(self):
#         data = json.loads(self.request.body)
#         try:
#             login = data["username"]
#             password = data["password"]
#         except:
#             self.set_status(403)
#             return

#         if password:
#             query = "SELECT id, login FROM user WHERE login = %s AND password = SHA1(%s)"
#             result = self.db.get(query, login, password)

#         if result is not None and result.id is not None:
#             dataToken = {"id": result.id, "login": result.login}
#             token = jwt.encode(dataToken, "nyxjs", algorithm='HS256')
#             status = True
#             res = result
#         else:
#             token = None
#             status = False
#             res = "Invalid Username or Password."

#         self.write({"data": res, "result": status, "token": token})
#         self.finish()


if __name__ == '__main__':
    ioloop = IOLoop.instance()
    ioloop.run_sync(test)


    