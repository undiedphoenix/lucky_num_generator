import random
import string
import operator
import sys
def generate_redball_num():
	"产生6位红色号码"
	a = range(1,34) #包括start 1 不包括stop34  即 1<= n <34
	redball = random.sample(a,6)
	return redball

def generate_blueball_num():
	"产生1位蓝色号码"
	blueball = random.randint(1,16)
	return blueball

def print_to_log_file(mylucky,myspnum,count):
	"输出到文件"
	log_file = open("H:\zzg\lucky_python\create_lucky_00011.txt", "a")
	stdout_backup = sys.stdout #backup oringial std
	sys.stdout = log_file      #重定向
	print(mylucky,'[',myspnum,']','--',count)
	log_file.close()
	sys.stdout = stdout_backup #恢复

def get_count_from_database(mylucky,myspnum):
	ssq_len = 6
	line_num = 0
	match0num = match1num = match2num = match3num = match4num = match5num = match6num = 0
	match01num = match11num = match21num = match31num = match41num = match51num = match61num = 0

	file = open("H:\zzg\lucky_python\lucky_database.txt")
	while 1: #proce file loop
		lines = file.readlines(100000)
		if not lines:
			break #proce file loop
		for line in lines:
			match_num = 0 #
			line = line[0:len(line)-1] #去掉 \n
			ll = line.split('	')     #
			#print(ll) #output
			#print(int(ll[1]))
			for x in mylucky :
				for i in range(ssq_len) :
					if x == int(ll[i]) :
						#print("find a same num in database:",int(ll[i]))
						match_num+=1				
			#print("matchnum = ",match_num) #ouput
			line_num +=1
			if match_num == 0:
				match0num += 1
				if myspnum == int(ll[6]):
					match01num += 1
					match0num -= 1 #
			elif match_num == 1:
				match1num += 1
				if myspnum == int(ll[6]):
					match11num += 1
					match1num -= 1
			elif match_num == 2:
				match2num += 1
				if myspnum == int(ll[6]):
					match21num += 1
					match2num -= 1
			elif match_num == 3:
				match3num += 1
				if myspnum == int(ll[6]):
					match31num += 1
					match3num -= 1
			elif match_num == 4:
				match4num += 1
				if myspnum == int(ll[6]):
					match41num += 1
					match4num -= 1
			elif match_num == 5:
				match5num += 1
				if myspnum == int(ll[6]):
					match51num += 1
					match5num -= 1
			elif match_num == 6:
				match6num += 1
				if myspnum == int(ll[6]):
					match61num += 1
					match6num -= 1
		#proce file loop
	count = [match0num,match1num,match2num,match3num,match01num,match11num,match21num,\
	match4num,match31num,match5num,match41num,match51num,match6num,match61num]
	return count

def count_one_array_num(reds,blue):
	"输入一个开奖号码，统计在历史记录中的情况"
	count = get_count_from_database(reds,blue)
	print(blue,'[',blue,']','--',count)
	print_to_log_file(reds,blue,count);
	return

def random_num_count(f61,f60,f51,f41,f50,f31,f40):
	"生成一个随机数，统计在数据库中的历史情况，循环找到符号条件的随机数"
	while 1: #main loop
		mylucky = generate_redball_num();
		myspnum = generate_blueball_num();
		count = get_count_from_database(mylucky,myspnum)	
		print(mylucky,'[',myspnum,']','--',count)
		
		#if count[13] == f61 and count[12] == f60 and count[11] == f51 and count[10] == f41 \
		#and count[9] == f50 and count[8] == f31 and count[7] == f40 :
		if count[13] == f61 and count[12] == f60 and count[11] == f51 and count[10] == f41 \
		and count[9] == f50 :
			mylucky.sort()
			print_to_log_file(mylucky,myspnum,count);
			break;#main loop	
	return
#main:
print("cout index mean: [0+0,1+0,2+0,3+0, 0+1,1+1,2+1, 4+0,3+1, 5+0,4+1, 5+1,6+0, 6+1]")

lps = 0
while lps < 2200 :
	random_num_count(0,0,0,1,1,8,9)
	lps += 1


'''
#mylucky = [3,7,20,21,25,31];myspnum = 14
#mylucky = [1,19,25,26,27,33];myspnum = 10
mylucky = [2,6,12,17,25,28];myspnum = 12
count_one_array_num(mylucky,myspnum)
mylucky = [3,14,16,20,31,32];myspnum = 9
count_one_array_num(mylucky,myspnum)
mylucky = [4,6,9,14,20,29];myspnum = 14
count_one_array_num(mylucky,myspnum)
mylucky = [8,13,14,18,23,33];myspnum = 6
count_one_array_num(mylucky,myspnum)
mylucky = [1,6,7,11,13,15];myspnum = 5
count_one_array_num(mylucky,myspnum)
mylucky = [21,22,25,28,29,30];myspnum = 8
count_one_array_num(mylucky,myspnum)
mylucky = [2,14,20,24,28,32];myspnum = 16
count_one_array_num(mylucky,myspnum)
mylucky = [4,7,11,14,29,32];myspnum = 12

mylucky = [2,5,7,9,11,27];myspnum = 16
count_one_array_num(mylucky,myspnum)
'''