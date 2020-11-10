class Knife:
    pass


class Pistol:
    def shoot(self):
        pass


class Rifle:
    def shoot(self):
        pass


class Grenade:
    def boom(self): pass


class P2000(Pistol):
    pass


class M16(Rifle):
    pass


class Human:
    _health = 100


class Player(Human):
    _armour = 0
    _money = 1000

    _knife = None
    _pistol = None
    _rifle = None
    _grenades = []


class AbstractBuilder:
    _health = 100
    _armour = 0
    _money = 1000
    _knife = Knife()

    _rifle = None
    _grenades = []

    def armour(self, armour):
        self._armour = armour
        return self

    def pistol(self, pistol):
        self._pistol = pistol
        return self

    def rifle(self, rifle):
        self._rifle = rifle
        return self

    def grenade(self, grenade):
        assert len(self._grenades) < 3, "Available amout is exceeded"
        self._grenades.append(grenade)
        return self

    def build(self): return None


class CounterTerroristBuidler(AbstractBuilder):
    _pistol = P2000()
    _defuse_kit = None

    def defuse_kit(self, defuse_kit):
        self._defuse_kit = defuse_kit

    def build(self): return CounterTerrorist(self)


class CounterTerrorist(Player):
    _defuse_kit = None

    def __init__(self, builder):
        self._health = builder._health
        self._armour = builder._armour
        self._money = builder._money

        self._knife = builder._knife
        self._pistol = builder._pistol
        self._rifle = builder._rifle
        self._defuse_kit = builder._defuse_kit


counter_terrorist = CounterTerroristBuidler()\
    .armour(100)\
    .pistol(P2000)\
    .rifle(M16())\
    .grenade(Grenade()) \
    .grenade(Grenade()) \
    .build()

print(str(counter_terrorist))
