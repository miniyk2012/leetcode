from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, Boolean, ForeignKey, create_engine
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True, pool_size=20, )

Scoped_Session = scoped_session(sessionmaker(bind=engine))
Session = sessionmaker(bind=engine)
s1 = Session()
s2 = Session()
print(s1 is s2)  # False

session = Scoped_Session()
session2 = Scoped_Session()
print(session is session2)  # True
Scoped_Session.remove()
session3 = Scoped_Session()
print(session is session3)


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
               "cookie_recipe_url='{self.cookie_recipe_url}', " \
               "cookie_sku='{self.cookie_sku}', " \
               "quantity={self.quantity}, " \
               "unit_cost={self.unit_cost})".format(self=self)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "User(username='{self.username}', " \
               "email_address='{self.email_address}', " \
               "phone='{self.phone}', " \
               "password='{self.password}')".format(self=self)


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(), default=False)

    user = relationship("User", backref=backref('orders', order_by=order_id))

    def __repr__(self):
        return "Order(user_id={self.user_id}, " \
               "shipped={self.shipped})".format(self=self)


class LineItem(Base):
    __tablename__ = 'line_items'
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    order = relationship("Order", backref=backref('line_items', order_by=line_item_id))
    cookie = relationship("Cookie", uselist=False)

    def __repr__(self):
        return "LineItems(order_id={self.order_id}, " \
               "cookie_id={self.cookie_id}, " \
               "quantity={self.quantity}, " \
               "extended_cost={self.extended_cost})".format(
            self=self)


Base.metadata.create_all(engine)

"""
session.commit() 和session.flush()区别:
在SQLAlchemy中一个Session（可以看作）是一个transaction，每个操作（基本上）对应一条或多条SQL语句，
这些SQL语句需要发送到数据库服务器才能被真正执行，
而整个transaction需要commit才能真正生效，如果没提交，一旦你的程序挂了，所有未提交的事务都会被回滚到事务开始之前的状态。
"""

if __name__ == '__main__':
    cc_cookie = Cookie(cookie_name='chocolate chip',
                       cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                       cookie_sku='CC01',
                       quantity=12,
                       unit_cost=0.50)
    session.add(cc_cookie)
    session.commit()
    print(cc_cookie.cookie_id)
