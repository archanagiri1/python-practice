with open("simple.txt", "w") as f:
    f.write("hello\npython\nworld\n")

with open("simple.txt","r") as f:
    lines = f.readlines()

print("total lines:",len(lines))