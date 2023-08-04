# BlacKrab666
# Using both self and cls

# Class definition with the use of both self and/or cls keywords/statments

class myClass:
    __version2 = 'v2.3'

    # extra work to insist that __version2 accepts only string input
    assert isinstance(__version2, str), 'Please only ensure that version is a text/string'

     # initialization of object via class constructor
    def __init__(self):
        self.__version = 'v1.2'

    # use of self keyword
    def myNormalMethod(self):
        print(self.__version)

    # use of cls keyword
    @classmethod
    def myClassMethod(cls):
        print(cls.__version2)

    # use of both self and cls keywords, self must be first being implicit and cls second being explicitly required and supplied.
    def myMethod(self, cls):
        print(self.__version)
        print(cls.__version2)

       
#------------------------------------------       
# Object creation and usage:

newObj = myClass()

newObj.myNormalMethod()

myClass.myNormalMethod(newObj)

# the object is passed to the class implicitly and explicitly with the use of self and cls keyword
newObj.myMethod(newObj)


#------------------------------------------
# Output:
# v1.2
# v1.2
# v1.2
# v2.3
# If you replace the text/string of __version2 to anything other then string/str then the below error is thrown:
# AssertionError: Please only ensure that version is a text/string
