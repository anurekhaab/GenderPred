from flask import Flask
from app1 import views

app1 = Flask(__name__)

# url
app1.add_url_rule('/base','base',views.base)
app1.add_url_rule('/','index',views.index)
app1.add_url_rule('/faceapp','faceapp',views.faceapp)
app1.add_url_rule('/faceapp/gender','gender',views.gender,methods=['GET','POST'])
# 
if __name__ == "__main__":
    app1.run(debug=True)