

app = Flask(__name__)
db = SQLAlchemy(app)

from flask_portfolio import routes
