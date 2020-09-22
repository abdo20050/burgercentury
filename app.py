from flask import *
import pyrebase
config={
    "apiKey": "AIzaSyBIpdfSBXrKFKCOMqMIlNJQ5qfVBBzmudI",
    "authDomain": "burgersession-e7d00.firebaseapp.com",
    "databaseURL": "https://burgersession-e7d00.firebaseio.com",
    "projectId": "burgersession-e7d00",
    "storageBucket": "burgersession-e7d00.appspot.com",
    "messagingSenderId": "77896476797",
    "appId": "1:77896476797:web:76da0b8d8e5f9f55806914",
    "measurementId": "G-C1L6PS8PWM"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
users= db.child("names").child("name").get()
#db.child("names").push({"name":"abdo"})
#db.child("names").child("name").update({"name":"fatouh"})
#db.child("users").child("Morty").set(data)

app = Flask(__name__)

@app.route('/', methods=['GET','Post'])
def index():
    if request.method=='POST':
        city=request.form['city']
        phone=request.form['phone']
        lastNum=request.form['last_numbers']
        name=request.form['Name']
        if lastNum=="" or phone== "" or name=="":
            return render_template("index.html",ww="أدخل جميع البيانات")
        if len(lastNum)>2:
            return render_template("index.html",ww="أدخل أخر رقمين بس من هويتك يالحبيب")
        if int(lastNum)>90:
            return render_template("index.html",ww="والله الله يعينك... انطرلك {} سنوات وبعدها فكر في العرض".format(int(lastNum)-90))
        db.child(city).child("nums").child(lastNum).child(phone).set("{}: {}".format(name,phone))
        listNum = db.child(city).child("nums").get()
        
        finalNums = getList(lastNum,listNum)
        if finalNums== []:
            return render_template("index.html",ww="والله مافي والعذر والسموحة.. اصبر شوي ")
        return render_template("index.html",t=finalNums,ww="أرقام الي يكملوك :)")
    return render_template("index.html")

def getList(lastNum,lists):
    x = int(lastNum)%100
    finalNames =[]
    for e in lists.each():
        if int(e.key())+x==90:
            finalNames.extend(list(e.val().values()))
    return finalNames

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

