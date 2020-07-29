from sqlalchemy import schema, types
from sqlalchemy.engine import create_engine


def main():
    metadata = schema.MetaData()

    page_table = schema.Table('page', metadata,
                              schema.Column('id', types.Integer, primary_key=True),
                              schema.Column('name', types.Unicode(255), default=u''),
                              schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
                              schema.Column('content', types.Text(), default=u''),
                              )
    print(metadata.tables['page'] is page_table)
    for t in metadata.sorted_tables:
        print("Table name: ", t.name)
        print("t is page_table: ", t is page_table)

    for column in page_table.columns:
        print("Column Table name: ", column.type)

    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata.bind = engine

    metadata.create_all(checkfirst=True)


if __name__ == '__main__':
    main()
