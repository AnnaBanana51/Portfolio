from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
    if request.method == 'POST':
        Contace_name = request.form['name']
        Email = request.form['email']
        Message = request.form['message']
    else:
        return f"this was a {request.method}" 
    


if __name__ == "__main__":
    app.run(debug=True)