class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class variable: {cls.class_variable}")

# 使用类方法，不需要创建实例
MyClass.class_method()