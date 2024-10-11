from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from all origins
