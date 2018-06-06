#!C:/Program Files/Python36/Python
print("Content-type:text/html")
print()
import cgi,cgitb
import pymysql,time
import fun

class Login_db(object):
    def __init__(self):
        self.db = pymysql.connect("127.0.0.1","giles","4011","login_info" )
        self.cursor = self.db.cursor()
    def check(self,name,pswd):
        self.name=name
        self.pswd=pswd
        try:
            self.cursor.execute("""SELECT * FROM user_detail """)
            results = self.cursor.fetchall()
            for i in range(0,len(results)):
                if self.name in results[i] and self.pswd in results[i]:
                    fun.success(self.name)
                    return
            fun.failure("No user in this name")
            time.sleep(2)
            fun.signup()
        except:
            fun.failure("wrong password")
        
    def close_dp(self):
        self.db.close()

form=cgi.FieldStorage()
userName=form.getvalue("userName")
password=form.getvalue("Pwd")
my_login=Login_db()
my_login.check(userName,password)    
my_login.close_dp()  