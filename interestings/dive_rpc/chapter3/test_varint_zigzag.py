from interestings.dive_rpc.chapter3.varint import VarInt
from interestings.dive_rpc.chapter3.zigzag import ZigZag


class TestVarInt:
    @staticmethod
    def test_encode():
        assert VarInt.encode(0).hex() == '00'
        assert VarInt.encode(127).hex() == '7f'
        assert VarInt.encode(128).hex() == '8001'
        assert VarInt.encode(256).hex() == '8002'
        assert VarInt.encode(16382).hex() == 'fe7f'
        assert VarInt.encode(16383).hex() == 'ff7f'
        assert VarInt.encode(16384).hex() == '808001'
        assert VarInt.encode(500).hex() == 'f403'
        assert VarInt.encode(133979).hex() == 'db9608'
        assert VarInt.encode(1337).hex() == 'b90a'

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

        assert ZigZag.decode(ZigZag.encode(-250)) == -250
        assert ZigZag.decode(ZigZag.encode(500)) == 500
