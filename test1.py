print(" - Enter: Test 1")

try:
    f = open("demo1.txt", "r")
    a = f.read()
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

print("     demo1.txt: " + a + " != 11234567")
if a == "11234567":
    print(" >>>> OK: demo1.txt")
else:
    print(" <<<<<<<<< NOK")
    exit(1)



print(" - Exit:  Test 1")
