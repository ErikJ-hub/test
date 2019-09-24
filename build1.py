import logging

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(filename='test.log', format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.setLevel(logging.INFO)
logger = logging.getLogger()



try:
    f = open("test.log", "w")
except IOError:
    logger.critical('unable to open(test.log)')
    exit(1)
finally:
    f.writelines("----------------\n")
    f.writelines("--  test.log  --\n")
    f.writelines("----------------\n")
    f.close()

logger.info('Start: Build 1')
print(" - Enter: Build 1")

try:
    f = open("demo1.txt", "w")
except IOError:
    logger.critical('unable to open(demo1.txt)')
    exit(1)
finally:
    f.writelines("1234567")
    f.close()

try:
    f = open("demo2.txt", "w")
except IOError:
    logger.critical('unable to open(demo2.txt)')
    exit(1)
finally:
    f.writelines("1234567")
    f.close()

print(" - Exit:  Build 1")
logger.info('Exit:  Build 1')
