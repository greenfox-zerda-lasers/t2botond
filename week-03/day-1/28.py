aa = [1, 2, 3]
out = 0
# if the aa list contains one element set the out to 1
# if the aa list contains two element set the out to 2
# if the aa list contains more than 2 set the out to 10
# if the aa contains no elements it should set to -1
print(len(aa))
if len(aa)==0:
    out=1
    print(out)
elif len(aa)==1:
    out=2
    print(out)
elif len(aa)>1:
    out=10
    print(out)
else :
    out=-1
    print(out)
