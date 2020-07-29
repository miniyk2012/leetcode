from sqlalchemy import select, MetaData, Table, Column, Integer, Unicode, Text, create_engine, and_, or_, not_

metadata = MetaData()

page_table = Table('page', metadata,
                   Column('id', Integer(), primary_key=True),
                   Column('name', Unicode(255), default=u''),
                   Column('title', Unicode(255), default=u'Untitled Page'),
                   Column('content', Text(), default=u''),
                   )

engine = create_engine('sqlite:///:memory:', echo=True)
metadata.create_all(engine)


def select_demo():
    connection = engine.connect()
    s = select([page_table.c.title])
    print(s)
    result = connection.execute(s)
    print(result.keys())
    for row in result:
        print(row)
    connection.close()


def condition_select():
    connection = engine.connect()
    s = select([page_table], and_(page_table.c.id <= 10, page_table.c.name.like(u't%')))
    s = s.order_by(page_table.c.title.desc(), page_table.c.id)
    result = connection.execute(s)
    print(result.fetchall())
    connection.close()


def insert_demo():
    connection = engine.connect()
    ins = page_table.insert(
        values=dict(name=u'test1', title=u'Test Page1', content=u'Some content1!')
    )
    print(ins)
    print(ins.compile().params)
    result = connection.execute(ins)
    print(result.rowcount)
    print(result.inserted_primary_key)

    # 批量插入
    connection.execute(page_table.insert(), [
        dict(name=u'ltest2', title=u'Test Page2', content=u'Some content2!'),
        dict(name=u'test3', title=u'Test Page3', content=u'Some content3!'),
    ])

    connection.close()


def main():
    print('insert')
    insert_demo()
    print('-----')
    print('select')
    select_demo()
    print('-----')
    print('condition_select')
    condition_select()


if __name__ == '__main__':
    main()
