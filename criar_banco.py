from fkpinterest import database, app
from fkpinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()