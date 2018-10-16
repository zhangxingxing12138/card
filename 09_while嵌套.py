# 外层循环的计数器（行）
row = 1
# while条件是: 小于10行
while row <= 10:
   # 内层循环的计数器（列）
   col = 1
   # while循环的条件是：col<=row相当于列小于行可以循环，不满足条件时候停止循环
   while col <= row:
      # 输出小星星,有多少列就输出多少小星星,那么这个列？谁决定  行决定
      print('%d * %d = %d'%(row,col,row*col),end='\t')
      col+=1
   # 换行
   print('\n')
   row+=1


