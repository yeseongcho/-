library(dplyr)
library(tidyr)
library(ggplot2)
library(reshape2)
library(caret)
library(ROCR)
library(rpart)
library(class)
library(leaps)
library(kknn)
library(MASS)
library(earth)
library(randomForest)

balanced_accuracy <- function(tb){
  sensitivity <- sum(tb[1,1])/sum(tb[,1])
  specificity <- sum(tb[2,2])/sum(tb[,2])
  return((sensitivity+specificity)/2)
  
}

calcRMSE <- function(label, estimation){
  return(sqrt(mean((label-estimation)**2)))
}

load("C:/Users/sec/Desktop/교과목들/데이터 과학/final_test.RData")
# 데이터셋을 확인

# type 전환등 할거 하고 type 들 안맞을 수 있으니까 확인

# randomForest 적용 --> 미리 넣어봄

# 변수 추출 및 본격적인 주물럭

str(shopping_trains)
shopping_trains <- shopping_train
shopping_tests <- shopping_test

shopping_trains$SpecialDay <- as.factor(shopping_trains$SpecialDay)
shopping_tests$SpecialDay <- as.factor(shopping_tests$SpecialDay)

shopping_trains$SpecialDay <- as.numeric(shopping_trains$SpecialDay)
shopping_tests$SpecialDay <- as.numeric(shopping_tests$SpecialDay)

shopping_trains$OperatingSystems <- as.factor(shopping_trains$OperatingSystems)
shopping_tests$OperatingSystems <- as.factor(shopping_tests$OperatingSystems)

shopping_trains$OperatingSystems <- as.numeric(shopping_trains$OperatingSystems)
shopping_tests$OperatingSystems <- as.numeric(shopping_tests$OperatingSystems)

shopping_trains$Browser <- as.factor(shopping_trains$Browser)
shopping_tests$Browser <- as.factor(shopping_tests$Browser)

shopping_trains$Browser <- as.numeric(shopping_trains$Browser)
shopping_tests$Browser <- as.numeric(shopping_tests$Browser)

shopping_trains$Region <- as.factor(shopping_trains$Region)
shopping_tests$Region <- as.factor(shopping_tests$Region)

shopping_trains$Region <- as.numeric(shopping_trains$Region)
shopping_tests$Region <- as.numeric(shopping_tests$Region)

shopping_train$Weekend <- as.factor(shopping_train$Weekend)
shopping_test$Weekend <- as.factor(shopping_test$Weekend)
shopping_train$Weekend <- as.logical(shopping_train$Weekend)
shopping_test$Weekend <- as.logical(shopping_test$Weekend)

shopping_trains$Region <- as.numeric(shopping_trains$Region)
shopping_tests$Region <- as.numeric(shopping_tests$Region)

shopping_trains$TrafficType <- as.factor(shopping_trains$TrafficType)
shopping_tests$TrafficType <- as.factor(shopping_tests$TrafficType)

shopping_trains$TrafficType <- as.numeric(shopping_trains$TrafficType)
shopping_tests$TrafficType <- as.numeric(shopping_tests$TrafficType)

shopping_trains$Revenue <- as.factor(shopping_trains$Revenue)
shopping_trains$Revenue <- as.logical(shopping_trains$Revenue)

shopping_trains <- shopping_train
shopping_tests <- shopping_test

str(shopping_trains)
str(shopping_train)
str(shopping_train)
str(shopping_tests)

table(shopping_trains$SpecialDay)
table(shopping_tests$SpecialDay)

names(shopping_trains)
nrow(shopping_tests)
shopping_trains <- shopping_trains[, c(-19, -20)]
shopping_tests <- shopping_tests[, c(-18, -19)]
ncol(shopping_trains)

rf.fit <- randomForest(Revenue~., data=shopping_trains, mtry=4, ntree=500, importance=T)
shopping_trains$pred <- predict(rf.fit, newdata=shopping_trains, type='response')
aggregate(pred~Revenue, data=shopping_trains, mean)

shopping_trains$pred_logic <- ifelse(shopping_trains$pred >0.5, TRUE, FALSE)
tb <- table(pred = shopping_trains$pred_logic, actual = shopping_trains$Revenue)
tb
balanced_accuracy(tb)
p_rf <- prediction(shopping_trains$pred, shopping_trains$Revenue)
p_auc <- performance(p_rf, 'auc')
p_auc@y.values[[1]]

names(shopping_tests)

shopping_tests$pred <- predict(rf.fit, newdata=shopping_tests, type='response')
length(shopping_tests$pred)
shopping_tests$pred_logic  <- ifelse(shopping_tests$pred >0.5, 1, 0)
prob_shopping_test <- shopping_tests$pred
pred_shopping_test <- shopping_tests$pred_logic
save(prob_shopping_test, pred_shopping_test, pred_housing_test, file="st21600685.RData")
str(shopping_trains)
stepAIC(logistics1, direction="both")
# PageValue랑 ProductRelated는 고민좀
earth <- earth(Revenue~., data=shopping_train, nfold=5, ncross=3)
evimp(earth)
sub.fit <-regsubsets(Revenue~. ,data=shopping_train)
plot(sub.fit, scale='Cp')
earths <- earth(Revenue~Administrative+Administrative_Duration+Informational+Informational_Duration+ProductRelated+ProductRelated_Duration+
                  +BounceRates+ExitRates+SpecialDay+Month+Region*TrafficType+VisitorType+Weekend+Region+
                  PageValues+Administrative*PageValues+
                  Informational*SpecialDay+BounceRates*ExitRates+TrafficType*Region+VisitorType*Region+PageValues*BounceRates+
                  PageValues*ExitRates+Administrative_Duration*PageValues+Month*ExitRates+Administrative*SpecialDay+
                  Administrative_Duration*PageValues+PageValues*ProductRelated+Month*ProductRelated+ProductRelated*Informational+
                  Administrative*ProductRelated
                , data=shopping_trains, nfold=5, ncross=3)
evimp(earths)
shopping_trains$pred <- predict(earths, newdata=shopping_trains, type='response')
aggregate(pred~Revenue, data=shopping_trains, mean)
shopping_trains$pred_logic <- ifelse(shopping_trains$pred > 0.4, TRUE, FALSE)
tbs <- table(pred=shopping_trains$pred_logic, actual = shopping_trains$Revenue)
tbs
balanced_accuracy(tbs)
p <- prediction(shopping_trains$pred, shopping_trains$Revenue)
auc <- performance(p, 'auc')
auc@y.values[[1]]
shopping_tests$pred <- predict(earths, newdata=shopping_tests, type='response')
shopping_tests$pred_logic  <- ifelse(shopping_tests$pred >0.4, 1, 0)
prob_shopping_test <- shopping_tests$pred
pred_shopping_test <- shopping_tests$pred_logic
save(prob_shopping_test, pred_shopping_test, pred_housing_test, file="st21600685.RData")

str(shopping_trains)

plot(density(shopping_trains$BounceRates))
plot(density(shopping_trains$ExitRates))

logistics1 <- glm(Revenue~Administrative+Administrative_Duration+Informational+Informational_Duration+ProductRelated+ProductRelated_Duration+
                    BounceRates+ExitRates+SpecialDay+Month+Browser+Region*TrafficType+VisitorType+Weekend+Region+TrafficType+
                    PageValues+SpecialDay*Weekend+VisitorType*Browser+Browser*OperatingSystems+Informational*Informational_Duration+
                    Informational*SpecialDay
                    
                    , data=shopping_trains, family=binomial)
shopping_trains$pred <- predict(logistics1, newdata=shopping_trains, type='response')
aggregate(pred~Revenue, data=shopping_trains, mean)
shopping_trains$pred_logic <- ifelse(shopping_trains$pred >0.46, TRUE, FALSE)
tbs <- table(pred=shopping_trains$pred_logic, actual = shopping_trains$Revenue)
tbs
p <- prediction(shopping_trains$pred, shopping_trains$Revenue)
auc <- performance(p, 'auc')
auc@y.values[[1]]
shopping_tests$pred <- predict(logistics1, newdata=shopping_tests, type='response')
shopping_tests$pred_logic  <- ifelse(shopping_tests$pred >0.4, 1, 0)
prob_shopping_test <- shopping_tests$pred
pred_shopping_test <- shopping_tests$pred_logic
save(prob_shopping_test, pred_shopping_test, pred_housing_test, file="st21600685.RData")



logistics <- glm(Revenue~Administrative+Administrative_Duration+Informational+Informational_Duration+ProductRelated+ProductRelated_Duration+
                   BounceRates+ExitRates+SpecialDay+Month+OperatingSystems+Browser+Region+TrafficType+VisitorType+Weekend+
                   TrafficType*VisitorType+Browser*VisitorType+
                   SpecialDay*Weekend+Browser*TrafficType+PageValues+Informational*Informational+ProductRelated*ProductRelated_Duration+
                   TrafficType*ProductRelated
                   , data=shopping_trains, family=binomial)
shopping_trains$pred <- predict(logistics, newdata=shopping_trains, type='response')
aggregate(pred~Revenue, data=shopping_trains, mean)
shopping_trains$pred_logic <- ifelse(shopping_trains$pred >0.56, TRUE, FALSE)
p <- prediction(shopping_trains$pred, shopping_trains$Revenue)
auc <- performance(p, 'auc')
auc@y.values[[1]]

table(shopping_trains$TrafficType)
table(shopping_tests$TrafficType)


shopping_tests$pred <- predict(logistics, newdata=shopping_tests, type='response')


shopping_tests$pred_logic  <- ifelse(shopping_tests$pred >0.4, 1, 0)
prob_shopping_test <- shopping_tests$pred
pred_shopping_test <- shopping_tests$pred_logic
save(prob_shopping_test, pred_shopping_test, file="st21600685.RData")


housing_trains <- housing_train
housing_tests <- housing_test

str(housing_train)

summary(housing_trains$X2)
library(lubridate)
housing_trains$age_group <- cut(housing_trains$X2, breaks = c(0,8.95,15.60,17.24,26.55,43.80,Inf), lables=c("1","2","3","4","5","6"), right=F)
housing_tests$age_group <- cut(housing_tests$X2, breaks = c(0,8.95,15.60,17.24,26.55,43.80,Inf), lables=c("1","2","3","4","5","6"), right=F)

housing_trains <- housing_trains[, c(-1)]
housing_tests <- housing_tests[, c(-1)]

housing_trains$X4 <- as.factor(housing_trains$X4)
housing_tests$X4 <- as.factor(housing_tests$X4)
housing_trains$X4 <- as.numeric(housing_trains$X4)
housing_tests$X4 <- as.numeric(housing_tests$X4)
table(housing_trains$X4)
table(housing_tests$X4)
str(housing_trains)
rf.fit2 <- randomForest(Y~., data=housing_trains, mtry=3, ntree=700, importance=T)
rf.fitts <- predict(rf.fit2, newdata=housing_trains)
rf.tests <- predict(rf.fit2, newdata=housing_tests)
calcRMSE(rf.fitts, housing_trains$Y)
pred_housing_test <- as.vector(rf.tests)
save(prob_shopping_test, pred_shopping_test, pred_housing_test, file="st21600685.RData")
pred_housing_final_test <- pred_housing_test

