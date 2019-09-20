import logging

logging.basicConfig(level=logging.INFO)  # CRITICAL, ERROR, WARNING, INFO or DEBUG #
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And this, too')
logging.critical('And this, too')

print(" - Enter: Test 1")
filename = "demo1.txt"
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
    logging.error('This was NOT OK')
    exit(1)

print(" - Exit:  Test 1")
