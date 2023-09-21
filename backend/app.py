from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@mysql/{os.environ['MYSQL_DB']}"
db = SQLAlchemy(app)

class ClickCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/increment', methods=['POST'])
def increment_count():
    counter = ClickCounter.query.first()
    if counter is None:
        counter = ClickCounter()
        db.session.add(counter)
    counter.count += 1
    db.session.commit()
    return "OK", 200

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
