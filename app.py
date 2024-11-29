from flask import Flask, request, render_template, make_response, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "123"

@app.route('/')
def index():
    consent = request.cookies.get('cookie_consent')
    return render_template('index.html', consent=consent)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route('/consent', methods=['GET', 'POST'])
def consent():
    if request.method == 'POST':
        consent_value = request.form.get('consent')
        response = make_response(redirect(url_for('index')))
        if consent_value == "accept":
            response.set_cookie('cookie_consent', 'accepted', max_age=86400)
        elif consent_value == "reject":
            response.set_cookie('cookie_consent', 'rejected', max_age=86400)
        flash("Your preferences have been saved")
        return response
    return render_template('consent.html')

if __name__ == '__main__':
    app.run(debug=True)

