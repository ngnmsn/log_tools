from datetime import datetime, timedelta, timezone
import time
import random
import string

def main():
    start_time = time.time()
    list = []
    JST = timezone(timedelta(hours=+9), 'JST')

    for i in range(10000):
        current_time = (datetime.now(JST).strftime('%Y/%m/%d %H:%M:%S.%f')[:-3])
        log_message = "[" + current_time + "] " + ramdomstr(100)
        list.append(log_message)
        time.sleep(0.001)

    with open('./inlog/inlog_1.log', 'w') as inlog:
        list_joined = "\n".join(list)
        inlog.write(list_joined)

    elapsed_time = time.time() - start_time
    print(elapsed_time)

def ramdomstr(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

if __name__=='__main__':
    main()
