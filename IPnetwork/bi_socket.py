#!/usr/local/bin/python
# A template for top-level scripts
# 14 Jan 2017 
'''Demo of socket to socket communication. 
'''
import logging
import pprint
import re, string
import sys, os
import datetime, time
import socket

DBG = False
MSG_LEN = 3

# Check the version
if sys.version[:3] != '3.6':
    print("Found python version ", sys.version[:5], " expected version 3.6.0", file=sys.stderr, flush=True)

# This will force the logger to use this file name in messages.
logger = logging.getLogger(__name__)

### basic logging setup #################################################
def init_logger():
    """Sets configuration on global logger.
    Set src_file=__name__ in your script so the file name appears in the log properly.
    """
    if DBG:
        llevel = logging.DEBUG
    else:
        llevel = logging.INFO

    ## Log file placed in the script directory
    log_file = (re.sub(r'.py$', '', os.path.basename(sys.argv[0])) + '_'
                         + datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
                         + '_' + str('V' if DBG else '') + '.log')
    logging.basicConfig(filename=log_file, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=llevel)
    print("Logging to " + log_file, file=sys.stderr)
    logger.info('In ' + sys.argv[0] + " START LOGGING: " + __name__ + ' to ' + log_file)


### write to the log using pprint ####################################
def log_object(the_obj):
    logger.info('\n'+ pprint.pformat(the_obj))

### Socket code ######################################################
def socket_config():
    
    ssend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s = socket.create_connection((socket.gethostname(), 5555))   # may be pythonic
    # ssend.connect((socket.gethostname(), 20))
    ssend.bind((socket.gethostname(), 80))
    return ssend

# def mysend(msg, s):
#     totalsent = 0
#     while totalsent < MSG_LEN:
#         sent = s.send(msg[totalsent:])
#         if sent == 0:
#             raise RuntimeError("socket connection broken")
#         totalsent = totalsent + sent


def myreceive(s):
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSG_LEN:
        chunk = s.recv(min(MSG_LEN - bytes_recd, 2048))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return b''.join(chunks)



### Main ##############################################################
def main(args):
    '''An example of what is (or is not) in main. All log and parsing setup
       is already done.'''
    logger.info("In template:main")
    ## pprint multi-line output to the log
    log_object(list(string.ascii_letters))
    ## Get two sockets
    s1 = socket_config()
    myreceive(s1)
    #s2 = socket_config()
    s1.close()
    #s2.close()
    

########################################################################
if __name__ == '__main__':

## If invoked with no args, just print the usage string
    if len(sys.argv) == 1:
        print(__doc__)
        sys.exit(-1)

    if '-v' in sys.argv:
        del(sys.argv[sys.argv.index('-v')])
        DBG = True
        
    args  = sys.argv[1:]
    init_logger()
    logger.info(args)          ## log what args are set
    main_start = time.clock()  ## Wrap main() in a timer.
    main(args)
    logger.info(sys.argv[0] + " Done, in " + '%5.3f'
                % (time.clock() - main_start) + "secs!")

### EOF (C) 2014  C9 Inc.
