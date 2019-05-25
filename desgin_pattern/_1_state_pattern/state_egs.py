from __future__ import annotations
from typing import Type

class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, state: Type[ConnectionState]):
        self._state = state

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)

    def read(self):
        self._state.read(self)

    def write(self, data):
        self._state.write(self, data)


class ConnectionState:
    @staticmethod
    def close(conn):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def close(conn: Connection):
        raise RuntimeError('already closed')

    @staticmethod
    def open(conn: Connection):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def read(conn):
        raise RuntimeError('cant read')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('cant read')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def close(conn: Connection):
        conn.new_state(ClosedConnectionState)

    @staticmethod
    def open(conn):
        raise RuntimeError('already open')

    @staticmethod
    def read(conn):
        print('read success')

    @staticmethod
    def write(conn, data):
        print('write success')


if __name__ == '__main__':
    c = Connection()
    print(c._state)
    try:
        c.read()
    except RuntimeError as e:
        pass
    c.open()
    c.read()
    c.write('aa')
