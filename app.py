from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Python CI/CD on EC2 🚀 {datetime.datetime.utcnow().isoformat()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
