from validator import BaseValidator

__all__ = 'TextValidator'


class TextValidator(BaseValidator):

    def validate(self, value: str):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно быть текстом')
        if not value.istitle():
            raise ValueError(f'Значение {value} должно начинаться с заглавной буквы')

