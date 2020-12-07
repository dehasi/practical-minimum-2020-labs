class Either:
    result = None
    error = None

    def __init__(self, result=None, error=None):
        if error is None:
            assert result is not None, "Both left and right are none"
        else:
            assert result is None, "Both left and right are not none"

        self.result = result
        self.error = error

    def is_result(self):
        return self.result is not None

    def is_error(self):
        return not self.is_result()

    def get_result(self):
        assert self.result is not None, f'Result is None, error={self.error}'
        return self.result

    def get_error(self):
        return self.error

    def map(self, function):
        if self.is_result():
            return Either(result=function(self.get_result()))
        return self


def get_from_somewhere(id):
    if id % 2 == 0:
        return Either(id)
    else:
        return Either(error=ArithmeticError("Some message", id))


result = get_from_somewhere(2)\
    .map(lambda x: x * 2)\
    .get_result()
print(result)
