class Test01:
    def __init__(self, text01):
        self.text01 = text01


class Test02(Test01):
    def __init__(self, text02, **kwargs):
        super().__init__(**kwargs)
        self.text02 = text02


class Test03:
    def __init__(self, text03, **kwargs):
        super().__init__(**kwargs)
        self.text03 = text03


class Test04(Test03, Test02):
    def __init__(self, text04, **kwargs):
        self.text04 = text04
        super().__init__(**kwargs)


test = Test04("test", text01="test01", text02="test02",
              text03="test03")

print(test.text04)
print(test.text01)
