import logging

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.setLevel(logging.INFO)

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
