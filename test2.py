import logging

# logger = logging.getLogger('__name__')
# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(filename='test.log', format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

logger.info('Enter: Test 2')

print(" - Enter: Test 2")
filename = "demo2.txt"
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
    print(" <<<< NOK: " + filename  + ": " + a + " != " + compere)
    logger.error('  - NOT OK: ' + filename + ": " + a + " != " + compere)
    exit(1)

print(" - Exit:  Test 2")
logger.info('Exit:  Test 2')