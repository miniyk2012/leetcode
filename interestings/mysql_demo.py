import MySQLdb as mdb
import sys

try:
    conn = mdb.connect('localhost', 'root', '123456', 'testdb')
    cursor = conn.cursor()

    cursor.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                   ("Leo afsda", "16"))
    cursor.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                   ("a afdas", "17"))
    cursor.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                   ("Leonid Leonov", "18"))

    conn.commit()

    cursor.close()
    conn.close()

except mdb.Error as e:

    conn.rollback()
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

    cursor.close()
    conn.close()