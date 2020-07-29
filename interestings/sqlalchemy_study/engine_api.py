from sqlalchemy import create_engine, text


def main():
    engine = create_engine('sqlite:///:memory:', echo=True)
    connection = engine.connect()  # 这里是从连接池取一个连接
    connection.execute(
        """
        CREATE TABLE users (
            username VARCHAR PRIMARY KEY,
            password VARCHAR NOT NULL
        );
        """
    )
    connection.execute(
        # 推荐使用text封装sql, 参数须以:号引出
        text("""
        INSERT INTO users (username, password) VALUES (:username, :password);
        """),
        {'username': "foo", 'password': "bar"}
    )
    result = connection.execute("SELECT * FROM users")  # ResultProxy
    print(result.rowcount)  # 最近一次 execute() 创建或影响的行数, update和insert才会有>0
    print(result.keys())  # 结果包含的列
    first_row = result.fetchall()[0]
    print(first_row)
    print(first_row.password)
    print(result.fetchall())
    print('*' * 10)
    for row in result:
        print("username:", row['username'])
    connection.close()


if __name__ == '__main__':
    main()
