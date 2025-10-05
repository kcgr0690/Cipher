from flask import Flask, render_template, request
from cipher import encode, decode

app = Flask(name)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    mode = ""
    input_text = ""
    if request.method == 'POST':
        mode = request.form.get('mode')
        input_text = request.form.get('input_text', '')
        if mode == 'encode':
            result = encode(input_text)
        elif mode == 'decode':
            result = decode(input_text)
    return render_template('index.html', result=result, mode=mode, input_text=input_text)

if name == 'main':
    app.run()