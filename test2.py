import logging
import log


logger = logging.getLogger('test2')
# logger.setLevel(logging.DEBUG)

logger.info('Enter: Test 2')

print(" - Enter: Test 2")
filename = "demo2.txt"
compere = "11234567"

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
    print(" <<<< NOK: " + filename  + ": " + a + " != " + compere)
    logger.error('NOT OK: ' + filename + ": " + a + " != " + compere)
    exit(1)

print(" - Exit:  Test 2")
logger.info('Exit:  Test 2')