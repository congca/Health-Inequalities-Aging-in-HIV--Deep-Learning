#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('Normalization.csv')

# 查看数据的基本信息
print(df.info())
print(df.describe())
print(df.isnull().sum())  # 检查缺失值


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns

# 可视化因变量的分布
plt.figure(figsize=(10, 5))
sns.histplot(df['aar'], bins=30, kde=True)
plt.title('Distribution of AAR')
plt.xlabel('AAR')
plt.ylabel('Frequency')
plt.show()



# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

# 可视化因变量的分布
plt.figure(figsize=(10, 5))
sns.histplot(df['eeaa'], bins=30, kde=True)
plt.title('Distribution of EEAA')
plt.xlabel('EEAA')
plt.ylabel('Frequency')
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns

# 可视化因变量的分布
plt.figure(figsize=(10, 5))
sns.histplot(df['peaa'], bins=30, kde=True)
plt.title('Distribution of peaa')
plt.xlabel('peaa')
plt.ylabel('Frequency')
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns

# 可视化因变量的分布
plt.figure(figsize=(10, 5))
sns.histplot(df['geaa'], bins=30, kde=True)
plt.title('Distribution of geaa')
plt.xlabel('geaa')
plt.ylabel('Frequency')
plt.show()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns

# 可视化因变量的分布
plt.figure(figsize=(10, 5))
sns.histplot(df['dnamtladjage'], bins=30, kde=True)
plt.title('Distribution of dnamtladjage')
plt.xlabel('dnamtladjage')
plt.ylabel('Frequency')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

# 定义因变量列表
dependent_vars = ['aar', 'eeaa', 'peaa', 'geaa', 'dnamtladjage']

# 创建子图
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
axes = axes.flatten()  # 便于访问每个子图

# 绘制每个因变量与Ozone的散点图
for i, var in enumerate(dependent_vars):
    axes[i].scatter(df['Ozone'], df[var], alpha=0.6)
    axes[i].set_title(f'Ozone vs {var}')
    axes[i].set_xlabel('Ozone')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

# 如果需要的话可以添加一个额外的子图用于展示整体的Ozone分布
axes[-1].scatter(df['Ozone'], df['Ozone'], color='red', alpha=0.3)
axes[-1].set_title('Ozone Distribution')
axes[-1].set_xlabel('Ozone')
axes[-1].set_ylabel('Ozone')
axes[-1].grid(True)

plt.tight_layout()
plt.show()


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

# 设置Seaborn风格
sns.set(style="whitegrid")

# 定义因变量列表
dependent_vars = ['aar', 'eeaa', 'peaa', 'geaa', 'dnamtladjage']

# 创建子图
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
axes = axes.flatten()  # 便于访问每个子图

# 绘制箱线图
for i, var in enumerate(dependent_vars):
    sns.boxplot(data=df, x='Temperature', y=var, ax=axes[i], palette="Set2")
    axes[i].set_title(f'Temperature vs {var}')
    axes[i].set_xlabel('Temperature')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

# 添加一个额外的子图用于小提琴图
for i, var in enumerate(dependent_vars):
    sns.violinplot(data=df, x='Temperature', y=var, ax=axes[i], palette="Set2", inner="quartile")
    axes[i].set_title(f'Temperature vs {var}')
    axes[i].set_xlabel('Temperature')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

plt.tight_layout()
plt.show()


# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt

# 设置Seaborn风格
sns.set(style="whitegrid")

# 定义因变量列表
dependent_vars = ['aar', 'eeaa', 'peaa', 'geaa', 'dnamtladjage']

# 创建子图
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
axes = axes.flatten()  # 便于访问每个子图

# 绘制每个因变量与Temperature的散点图
for i, var in enumerate(dependent_vars):
    sns.scatterplot(data=df, x='Temperature', y=var, ax=axes[i], alpha=0.6)
    axes[i].set_title(f'Temperature vs {var}')
    axes[i].set_xlabel('Temperature')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

# 添加一个额外的子图用于展示整体的Temperature分布
sns.histplot(df['Temperature'], bins=30, kde=True, ax=axes[-1], color='red', alpha=0.5)
axes[-1].set_title('Temperature Distribution')
axes[-1].set_xlabel('Temperature')
axes[-1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('Distribution.png', dpi=300)

plt.show()


# In[12]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设 df 是你的数据框
# 将第一列重命名为地理位置
location_mapping = {
    0: 'Baltimore',
    0.333333333: 'Chicago',
    1: 'Pittsburgh',
    0.666666667: 'LA'
}

# 替换第一列的值
df[df.columns[0]] = df[df.columns[0]].replace(location_mapping)

# 设置Seaborn风格
sns.set(style="whitegrid")

# 定义因变量列表
dependent_vars = ['aar', 'eeaa', 'peaa', 'geaa', 'dnamtladjage']

# 创建子图
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(18, 20))
axes = axes.flatten()  # 便于访问每个子图

# 绘制分组箱线图
for i, var in enumerate(dependent_vars):
    sns.boxplot(data=df, x=df.columns[0], y=var, ax=axes[i], palette="Set2")
    axes[i].set_title(f'{df.columns[0]} vs {var} (Boxplot)')
    axes[i].set_xlabel('Geographic Location')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

# 绘制小提琴图
for i, var in enumerate(dependent_vars):
    sns.violinplot(data=df, x=df.columns[0], y=var, ax=axes[i + len(dependent_vars)], palette="Set2", inner="quartile")
    axes[i + len(dependent_vars)].set_title(f'{df.columns[0]} vs {var} (Violin)')
    axes[i + len(dependent_vars)].set_xlabel('Geographic Location')
    axes[i + len(dependent_vars)].set_ylabel(var)
    axes[i + len(dependent_vars)].grid(True)

plt.tight_layout()
plt.savefig('Location .png', dpi=300)

plt.show()



# In[15]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设 df 是你的数据框
# 计算降水量和温度的95th百分位数
precipitation_threshold = df['Precipitation'].quantile(0.95)
temperature_threshold = df['Temperature'].quantile(0.95)

# 创建新的列指示极端天气事件
df['Extreme_Precipitation'] = df['Precipitation'] > precipitation_threshold
df['Extreme_Temperature'] = df['Temperature'] > temperature_threshold

# 定义因变量列表
dependent_vars = ['aar', 'eeaa', 'peaa', 'geaa', 'dnamtladjage']

# 创建可视化图形
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(18, 20))
axes = axes.flatten()  # 便于访问每个子图

# 绘制极端降水量对因变量的影响
for i, var in enumerate(dependent_vars):
    sns.boxplot(data=df, x='Extreme_Precipitation', y=var, ax=axes[i], palette="Set2")
    axes[i].set_title(f'Extreme Precipitation vs {var} (Boxplot)')
    axes[i].set_xlabel('Extreme Precipitation')
    axes[i].set_ylabel(var)
    axes[i].grid(True)

# 绘制极端温度对因变量的影响
for i, var in enumerate(dependent_vars):
    sns.boxplot(data=df, x='Extreme_Temperature', y=var, ax=axes[i + len(dependent_vars)], palette="Set2")
    axes[i + len(dependent_vars)].set_title(f'Extreme Temperature vs {var} (Boxplot)')
    axes[i + len(dependent_vars)].set_xlabel('Extreme Temperature')
    axes[i + len(dependent_vars)].set_ylabel(var)
    axes[i + len(dependent_vars)].grid(True)

plt.tight_layout()
plt.savefig('Impact of extreme precipitation and temperature in different cities on AAR, EEAA, dnamtladjage, and PEAA.png', dpi=300)
plt.show()


# In[16]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设 df 是你的数据框，且第一列已重命名为地理位置
# 计算降水量和温度的95th百分位数
precipitation_threshold = df['Precipitation'].quantile(0.95)
temperature_threshold = df['Temperature'].quantile(0.95)

# 创建新的列指示极端天气事件
df['Extreme_Precipitation'] = df['Precipitation'] > precipitation_threshold
df['Extreme_Temperature'] = df['Temperature'] > temperature_threshold

# 创建可视化图形
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(18, 20))
axes = axes.flatten()  # 便于访问每个子图

# 绘制城市与极端降水量的GEAA影响
for i, city in enumerate(df[df.columns[0]].unique()):
    city_data = df[df[df.columns[0]] == city]
    sns.boxplot(data=city_data, x='Extreme_Precipitation', y='geaa', ax=axes[i], palette="Set2")
    axes[i].set_title(f'{city} - Extreme Precipitation vs GEAA (Boxplot)')
    axes[i].set_xlabel('Extreme Precipitation')
    axes[i].set_ylabel('GEAA')
    axes[i].grid(True)

# 绘制城市与极端温度的GEAA影响
for i, city in enumerate(df[df.columns[0]].unique()):
    city_data = df[df[df.columns[0]] == city]
    sns.boxplot(data=city_data, x='Extreme_Temperature', y='geaa', ax=axes[i + len(df[df.columns[0]].unique())], palette="Set2")
    axes[i + len(df[df.columns[0]].unique())].set_title(f'{city} - Extreme Temperature vs GEAA (Boxplot)')
    axes[i + len(df[df.columns[0]].unique())].set_xlabel('Extreme Temperature')
    axes[i + len(df[df.columns[0]].unique())].set_ylabel('GEAA')
    axes[i + len(df[df.columns[0]].unique())].grid(True)

plt.tight_layout()
plt.savefig('Impact of extreme precipitation and temperature in different cities on GEAA.png', dpi=300)
plt.show()


# In[ ]:





# In[ ]:




