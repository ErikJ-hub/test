import logging

# logger = logging.getLogger('__name__')
# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(filename='test.log', format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


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
    logger.critical('This was NOT OK')
    exit(1)

print(" - Exit:  Test 2")
