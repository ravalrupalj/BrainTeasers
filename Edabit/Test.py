#from Edabit.Test import Test

class Test:

    @classmethod
    def assert_equals(self, obj1, obj2):
        if obj1 == obj2:
            return True
        else:
            raise Exception('Not match')




