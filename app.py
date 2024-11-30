from flask import Flask, request, render_template, make_response, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def index():
    analytics = request.cookies.get('cookie_analytics') == 'true'
    marketing = request.cookies.get('cookie_marketing') == 'true'
    functional = request.cookies.get('cookie_functional') == 'true'

    return render_template('index.html', analytics=analytics, marketing=marketing, functional=functional)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route('/consent', methods=['GET', 'POST'])
def consent():
    if request.method == 'POST':
        analytics = 'true' if request.form.get('cookie_analytics') else 'false'
        marketing = 'true' if request.form.get('cookie_marketing') else 'false'
        functional = 'true' if request.form.get('cookie_functional') else 'false'

        response = make_response(redirect(url_for('index')))
        response.set_cookie('cookie_analytics', analytics, max_age=86400, httponly=True)
        response.set_cookie('cookie_marketing', marketing, max_age=86400, httponly=True)
        response.set_cookie('cookie_functional', functional, max_age=86400, httponly=True)

        flash("Tus preferencias de cookies han sido guardadas.")
        return response

    analytics = request.cookies.get('cookie_analytics') == 'true'
    marketing = request.cookies.get('cookie_marketing') == 'true'
    functional = request.cookies.get('cookie_functional') == 'true'

    return render_template('consent.html', analytics=analytics, marketing=marketing, functional=functional)

if __name__ == '__main__':
    app.run(debug=True)
