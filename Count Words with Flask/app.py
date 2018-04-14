from flask import Flask, render_template, request

app = Flask(__name__)
guesses = ['Python', 'Java', 'C']
lang = 'Python'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess' , methods = ['GET', 'POST'])
def guess():
    return render_template('guess.html', disp=None, outdict = None)

@app.route('/calc', methods = ['POST'])
def calc():
    indata = request.form['indata']
    outdict = dict()
    for each in indata:
        if each in outdict:
            outdict[each] = outdict[each] + 1
        else:
            outdict[each] = 1
    return render_template('guess.html', disp=1, outdict = outdict)






if __name__ == '__main__':
    app.run(debug=True)
