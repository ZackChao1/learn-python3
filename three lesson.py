import sys
import tab


f_name='list.xt'
f=file(f_name)

staff_info={}
column_name=['td','name','dep','phone']
print(column_name)

for line in f.readlines():
    f_line=line.split()
    key=f_line[0]
    info=f_line[1:]
    staff_info[key]=info
f.close()

while True:
    print('''Please choose below option to proceed:
    1.modify
    2.search
    ''')
    try:
        option=int(raw_input('-->'))
    except ValueError as e:
        print('sdfsf %d' % e)
        continue
    if option==1:
        option=raw_input('sdfsdf').strip()
        f_option=option,split()
        print(f_option)

        
