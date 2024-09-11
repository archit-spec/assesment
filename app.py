# app.py
from flask import Flask
from flask_graphql import GraphQLView
from database import db_session, init_db
from schema import schema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

