from app.models import User
from app.db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='thisisausername', email='hello@hello.com', password='password12345'),
    User(username='hellohellohello', email='yoyoyo@yo.org', password='yayayay123'),
    User(username='googleit', email='googlit@nodont.org', password='grannyinabasket456'),
    User(username='RandyRandleson', email='notarcher@cyrilfiggis.com', password='woodhouse432'),
    User(username='iamthad', email='thadcastle@bms.com', password='imnotkevin54')
])

db.commit()
db.close()