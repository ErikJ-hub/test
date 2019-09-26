import logging
import log


logger = logging.getLogger('build1')
# logger.setLevel(logging.DEBUG)


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
