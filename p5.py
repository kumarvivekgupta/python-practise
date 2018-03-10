unit =input("enter units : ")
if unit<=150 :
 print "bill  = ",(unit*2.40)
elif unit<=300 :
 a=unit-150;
 print "bill = ",((150*2.40)+(a*3.00))
else :
 b=unit-300;
 print "bill = ",((150*2.40)+(150*3.00)+(b*3.20))