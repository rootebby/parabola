import matplotlib.pyplot as plt

a=[]
b=[]
# y=0
# x=-50
deg1 = int(input("1 (Küçük sayıyı giriniz): "))
deg2 = int(input("2 (Büyük sayıyı giriniz): "))
for x in range(deg1,deg2,1):
    y=x**2+2*x+2
    a.append(x)
    b.append(y)
    #x= x+1

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()