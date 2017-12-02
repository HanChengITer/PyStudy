# -*- coding:utf-8 -*-

# 代码编写思路：先抽象后具体；先写框架，后写实现。
# 1.获得源帐号、目标账号、转账金额
# 2.连接数据库
# 3.开始事务
# 4.提交或回滚
# *********************
# 下列动作可封装到一个类中
#   3.1检查源帐号是否可用
#   3.2检查目标账号是否可用
#   3.3检查源帐号是否有足够的钱
#   3.4源帐号扣款
#   3.5目标账号加钱


import MySQLdb

# parameters define here
src_id = input('input src account id >')
des_id = input('input des account id >')
money = input('money number >')

class MyException(Exception):
	def __init__(self,message):
		Exception.__init__(self)
		self.message=message   

class TransferMoney(object):
	def __init__(self,db_connect_instance):
		self.__db_conn=db_connect_instance

	def check_account_available(self,account_id):
		print "检查账户%s是否可用..." % account_id
		__sql="select * from account where acctid=%s" % account_id
		__curosr = self.__db_conn.cursor()
		__curosr.execute(__sql)
		#print "rowcount-->%s" % __curosr.rowcount
		if __curosr.rowcount!=1:
			print "账户%s不可用"% account_id
			raise MyException("账户%s不可用"% account_id)
		print "账户%s可用" % account_id
		__curosr.close()

	def check_enough_money(self,account_id, money):
		print "检查账户%s余额是否足够..." % account_id
		__sql="select * from account where acctid=%s and money>=%s" % (account_id, money)
		__curosr = self.__db_conn.cursor()
		__curosr.execute(__sql)
		#print "rowcount-->%s" % __curosr.rowcount
		if __curosr.rowcount!=1:
			print "账户%s余额不足"% account_id
			raise MyException("账户%s余额不足"% account_id)
		print "账户%s余额充足" % account_id
		__curosr.close()

	def reduce_money(self,account_id, money):
		print "账户%s开始扣款..." % account_id
		__sql="update account set money=money-%s where acctid=%s" % (money, account_id)
		__curosr = self.__db_conn.cursor()
		__curosr.execute(__sql)
		#print "rowcount-->%s" % __curosr.rowcount
		if __curosr.rowcount!=1:
			print "账户%s扣款失败"% account_id
			raise MyException("账户%s扣款失败"% account_id)
		print "账户%s扣款成功" % account_id
		__curosr.close()

	def add_money(self,account_id, money):
		print "账户%s开始加钱..." % account_id
		__sql="update account set money=money+%s where acctid=%s" % (money, account_id)
		__curosr = self.__db_conn.cursor()
		__curosr.execute(__sql)
		#print "rowcount-->%s" % __curosr.rowcount
		if __curosr.rowcount!=1:
			print "账户%s加钱失败"% account_id
			raise MyException("账户%s加钱失败"% account_id)
		print "账户%s加钱成功" % account_id
		__curosr.close()

def main():
	st_conn = MySQLdb.Connect(host='127.0.0.1',port=3306,user='yc',passwd='Yc_123456',db='st',charset='utf8')

	transfer_money = TransferMoney(st_conn)

	try:
		transfer_money.check_account_available(src_id)
		transfer_money.check_account_available(des_id)
		transfer_money.check_enough_money(src_id,money)
		transfer_money.reduce_money(src_id,money)
		transfer_money.add_money(des_id,money)
		st_conn.commit()
		print "从帐号%s转%s元到帐号%s成功！！！" % (src_id, money, des_id)
	except Exception as e:
		print "从帐号%s转%s元到帐号%s失败！！！" % (src_id, money, des_id)
		print e.message
		st_conn.rollback()

	st_conn.close()

main()