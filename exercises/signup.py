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
    def check(self):
        try:
            self.cursor.execute("""SELECT * FROM user_detail """)
            results = self.cursor.fetchall()
            for i in range(0,len(results)):
                if self.name in results[i]:
                    fun.exiting_user(self.name)
                    return False
            return True
        except:
            fun.failure()
        
    def insert(self,name,pswd):
        self.name=name
        self.pswd=pswd
        if self.check():
            try:
                self.cursor.execute("""INSERT INTO user_detail(USER_NAME,PASSWORD) 
                VALUES (%s,%s)""",(name,pswd))
                self.db.commit()
                fun.success(name)
                return 
            except:
                self.db.rollback()
        
    def close_dp(self):
        self.db.close()

form=cgi.FieldStorage()
userName=form.getvalue("userName")
password=form.getvalue("Pwd")
password1=form.getvalue("Pwd1")
if password != password1:
    fun.failure("password can't match")
else:
    my_login=Login_db()
    my_login.insert(userName,password)    
    my_login.close_dp()  