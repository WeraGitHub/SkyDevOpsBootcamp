from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello from Flask!"


@app.route('/bye')
def bye_world():
    return "Goodbye!"


@app.route('/static')
def static_page():
    return """
        <html>
            <head>
                <title>Simple Static Page</title>
            </head>
            <body>
                <h1>Simple Static Page</h1>
                <p>This is a simple, static web page created using Python Flask.</p>
            </budy>
        </html>
    """


@app.route('/dynamic/<name>')
def dynamic_page(name):
    return """
        <html>
            <head>
                <title>Dynamic Page</title>
            </head>
            <body>
                <h1>Dynamic Page</h1>
                <p>Hello {}!</p>
            </budy>
        </html>
    """.format(name)


@app.route('/info/<int:age>')
def age_page(age):
    return """
        <html>
            <head>
                <title>Info Page</title>
            </head>
            <body>
                <h1>Age Page</h1>
                <p>You are {} years old.</p>
            </budy>
        </html>
    """.format(age)


if __name__ == "__main__":
    app.run()
