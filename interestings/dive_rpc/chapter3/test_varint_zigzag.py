from interestings.dive_rpc.chapter3.varint import VarInt
from interestings.dive_rpc.chapter3.zigzag import ZigZag


class TestVarInt:
    @staticmethod
    def test_encode():
        assert VarInt.encode(0).hex() == '00'
        assert VarInt.encode(127).hex() == '7f'
        assert VarInt.encode(256).hex() == '8002'
        assert VarInt.encode(500).hex() == 'f403'
        assert VarInt.encode(133979).hex() == 'db9608'

    @staticmethod
    def test_decode():
        assert VarInt.decode(bytes.fromhex('00')) == 0
        assert VarInt.decode(bytes.fromhex('7f')) == 127
        assert VarInt.decode(bytes.fromhex('8002')) == 256
        assert VarInt.decode(bytes.fromhex('f403')) == 500
        assert VarInt.decode(bytes.fromhex('db9608')) == 133979


class TestZigZag:
    def test_encode(self):
        assert ZigZag.encode(157) == VarInt.encode(314)
        assert ZigZag.encode(-250) == VarInt.encode(499)
        assert ZigZag.encode(0) == VarInt.encode(0)

    def test_decode(self):
        bytes_value = VarInt.encode(500)
        assert ZigZag.decode(bytes_value) == 250

        bytes_value = VarInt.encode(499)
        assert ZigZag.decode(bytes_value) == -250

        bytes_value = VarInt.encode(0)
        assert ZigZag.decode(bytes_value) == 0
