# Q1.
ins <- read.csv("C:/Users/sec/Downloads/insurance.csv")

str(ins)
library(tidyr)
library(stringr)

library(dpltr)
library(lubridate)

# Q2.
glimpse(ins)
View(ins)
str(ins)
# Q3.
ins$bmi[which.max(ins$bmi)]
ins$bmi_range <- cut(ins$bmi, breaks = c(0, 18.5, 24.9, 53.13), right=T, labels = c("light", "normal", "heavy"))
tapply(ins$charges, ins$bmi_range, mean)

# Q4.
ins_male <- ins[which(ins$sex=='male'), ]
ins_female <- ins[which(ins$sex=='female'), ]
# Q5.
mean(ins_male$bmi)
mean(ins_female$bmi)
var(ins_male$bmi)
var(ins_female$bmi)
plot(density(ins_male$bmi))
plot(density(ins_female$bmi))
plot(density(ins$charges))


# Q6.
tapply(ins$charges, ins$smoker, mean)

# Q7.
plot(tapply(ins$charges, ins$children, mean))


# Q8.
quantile(ins$age, c(0.1,0.9))nrow(ins_male)/nrow(ins_male[which(ins_male$smoker == "yes"), ])
ins_young <- ins[which(ins$age<= 19), ]
ins_old <- ins[which(ins$age >= 59), ]
Y <- mean(ins_young$charges)
O <- mean(ins_old$charges)
O - Y

# Q9.
tapply(ins$charges, ins$sex, mean)

# Q10.
nrow(ins_male[which(ins_male$smoker == "yes"), ])/nrow(ins_male)
nrow(ins_male[which(ins_female$smoker == "yes"), ])/nrow(ins_female)

mean(ins_male$charges) # 남성이 더 보험료 큼
mean(ins_female$charges)

nrow(ins_male[which(ins_male$smoker == 'yes'), ])
nrow(ins_female[which(ins_female$smoker == 'yes'), ])
ins$sex <- as.factor(ins$sex)

summary(lm(ins$charges~ ins$age+ins$sex+ins$children+ins$smoker+ins$region))

summary(lm(ins_male$charges~ ins_male$age+ins_male$children+ins_male$smoker+ins_male$region))

summar9y(lm(ins_female$charges~ ins_female$age+ins_female$children+ins_female$smoker+ins_female$region))


ins <- transform(ins, sex_male = ifelse(sex =="male", 1, 0), 
                      sex_female = ifelse(sex=="female", 1, 0),
                      smoker_yes = ifelse(smoker == "yes", 1, 0),
                      smoker_no = ifelse(smoker == "no", 1, 0))
View(ins) 

summary(lm(ins$charges ~ ins$age + ins$children + ins$sex_male + ins$sex_female + ins$smoker_yes + ins$smoker_no))

install.packages("dummies")
library(dummies)
inss <- dummy.data.frame(ins)
View(inss)

summary(lm(charges~., data = inss))

ins$smoker_dummys 






# Tidy Data

auto <- read.table("C:/Users/sec/Downloads/automobile.tsv", header = T)
View(auto)
auto <- spread(auto, specification, value)

colnames(auto)
