from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello():
    return "Hello & Welcome Python-Flask and Docker!"

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
