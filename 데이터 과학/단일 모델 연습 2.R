View(adult)

# na가 없다?!
colSums(is.na(adult))

# 인종에 따른 수익 분포는?

adult.indexs <- createDataPartition(adult$income_mt_50k, p = .7, list = F)

adult.r.train <- adult[adult.indexs, ]
adult.r.test <- adult[-adult.indexs, ]

prop.table(table(adult.r.train$income_mt_50))

prop.table(table(adult.r.test$income_mt_50k))

table(adult.r.train$race, adult.r.train$income_mt_50k)


md <- prop.table(table(adult.r.train$race, adult.r.train$income_mt_50k), margin = 1)[, 2]
sort(md)

adult.r.train$prob <- md[adult.r.train$race]

# 가장 좋은 threshold를 찾기 위한 과정에서 prediction 함수는 다음과 같이 사용이 가능하다.
P <- prediction(adult.r.train$prob, adult.r.train$income_mt_50k)
plot(performance(P, 'acc'))
plot(performance(P, 'rec'))
plot(performance(P, 'prec'))

# 한 대충 threshold를 0.2 정도로 잡아보자 이걸로만 봐서는 잘 이해가 안된다

adult.r.train$prediction <- adult.r.train$prob > 0.25568
adult.r.train$prediction <- adult.r.train$prob > 0.2616591
# 대체 뭐가 가장 맞는 threshold일까? 이거는 사실 데이터셋이 갖는 의미에 따라 다름!
t <- table(pred = adult.r.train$prediction, actual = adult.r.train$income_mt_50k)

ac <- sum(diag(t))/sum(t)
ac

auc <- performance(P, 'auc')
plot(performance(P, 'tpr', 'fpr'))
auc@y.values[[1]]



str(insurance)
View(insurance)

# 다행히 NA는 없다.
colSums(is.na(insurance))

# 이번에는 bmi를 설명 변수로 가지고 와보자
summary(insurance$bmi)
insurance$bmi_group <- cut(insurance$bmi, breaks = c(0, 20, 30, 40, Inf), labels = c('under20', '20', '30', 'over40'), right = F)
# 사실 실전에는 무조건 NA가 있을 거다. 그러한 NA를 어떻게 처리할 것인가가 앞으로 네가 갖는 숙제일듯.

hist(insurance$charges)
plot(density(insurance$charges))

# 편향된 데이터 통제를 위해 log 취함
insurance$charges_log <- log10(insurance$charges)
plot(density(insurance$charges_log))


# train data, test data 셋 지정
insurance.index <- createDataPartition(insurance$charges_log, p=.8, list= F)
insurance.train <- insurance[insurance.index, ]
insurance.test <- insurance[-insurance.index, ]
plot(density(insurance.train$charges_log))
plot(density(insurance.test$charges_log))

# 설명 변수에 따른 타겟 변수의 평균치
mdls <- tapply(insurance.train$charges_log, insurance.train$bmi_group, mean)
insurance.train$prediction <- mdls[insurance.train$bmi_group]
insurance.train[, c('prediction', 'charges_log')]

# 모델링 점검을 위해 error 값 구함
insurance.train$error <- insurance.train$charges_log - insurance.train$prediction

mse <- mean(insurance.train$error**2)
rmse <- sqrt(mse)
mse
rmse

insurance.test$prediction <- mdls[insurance.test$bmi_group]
insurance.test$error <- insurance.test$charges_log - insurance.test$prediction

Mse <- mean(insurance.test$error ** 2)
Mse
Rmse <- sqrt(Mse)
Rmse

sd(insurance.test$charges_log)

Rss <- sum(insurance.test$error ** 2)
Sst <- sum((insurance.test$charges_log - mean(insurance.test$charges_log))**2)
RSQ <- 1 - (Rss/Sst)
RSQ

summary(lm(charges_log~bmi_group, data = insurance))

install.packages("ElemStatLearn")
library(ElemStatLearn)
install.packages("ElemStatLearn")

