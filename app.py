from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = b'6a0ade16e6be10bf0c04562c9112220b7c64529ade39ba2bfe18a62f1ddb2133'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
    else:
        username = None

    visit_counter = 0

    if request.cookies.get('visited'):
        visit_counter = int(request.cookies['visited'])

    response = make_response(render_template('index.html', visited=visit_counter, username=username))
    response.set_cookie('visited', str(visit_counter + 1))
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('logging.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
