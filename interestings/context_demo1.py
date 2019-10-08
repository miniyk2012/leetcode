from contextlib import contextmanager


class Connction:

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        print("close conn")

    def get_cursor(self):
        return Cursor()


class Cursor:

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        print("close cursor")


@contextmanager
def outer():
    conn = Connction()
    yield conn
    conn.close()


@contextmanager
def inner():
    with outer() as conn:
        cursor = conn.get_cursor()
        yield cursor
        cursor.close()


if __name__ == '__main__':
    with inner() as cursor:
        print("trans")

    print()

    with Connction() as conn, conn.get_cursor() as cursor:
        print("trans")
