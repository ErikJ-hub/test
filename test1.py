print(" - Enter: Test 1")

try:
    f = open("demo1.txt", "r")

    if f.read() == "1234567":
        print(" >>>> OK: demo1.txt")
    else:
        print(" <<<<<<<<< NOK")

except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


print(" - Exit:  Test 1")
