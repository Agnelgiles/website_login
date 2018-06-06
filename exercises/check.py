#!C:/Program Files/Python36/Python
print("Content-type:text/html")
print()
import cgi,cgitb
import fun

cgitb.enable()

form=cgi.FieldStorage()

wish=form.getvalue("wish")

if wish.lower()=="login":
    fun.log_in()
else:
    fun.signup()

