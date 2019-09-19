print(" - Enter: Test 2")
filename = "demo2.txt"
compere = "1234567"

try:
    f = open(filename, "r")
    a = f.read()
except:
    print("   -- Something went wrong when writing to the file: " + filename)
finally:
    f.close()

print("     " + filename + ": " + a + " != " + compere)
if a == compere:
    print(" >>>> OK: " + filename)
else:
    print(" <<<< NOK: " + filename)
    exit(1)

print(" - Exit:  Test 2")
