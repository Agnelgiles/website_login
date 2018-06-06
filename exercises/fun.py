def create_table():
    import pymysql
    db = pymysql.connect("127.0.0.1","giles","4011","login_info" )
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS USER_DETAIL")
    cursor.execute("""CREATE TABLE USER_DETAIL (USER_NAME  CHAR(10) NOT NULL,
                     PASSWORD  CHAR(10) NOT NULL,PRIMARY KEY(USER_NAME) )""")
def success(name):
    print("<html>")
    print("<head>")
    print("""<meta charset="utf-8" />""")
    print("""<link rel="icon" type="image/jpg" href="http://pappugroup.com/img/icons/pg.jpg"/>""")
    print("<title>%s</title>" %(name))
    print("<style>")
    print("""h1{border-left: 6px solid midnightblue;background-color: lightgrey;
           font-family: 'Times New Roman', Times, serif;}""")
    print("</style>")
    print("""</head><body><center><h1>welcome! %s</h1></center>
         </body></html>""" %(name))  
def signup():
    print("""<!DOCTYPE HTML><html lang="en-US"><head><title>Sign up </title>
    <link rel="icon" type="image/jpg" href="http://pappugroup.com/img/icons/pg.jpg" />
    <style>body {background-color: white;font-family: 'Times New Roman', Times, serif;}
    fieldset {background-color: #d1cec8;align-content: center;border: 8px ridge #447cd6;
    max-width: 400px;padding: 16px;}label{float: left;width: 25%; margin-right: auto;
    text-align: right;}p{font-family: 'Courier New', Courier, monospace;}h1 {color: #447cd6;
    background-color: white}</style><meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
    <body><form action="signup.py" method="post"><center><fieldset><legend><h1>Sign up</h1>
    </legend><label for="userName">User Name</label><input type="text" name="userName" />
    </p><label for="Pwd">Password</label><input type="password" name="Pwd" /></p>
    <label for="Pwd1">Re-type Password</label><input type="password" name="Pwd1" /></p>
    <p title="Log In"><input type="submit" value="sign up"></p></fieldset></center>
    </form></body></html>""")
def log_in():
    print("""<!DOCTYPE html><html lang="en-US"><head><title>Log In </title>
	<link rel="icon" type="image/jpg" href="http://pappugroup.com/img/icons/pg.jpg"/>
	<style>body {background-color:white;font-family:'Times New Roman', Times, serif;}
    fieldset {background-color: #d1cec8;align-content: center; border: 8px ridge #447cd6;
     max-width: 400px; padding:16px;}label {float:left;  width:25%; margin-right:auto; text-align:right; }
    p {font-family: 'Courier New', Courier, monospace;}h1 {color: #447cd6;background-color: white}
    </style><meta charset = "UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head><body> <form action="login.py" method="post"><center><fieldset><legend ><h1>Log In</h1></legend>
    <label for="userName">User Name</label><input type = "text" name = "userName" /></p><label for="Pwd">Password</label>
    <input type = "password" name = "Pwd" /></p><p title="Log In"><input type= "submit" value="Log In"></p>
     </fieldset></center></form></body> </html>""" )
def failure(word):
    print("""<html><head><meta charset="utf-8" />
    <link rel="icon" type="image/jpg" href="http://pappugroup.com/img/icons/pg.jpg"/>
    <title>Failure</title><style>
    h1{border-left: 6px solid midnightblue;background-color: lightgrey;
    font-family: 'Times New Roman', Times, serif;}</style></head><body><center><h1>%s!!!</h1></center>
     </body></html>""" %(word))  
def exiting_user(name):
     print("""<html><head><meta charset="utf-8" />
    <link rel="icon" type="image/jpg" href="http://pappugroup.com/img/icons/pg.jpg"/>
    <title>Failure</title><style>
    h1{border-left: 6px solid midnightblue;background-color: lightgrey;
    font-family: 'Times New Roman', Times, serif;}</style></head><body><center><h1>%s already
    exit.<br>Try another name</h1></center></body></html>"""%(name)) 