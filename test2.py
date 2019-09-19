print(" - Enter: Test 2")

try:
    f = open("demo2.txt", "r")
    a = f.read()
    print(a)
    if a == "1234567":
        print(" >>>> OK: demo2.txt")
    else:
        print(" <<<<<<<<< NOK")

except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


print(" - Exit:  Test 2")
