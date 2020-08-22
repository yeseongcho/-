Linear Regression Part

unemployment <- read.csv("https://github.com/hbchoi/SampleData/raw/master/unemployment.csv")

library(caret)
library(ROCR)
library(tidyr)
library(stringr)
library(dplyr)
library(ggplot2)
unemployment

alpha <- 1
unemployment$est_y <- alpha* unemployment$male_unemployment
unemployment$error <- unemployment$female_unemployment - unemployment$est_y

unemployment

# MSE
mean(unemployment$error**2)

# 그래프화
plot(x = unemployment$male_unemployment, y = unemployment$female_unemployment,
     main = 'simple example', 
     xlab = 'male unemployment rate %', 
     ylab = 'fmale unemployment rate %', 
     xlim = c(0, 10), ylim = c(0, 10))
abline(0, alpha, col='red')
text(x=2, y=8, 'y=x', col='red')

# alpha를 바꾸어보면?
alpha <- 0.9
# 조금 더 에러값이 감소한다!!

# alpha값이 변할 때마다 MSE값 추적
# 이렇게 코드를 구성하는 연습을 해본다!
findMSE <- function(alpha){
  mse <- mean((unemployment$female_unemployment - unemployment$male_unemployment*alpha)**2)
}
alpha_list <- seq(0.5, 1.5, 0.01)
MSE_list <- sapply(alpha_list, findMSE)
plot(x=alpha_list, y=MSE_list, xlab = 'alpha', ylab = 'MSE')
best_alpha <- alpha_list[which.min(MSE_list)]
best_alpha

# best_alpha로 다시 값을 개선
plot(x=unemployment$male_unemployment, y=unemployment$female_unemployment)
abline(0, best_alpha, col='red')

# 하지만 원래 절편항이 있음을 인지 -- 에러텀의 느낌이겠지
# 편의상 이를 beta항이라고 하자
alpha <- 0.6945
beta <- 1.4341
unemployment$est_y <- alpha*unemployment$male_unemployment + beta
unemployment$error <- unemployment$female_unemployment - unemployment$est_y
unemployment
mean(unemployment$error**2)

fmla <-female_unemployment~male_unemployment
unemployment_model <- lm(fmla, data=unemployment)
summary(unemployment_model)

# 요기 전처리 과정 이해한다.
plot(mtcars$wt, mtcars$mpg)
fit.line <- lm(mpg~wt, data=mtcars)
abline(fit.line, col='red')
cf <- round(coef(fit.line),2)
eq <- paste0('mpg = ', cf[1], ifelse(sign(cf[2])==1, '+', '-'), abs(cf[2]), " car weight")
mtext(eq,3,line=-2)

# 보험료 징수 예측 데이털르 통해 한번 분석해보자
load(url('https://github.com/hbchoi/SampleData/raw/master/insurance.RData'))
str(insurance)

# createDataPartition말고도 학습, 테스트 분할하는 방법을 다 알고 있어야 한다.
# 교수님의 방법을 참고해보자
set.seed(2020)
ncustomer <- nrow(insurance)
rgroup <- runif(ncustomer)
train.df <- subset(insurance, rgroup <= 0.8)
test.df <- subset(insurance, rgroup > 0.8)

dim(train.df)
dim(test.df)

ins_model1 <- lm(charges~ age + sex + bmi + children + smoker + region, data = train.df)
ins_model1

# User defined Function
calcRMSE <- function(label, estimation){
  return(sqrt(mean(label - estimation)**2))
}
calcR2 <- function(label, estimation){
  RSS = sum((label-estimation)**2)
  SStot = sum((label-mean(label))**2)
  return(1-RSS/SStot)
}

train.df$pred <- predict(ins_model1, newdata=train.df)
test.df$pred <- predict(ins_model1, newdata = test.df)
calcRMSE(train.df$charges, train.df$pred)
calcR2(train.df$charges, train.df$pred)
calcRMSE(test.df$charges, test.df$pred)
calcR2(test.df$charges, test.df$pred)



summary(ins_model1)
# 모형 자체에 대한 시각화
ggplot(train.df, aes(x=pred, y=charges))+
  geom_point(alpha = 0.2, col ='black')+
  geom_smooth()+
  geom_line(aes(x=charges,y=charges), col='blue', linetype=2)

# 
ggplot(train.df, aes(x=pred,y=pred-charges))+
  geom_point(alpha=0.2, col='black')+
  geom_smooth()+
  geom_hline(yintercept=0, col='blue',linetype=2)


###### 개중요 피처링 파트############### 실제로 R2를 높이는 다양한 인사이트들이 있다!!

# 1) 제곱을 해주는 파트
# 2) range변수화
# 3) 상호작용항

train.df$bmi30 <- ifelse(train.df$bmi >= 30, 1, 0)
test.df$bmi30 <- ifelse(test.df$bmi>=30, 1, 0)
ins_model <- lm(charges~ age+ I(age^2)+sex+bmi+children+bmi30*smoker+region, train.df)
summary(ins_model)
train.df$pred <- predict(ins_model, newdata=train.df)
test.df$pred <- predict(ins_model, newdata=test.df)
# 이제 이렇게 나온 녀석을 가지고 test에도 적용해주는 과정이 남았다!
calcRMSE(train.df$charges, train.df$pred)
calcR2(train.df$charges, train.df$pred)
calcRMSE(test.df$charges, test.df$pred)
calcR2(test.df$charges, test.df$pred)

# 동일하게 시각화과정을 거쳐준다!
ggplot(train.df, aes(x=pred, y=charges))+
  geom_point(alpha = 0.2, col ='black')+
  geom_smooth()+
  geom_line(aes(x=charges,y=charges), col='blue', linetype=2)

# 
ggplot(train.df, aes(x=pred,y=pred-charges))+
  geom_point(alpha=0.2, col='black')+
  geom_smooth()+
  geom_hline(yintercept=0, col='blue',linetype=2)


quiz <- data.frame(A=c(0,1,2,3,4,5,6), B=c(0,55,120,188,252,307,366))
quiz

quizs <- lm(B~A, data=quiz)

quiz2 <- data.frame(x=c(2,5,10,15,20), y=c(1,25,21,32,41))
quiz2
quizs2 <- lm(y~x, data=quiz2)
quizs2

quiz3 <- data.frame(x=c(5,10,2,4,12,9), y=c(T,T,F,F,T,F))
quizs3 <- glm(y~x, data=quiz3, family=binomial(link='logit'))
coefficients(quizs3)

answer <- 0.383*20-2.679
answer
sigmoid(answer)
1/(1+exp(-answer))
