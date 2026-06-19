from flask import Flask
from routes import main
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)