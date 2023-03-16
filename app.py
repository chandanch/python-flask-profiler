from flask import Flask
from time import sleep
from werkzeug.middleware.profiler import ProfilerMiddleware


app = Flask(__name__)
app.wsgi_app = ProfilerMiddleware(
    app.wsgi_app, restrictions=[30], profile_dir="profiler"
)


def get_data():
    sleep(2)
    return "Data"


@app.route("/healthcheck", methods=["GET"])
def health_check():
    print("health check")
    get_data()
    return {"status": "OK", "message": "Success"}


@app.route("/products", methods=["GET"])
def get_products():
    sleep(3)
    return ["Namer", "erer", "erere"]


if __name__ == "__main__":
    app.run(port=5000, debug=True)
