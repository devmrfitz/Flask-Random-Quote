from flask import Flask, render_template, url_for, request
import requests
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))

@app.route('/', methods = ['GET'])
def random_quote():
    if request.method == 'GET':
        quote = requests.get('https://zenquotes.io/api/random/')
        quote_dict = quote.json()[0]
        quote_text = quote_dict['q']
        quote_author = quote_dict['a']
        return render_template('index.html', text = quote_text, author = quote_author)
    return render_template('index.html', text = '', author = '')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

