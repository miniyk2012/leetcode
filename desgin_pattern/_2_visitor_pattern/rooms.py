class Room:
    def __init__(self):
        pass

    def get_name(self):
        return self.name

    def accept(self, visitor: 'Visitor'):
        pass


class KeTing(Room):
    def __init__(self):
        self.name = '客厅'

    def accept(self, visitor: 'Visitor'):
        visitor.visit_keting(self)


class ChuFang(Room):
    def __init__(self):
        self.name = '厨房'

    def accept(self, visitor: 'Visitor'):
        visitor.visit_chufang(self)


class Visitor:
    def visit_chufang(self, room: Room):
        print('吃点东西: ' + room.get_name())

    def visit_keting(self, room: Room):
        print('睡一觉: ' + room.get_name())


if __name__ == '__main__':
    rooms = [KeTing(), ChuFang()]
    visitor = Visitor()
    for room in rooms:
        room.accept(visitor)
