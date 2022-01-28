from app import app, db
#Adding a shell context
from app.models import Store, Sale, Purchase, Product, User, Role, Setting

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 
            'Store': Store,
            'Sale': Sale,
            'Purchase': Purchase,
            'Product': Product,
            'User': User,
            'Role': Role,
            'Setting': Setting}
