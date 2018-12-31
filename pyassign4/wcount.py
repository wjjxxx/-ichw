#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.
__author__ = "王俊杰"
__pkuid__  = "1800011822"
__email__  = "1800011822@pku.edu.cn"
"""

import sys, functools, string, urllib.error
from urllib.request import urlopen

def record(a_line):
    #对于一行，统计字数，得到一个字典    
    p_list = [i for i in string.punctuation]
    p_list.remove("'") 
    p_list.remove('-')
    for i in p_list:
        str_line = a_line.replace(i,' ')
        a_list = str_line.split()
        txt_list = [i.lower() for i in a_list]
    #去掉标点和大小写的区分
    
    for j in txt_list:
        if j not in word_dict:
            word_dict.update({j:1})
        else:
            word_dict[j] += 1
    #记录单词    

def wcount(lines, topn = 10):
    #输出最多的
    global word_dict
    word_dict = {}
    
    str_line = lines.readline().decode() 
    while str_line:
        record(str_line)
        str_line = lines.readline().decode()
    #一行一行记录单词
    
    def last(b):
        return b[1]
    word_list = sorted(word_dict.items(),\
                      key=lambda last(x),reverse = True)
    #将word_dict排序
    
    print(' '*3+'Word'.ljust(30),'Times'.center(10))
    for num in range(min(len(word_list),topn)):
        print(' '*3+word_list[num][0].ljust(30),\
              str(word_list[num][1]).center(10))
    #如果词不够就全输出来
    
if __name__ == '__main__':
    if  len(sys.argv) == 1 or len(sys.argv) > 3:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output.'+
              ' If not given, will output top 10 words')
        sys.exit(1)
    else:
        try:
            doc = urlopen(sys.argv[1])
        except urllib.error.URLError:
            print(sys.exc_info()[1])
        except urllib.error.HTTPError:
            print(sys.exc_info()[1])
        except ValueError:
            print(sys.exc_info()[1])
        #检测URL
        
        else:  
            try:
                sys.argv[2].isdigit()
            except IndexError:
                wcount(doc)
            else:
                if not sys.argv[2].isdigit():
                    print('Invalid number input.'+
                          'Check and reinput number.')
                    sys.exit(1)
                else:
                    wcount(doc, int(sys.argv[2]))
        #检测数据
