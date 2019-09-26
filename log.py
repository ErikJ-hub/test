import logging
import os

test = os.getenv('TEST_LOGFILE')
# test_logfile = os.getenv('USERNAME')
if test is not None:
    print(test)
else:
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


# for a in os.environ:
#     print('Var: ', a, 'Value: ', os.getenv(a))
# print("all done")

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(filename='test.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)