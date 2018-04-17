#coding:utf-8
import pymysql
mysql_info={
    "host":"192.168.20.35",
    "user":"root",
    "password":'begoit',
    'db':'mysql'
#    'charset':'utf8',
#    'port':'3306'
    }

class MysqlUtil():
    """
    mysql数据库相关操作
    连接数据库信息：mysql_info
    创建游标：mysql_excute
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    """
    def __init__(self):
        self.db_info=mysql_info
        '''连接池方式'''
        self.conn=MysqlUtil._getConnect(self.db_info)

    @staticmethod
    def _getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn=pymysql.connect(host=db_info['host'],
                                 user=db_info['user'],
                                 passwd=db_info['password'],
                                 db=db_info['db'])
#                                charset=db_info['charset'],
#                                 port=db_info['port'])

            return conn
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def mysql_execute(self,sql):
            '''执行sql语句'''
            cur=self.conn.cursor()
            try:
                cur.execute(sql)
            except Exception as a:
                self.conn.rollback()  #sql执行异常后回滚
                print('执行SQL语句出现异常:%s'%a)
            else:
                cur.close()
                self.conn.commit()   #sql无异常提交

    def mysql_getrows(self,sql):
            '''返回查询结果'''
            cur=self.conn.cursor()
            try:
                cur.execute(sql)
            except Exception as a:
                print('执行sql语句出现异常:%s'%a)
            else:
                rows=cur.fetchall()
                cur.close()
                return rows

    def mysql_getstring(self,sql):
            '''查询某个字段的对应值'''
            rows=self.mysql_getrows(sql)
            if rows!=None:
                for row in rows:
                    for i in  row:
                        return i

    def mysql_close(self):
            '''关闭close mysql'''
            try:
                self.conn.close()
            except Exception as a:
                print('数据库关闭时异常:%s'%a)

    # MySQLdb.connect()     建立数据库连接
    # cur = conn.cursor()    #通过获取到的数据库连接conn下的cursor()方法来创建游标。
    # cur.execute()    #过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作。
    # cur.close()     # cur.close() 关闭游标
    # conn.commit()   # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
    # conn.rollback() # 发生错误时候回滚
    # conn.close()     # Conn.close()关闭数据库连接

if __name__=='__main__':
    mysql=MysqlUtil()
    sql="select last_update from engine_cost where cost_name='io_block_read_cost'"
    mysql.mysql_execute(sql)
#    print(aaa)
    print(mysql.mysql_getrows(sql))
    print(mysql.mysql_getstring(sql))
    mysql.mysql_close()
