from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from run_model import complete_text

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Asdf1234@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xwbxfspqsufoaw:20bc5c82140ec5907d074faf606aa125fe674daf844e5e31b871e74dd649742e@ec2-184-72-236-57.compute-1.amazonaws.com:5432/denggob0t61pq4'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class TextGen(db.Model):
#     __tablename__ = 'textgen'
#     id = db.Column(db.Integer, primary_key=True)
#     style = db.Column(db.String(200))
#     start_string = db.Column(db.String(200))
#     length = db.Column(db.Integer)
#     variability = db.Column(db.Float)
#     quote = db.Column(db.Text())

#     def __init__(self, style, start_string, length, variability, quote):
#         self.style = style
#         self.start_string = start_string
#         self.length = length
#         self.variability = variability
#         self.quote = quote

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        style = request.form['style']
        start_string = request.form['start_string']
        length = int(request.form['length'])
        variability = float(request.form['variability'])
        if style == '' or start_string == '':
            return render_template('index.html', message='Please enter required fields')
        else:
            quote = complete_text(text=start_string, n_chars=length, temperature=variability, model_name=style)
            # data = TextGen(style, start_string, length, variability, quote)
            # db.session.add(data)
            # db.session.commit()
            # send_mail(style, start_string, length, variability)
            return render_template('success.html', message=quote)
        # else:
        #     return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()