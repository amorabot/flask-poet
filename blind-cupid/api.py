from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def serve_root():
    return app.send_static_file('index.html')




if __name__ == "__main__":
    app.run(debug=True)