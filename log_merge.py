import glob

inlogs = glob.glob('./inlog/*.log')
print("-----inlogs-----")
print(inlogs)
print(type(inlogs))

with open('merge.log', 'w') as merge:
    for inlog in inlogs:
        with open(inlog, 'r') as inlog:
            merge.write(inlog.read())
            merge.write('\n')


with open('merge.log' ,'r') as merge:
    merge_list = merge.read().splitlines()
    print("-----merge_list------")
    print(merge_list)
    print(type(merge_list))
    merge_sorted_list = sorted(merge_list)
    print("-----merge_sorted_list------")
    print(merge_sorted_list)
    print(type(merge_sorted_list))
    with open('merge_sorted.log', 'w') as mergesorted:
        n = "\n".join(merge_sorted_list)
        mergesorted.write(n)

