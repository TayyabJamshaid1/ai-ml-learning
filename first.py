class Person:
      name="Chair"

      @classmethod
      def changeNameMethod(cls,updatedName):
            cls.name=updatedName
            return cls.name


p1=Person()
print(p1.changeNameMethod("Glass"))
print(Person.name)


