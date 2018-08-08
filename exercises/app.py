from flask import Flask, render_template
app = Flask(__name__)

#@app.route('/')
#def regester_page():
#    exersice=["pullup" , " pushup" , "musculeup" , "situp" , "planche" ]
#    return render_template(
#        "hello1.html",
#        exersice=exersice,
#        likes_same_sport=True)

@app.route('/home')
def home_page():
    return render_template(
       "hello.html")

if __name__ == '__main__':
   app.run(debug = True)