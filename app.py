from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample data for the Membership page
members = [
    {"name": "John Doe", "membership_type": "Gold", "expires": "2025-12-01"},
    {"name": "Jane Smith", "membership_type": "Silver", "expires": "2024-06-15"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate credentials (for now, just redirecting to the membership page)
        return redirect(url_for('membership'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Save the new user to database (not implemented here)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/membership')
def membership():
    return render_template('membership.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
