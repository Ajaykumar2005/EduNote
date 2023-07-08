from flask import Flask, render_template, request, send_from_directory,redirect,url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', file_list=file_list)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
    return 'Upload successful!'

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Define a list to store registered users
users = []


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get user input from the signup form
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        if '@'  in email:
            users.append({'username': username, 'password': password,'email':email})
# Store the user data in the list (You can modify this to store in a database)
        
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from the login form
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the registered users list
        for user in users:
            if user['email'] == email and user['password'] == password:
               
               return redirect(url_for('index'))

        return 'Invalid username or password'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

