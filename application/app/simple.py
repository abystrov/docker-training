from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P@ssw0rd@db/visitors'
db = SQLAlchemy(app)


class Visitor(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=False)
	age = db.Column(db.String(80), unique=False)

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return '<User %r>' % self.username


db.create_all()


@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        fage = request.form['age']
        fname = request.form['name']
        user = Visitor(fage, fname)
        db.session.add(user)
        db.session.commit()
        return render_template('age.html',fage=fage,fname=fname)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
