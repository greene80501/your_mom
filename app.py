from flask import Flask, render_template

app = Flask(__name__)

# Route for the index page
@app.route("/")
def index():
    return render_template("file1.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context=("cert.pem","key.pem"))
