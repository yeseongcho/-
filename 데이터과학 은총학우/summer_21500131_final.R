library(caret)
library(tidyr)
library(tidyverse)
library(Epi)
library(ROCR)
library(class)
library(dplyr)
library(cluster)
library(fpc)

# get_arruracy 
get_acuuracy <- function(pred, actual){
  tble <- table(actual, pred)
  return( (tble[1,1]+tble[2,2])/sum(tble))
}

table(actual = train$income, pred = train$prediction_workclass)
table( pred = train$prediction_workclass , actual =train$income)

# get_precision
table(actual = train$income, pred = train$prediction_workclass)

get_precision <- function(pred, actual){
  tble <- table(actual, pred)
  return( (tble[2,2])/ sum(tble[1,2],tble[2,2]))
}



#############################################################################

calAUC <- function(predCol, targetCol){
  perf <- performance(prediction(predCol, targetCol), 'auc') 
  as.numeric(perf@y.values)
}


knn_AUC <- function(k_value){
  test.knn_pred_P <- knn(train = train.knn_new , test = test.knn_new , cl = train.knn_label, k = k_value, prob = TRUE)
  test_pred_prob <- ifelse(test.knn_pred_P == 'rich', 
                           attributes(test.knn_pred_P)$prob,
                           1-attributes(test.knn_pred_P)$prob)
  a <- calAUC(test_pred_prob,test.knn_label== 'rich')
}

#############################################################################
# classification
#### logistic

occupancy_train <- read_csv("occupancy_train.csv")
occupancy_test <- read_csv("occupancy_test_student.csv")

occ.train <- occupancy_train 
occ.test <- occupancy_test



###Stepwise Regression 
names(occ.train )
occ.train$Occupancy <- as.factor(occ.train$Occupancy)




# 종속변수 확인
occ.train$Occupancy <- as.factor(occ.train$Occupancy)


###########
str(occ.train)
occ.train$date_time <- as.character.Date(occ.train$date)
occ.train <- separate(occ.train, date, c("year", "month", "day"),sep="-")
str(occ.train)
occ.train <- occ.train[,-3]
str(occ.train)
occ.train <- occ.train[,-1]
str(occ.train)
occ.train <- occ.train[,-8]

names(occ.train)

#########

model <- glm(Occupancy ~  Temperature+ Humidity +  Light   +  CO2 +HumidityRatio, data = occ.train, 
             family = binomial(link='logit'))

summary(model)

library(MASS)
step <- stepAIC(model, direction = "both")

summary(step)


model2 <- glm(Occupancy ~ Temperature + Light + CO2 + HumidityRatio, 
              family = binomial(link = "logit"), data = occ.train)

summary(model2)

occ.train$pred <- predict(model2, newdata = occ.train, type = 'response')

train_pred_vector <- ifelse(occ.train$pred  < 0.6 , "0","1")
mean(occ.train$Occupancy  == train_pred_vector) # 0.986


calAUC(occ.train$pred , occ.train$Occupancy) # 0.9945



## test (pred, act)
prob_occupancy_test <- predict(model2, newdata = occ.test, type = 'response')
pred_occupancy_test <- ifelse(occ.test$pred  < 0.6 , "0","1")
pred_occupancy_test <- as.numeric(pred_occupancy_test)





###########################################################################












calcRMSE <- function(label, estimation){ 
  return(sqrt(mean((label - estimation) ** 2)))
}


calcR2 <- function(label, estimation){ 
  RSS = sum((label - estimation) ** 2)
  SStot = sum((label - mean(label)) ** 2)
  return(1-RSS/SStot)
}

## linear regression
traffic_train <- read_csv("C:/Users/21500/Desktop/2019_summer_final/traffic_train.csv")

tra.train <- traffic_train
tra.train$date_time <- as.character.Date(tra.train$date_time)
tra.train <- separate(tra.train, date_time, c("year", "month", "day"),sep="-")
str(tra.train)
tra.train <- tra.train[,-8]
str(tra.train)
tra.train <- tra.train[,-9]
 


tra.test <- traffic_test_student
tra.test$date_time <- as.character.Date(tra.test$date_time)
tra.test <- separate(tra.test, date_time, c("year", "month", "day"),sep="-")
str(tra.test)
tra.test <- tra.test[,-8]
str(tra.test)
tra.test <- tra.test[,-9]



str(tra.train)
names(tra.train)

######### full model
tra_model.full <- lm(traffic_volume ~ holiday + temp+ rain_1h + snow_1h 
                      + clouds_all+weather_main +month+weather_description, tra.train)


summary(tra_model.full)


###Stepwise Regression 
library(MASS)
step <- stepAIC(tra_model.full, direction = "both")
summary(step)

#display result
step$anova

# new
tra_model_remove <- lm(traffic_volume ~ holiday + temp+I(temp^2) + clouds_all+I(clouds_all^2) + month +
                         weather_description, tra.train)


summary(tra_model_remove)




###### predinction ######
pred_traffic_test <- predict(tra_model_remove, newdata = tra.test)



save(prob_occupancy_test,pred_occupancy_test,pred_traffic_test ,file = "st21500131.RData")


