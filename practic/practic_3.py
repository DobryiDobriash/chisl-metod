import numpy as np

a = np.arange(24).reshape(6, 4)

b = a.reshape(4, 6)
c = a.reshape(2, 3, 4)
d = a.reshape(24,)

col = a[:, 2]
print("\ncol =", col)
print("col.base is a или связан:", col.base is a)

col[0] = 999
print("После col[0] = 999:")
print("col      :", col)
print("a[:, 2]  :", a[:, 2])  
print("a[0, 2]  :", a[0, 2])   

a[0, 2] = 2

mask = a > 10
filtered = a[mask]
print("\nЭлементы > 10:", filtered)
print("Их количество :", filtered.size)
print("Среднее       :", filtered.mean())

row_means = a.mean(axis=1, keepdims=True)    
centered = a - row_means
print("\nСредние по строкам (6,1):\n", row_means)
print("Форма результата:", centered.shape)    
print("Суммы по строкам (≈0):\n", centered.sum(axis=1))
print("Максимум |суммы|:", np.abs(centered.sum(axis=1)).max())