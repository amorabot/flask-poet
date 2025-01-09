from flask import Flask
from routes import routes

app = Flask(__name__)

@app.route('/')
def serve_root():
    return app.send_static_file('index.html')


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