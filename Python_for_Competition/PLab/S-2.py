import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,7,0.5)

y = 10*np.random.rand()+x * np.random.rand() + 2*np.random.rand()*x**2  +x**3

plt.scatter(x,y)
plt.show()



coef_1 = np.polyfit(x,y,1) 
y_pred_1 = coef_1[0]*x+ coef_1[1] 


# coef_2 = np.polyfit(x,y,2) 
# y_pred_2 = coef_2[0]*x**2+ coef_2[1]*x + coef_2[2] 

# coef_3 = np.polyfit(x,y,3) 
# y_pred_3 = np.poly1d(coef_3)(x) 
print(coef_1[0],coef_1[1])
plt.scatter(x,y,label="raw_data") 
plt.plot(x,y_pred_1,label="d=1") 
# plt.plot(x,y_pred_2,label="d=2") 
# plt.plot(x,y_pred_3,label = "d=3") 
plt.legend(loc="upper left")
plt.title("least square fitting")
plt.show()