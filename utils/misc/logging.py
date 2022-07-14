import logging

file_log = logging.FileHandler('data/myapp.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out),
                    format=u'%(filename)s.%(funcName)s [LINE:%(lineno)d] #%(levelname)-6s [%(asctime)s]  %(message)s',
                    datefmt='%d.%m.%Y %H:%M:%S',
                    level=logging.INFO)
