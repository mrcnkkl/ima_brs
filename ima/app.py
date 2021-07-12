from flask import Flask


app = Flask(__name__)


def create_app():
    return app


def main():
    create_app().run(debug=True)


if __name__ == "__main__":
    main()
