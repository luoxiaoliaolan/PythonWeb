from flask import Flask, escape

app = Flask(__name__)


@app.route('/user/<username>', methods=['GET'])
def show_user(username):
    return 'User: %s' % escape(username)


if __name__ == '__main__':
    app.run()
