class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):  #@property creates an illusion that a method seems to be a property [encapsulation]
        return 10 * self._value

    @ten_value.setter  #method.setter , we can change the value of the respective getter
    def ten_value(self, newvalue):
        self._value = newvalue/10


obj = MyClass(20)
obj.show()
obj.ten_value = 89
print(obj.ten_value)
print(obj._value)