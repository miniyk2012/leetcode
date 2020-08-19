from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy import select

metadata = MetaData()
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

artist = Table('artist', metadata, autoload=True, autoload_with=engine)
album = Table('album', metadata, autoload=True, autoload_with=engine)

if __name__ == '__main__':
    print(album.foreign_keys)
    print(metadata.tables['artist'] is artist)
    print(metadata.tables['album'])
    print(artist.columns.keys())

    s = select([artist]).limit(10)
    print(engine.execute(s).fetchall())
