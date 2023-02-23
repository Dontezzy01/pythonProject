from array import*
vals=array("i", (23,24,9,12,-82,4,89,7,12,34,44))
#print(vals.buffer_info())
#print(vals.typecode)
#vals.reverse()
#print(vals[3])
#for i in range(len(vals)):
# or
#for e in vals:
    #print(e)


#Array using character
#char=array("u", ("a","e","i","o","u"))
#for i in char:
 #   print(i)

#or
#to print another in an Array
#NewArray=array(vals.typecode,(afor a in vals))
#to square up
NewArray=array(vals.typecode,(a*a for a in vals))
for e in NewArray:
    print(e)

