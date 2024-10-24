import matplotlib.pyplot as p
#list for time
time=[5,10,15,20,25,30,35,40,45,50]
velocity1=[10,20,30,40,50,60,70,80,90,95]
velocity2=[15,25,35,47,58,69,78,79,34,89]
p.plot(time,velocity1,linestyle='dashed',marker='2')
p.plot(time,velocity2,linestyle='dashdot',marker=7)
p.title("TIME VELOCITY LINE GRAPH")
p.xlabel("time")
p.ylabel("Velocity")
#p.legend()
p.show()