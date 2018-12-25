# 密码重试程序
# password = ‘a123456’
# 让使用者重复输入三次密码， 最多输入三次
# 如果正确 印出 “登陆成功！”
# 如不正确 印出 “密码错误，还有__次机会！”
password = 'a123456'
i = 3
while i > 0:
	pwd = input('请输入密码')
	if pwd == password:
		print('登入成功')
		break # 逃出回圈
	else:
		i = i - 1
		print('密码错误！还有' , i, '次机会')
		
