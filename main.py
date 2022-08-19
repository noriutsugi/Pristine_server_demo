from subprocess import Popen, PIPE
bt_conn = '1'
dev_conn = '1'
pin_1 = '1'
pin_2 = '1'
pin_3 = '1'
process = Popen(['python3', 'matrix.py', bt_conn, dev_conn, pin_1, pin_2, pin_3], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
