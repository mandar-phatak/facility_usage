from flask import Flask, render_template

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'my'

@app.route('/')
def helloworld():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug=True)