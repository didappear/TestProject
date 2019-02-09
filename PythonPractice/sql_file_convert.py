#! /usr/bin/env python
#_*_coding:utf-8_*_
#第一部分:sql解析
import os
def sql_parse(sql):
    '''
    sql_parse--->insert_parse,delete_parse,update_parse,select_parse
    sql解析总控
    :param sql:用户输入的字符串
    :return: 返回字典格式sql解析结果
    '''''
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    sql_l=sql.split(' ')
    print(sql_l)
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    print('res is %s' %res)
    return res

def insert_parse(sql_l):
    # insert into db.t1 values 鲁海宝,35,13910015353,测试,2005-06-27
    '''
    sql解析分支:insert
    :param sql_l: sql按照空格分割的列表
    :return: 返回字典格式的sql解析结果
    '''''
    sql_dic={
        'func':insert, #函数名
        'insert':[],   #insert选项,留出扩展
        'into':[],     #表名
        'values':[],   #值
    }
    return handle_parse(sql_l,sql_dic)

def delete_parse(sql_l):
    # delete from db.t1 where id=1
    '''
    sql解析分支:delete
    :param sql_l: sql按照空格分割的列表
    :return: 返回字典格式的sql解析结果
    '''''
    sql_dic={
        'func':delete,
        'delete':[], #delete选项,留出扩展
        'from':[],   #表名
        'where':[],  #filter条件
    }
    return handle_parse(sql_l,sql_dic)

def update_parse(sql_l):
    # update db.t1 set id=2 where name='alex'
    '''
    sql解析分支:update
    :param sql_l: sql按照空格分割的列表
    :return: 返回字典格式的sql解析结果
    '''''
    sql_dic={
        'func':update,
        'update':[], #update选项,留出扩展
        'set':[],    #修改的值
        'where':[],  #filter条件
    }
    return handle_parse(sql_l,sql_dic)

def select_parse(sql_l):
    # select * from db1.emp where not id= 1 and name = 'alex' or name= 'sb' limit 3
    '''
    sql解析分支:select
    :param sql_l: sql按照空格分割的列表
    :return: 返回字典格式的sql解析结果
    '''''
    sql_dic={
        'func':select,
        'select':[], #查询字段
        'from':[],   #表
        'where':[],  #filter条件
        'limit':[],  #limit条件
    }
    return handle_parse(sql_l,sql_dic)

def handle_parse(sql_l,sql_dic):
    '''
    填充sql_dic
    :param sql_l: sql按照空格分割的列表
    :param sql_dic: 待填充的字典
    :return: 返回字典格式的sql解析结果
    '''''
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag=False
        if not tag and item in sql_dic:
            tag=True
            key=item
            continue
        if tag:
            sql_dic[key].append(item)
    #print('before \033[33;1m%s\033[0m' %sql_dic)
    if sql_dic.get('where'):
       # print(sql_dic.get('where'))
        sql_dic['where']=where_parse(sql_dic.get('where'))

    #print('after \033[33;1m%s\033[0m' %sql_dic)
    return sql_dic

def where_parse(where_l):
    '''
    对用户输入的where子句后的条件格式化,每个子条件都改成列表形式
    :param where_l: 用户输入where后对应的过滤条件列表
    :return:
    '''
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            #print('char is %s' %char)
            if len(char) != 0:
                char=three_parse(char) #将每一个小的过滤条件如,name>=1转换成['name','>=','1']
                res.append(char)
            res.append(i)
            char = ''

        else:
          char+=i
       #print('res.append is %s' % res)
    else:
        char=three_parse(char)
        res.append(char)
    #print('after res.append is %s' %res)
    return res

def three_parse(exp_str):
    '''
    将每一个小的过滤条件如,name>=1转换成['name','>=','1']
    :param exp_str:条件表达式的字符串形式,例如'name>=1'
    :return:
    '''''
    print('three_opt before is \033[34;1m%s\033[0m' %exp_str)
    key=['>','=','<']
    res=[]
    char=''
    opt=''
    tag=False
    for i in exp_str:#id>23
        if i in key:
            tag=True
            if len(char) !=0:
                res.append(char)
                char=''
            opt+=i
        if not tag:
            char+=i
        if tag and i not in key:
            tag=False
            res.append(opt)#
            opt=''
            char+=i
    else:
        res.append(char)
    print('res is %s ' %res)
    #新增like功能
    if len(res) == 1:#['namelike_ale5']
        res=res[0].split('like')
        res.insert(1, 'like')
    return res


#第二部分:sql执行
def sql_action(sql_dic):
    '''
    执行sql的统一接口,内部执行细节对用户完全透明
    :param sql:
    :return:
    '''''
    return sql_dic.get('func')(sql_dic)

def insert(sql_dic):
    #print('insert %s' %sql_dic)
    db,table=sql_dic.get('into')[0].split('.')
    with open('%s/%s' %(db,table),'ab+') as fh:
        offs = -100
        while True:
            fh.seek(offs,2)
            lines = fh.readlines()
            if len(lines)>1:
                last = lines[-1]
                break
            offs *= 2
        last=last.decode(encoding='utf-8')
        #print(last)
        last_id=int(last.split(',')[0])
        new_id=last_id+1
        #insert into db1.emp values 张国辉,30,18500841678,运维,2007-8-1
        record=sql_dic.get('values')[0].split(',')
        print(record)
        #record.insert(0,26)
        #['26', 'alex', '18', '13120378203', '运维', '2013-3-1\n']
        record_str=','.join(record)+'\n'
        print('record_str: %s' %record_str)
        fh.write(bytes(record_str,encoding='utf-8'))
        fh.flush()
    return [['insert successful']]

def delete(sql_dic):
    db,table=sql_dic.get('from')[0].split('.')
    bak_file=table+'_bak'
    #使用open()方法把需要修改的文件打开为两个文件，然后逐行度日内存，找到需要删除的行时，用后面的行逐一覆盖
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        del_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            print(zip(title.split(','),line.split(',')))
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if not filter_res:
                w_file.write(line)
            else:#为真表示已经找到要输出的行
                del_count+=1 #1
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[del_count],['delete successful']]

def update(sql_dic):
    #update db1.emp set id='sb' where name like alex
    db,table=sql_dic.get('update')[0].split('.')
    set=sql_dic.get('set')[0].split(',')
    #print('set is %s'%set)
    #print('from update %s' %sql_dic)
    set_l=[]
    for i in set: #set=["id='sb'"]  id='sb'
        #print('i is %s'%i)
        set_l.append(i.split('='))
    print('sel_l %s' %set_l) #[['id', "'sb'"]]
    bak_file=table+'_bak'
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        update_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            #print('dic %s' %dic)
            #print('filter_res is %s' %filter_res)
            if filter_res:  #dic {'id': 'sb', 'name': 'alex', 'age': '18', 'phone': '13120378203', 'dept': '运维', 'enroll_date': '2013-3-1\n'}
                for i in set_l:#[['id', "'sb'"]] i=['id', "'24'"]
                    print('i %s'%i)
                    #print(i)
                    k=i[0] #k=id
                    #print(k)
                    v=i[-1].strip("'") #v=sb
                    print(v)
                    #print('k v %s %s' %(k,v))
                    dic[k]=v   #dic[id]=sb
                #print('change dic is %s ' %dic)
                line=[]
                for i in title.split(','):#i=[id,name,age,phone,dept,enroll_date"]
                    line.append(dic[i])    #line=[14,王新凯,22,15369965127,运维,2015-10-31]
                print('line is %s' %line)
                update_count+=1
                line=','.join(line)
            print(line)
            w_file.write(line)


        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[update_count],['update successful']]

def select(sql_dic):
    db,table=sql_dic.get('from')[0].split('.')
    fh=open("%s/%s" %(db,table),'r',encoding='utf-8')

    filter_res=where_action(fh,sql_dic.get('where'))
    print('from in select ',sql_dic.get('where'))
    # print('filter_res is ====>',filter_res)
    fh.close()

    limit_res=limit_action(filter_res,sql_dic.get('limit'))
    #print('limit_res is ====>',limit_res)

    search_res=search_action(limit_res,sql_dic.get('select'))
    print('select_res is ====>',search_res)

    return search_res

def where_action(fh,where_l):
    res=[]
    logic_l=['and','or','not']
    title="id,name,age,phone,dept,enroll_date"
    if len(where_l) !=0:
        for line in fh:
            dic=dict(zip(title.split(','),line.split(',')))
            logic_res=logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
            print(dic)
    else:
        res=fh.readlines()
    #print('where_action is %s' %res)
    return res

def logic_action(dic,where_l):
    res=[]
    print('from logic_action',where_l)
    for exp in where_l:
        if type(exp) is list:
            exp_k,opt,exp_v=exp
            if exp[1] == '=':
                opt='%s=' %exp[1]
            if dic[exp_k].isdigit():
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v="'%s'" %dic[exp_k]
            if opt != 'like':
                exp=str(eval("%s%s%s" %(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp='True'
                else:
                    exp='False'
        res.append(exp)
        print('res is %s' %res)
    res=eval(' '.join(res))
    #print('==\033[45;1m%s\033[0m' %(res))
    return res

def limit_action(filter_res,limit_l):
   # print('filter_res is %s' %filter_res)
    res=[]
    if len(limit_l) !=0:
        index=int(limit_l[0])
        res=filter_res[0:index]
    else:
        res=filter_res

    return res

def search_action(limit_res,select_l):
    #print('limit_res is %s' %limit_res)
    #print('select_l is %s' %select_l)
    #print('limit_res is %s' % limit_res)
    res=[]
    fileds_l=[]
    title="id,name,age,phone,dept,enroll_date"
    if select_l[0] == '*':
        res=limit_res
        fileds_l=title.split(',')
    else:

        for record in limit_res:
            print('record is %s' %record)


            dic=dict(zip(title.split(','),record))
            #seprint("dic is %s " %dic)
            fileds_l=select_l[0].split(',')
            #print('from search_aciton %s'%fileds_l)
            r_l=[]
            for i in fileds_l:
                r_l.append(dic[i].strip())
            res.append(r_l)
    #print("dic is %s " % dic)
    #print('fileds_l is %s' %fileds_l)
    print('res is %s' %res)
    return [fileds_l,res]



if __name__ == '__main__':
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':break
        if len(sql) == 0:continue

        sql_dic=sql_parse(sql)

        if len(sql_dic) == 0:continue #输入命令非法
        res=sql_action(sql_dic)
        print(sql_dic)
        print(res)

        for i in res[-1]:
            print(i)