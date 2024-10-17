import numpy as np

x= np.array(
    [
        [1,1],
        [1,2],
        [1,3],
        [1,4],
        [1,5]
    ]
)
y= np.array(
    [13, 11, 9, 7, 5]
)
print(x.T)
x_t = x.T
print(x_t*x)