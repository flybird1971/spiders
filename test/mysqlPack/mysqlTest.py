#coding:utf8
import MySQLdb as mdb
import random
import sys
sys.path.append("../")
from module.module import  randStr
__author__ = 'flybird1971'

# 参加文档 http://zetcode.com/db/mysqlpython/

connect = None
try:
    #建立连接
    #connect = mdb.connect(ip,user,passwd,dbname)
    connect = mdb.connect(host='127.0.0.1',user='root',passwd='123456')

    #选择数据库
    connect.select_db('python')

    #创建游标
    cur = connect.cursor()

    #查看版本
    print cur.execute('select version()')
    print cur.fetchone()
    #raise IOError("HAHHAHA")

    #sqlStr = 'drop table if exists test'
    #print cur.execute(sqlStr)
    sqlStr  = 'create table if not exists test('
    sqlStr += 'id int(11) unsigned primary key auto_increment,'
    sqlStr += 'value varchar(255) not null default "" comment "val"'
    sqlStr += ')engine=InnoDB DEFAULT charset=utf8 comment="test"'
    #执行sql语句
    #with connect :
        #print cur.execute(sqlStr)

    print cur.execute("show tables")
    print cur.fetchone()

    #插入数据
    with connect:
        print "insert some data into test table ..."
        insertSql = 'insert into test (id,value) values (null,"t.liu")'
        print cur.execute(insertSql)

    #批量插入
    with connect:
        print "batch insert starting ....  "
        insertSql = "insert into test (id,value) values (null,%s)"
        insertDataList = []
        max = 100
        while max > 0:
            max -= 1
            insertDataList.append(randStr(random.randint(4,18)))
        print cur.executemany(insertSql,insertDataList)
        print "batch insert over total insert %d records " % (cur.rowcount)


    #查询数据
    print "select ... "
    print cur.execute("select * from test")

    #获取上条语句执行后影响记录总条数
    print cur.rowcount
    print cur.fetchmany(cur.rowcount)

    #元组集合，包含字典元素，
    print "result dictory format : "
    curDict = connect.cursor(mdb.cursors.DictCursor)
    curDict.execute("SELECT * FROM test LIMIT 4")
    rows = curDict.fetchall()
    desc = cur.description
    print desc
    print "*"*88
    for row in rows:
        print row["id"], row["value"]


    #安全查询Prepared statements
    cur.execute("select * from test where value=%s",('t.liu'))
    print cur.fetchmany(cur.rowcount)

    #事务自动开启提交
    #connect.commit()

    #关闭游标
    cur.close()
    curDict.close()
except mdb.Error,e:
    print "has error %d : %s " % (e.args[0],e.args[1])
    pass
finally:
    if connect:
        #关闭数据库连接
        connect.close()
