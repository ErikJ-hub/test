import logging

f = open("test.log", "w")
f.writelines("----------------")
f.close()

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(filename='test.log', format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.setLevel(logging.INFO)
logger = logging.getLogger()


print(" - Enter: Build 1")

f = open("demo1.txt", "w")
f.writelines("1234567")
f.close()

f = open("demo2.txt", "w")
f.writelines("1234567")
f.close()

print(" - Exit:  Build 1")
