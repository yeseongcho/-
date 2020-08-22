단일 변수 모델 구축 연습 with adult

load(url('https://github.com/hbchoi/SampleData/raw/master/adult.RData'))
View(adult)
str(adult)
adult$education
library(caret)

adults <- adult

## 학습 데이터랑 시험 데이터를 구분!! -- 난수를 통한 indexing과 createDataPartition을 이용하여 indexing하는 방법 2개를 모델링

set.seed(2020)
n <- nrow(adults)
ns <- runif(n)

adults.train1 <- subset(adults, ns<=0.8)
adults.test1  <- subset(adults, ns>0.8)

adults.train.indexing <- createDataPartition(adults$income_mt_50k, p = .8, list=F)
adults.train2 <- adults[adults.train.indexing, ]
adults.test2 <- adults[-adults.train.indexing, ]

## 학습 데이터랑 시험 데이터의 데이터 구조가 유사한 지 확인.. 목표 변수의 구성을 확인하여 준다.

prop.table(table(adults.train1$income_mt_50k))
prop.table(table(adults.test1$income_mt_50k))

prop.table(table(adults.train2$income_mt_50k))
prop.table(table(adults.test2$income_mt_50k))

## 설명 변수인 education 항목을 떼와보자

## 이렇게 구분하는 방법을 알아야 한다!! 이걸 할 줄 알았으면 중간고사는 맞았을듯!! 
# table()함수에 대한 명확한 이해가 필요하다
table(adults.train1$education, adults.train1$income_mt_50k)

probs.table <- prop.table(table(adults.train1$education, adults.train1$income_mt_50k), margin = 1)
probs <- probs.table[, 2]

# 이렇게 indexing 자체의 named 성질을 이용해서 하는 방법도 반드시 네 꺼가 되어야 한다 예성아
adults.train1$probs <- probs[adults.train1$education]

adults.train1[, c('education', 'probs', 'income_mt_50k')]

probs.table
## 직업 군 별로 threshold를 다르게 부여하는 것은 불가능한가? -- 그다지 좋은 예측 모델을 만들지는 못한다.

threshold <- mean(probs) 


adults.train1$prediction <- adults.train1$probs > threshold
adults.train1$education <- str_trim(adults.train1$education)
adults.train1$education <- as.character(adults.train1$education)
head(adults.train1)

conf <- table(pred = adults.train1$prediction, actual = adults.train1$income_mt_50k)
conf
sum(diag(conf))/sum(conf)

adults.test1

props <- prop.table(table(adults.test1$education, adults.test1$income_mt_50k), margin=1)[, 2]
adults.test1$props <- props[adults.test1$education]
adults.test1
props
probs
adults.test1$education <- str_trim(adults.test1$education)
adults.test1$education <- as.character(adults.test1$education)


adults.test1$prediction <- threshold(adults.test1$props, adults.test1$education)
adults.test1[, c('education', 'prediction', 'income_mt_50k')]

conf <- table(pred = adults.test1$prediction, actual = adults.test1$income_mt_50k)
sum(diag(conf))/sum(conf)


## 동일한 과정을 train2 test2 데이터 셋에도 적용시켜서 체화를 해보자 -- 유사한 거 같아..

prob2 <- prop.table(table(adults.train2$education, adults.train2$income_mt_50k), margin = 1)[, 2]
prop2 <- prop.table(table(adults.test2$education, adults.test2$income_mt_50k), margin = 1)[, 2]
adults.train2$probs <- prob2[adults.train2$education]
adults.train2[, c('education', 'probs', 'income_mt_50k')]
thresholds <- mean(prob2)
adults.train2$prediction <- adults.train2$probs > thresholds


confs <- table(pred = adults.train2$prediction, adults.train2$income_mt_50k)
sum(diag(confs))/sum(confs)

# 테스트할 데이터랑 분포가 유사한 지 확인해본다
plot(density(prob2))
plot(density(prop2))

p <- prediction(adults.test1$props, adults.test1$income_mt_50k)
plot(performance(p, 'tpr', 'fpr'))
auc1 <- performance(p, 'auc')
auc1@y.values[[1]]

p1 <- prediction(adults.test2$)

# banks 데이터로도 확인해보자

banks <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/bank_hw.csv")
str(banks)
library(tidyr)
library(dplyr)
library(ROCR)
library(caret)

banks_index <- createDataPartition(banks$y, p = .7, list=F)
banks_train <- banks[banks_index, ]
banks_test <- banks[-banks_index, ]

prop.table(table(banks_train$y))
prop.table(table(banks_test$y))

plot(density(prop.table(table(banks_train$y))))
plot(density(prop.table(table(banks_test$y))))


props <- prop.table(table(banks_train$job, banks_train$y), margin= 1)[, 2]
props

means <- sapply(table(banks_train$job), function(x){x/3165})

props <- props+means

threshold <- mean(props)
threshold
props2 <- prop.table(table(banks_train$job, banks_train$y), margin= 1)[, 2]
props2
threshold2 <-  mean(prop.table(table(banks_train$job, banks_train$y), margin= 1)[, 2])
threshold2

banks_train$p <- props[banks_train$job]
banks_train$p2 <- props2[banks_train$job]
banks_train[, c('job', 'p', 'p2', 'y')]
banks_train$prediction <- banks_train$p > threshold # 조정한 평균
banks_train$prediction2 <- banks_train$p2 > threshold2 # 평균

t1 <- table(pred = banks_train$prediction, actual = banks_train$y)
t2 <- table(pred = banks_train$prediction2, actual = banks_train$y)

acc1 <- sum(diag(t1))/sum(t1)
acc2 <- sum(diag(t2))/sum(t2)
acc1
acc2

plot(performance(prediction(banks_train$p2, banks_train$y), 'tpr', 'fpr'))

propss <- prop.table(table(banks_test$job, banks_test$y), margin = 1)[,2]
propss

banks_test$p <- props[banks_test$job]
banks_test$p
banks_test[, c('job', 'p', 'y')]
banks_test$prediction1 <- banks_test$p > threshold
banks_test$prediction2 <- banks_test$p > threshold2
banks_test$prediction3 <- banks_test$p > threshold3
banks_test[, c('prediction1', 'prediction2', 'prediction3', 'y')]
threshold3 <- 0.1
tt1 <- table(pred = banks_test$prediction1, actual = banks_test$y)
tt2 <- table(pred = banks_test$prediction2, actual = banks_test$y)
tt3 <- table(pred = banks_test$prediction3, actual = banks_test$y)
tt1
tt2
tt3

accs1 <- sum(diag(tt1))/sum(tt1)
accs2 <- sum(diag(tt2))/sum(tt2)
accs3 <- sum(diag(tt3))/sum(tt3)
accs3

## ROC curve 이해가 잘 안된다!!
p1 <- prediction(banks_test$p, banks_test$prediction1)
p1 <- prediction(banks_test$p, banks_test$y)
p2 <- prediction(banks_test$p, banks_test$prediction2)
p2 <- prediction(banks_test$p, banks_test$y)
p3 <- prediction(banks_test$p, banks_test$y)
plot(performance(p1, 'tpr', 'fpr'))

# 우선
sv_model_job에서는 이 걸 구축한 것이 train데이터에서 기반했고 그 셋을 동일하게 test에서도 사용하였다는 것이 중요!!
ROC curve는 전반적인 모델의 테스트를 측정하는 것!!!
threshold를 어떤 것을 사용하였느냐는 그 내부의 문제
직접 ROC curve를 구해봐서 어느 정도가 가장 좋은 threshold를 cutoff 내에서 구해 모델에
적용해볼 수 있다.

insu <- insurance

str(insu)

# 종속 변수에 대한 전반적인 흐름을 파악하는 것은 필수
hist(insu$charges)
plot(density(insu$charges))
# right-skwed 형태 - log를 취해주어 정규한 형태로 변환해준다
insu$charges_log <- log10(insu$charges)
plot(density(insu$charges_log))

# train data, test data 구분
ins_index  <- createDataPartition(insu$charges_log, p = .8, list = F)
insu.train  <- insu[ins_index, ]
insu.test  <- insu[-ins_index, ]

expc <- tapply(insu.train$charges_log, insu.train$region, mean)
insu.train$expc <- expc[insu.train$region]
insu.train[, c('expc', 'charges_log')]

insu.train$error <- insu.train$charges_log - insu.train$expc
MSE <- mean(insu.train$error ** 2) 
RMSE <- sqrt(mean(insu.train$error**2))
RMSE
MAPE_ratio <- abs(insu.train$error/insu.train$charges_log)
MAPE <- mean(MAPE_ratio)
MAPE

RSS <- sum(insu.train$error ** 2)
SST <- sum((insu.train$charges_log - mean(insu.train$charges_log))**2)
Rsq <- 1 - (RSS/SST)
Rsq

insu.test$expc <- expc[insu.test$region]
insu.test$error <- insu.test$charges_log - insu.test$expc

RSS <- sum(insu.test$error ** 2)
SST <- sum((insu.test$charges_log - mean(insu.test$charges_log))**2)
Rsq <- 1 - (RSS/SST)
Rsq # 이 경우는 Rsq가 음수가 나온다??

summary(lm(insu.test$charges_log~insu.test$region))

######################## 질문!! -- 이 경우, Rsq와 lm의 결과가 다른데 의미상 어떻게 다른 것인가?

# age로도 추정해보자
summary(insu.train$age)
summary(insu.test$age)
insu.train$age_group <- cut(insu.train$age, breaks = c(0, 20, 30, 40, 50, 60, Inf), right = F, labels = c("under20", "20s", "30s", "40s", "50s", "over60s"))
insu.test$age_group <- cut(insu.test$age,  breaks = c(0, 20, 30, 40, 50, 60, Inf), right = F, labels = c("under20", "20s", "30s", "40s", "50s", "over60s"))


expectation <- tapply(insu.train$charges_log, insu.train$age_group, mean)
insu.train$age_exp <- expectation[insu.train$age_group]
insu.train[, c('age_exp', 'age', 'charges_log')]

insu.train$error_age <- insu.train$charges_log - insu.train$age_exp

RSS <- sum(insu.train$error_age ** 2)
SST <- sum((insu.train$charges_log - mean(insu.train$charges_log))**2)
Rsq <- 1 - (RSS/SST)
Rsq

insu.test$age_exp <- expectation[insu.test$age_group]
insu.test$error_age <- insu.test$charges_log - insu.test$age_exp

RSS <- sum(insu.test$error_age ** 2)
SST <- sum((insu.test$charges_log - mean(insu.test$charges_log))**2)
Rsq <- 1 - (RSS/SST)
Rsq

summary(lm(insu.train$charges_log~ insu.train$age_group))

summary(lm(insu.test$charges_log~insu.test$age_group))

