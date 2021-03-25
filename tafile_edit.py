import tarfile
from pathlib import Path

p = Path('.')

print(p)
print(type(p))

newpath = p / 'bar' / Path('ppath')

print(newpath)
print(type(newpath)) 

cd = Path.cwd()
print(cd)
print(type(cd))

tmpdir = cd / Path('tmp')
Path.mkdir(tmpdir)

tmp_txt = tmpdir / Path('tmp.txt')

print(tmp_txt)
print(type(tmp_txt))

print(tmp_txt.exists())

tmp_txt.touch()

print(tmp_txt.exists())

tmp_txt.write_text("line 1\nline 2\nline 3")

for i in range(100):
    tmp_tar_name = "./tar" + str(i+1) + ".tar.gz"
    with tarfile.open(tmp_tar_name, 'w:gz') as tf:
        tf.add('tmp/tmp.txt')
        tf_list = tf.getmembers()
        print(tf_list)
        print(type(tf_list))










