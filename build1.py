import logging
logging.basicConfig(level=logging.INFO)  # CRITICAL, ERROR, WARNING, INFO or DEBUG #
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And this, too')
logging.critical('And this, too')

print(" - Enter: Build 1")

f = open("demo1.txt", "w")
f.writelines("1234567")
f.close()

f = open("demo2.txt", "w")
f.writelines("1234567")
f.close()

print(" - Exit:  Build 1")
