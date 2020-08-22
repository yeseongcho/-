# imbalalced data 대비 이거 이용하자.
balanced_accuracy <- function(tb){
  sensitivity <- sum(tb[1,1])/sum(tb[,1])
  specificity <- sum(tb[2,2])/sum(tb[,2])
  return((sensitivity+specificity)/2)
  
}

tb3

sum(diag(tb3))/sum(tb3)

balanced_accuracy(tb3)

str(student.train)

library(MASS)
simple <- lm(G3~., data=student.train)
summary(simple)
calcRMSE(student.train$G3, simple$fitted.values)
stepAIC(simple, direction="both")

earths <- earth(G3~., data=student.train)

linear <- lm(G3~Medu+Fedu+studytime+romantic*traveltime, data=student.train)

plotmo(earths)
evimp(earths)

summary(earths)
summary(linear)

calcRMSE(student.train$G3, linear$fitted.values)

students.trains <- student.train
# 유의미한 피처를 알았으니까
# 전체 모델에서 type 바꾸고
# 소거법으로 테스트 하는 것이 좋을 듯..!
str(students.trains)
# 자체적인 교차검증을 한다고 보면 된다...!
first_linear <- lm(G3 ~ school + famsize + Medu + Mjob + Fjob + studytime + 
                     failures + Medu*studytime + Medu*higher +schoolsup + famsup + higher + internet + romantic + 
                     goout + health +class+health*absences+goout*failures, data = students.trains)

# factor랑 numeric을 동시에 같이 train, test에 적용시켜주는 sense
students.trains$Medu <- as.factor(students.trains$Medu)
students.trains$studytime <- as.factor(students.trains$studytime)
students.trains$failures <- as.factor(students.trains$failures)
students.trains$goout <- as.factor(students.trains$goout)

students.trains$Medu <- as.numeric(students.trains$Medu)
students.trains$studytime <- as.numeric(students.trains$studytime)
students.trains$failures <- as.numeric(students.trains$failures)
students.trains$goout <- as.numeric(students.trains$goout)

summary(first_linear)
calcRMSE(student.train$G3, first_linear$fitted.values)
str(student.train)

str(credit_train)
simple_logistic <- glm(default.payment.next.month~., data=credit_train, family=binomial)
# 가능은 하다..! 하지만 시간이 좀 걸리네..ㅠㅠㅠ
stepAIC(simple_logistic, direction="both")
library(leaps)
subs <- regsubsets(default.payment.next.month~., data=credit_train)
plot(subs, scale='Cp')

logistics_earth <- earth(default.payment.next.month~., data=credit_train)
plotmo(logistics_earth)
evimp(logistics_earth)

str(student.train)

student.train$guardian

credit_scale <- credit_train

credit_scale$SEX <- as.factor(credit_train$SEX)
credit_scale$EDUCATION <- as.factor(credit_train$EDUCATION)
credit_scale$MARRIAGE <- as.factor(credit_train$MARRIAGE)

str(credit_scale)

credit_scale$LIMIT_BAL <- scale(credit_train$LIMIT_BAL)
credit_scale$PAY_1 <- as.factor(credit_scale$PAY_1)
credit_scale$PAY_2 <- as.factor(credit_scale$PAY_2)
credit_scale$PAY_3 <- as.factor(credit_scale$PAY_3)
credit_scale$PAY_4 <- as.factor(credit_scale$PAY_4)
credit_scale$PAY_5 <- as.factor(credit_scale$PAY_5)
credit_scale$PAY_6 <- as.factor(credit_scale$PAY_6)
credit_scale$BILL_AMT1 <- scale(credit_train$BILL_AMT1)
credit_scale$BILL_AMT2 <- scale(credit_train$BILL_AMT2)
credit_scale$BILL_AMT3 <- scale(credit_train$BILL_AMT3)
credit_scale$BILL_AMT4 <- scale(credit_train$BILL_AMT4)
credit_scale$BILL_AMT5 <- scale(credit_train$BILL_AMT5)
credit_scale$BILL_AMT6 <- scale(credit_train$BILL_AMT6)
credit_scale$PAY_AMT1 <- scale(credit_train$PAY_AMT1)
credit_scale$PAY_AMT2 <- scale(credit_train$PAY_AMT2)
credit_scale$PAY_AMT3 <- scale(credit_train$PAY_AMT3)
credit_scale$PAY_AMT4 <- scale(credit_train$PAY_AMT4)
credit_scale$PAY_AMT5 <- scale(credit_train$PAY_AMT5)
credit_scale$PAY_AMT6 <- scale(credit_train$PAY_AMT6)

credit_scale_test <- credit_test
credit_scale_test$SEX <- as.factor(credit_scale_test$SEX)
credit_scale_test$EDUCATION <- as.factor(credit_scale_test$EDUCATION)
credit_scale_test$MARRIAGE <- as.factor(credit_scale_test$MARRIAGE)

credit_scale_test$LIMIT_BAL <- scale(credit_scale_test$LIMIT_BAL)
credit_scale_test$PAY_1 <- as.factor(credit_scale_test$PAY_1)
credit_scale_test$PAY_2 <- as.factor(credit_scale_test$PAY_2)
credit_scale_test$PAY_3 <- as.factor(credit_scale_test$PAY_3)
credit_scale_test$PAY_4 <- as.factor(credit_scale_test$PAY_4)
credit_scale_test$PAY_5 <- as.factor(credit_scale_test$PAY_5)
credit_scale_test$PAY_6 <- as.factor(credit_scale_test$PAY_6)
credit_scale_test$BILL_AMT1 <- scale(credit_scale_test$BILL_AMT1)
credit_scale_test$BILL_AMT2 <- scale(credit_scale_test$BILL_AMT2)
credit_scale_test$BILL_AMT3 <- scale(credit_scale_test$BILL_AMT3)
credit_scale_test$BILL_AMT4 <- scale(credit_scale_test$BILL_AMT4)
credit_scale_test$BILL_AMT5 <- scale(credit_scale_test$BILL_AMT5)
credit_scale_test$BILL_AMT6 <- scale(credit_scale_test$BILL_AMT6)
credit_scale_test$PAY_AMT1 <- scale(credit_scale_test$PAY_AMT1)
credit_scale_test$PAY_AMT2 <- scale(credit_scale_test$PAY_AMT2)
credit_scale_test$PAY_AMT3 <- scale(credit_scale_test$PAY_AMT3)
credit_scale_test$PAY_AMT4 <- scale(credit_scale_test$PAY_AMT4)
credit_scale_test$PAY_AMT5 <- scale(credit_scale_test$PAY_AMT5)
credit_scale_test$PAY_AMT6 <- scale(credit_scale_test$PAY_AMT6)

str(credit_scale_test)

logisitc_scale <- glm(default.payment.next.month~PAY_1*PAY_AMT1+PAY_2*PAY_AMT2+PAY_3*PAY_AMT3+PAY_4*PAY_AMT4+PAY_5*PAY_AMT5+PAY_6*PAY_AMT6
                      +LIMIT_BAL_GROUP+SEX+EDUCATION+MARRIAGE+BILL_AMT1+BILL_AMT2+BILL_AMT3+BILL_AMT4+BILL_AMT5+BILL_AMT6+
                        +age_group+SEX*MARRIAGE+SEX*EDUCATION,data=credit_scale, family=binomial)
credit_scale$pred <- predict(logisitc_scale, newdata=credit_scale, type='response')
aggregate(pred~default.payment.next.month, data=credit_scale, mean)
credit_scale$pred_logic <- ifelse(credit_scale$pred >0.2, 1, 0)
tb_scale <- table(pred=credit_scale$pred_logic, actual = credit_scale$default.payment.next.month)
balanced_accuracy(tb_scale)
p_scale <- prediction(credit_scale$pred, credit_scale$default.payment.next.month)

aucs_scale <- performance(p_scale, 'auc')
aucs_scale@y.values[[1]]
credit_scale_test$pred <- predict(logisitc_scale, newdata=credit_scale_test, type='response')
credit_scale_test$pred_logic <- ifelse(credit_scale_test$pred >0.2, 1, 0)
prob_default_test <- credit_scale_test$pred
pred_default_test <- credit_scale_test$pred_logic
save(pred_grade_test, prob_default_test, pred_default_test, file="st21600685.RData")

credit_scale$LIMIT_BAL_GROUP <- cut(credit_trains$LIMIT_BAL, breaks=c(10000,50000,140000,167746,240000,1000000), labels = c("1","2","3","4","5"), right=F)
credit_scale_test$LIMIT_BAL_GROUP <- cut(credit_tests$LIMIT_BAL, breaks =c(10000,50000,140000,167746,240000,1000000), labels = c("1","2","3","4","5"), right=F )
credit_scale$age_group <- cut(credit_trains$AGE, breaks = c(20, 30, 40, 50, 60,70,80), labels = c("1","2","3","4","5","6"), right=F)
credit_scale_test$age_group <- cut(credit_tests$AGE, breaks = c(20, 30, 40, 50, 60,70,80), labels = c("1","2","3","4","5","6"), right=F)

# 재미로 random forest는 어떠할 지 확인해보자
library(randomForest)
str(student.trains)
# ntree는 linear의 경우 경험적으로 늘려보자
credit_train$default.payment.next.month <- as.factor(credit_train$default.payment.next.month)
rf.fit <- randomForest(G3~., data=student.train, mtry=11, ntree=650, importance=T)

rf.fitts <- predict(rf.fit, newdata=student.train)
rf.test <- predict(rf.fit, newdata=student.test.nolabel)
calcRMSE(rf.fitts, student.train$G3)
pred_grade_test <- as.vector(rf.test)

credit_train <- credit_train[,c(-25, -26)]
str(credit_train)
names(credit_train)
# classification은 상대적으로 연산 시간이 오래 걸려 적용하기 어려울듯 우선, regression에서 적용을 시켜보자
# 요거는 나중에 시간 날때 따로 해보자 성능이 엄청 오르기는 한다..!
# 우선 classification은 시간이 걸리니까 그냥 ntree를 500으로 잡고간다...!
credit_train$SEX <- as.factor(credit_train$SEX)
credit_train$EDUCATION <- as.factor(credit_train$EDUCATION)
credit_train$MARRIAGE <- as.factor(credit_train$MARRIAGE)

credit_test$SEX <- as.factor(credit_test$SEX)
credit_test$EDUCATION <- as.factor(credit_test$EDUCATION)
credit_test$MARRIAGE <- as.factor(credit_test$MARRIAGE)

credit_train$SEX <- as.numeric(credit_train$SEX)
credit_train$EDUCATION <- as.numeric(credit_train$EDUCATION)
credit_train$MARRIAGE <- as.numeric(credit_train$MARRIAGE)

credit_train$default.payment.next.month <- as.numeric(credit_train$default.payment.next.month)
rf.classfi <- randomForest(default.payment.next.month~., data=credit_train, mtry=4, ntree=500, importance = T)
rf.classfi <- randomForest(x=credit_train[, -c(24, 25,26)], y = credit_train$default.payment.next.month, 
                           mtry=4, ntree=500, importance = T)
credit_train$pred <- predict(rf.classfi, newdata=credit_train[, -c(24, 25,26)], type='prob')[,2]
credit_train$pred
aggregate(pred~default.payment.next.month, data=credit_train, mean)
credit_train$pred_logic <- ifelse(credit_scale$pred >0.5, 1, 0)
p_rf <- prediction(credit_train$pred, credit_train$default.payment.next.month)
?randomForest()
p_auc <- performance(p_rf, 'auc')
p_auc@y.values[[1]]

credit_test <- credit_test[, c(-24, -25)]
names(credit_test)
names(credit_train)
str(credit_train)
str(credit_test)
credit_test
credit_test$pred <- predict(rf.classfi, newdata=credit_test, type='prob')[,2]
credit_test$pred_logic  <- ifelse(credit_test$pred >0.5, 1, 0)
prob_default_test <- credit_test$pred
pred_default_test <- credit_test$pred_logic
save(pred_grade_test, prob_default_test, pred_default_test, file="st21600685.RData")
