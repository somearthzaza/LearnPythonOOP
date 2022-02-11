class test01:
    def __init__(self, text01):
        self.text01 = text01


class test02(test01):
    def __init__(self, text01, text02):
        super().__init__(text01, **k)
        self.text02 = text02


class test03:
    def __init__(self, text03):
        self.text03 = text03


class test04:
    def __init__(self) -> None:
