from flask import Flask, views,url_for,jsonify

app = Flask(__name__)


class JSONView(views.View):
    def get_data(self):
        raise  NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(views.View):
    def dispatch_request(self):
        return {"username":'whl','password':'111111'}


app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


class LoginView(views.View):
    def dispatch_request(self):
        return 'login view'


class RegistView(views.View):
    def dispatch_request(self):
        return 'regist view'


app.add_url_rule('/login/',  view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
