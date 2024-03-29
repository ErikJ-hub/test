import logging
import log


# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logger = logging.getLogger('test1')
# logger.setLevel(logging.DEBUG)

logger.info('Enter: Test 1')
print(" - Enter: Test 1")
filename = "demo1.txt"
compere = "1234567"

try:
    f = open(filename, "r")
    a = f.read()
except IOError:
    logger.critical('unable to open(' + filename + ')')
    exit(1)
finally:
    f.close()

print("     " + filename + ": " + a + " != " + compere)
if a == compere:
    print(" >>>> OK: " + filename)
else:
    print(" <<<< NOK: " + filename)
    logger.error('NOT OK: ' + filename + ": " + a + " != " + compere)
    exit(1)

print(" - Exit:  Test 1")
logger.info('Exit:  Test 1')