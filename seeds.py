from app.models import User, Post
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

db.add_all([
    Post(title='Donec posuere metus vitae ipsum', post_url='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', user_id=1),
    Post(title='Morbi non quam nec dui luctus rutrum', post_url='https://nasa.gov/donec.json', user_id=1),
    Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', post_url='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', user_id=2),
    Post(title='Nunc purus', post_url='http://desdev.cn/enim/blandit/mi.jpg', user_id=3),
    Post(title='Pellentesque eget nunc', post_url='http://google.ca/nam/nulla/integer.aspx', user_id=4)
])
db.commit()

db.close()