from flask import Flask, render_template, request
from main import create_trie, spelling_bee_solver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    outer_letters = request.form['outer_letters']
    middle_letter = request.form['middle_letter'].lower()
    dictionary = request.form['dictionary']
    file = "short.txt" if dictionary == "short" else "long.txt"
    trie = create_trie(file)
    split = [l.lower() for l in outer_letters]
    answer = [w.upper() for w in spelling_bee_solver(split,trie,middle_letter)]
    return render_template("result.html",words=answer)

if __name__ == '__main__':
    app.run(port = 8080, debug=True)