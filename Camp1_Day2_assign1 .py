Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
v = Sessions_Attended["sessions"]
print(v)
f = v.split(',')
print("I have attended "+str(len(f))+" sessions")