@[TOC](DOcplex之整数规划)

# 举例：混合整数规划
```
max 800*x1 + 300*x2
s. t. 
	6 * x1 + 8 * x2 <= 120
	10 * x1 + 5 * x2 <= 100
	x1, x2 >= 0 且均为整数
```
## 创建模型

```python
from docplex.model import Model

model = Model()
```

## 添加变量
```python
#创建变量列表
x_list = [i for i in range(2)] 
X = model.integer_var_list(x_list, name='x')
```
上面一次性创建三个X变量，不懂得可以参考前面一篇线性规划的文章

## 添加目标函数
$max:800*x1 + 300*x2$
```python
model.maximize(4*X[0] + 6*X[1] + 2*X[2])
```
## 添加约束条件
**s.t.**
$6 * x1 + 8 * x2 <= 120$
$10 * x1 + 5 * x2 <= 100$
```python
model.add_constraint(4*X[0] - 4*X[1] >= 7)
model.add_constraint(-X[0] + 6*X[1] <= 5)
model.add_constraint(-X[0] + X[1] + X[2] <= 5)
```
## 求解模型
```python
sol = model.solve() #输出解
print（sol） #获取默认形式的输出
print(sol.get_all_values()) #获取所有的变量解
print(sol.solve_details) #获取解的详细信息，如时间，gap值等
```
```python
# print（sol）
solution for: docplex_model1
objective: 8000
x_0=10
# print(sol.get_all_values())
[10.0, 0]
# print(sol.solve_details)
status  = integer optimal solution
time    = 0.015 s.
problem = MILP
gap     = 0%
```
目标值8000
x1=10
x2=0
求解时间0.015s（飞一样速度，相比手算）
gap=0（精确解无疑了）
