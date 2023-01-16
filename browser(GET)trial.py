from flask import Flask, request

app = Flask(__name__)

@app.route('/test')
def test():
    name = request.args.get("get_name")
    mobile =request.args.get("get_mobile")
    mail = request.args.get("get_id")
    return "This is my 1st function in browser to get {} {} {}". format(name, mobile, mail)

if __name__ == '__main__':
    app.run()