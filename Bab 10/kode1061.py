def generator():
    yield 0
    yield 1
    yield 2

obj_gen = generator()

for i in (obj_gen):
    print(i)
