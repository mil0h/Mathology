from flask import Flask, render_template

app = Flask(__name__)

COMMENTS = [
    {
        'username': 'Jack Robinson',
        'text': 'I love this app!',
        'likes': '0'
    },
    {
        'username':
        'Gbenga Sobowale',
        'age':
        '41',
        'text':
        'My daughter uses the website and has started to really enjoy maths. Props to the devs!'
    },
    {
        'username':
        'Scarlet Smith',
        'age':
        '9',
        'text':
        'Because of this website, I can now do addition and subtraction. I am so happy!'
    },
    {
        'username':
        'Snow White',
        'age':
        '18',
        'text':
        'The dwarves have loved using the fun and interactive website. I am glad I discovered it!'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', comments=COMMENTS)

@app.route("/level1")
def level1stuff():
  return render_template('level1.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

