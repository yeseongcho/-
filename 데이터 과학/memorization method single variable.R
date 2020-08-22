중간고사 이후의 데이터 과학
미친듯이 해야한다.

본격적인 modeling을 들어간다!!
  
Memorization Method - Part1

load(url('https://github.com/hbchoi/SampleData/raw/master/adult.RData'))
adult

train 데이터랑 test 데이터를 구분짓는 연습 해보자!! 이 알고리즘을 익혀놓으면 좋다
  
set.seed(2020)
n_sample <- nrow(adult)
r_group <- runif(n_sample)

adult.train <- subset(adult, r_group <= 0.8)
adult.test <- subset(adult, r_group > 0.8)
adult.train

이러한 caret 패키지에 있는 추출 방법도 사용할 수 있다. 
sample을 활용하는 방법도 caret 내용에 있으니 참고
createDataPartition을 사용하는 연습을 많이 해보자
(층화 랜덤 추출을 해주기 때문에 더 효율적!)
library(caret)
adult.indexing <- createDataPartition(adult$income_mt_50k, p=.8, list=F)
adult.train2 = adult[adult.indexing, ]
adult.test2 = adult[-adult.indexing, ]
adult.train2

dim(adult.train)
dim(adult.test)

createDataPartition 이거 활용한 경우의 비율두 구해보자!

prop.table 이라는 테크닉을 반드시 알자!! 이미 쓴맛 많이 봤잖아!!
  
table(adult.train$income_mt_50k)
# 이렇게 쓰는 코드 연습!!
prop.table(table(adult.train$income_mt_50k))
prop.table(table(adult.test$income_mt_50k))
prop.table(table(adult.train2$income_mt_50k))
prop.table(table(adult.test2$income_mt_50k))

# train과 test의 데이터 구성 비율이 같은 지를 꼭 체크하는 습관!!!


## ftable과 prop.table에 대한 간단한 설명은 요 링크 참고
# http://blog.naver.com/PostView.nhn?blogId=padosori60&logNo=220868082613

mtcars[, c("gear", "carb")]
prop.table(table(mtcars$gear, mtcars$carb))
## prop.table은 도수분포표, 교차표의 상대 도수 값을 얻기 위하여 이용!


## 직업에 대해 50만 불이 넘냐 안넘냐를 추측하는 single variable model구축
train데이터 내에 있는 녀석들의 전반적인 분포 체크
tble <- table(adult.train$occupation, adult.train$income_mt_50k)
tble
prop.table(tble, margin=1) ## 1은 행 별로 합쳐 상대 도수 반면 2는 열 별로 합쳐 상대 도수, 자세한 건 링크 참고

#prop.table(tble, margin = 2)
## margin을 안 주게 되면 전체 합 분의 상대 도수를 구하게 된다!

# prop.table의 True부분만 떼와서 써먹어보자
sv_model_job <- prop.table(tble, margin=1)[,2]
sort(sv_model_job, decreasing=T)
이 결과를 해석해볼 수 있겠니??

sv_model_job
# 이게 무슨 말일까?? 이러한 테크닉은 생각도 못했다..
sv_model_job[adult.train$occupation]
 

adult.train$est_prob <- sv_model_job[adult.train$occupation]
head(adult.train[, c("occupation", "est_prob", "income_mt_50k"), 10])

확률이 0.4를 넘는 경우를 대강 TRUE라고 예측을 해보면
그 값을 threshold로 잡아보자
threshold <- 0.48
adult.train$prediction <- adult.train$est_prob > threshold
head(adult.train[, c('occupation', 'est_prob', 'income_mt_50k', 'prediction'), 10])


실제로 그 정확도를 측정하는 기준!!
table에서 제공한다!! - pred와 actual 인자를 통해
caret 패키지에 confusionMatrix 함수를 사용할 수도 있다!!
#  이 경우는 직접 confusionMatrix를 구축한 경우
conf.table <- table(pred = adult.train$prediction, actual = adult.train$income_mt_50k)
conf.table

# confusionMatrix에 대하여 -- 자세한 건 caret 패키지 공부 자료 참고
# prediction, Recall, Accuracy

1) Precision 정밀도 정밀도란 모델이 True라고 분류한 것 중에서 실제로 True인 것의 비율을 의미한다.
2) Recall 재현율 재현율이란 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율을 의미한다.
Precision과 Recall은 함께 고려되어야 한다

Accuracy 정확도

하지만 True , 날씨가 맑은 경우만 존재하지 않기에, False인 경우도 고려하여 한꺼번에 계산해 준 지표가 바로 Accuracy이다.

즉, 총 4가지 케이스(TT, TF, FT, FF) 중에서 (TT+FF), 즉 예측이 맞은 경우를 분자로 가져 확률를 구하면 된다.

# diag..? -- 매트릭스에서 주대각성분을 지칭 - 이 경우는 정답을 맞춘 경우를 지칭하겠지 -- 이 테크닉도 기억하고 있자
accuracy <- sum(diag(conf.table)) / sum(conf.table)
accuracy 

precision <- sum(conf.table[2, 2])/sum(conf.table[2, ])
recall <- sum(conf.table[2,2])/sum(conf.table[, 2])
precision
recall

실제로 학습 데이터에는 예측이 좋지만
테스트 데이터에는 예측이 좋지 않은 일명
Overfitting(과적합) 문제가 발생할 수 있다!! 

##이 모델링의 경우 test도 같은 전처리를 해준다!!
adult.test$est_prob <- sv_model_job[adult.test$occupation]
adult.test$prediction <- adult.test$est_prob > threshold 
adult.test$prediction2 <- adult.test$est_prob > threshold2
adult.test$prediction3 <- adult.test$est_prob > threshold3 
conf.tables <- table(pred = adult.test$prediction, actual = adult.test$income_mt_50k)
conf.tables

accuracies <- sum(diag(conf.tables))/sum(conf.tables)
accuracies

ROC curve!! -- regression 파트 부분 참고

tpr -  True positive model
: 양성율 -- 민감도 (1인 케이스에 대해 1로 잘 예측한 비율) -- recall과 유사

fpr == False positive model
: 위양성율 --   1 -특이도(0인 케이스에 대해 1로 잘못 예측한 비율)
특이도란 0인 케이에 대해 0으로 잘 예측한 비율을 말함

library(ROCR)

## x는 연속형 변수여야 한다 y는 상관이 없는건가?
# prediction <- 예측한 녀석과 테스트 데이터를 비교 수행
# performance <- 해당 자료를 그릴 준비

p <- prediction(adult.test$est_prob, adult.test$income_mt_50k)
plot(performance(p, 'tpr', 'fpr')) #--- # performance (cut, ...a)
?performance
# https://thebook.io/006723/ch09/03/02-1/ -- performance 함수에 대한 자세한 설명 제공
plot(performance(p, 'acc'))
plot(performance(p, 'rec'))
plot(performance(p, 'prec'))
plot(performance(p, 'prec', 'rec'))
?performance
## x축의 cutoff를 이용하여 실제로 가장 크게 하는 threshold를 추측할 수 있다??

AUC를 구하는 방법은 걍 외우자. 이런게 있다!!
AUC <- performance(p, 'auc')

AUC@y.values[[1]] # @는 뭐지?

교수님 방법 함수를 만든다.
calAUC <- function(predCol, targetCol){
  perf <- performance(prediction(predCol, targetCol), 'auc')
  as.numeric(perf@y.values)
}


# Continuous 데이터 처리 방법

49살인 경우가 80%는 True
하지만 49살인 경우의 표본은 적당한가?
나이, 키, 몸무게 등은 이러한 수치를 사용할 수 있을까?
이러한 변수들은 여러가지 factor type으로 group화 시키는 것이
더 유용하다고 할 수 있다!!!

age_group을 나누어 adult 데이터 셋에 적용해보자

summary(adult$age)

adult$age
adult.train$age_group <- cut(adult.train$age, breaks = c(0, 20, 30, 40, 50, 60, Inf), right = F, labels =c("under20s", "20s", "30s", "40s", "50s", "over60s"))



tble <- prop.table(table(adult.train$age_group, adult.train$income_mt_50k), margin = 1)[, 2]
tble
# 이렇게 해서 확률의 분포 현황을 더 자세히 알 수 있다!!
sort(tble, decreasing = T)


adult.train$age_prop <- tble[adult.train$age_group]

tas <- adult.train[, c('age_group', 'age_prop', 'income_mt_50k')]

# False인 경우, True인 경우 각각의 평균을 이용하여 가중 평균을 구함

tas %>% filter(adult.train$income_mt_50k == "FALSE") -> tas1
tas %>% filter(adult.train$income_mt_50k == "TRUE") -> tas2
A <- mean(tas1$age_prop)
B <- mean(tas2$age_prop)
th <- (A+B)/2
th2 <- mean(adult.train$age_prop)
th2
adult.train$age_prediction <- adult.train$age_prop > 0.35

tab <- table(pred = adult.train$age_prediction, actual = adult.train$income_mt_50k)
ac <- sum(diag(tab))/sum(tab)
ac
tab
pr <- sum(tab[2, 2])/sum(tab[2, ])
re <- sum(tab[2, 2])/sum(tab[, 2])
pr
re

# 어떠한 threshold가 가장 좋을까? 케이스마다 다르다! 
# 우선 나는 th가 0.35일떄루 해볼게!
p_age <- prediction(adult.train$age_prop, adult.train$income_mt_50k)
plot(performance(p_age, 'prec'))

summary(adult.test$age)
adult.test$age_group <- cut(adult.test$age, breaks = c(0, 20, 30, 40, 50, 60, Inf), right=F, labels = c("under20s", "20s", "30s", "40s", "50s", "over60s"))

adult.test$age_prop <- tble[adult.test$age_group]

adult.test$age_prediction <- adult.test$age_prop > 0.35

tab2 <- table(pred = adult.test$age_prediction, actual = adult.test$income_mt_50k)
tab2
ac2 <- sum(diag(tab2))/sum(tab2)
ac2
pr <- sum(tab2[2, 2])/sum(tab2[2, ])
re <- sum(tab2[2, 2])/sum(tab2[, 2])
pr
re

p_age2 <- prediction(adult.test$age_prop, adult.test$income_mt_50k)
plot(performance(p_age2, 'tpr', 'fpr'))
aucs <- performance(p_age2, 'auc')
aucs@y.values[[1]]


# Regression에 대해 본격적으로 나아가볼까

load(url("https://github.com/hbchoi/SampleData/raw/master/insurance.RData"))

str(insurance)
summary(insurance)
# 목적 변수의 대강의 분포를 확인하는 것도 매우 중요하다!
hist(insurance$charges)
plot(density(insurance$charges))

insurance$charges_log <- log10(insurance$charges)
plot(density(insurance$charges_log))

Single variable in Regression Model

charge_log <- target variable
smoker <- explain variable

df <- insurance

indexing <- createDataPartition(df$charges_log, p = .7, list = F)
df.train <- df[indexing, ]
df.test <- df[-indexing, ]
plot(density(df.train$charges_log))
plot(density(df.test$charges_log))

# 여기도 같은 방식이다.
sv_reg_smoker <- tapply(df.train$charges_log, df.train$smoker, mean)
sv_reg_smoker

df.train$pred_charges_log <- sv_reg_smoker[df.train$smoker]
df.train[, c('pred_charges_log', 'smoker', 'charges_log', 'charges')]

df.train$error <- df.train$charges_log - df.train$pred_charges_log

plot(density(df.train$error))

summary(df.train$error)

# 보면 알겠지만, 오차의 경우 양수, 음수로 되어 있다.
# 이를 다 합하면 둘이 상쇄되어 0이 되어버리는 경우 존재
# 보통 제곱을 해서 양수로 전환해준다.

# 대강의 성능을 판단해주는 아이들?
# MSE, RMSE, MAPE 부분 Classification Dra 공부 참조! 
#################################################################   MSE, RMSE, RSS, SST 같은 통계 수치는 반드시 외우고 이해해야 한다!!!
MSE_train <- mean(df.train$error ** 2)
MSE_train
# Mean Squared Error
RMSE_train <- sqrt(MSE_train)
RMSE_train
# Root Mean Squared Error
DiffRatio <- abs((df.train$error)/df.train$charges_log)
MAPE_train <- mean(DiffRatio)
MAPE_train
# Mean Absolute Percentage Error

df.test$pred_charges_log <- sv_reg_smoker[df.test$smoker]

df.test$error <- df.test$charges_log - df.test$pred_charges_log

MSE_test <- mean(df.test$error ** 2)
MSE_test
RMSE_test <- sqrt(MSE_test)
RMSE_test
DiffRatio2 <- abs((df.test$error)/df.test$charges_log)
MAPE_test <- mean(DiffRatio2)
MAPE_test

# train이랑 test 랑 RMSE를 비교해서 비슷하게 나오면 overfitting은 아닌듯!

# RMSE 수치가 나왔는데 이게 좋은 거냐.. 안 좋은 거냐? 궁금할 수가 있죠
# 얼마나 좋아야 좋은 거냐..?

# 이럴 때 보통 표준 편차랑 많이 비교한다!
# 단순한 평균으로 때린 예측 모형의 정확도가 sd로 나타내지게 되는데
# 이것보다는 예측을 잘해야 한다!! 당연하겠지
RMSE_test
sd(df.test$charges_log)
RMSE_train
sd(df.train$charges_log)

# 직접 R2를 만들 수 있다

RSS <- sum(df.test$error ** 2)
SST <- sum((df.test$charges_log - mean(df.test$charges_log))**2)
Rsq <- 1 - (RSS/SST)
Rsq
