다항 변수 모델 구축 연습!!
Multivariable Memorization

#Decision Tree
# 의사결정나무 - rpart라는 library 중요!

library(rpart)

# 대출을 해주었을 때, default였는지 rapid였는지를 나타내는 데이터 프레임
load(url("https://github.com/hbchoi/SampleData/blob/master/dtree_data.RData?raw=true"))
str(loans)


#rpart()라는 함수를 생각해보자

loan_model <- rpart(outcome~loan_amount + credit_score, data = loans, method = 'class', control = rpart.control(cp = 0))

loan_model

(11312-5654)/11312

5654 # default 
(5654)/11312 # default prob
(11312-5654) # rapid
(11312-5654)/11312 # rapid prob

631/1667 # rapid
(1667-631)/1667 # default

#install.packages('rpart.plot')
library(rpart.plot)

# rpart.plot을 통해 그려줄 수 있다.
rpart.plot(loan_model)

# 보다 상세히 조건 추가
rpart.plot(loan_model, type = 3, box.palette = c("red", "green"), fallen.leaves = T)

bankruptcy_train_dt <- bankruptcy_train
# corpID 항목제거
bankruptcy_train_dt <- bankruptcy_train_dt[,-1]
# decision tree 모델링 -- 모든 변수 사용
bank_model <- rpart(Class~., data = bankruptcy_train_dt, method = 'class', control = rpart.control(cp=0))

rpart.plot(bank_model, type = 3, box.palette = c("red", "green"), fallen.leaves = T)

bankruptcy_test_dt <- bankruptcy_test

# corpID 항목제거
bankruptcy_test_dt <- bankruptcy_test_dt[, -1]

# predict() 함수 사용 -- type = 'class' 활용
predic <- predict(bank_model, type = 'class', newdata = bankruptcy_test_dt)

table(bankruptcy_test_dt$Class, predic) # 이렇게 확인... 


### Decision Tree의 경우 과적합의 문제가 클 수 있다...!
# ex) 신용도 높고 빌리는 양이 적고 구로구에 사는 1명의 경우 -- 대출해주자 100%
# 이러한 경우가 과적합 문제가 발생할 수 있게된다...!

loan_index <- createDataPartition(loans$outcome, p =.75, list = F)
loan_train <- loans[loan_index, ]
loan_test <- loans[-loan_index, ]

loan_model_train <- rpart(outcome~. , data = loan_train, method = 'class', control = rpart.control(cp=0))
## 예측 모델링을 적용한 것을 데이터프레임에 구축시켜주어서 예측값 비교하는 이러한 테크닉들을 숙지한다..!
loan_train$pred <- predict(loan_model_train, newdata = loan_train, type='class')
table(loan_train$pred, loan_train$outcome)

mean(loan_train$outcome == loan_train$pred)

loan_test$pred <- predict(loan_model_train, newdata = loan_test, type = 'class')

table(pred = loan_test$pred, loan_test$outcome)

mean(loan_test$outcome == loan_test$pred)

## 예측 이후 pred 삭제 과정까지 거쳐주는 것이 좋다...!!
loan_train <- loan_train[, -15]
loan_test <- loan_test[, -15]


# tree가 너무 복잡해져서 과적합의 문제가 발생할 때 사용할 수 있는 처리방법..!!

# pruning..! 가지 치기의 방법이 있다..!!!

# 1. pre-pruning
# max_depth 고정, min split 고정

# 2. post-pruning
# 일정 entropy의 변화량이 점차 줄지 않는 경우 더 이상 split하지 않게 조건 설정

## 1. pre-pruning의 경우
loan_model_pre <- rpart(outcome~., data = loan_train, method = 'class', control = rpart.control(cp=0, maxdepth=6))

loan_test$pre <- predict(loan_model_pre, newdata = loan_test, type = 'class')
mean(loan_test$pre==loan_test$outcome)
# 조금 더 올라감

## 2. post-pruning의 경우
loan_model_post <- rpart(outcome~., data = loan_train, method = 'class', control = rpart.control(cp=0, minsplit = 500))

loan_test$post <- predict(loan_model_post, newdata = loan_test, type = 'class' )
mean(loan_test$post==loan_test$outcome)
# 조금 더 올라감

## 그러면 이러한 기법을 사용할 때
# maxdepth랑 minsplit의 threshold를 선정하는 기준은 뭐지..?

## post-pruning의 경우 시각화 가능 -- plotcp를 통해
# minsplit을 무한정 설정해놓으면
loan_model_post <- rpart(outcome~., data = loan_train, method = 'class', control = rpart.control(cp=0))
plotcp(loan_model_post)

# 여기서 plot의 결과로 대충 cp가 0.0014일때로 설정해준다 하면
# 이렇게 prune함수를 통해 가지치기를 해줄 수 있게 된다..!!
loan_model_post_prun <- prune(loan_model_post, cp = 0.0012)
loan_test$prune <- predict(loan_model_post_prun, loan_test, type = 'class')
mean(loan_test$outcome == loan_test$prune)
# 조금 더 향상함을 볼 수 있다..! 이러한 방법들이 있음을 인지..!!

############ 앞서 살펴보았던 bankruptcy 데이터를 통해
############ 다시 연습을 해보자..!!! -- untitled 25참고


bankruptcy_train_dt
bankruptcy_test_dt



##################
# K Nearest Neighbors 이하 KNN

# 최근접이웃 활용..!

library(class)
# pred <- knn(training_data, testing_data, training_labes)
# 대강 이런식으로 구성되는 것 같아!

# testing_data <- 예측하고자 하는 데이터
# training_data <- 아는 데이터
# training_labes <- 아는 데이터의 클래스 

위스콘신 데이터셋, 유방암 가려내기
환자들의 종양에 대한 데이터 존재
예를들어 radius의 경우도 radius데이터 하나가 있는 것이 아니라
그 radius의 평균, 최대, 최소 값으로 3가지의 지표로 구성됨

각각의 값들은 전부 연속형 데이터셋으로 구성되어 있음
타겟 변수는 factor 타입

wbcd <- read.csv("https://github.com/hbchoi/SampleData/raw/master/wisc_bc_data.csv", stringsAsFactors = F)

str(wbcd) 
View(wbcd)

# Id제거
wbcd <- wbcd[,-1]

# 타겟 변수 분포 확인
table(wbcd$diagnosis)

wbcd$diagnosis <- ifelse(wbcd$diagnosis == 'B', 'Benign', 'Malignant')

KNN에서 중요한 것이 변수마다 scale이 다른 경우
정규화를 통해 통제를 해주는 것이 좋다

# 이 경우도 보면 변수마다 scale이 다름을 확인할 수 있다!
summary(wbcd[c("radius_mean", "area_mean", "smoothness_mean")])
#
가장 많이 쓰는 정규화 방법 중 하나인 min_max normalization이 있다!!
0~1사이로 다 압축해버리는 거지..! 계량때 해봐서 기억날겨
하지만 이것도 한계가 많은 정규화 방법이었제

minmax_norm <- function(x){
  (x-min(x))/(max(x)-min(x))
}

wbcd
# 정규화 적용 각 변수별루
# sapply적용이 된 이녀석은 matrix형태로 반환이 된다.
wbcd_norm <- sapply(wbcd[,-1], minmax_norm)

summary(wbcd_norm[, c("radius_mean", "area_mean", "smoothness_mean")])

# 이러한 정규화가 적용된 녀석을 사용하자!!
dim(wbcd_norm)

# matrix형태이므로 그냥 값으로 대강 지칭한다.
wbcd_train <- wbcd_norm[1:469, ]
wbcd_test <- wbcd_norm[470:569, ]

# DRA 4강 공부할 때 능형회귀분석에서 테스트 셋 정리할 때 공부했겠지만
# 매트릭스 데이터의 경우, 목적 변수의 labeling을 따로 해준다
wbcd_train_label <- wbcd[1:469, 1]
wbcd_test_label <- wbcd[470:569, 1]

# 앞서 K 선택 방법으로 데이터 수의 제곱근을 취한 것을 k로 사용

k <- sqrt(nrow(wbcd_train))

## 예측 모형을 만들어보자
# 각각의 인자는 무엇을 의미할까??
?knn
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test, cl = wbcd_train_label, k = k)

# 예측 결과
wbcd_test_pred 

# 예측이 얼마나 잘되었나 확인해보자
tb <- table(wbcd_test_pred, wbcd_test_label)

sum(diag(tb))/sum(tb)
# 0.98로 매우 잘 예측했네..ㄷㄷ

#tb를 다시 확인해보자
tb

이 경우에 암이 아니라고 예측을 했는데 암이어버린 환자가 2명이 있었다.

false negative는 굉장히 위험한 결과를 나을 수 있으므로 이를 낮추는 과저이 필요하다

# So, we hope to avoid false negative rather than false positive
# How can?

# 확률을 직접 받아보아 확인해보자
wbcd_test_pred2 <- knn(train = wbcd_train, test = wbcd_test, cl = wbcd_train_label, k = k, prob = T)

# 확률들을 가져오고
wbcd_test_pred2

# 이 사람들이 암인지 아닌지를 판단한 결과
head(wbcd_test_pred2)

# 그렇게 판단한 확률 확인
head(attributes(wbcd_test_pred2)$prob)

# 각 나온 확률이 의미하는 바가 다르다. 즉, 다 암일 확률인 경우로 변환해주는 전처리 작업을 거친다
wbcd_test_pred_prob <- ifelse(wbcd_test_pred2 == "Malignant", attributes(wbcd_test_pred2)$prob, 1 - attributes(wbcd_test_pred2)$prob) 

# 암일 확률
head(wbcd_test_pred_prob)

## 이러한 threshold를 적절히 선택해주는 과정을 거치는 것이 좋다

# 여기서 이 확률들을 가지고 threshold를 조정해주어 보자
# recall을 높이고 precision을 줄이는 방법으로 가보자

# 우선 앞서 구한 지표의 성능을 ROC curve를 통해 확인해본다
library(ROCR)

plot(performance(prediction(wbcd_test_pred_prob, wbcd_test_label), 'tpr', 'fpr'))

AUC<-performance(prediction(wbcd_test_pred_prob, wbcd_test_label), 'auc')
AUC@y.values[[1]]

### 이제 본격적으로 threshold를 조정한 것을 어떻게 하는 지 방법을 따라가보자

# 기본적으로 KNN자체는 0.5의 threshold로 암이라고 진단?

# 이것을 좀 더 recall을 높이고 precision을 줄이기 위해
# threshold를 낮게 선정해보자
threshold <- 0.1
wbcd_test_pred_new <- ifelse(wbcd_test_pred_prob > threshold, 'Malignant', 'Benign')
reduce_precision_tb<- table(wbcd_test_label, wbcd_test_pred_new)
sum(diag(reduce_precision_tb))/sum(reduce_precision_tb)

# Accuracy is lower지만
# But, False Negative를 제로로 만듬!! -- 이게 더 중요한 의미를 갖는 것!!


### dummy 변수 처리 방법!!!! 개중요!!!!!!
# one hot encoding
sample_df <- data.frame(blood_type = c('A', 'B', 'A', 'O', 'AB'), 
                        skin_color = c('black','white', 'yellow', 'red', 'black'),
                        age=c(22,35,21,26,70))

sample_new_df <- predict(dummyVars(~blood_type+skin_color, data=sample_df), sample_df)
sample_new_df <- data.frame(sample_new_df)
sample_new_df$age <- sample_df$age
sample_new_df
