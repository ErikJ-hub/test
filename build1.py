print(" - Enter: Build 1")

f = open("demo1.txt", "w")
f.writelines("1234567")
f.close()

f = open("demo2.txt", "w")
f.writelines(["1234567"])
f.close()

print(" - Exit:  Build 1")
