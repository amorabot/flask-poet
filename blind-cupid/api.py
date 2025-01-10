from flask import Flask
from routes import routes
from model.user import user_repository

app = Flask(__name__)

@app.route('/')
def serve_root():
    return app.send_static_file('index.html')


@app.route('/template/<username>')
def create_template(username:str):
    print(f'{username} requested the creation of template users.')
    user_repository.create_template_users()
    return "Success!",200

#Test route!
@app.route('/<name>')
def my_view_func(name):
    return name


def main() -> None:
    print("Starting application...")
    routes.setup(app=app)
    app.run(debug=True)


if __name__ == "__main__":
    main()