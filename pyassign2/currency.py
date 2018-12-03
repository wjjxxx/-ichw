# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:09:47 2018

@author: HP
"""

a=input("")
b=input("")
c=input("")

def fanhui(a,b,c):
    #得到请求网址后返回的字符串
    from urllib.request import urlopen
    wangzhi=('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='\
             +a+"&to="+b+"&amt="+c)
    doc = urlopen(wangzhi)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr=jstr.split()
    return(jstr)
    
def tiqu(jstr):
    #在返回的字符串中提取出转换后值
    qian=[]
    for i in jstr:
        al=len(i)
        shu=str("0123456789")
        ji=0
        for b in range(al):
            zhao=i[b]
            if shu.count(zhao)==1:
                ji=ji+1
            else:
                ji=ji
        if ji!=0:
            i=[i]
            qian=qian+i
        #现在就只有转换前和转换后两个数了
    if len(qian)==2:
        qian=qian
    else:
        #间接判断输入是否合法
        print("错误！")
        return None
    qian=qian[1]
    mubiao=qian[1:]
    return(mubiao) 
    
def exchange(currency_from, currency_to, amount_from):
    a=fanhui(currency_from, currency_to, amount_from)
    b=tiqu(a)
    return(b)
    
d=exchange(a,b,c)
print(d)

def test_fanhui():
    #测试返回函数
    jstr=fanhui("USD","EUR","2.5")
    assert jstr==['{', '"from"', ':', '"2.5', 'United', 'States',\
                    'Dollars",', '"to"', ':', '"2.1589225', 'Euros",',\
                    '"success"', ':', 'true,', '"error"', ':', '""', '}']
    jstr=fanhui("USD","AED","2.5")
    assert jstr==['{', '"from"', ':', '"2.5', 'United', 'States',\
                    'Dollars",', '"to"', ':', '"9.182905', 'United', \
                    'Arab', 'Emirates', 'Dirhams",', '"success"', ':',\
                    'true,', '"error"', ':', '""', '}']
    jstr=fanhui("CAD","MMK","3")
    assert jstr==['{', '"from"', ':', '"3', 'Canadian', 'Dollars",', \
                    '"to"', ':', '"3508.824587556', 'Myanma', 'Kyats",',\
                    '"success"', ':', 'true,', '"error"', ':', '""', '}']

def test_tiqu():
    #测试提取函数
    b=tiqu(['{', '"from"', ':', '"2.5', 'United', 'States',\
                    'Dollars",', '"to"', ':', '"2.1589225', 'Euros",',\
                    '"success"', ':', 'true,', '"error"', ':', '""', '}'])
    assert b=="2.1589225"
    b=tiqu(['{', '"from"', ':', '"2.5', 'United', 'States',\
                    'Dollars",', '"to"', ':', '"9.182905', 'United', \
                    'Arab', 'Emirates', 'Dirhams",', '"success"', ':',\
                    'true,', '"error"', ':', '""', '}'])
    assert b=="9.182905"
    c=tiqu(['{', '"from"', ':', '"3', 'Canadian', 'Dollars",', \
                    '"to"', ':', '"3508.824587556', 'Myanma', 'Kyats",',\
                    '"success"', ':', 'true,', '"error"', ':', '""', '}'])
    assert c=="3508.824587556"

def test_exchange():
    #测试exchange函数
    d=exchange("USD","EUR","2.5")
    assert d=="2.1589225"
    d=exchange("USD","AED","2.5")
    assert d=="9.182905"
    d=exchange("CAD","MMK","3")
    assert d=="3508.824587556"
    
def testAll():
    #测试全部
    test_fanhui()
    test_tiqu()
    test_exchange()
    print("All tests passed!")

testAll()
