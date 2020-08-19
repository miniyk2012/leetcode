from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy import select
from sqlalchemy import ForeignKeyConstraint

metadata = MetaData()
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

artist = Table('Artist', metadata, autoload=True, autoload_with=engine)
album = Table('album', metadata, autoload=True, autoload_with=engine)

if __name__ == '__main__':
    print(album.foreign_keys)
    print(metadata.tables['Artist'] is artist)
    print(metadata.tables['album'])
    print(artist.columns.keys())

    s = select([artist]).limit(10)
    print(engine.execute(s).fetchall())
    print(album.foreign_keys)
    album.append_constraint(ForeignKeyConstraint(['ArtistId'], ['Artist.ArtistId']))
    print(album.foreign_keys)
    print(str(artist.join(album)))

    metadata.reflect(bind=engine)
    print(metadata.tables.keys())

    playlist = metadata.tables['Playlist']
    s = select([playlist]).limit(10)
    print(engine.execute(s).fetchall())
