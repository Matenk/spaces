def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

inner_function() # нельзя вызвать функцию в глобальном пространстве, т.к. она находится в другой области видимости (
# в локальном пространстве),
# чтобы сработал print нужно вызвать inner_function() внутри def test_function(), а потом уже
# в глобальном пространстве вызвать объемлющую функцию def test_function()

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()