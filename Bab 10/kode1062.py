def generator():
    yield 0
    yield 1
    yield 2
    yield "string"
    yield [0, 1, 2]
    yield (3, 4, 5)
    yield {"key1":"value1", "key2":"value2"}

obj_gen = generator()

for i in (obj_gen):
    print(i)
