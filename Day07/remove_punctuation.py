text = "Hello, world! Python is great."
result = "".join(ch for ch in text if ch.isalnum() or ch == " ")
print(result)
