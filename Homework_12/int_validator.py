from Python_course.Homework_12.validator import BaseValidator

__all__ = 'IntValidator'


class IntValidator(BaseValidator):

    def __init__(self, min_value: int = None, max_value: int = None):

        self.min_value = min_value
        self.max_value = max_value

    def validate(self, args):
        for value in args:
            if not isinstance(value, int):
                raise TypeError(f'Значение {value} должно быть целым числом')
            if self.min_value is not None and value < self.min_value:
                raise ValueError(f'Значение {value} должно быть больше {self.min_value}')
            if self.max_value is not None and value > self.max_value:
                raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

