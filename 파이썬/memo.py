import sys
import datetime

 # option = sys.argv[1]
# memo = sys.argv[2]
#
# print(option)
# print(memo)


#python memo.py -a

try:
    option = sys.argv[1]
except IndexError as e:
    print("{}에러 입니다. 생성할때는 '-a' 조회할때는 '-v'를 입력하세요 ".format(e))
else:
    if option == '-a':
        try:
            memo = sys.argv[2]
        except IndexError as e:
            print("문자를 입력하세요({})".format(e))
        else:
            f = open(u'D:/양순규/Notebooks/Notes/Home/연습중.txt', 'a', encoding='UTF8')
            now = datetime.datetime.now()
            nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
            f.write(nowDate)
            f.write('\n')
            f.write(memo)
            f.write('\n')
            f.write('\n')
            f.close()

    elif option == '-v':
        try:
            f = open('memo.txt', encoding='UTF8')
        except FileNotFoundError as e:
            print(" 파일을 찾을수 없습니다.({})".format(e))
        else:
            memo = f.read()
            f.close()
            print(memo)

