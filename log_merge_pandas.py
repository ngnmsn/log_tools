import pandas as pd
import time
import glob

def main():

    inlogs = glob.glob('./inlog/inlog_*.log')
    print("-----inlogs-----")
    print(inlogs)
    print(type(inlogs))

    for i in inlogs:
        df = pd.read_table(i)
        df.to_csv('./log.csv')
    
    print(df.head(10))
    print(df.tail(10))
            

    # df = pd.DataFrame([
    #     ["0001", "John", "Engineer"],
    #     ["0002", "Lily", "Sales"]],
    #     columns=['id', 'name', 'job']
    # )
    # df.to_csv("employee.csv", index=False)
    
if __name__=='__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
