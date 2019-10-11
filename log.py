import logging
import os

test = os.getenv('TEST_LOGFILE')

# test_logfile = os.getenv('USERNAME')
if test is not None:
    logging.basicConfig(filename=test,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
else:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


# for a in os.environ:
#     print('Var: ', a, 'Value: ', os.getenv(a))
# print("all done")

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
# logging.basicConfig(filename='test.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)