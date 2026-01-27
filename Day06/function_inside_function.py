def outer():
    def inner():
        return "Inner function executed"
    return inner()

print(outer())
