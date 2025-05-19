import os

from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder="src")

posts = [
    {'title': 'Don Chisciotte della Mancia', 'author': 'Miguel de Cervantes'},
    {'title': 'A Tale of Two Cities', 'author': 'Charles Dickens'},
    {'title': 'Il Signore degli Anelli', 'author': 'J.R.R. Tolkien'},
    {'title': 'Il Piccolo Principe', 'author': 'Antoine de Saint-Exupéry'},
    {'title': 'Harry Potter e la Pietra Filosofale', 'author': 'J.K. Rowling'}
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

@app.route
def serve_index():
    return send_file('index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
