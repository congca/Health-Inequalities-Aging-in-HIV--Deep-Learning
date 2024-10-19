# 加载所需的包
library(dplyr)
library(car)
library(broom)

 # 选择因变量
dependent_vars <- c("aar", "eeaa", "peaa", "geaa", "dnamtladjage")

# 创建一个空的数据框来存储结果
model_results <- data.frame()

# 循环构建模型
for (dep_var in dependent_vars) {
  # 将 macsidnumber 转换为因子变量
  data$macsidnumber <- as.factor(data$macsidnumber)
  
  # 创建线性回归模型，包含地区和其他控制变量
  formula <- as.formula(paste(dep_var, "~ macsidnumber * (Precipitation + Temperature + white + educbas)"))
  
  model <- lm(formula, data = data)
  
  # 检查多重共线性
  vif_values <- vif(model, type = 'predictor')
  
  # 收集模型结果
  model_summary <- summary(model)
  
  # 提取自变量名称
  independent_vars <- all.vars(formula)[-1]  # 去掉因变量名称
  independent_vars_str <- paste(independent_vars, collapse = ", ")  # 合并成字符串
  
  # 整理结果
  result <- tibble(
    dependent_variable = dep_var,  # 因变量名称
    independent_variables = independent_vars_str,  # 自变量名称
    coefficients = list(model_summary$coefficients),  # 模型系数
    r_squared = model_summary$r.squared,  # R平方值
    vif = list(vif_values)  # VIF值
  )
  
  model_results <- bind_rows(model_results, result)
}

# 查看 model_results
print(model_results)
R.version.string
