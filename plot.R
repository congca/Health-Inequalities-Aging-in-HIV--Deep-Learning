
# Load necessary libraries
library(tidyverse)
library(dplyr)
library(ggplot2)
library("readxl")

setwd("C:/Users/congc/Desktop/New folder")
data <- read.csv("Normalization.csv")
raw <- read.csv("Original.csv")

raw$Precipitation <- as.numeric(as.factor(raw$Precipitation))
raw$Temperature <- as.numeric(as.factor(raw$Temperature))


png('Distribution of Environmental Variables.png', height = 15, width = 25, units = 'cm', res = 300)
plot.new()
# 将数据转换为长格式，以便绘图
long_data <- raw %>%
  select(Precipitation, Temperature, SPWPM2.5, SBMPM2.5, CO, COAQI, NO2, NO2AQI, Ozone, OzoneAQI, SO2, SO2AQI) %>%
  pivot_longer(cols = everything(), names_to = "Variable", values_to = "Value")
# 绘制密度图
ggplot(long_data, aes(x = Value, fill = Variable)) +
  geom_density(alpha = 0.5) +
  facet_wrap(~ Variable, scales = "free") +
  labs(title = "Distribution of Environmental Variables", x = "Value", y = "Density") +
  theme_minimal()
dev.off()




# Save the plot as a PNG file
png('Distribution of Outcome Variables.png', height = 15, width = 25, units = 'cm', res = 300)
plot.new()
# Convert data to long format for plotting
long_data <- raw %>%
  select(aar, eeaa, peaa, geaa, dnamtladjage) %>%
  pivot_longer(cols = everything(), names_to = "Variable", values_to = "Value")

# Create the density plot with narrower density areas
ggplot(long_data, aes(x = Value, fill = Variable)) +
  geom_density(alpha = 0.5, adjust = 0.5) +  # Adjust the width of the density plot
  facet_wrap(~ Variable, scales = "free") +
  labs(title = "Distribution of Outcome Variables", x = "Value", y = "Density") +
  theme_minimal() +
  theme(legend.position = "none")  # Optional: remove legend for clarity

dev.off()




raw$casecontrol <- as.numeric(as.factor(raw$casecontrol))
raw$white <- as.numeric(as.factor(raw$white))
# Save the plot as a PNG file
# Check for non-finite values in the continuous variables
summary(raw$cum_pkyear)  # Check for NA, Inf, or -Inf
summary(raw$bmi)
# Optionally, remove non-finite values
raw_clean <- raw %>%
  filter(!is.na(cum_pkyear), !is.na(bmi), is.finite(cum_pkyear), is.finite(bmi))

# Save the plot as a PNG file
png('Distribution of Predictors.png', height = 15, width = 25, units = 'cm', res = 300)
plot.new()

# Convert the data to long format for categorical variables
long_data_cat <- raw_clean %>%
  select(casecontrol, white, educbas, visit, macsvisit, hivatvisit) %>%
  pivot_longer(cols = everything(), names_to = "Variable", values_to = "Category")

# Create the bar plots for categorical variables
p1 <- ggplot(long_data_cat, aes(x = Category, fill = Variable)) +
  geom_bar(position = "dodge", color = "black", width = 0.3) +  # Adjust width for aesthetics
  facet_wrap(~ Variable, scales = "free") +
  labs(title = "Distribution of Categorical Predictors", x = "Category", y = "Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"))  # Custom colors
# Create separate plots for continuous variables
p2_bmi <- ggplot(raw_clean, aes(x = bmi)) +
  geom_histogram(binwidth = 1, fill = "#1f77b4", color = "black", alpha = 0.7) +
  labs(title = "Distribution of BMI", x = "BMI", y = "Count") +
  theme_minimal()
 
p2_cum_pkyear <- ggplot(raw_clean, aes(x = cum_pkyear)) +
  geom_histogram(binwidth = 1, fill = "#ff7f0e", color = "black", alpha = 0.7) +
  labs(title = "Distribution of Cumulative Pack Years", x = "Cumulative Pack Years", y = "Count") +
  theme_minimal()

# Combine the two plots
combined_plot <- (p1 / p2_bmi) / p2_cum_pkyear  # Stack the plots vertically

# Save the combined plot as a PNG file
ggsave("Distribution of Predictors.png", plot = combined_plot, height = 15, width = 25, units = "cm", dpi = 300)
 
dev.off()

