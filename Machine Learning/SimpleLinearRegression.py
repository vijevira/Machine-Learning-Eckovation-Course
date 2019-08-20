import numpy as np
import matplotlib.pyplot as plt
def estimate_coef(x,y):
    n=np.size(x)
    mx,my=np.mean(x),np.mean(y)
    SSxy=np.sum(y*x-n*my*mx)
    SSxx=np.sum(x*x-n*mx*mx)
    b1=SSxy/SSxx
    b0=my-b1*mx
    return (b0,b1)

def plot_regression(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    ypred=b[0]+b[1]*x
    plt.plot(x,ypred,color="g")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def main():
    x=np.array(range(10))
    y=np.array([1,3,2,5,7,8,8,9,10,12])
    b=estimate_coef(x,y)
    print("estiamte coefficient:\nb0={}\nb1={}".format(b[0],b[1]))
    plot_regression(x,y,b)

if __name__=="__main__":
    main()
