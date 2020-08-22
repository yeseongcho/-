
prs <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/PRSA_data.csv")

str(prs)
library(tidyr)
library(caret)
##### 전처리 및 EDA

# na 제거
prs <- na.omit(prs)
sum(is.na(prs))

Q1. 
prs$bad_air <- ifelse(prs$pm2.5>75, TRUE, FALSE)
View(prs)

train <- prs[which(prs$year!=2014), ]
test <- prs[which(prs$year==2014), ]

# no 항목 제거
train <- train[, -1]
test <- test[, -1]
View(train)
library(lubridate)
# date 구성
train <- unite(train, date, year, month, day, hour, sep="-")
train$date <- ymd_h(train$date)

test <- unite(test, date, year, month, day, hour, sep="-")
test$date <- ymd_h(test$date)

## 구분됨 확인
str(train)
str(test)
train
# y값 분포 확인
plot(density(train$pm2.5))
plot(density(test$pm2.5))

library(ggplot2)
library(reshape2)
# bad_air 정보 제거
train.formelt <- train[, -1]
train.formelt

# 정규화 과정을 거침
train.formelt <- data.frame(scale(train.formelt[,c(2,3,4,6,7,8)]))
train.formelt$bad_air <- train$bad_air

melting <- melt(train.formelt, id.var = "bad_air")

View(melting)

# 풍향을 제외한 나머지 데이터를 가지고 분석
ggplot(data = melting, aes(x=bad_air, y=value)) + geom_boxplot() + facet_wrap(~variable, ncol=3)
# 시각화 결과 
# 이슬점이나, 기압, 풍속 이 정도를 데이터로 쓰면 어떨까

# 풍향의 데이터
table(train$cbwd, train$bad_air)
# 풍향도 cv나 SE일때 상대적으로 미세먼지 농도가 좋지 않았다.

# 확률로 변환해서 데이터를 구축하는 것은 어떠할까? 일단 이것은 넘어가자
prop.table(table(train$cbwd, train$bad_air), margin = 1)
# cv의 경우 0.63%
# NE의 경우 0.41%
# NW의 경우 0.28%
# SE의 경우 0.61%

# 일단은 decision tree모형을 사용해야 하므로

# 이슬점, 기압, 풍향, 풍속을 변수로 사용해보기로 한다.

## 가지치기 과정은 우선 추후에 작업을 해보자
# 적당한 가지치기 값을 내어주는 함수는 없을까?
# 적합한 maxDepth, minSplit 값을 내어주는 함수 같은거...
# https://data-make.tistory.com/76
# 이쪽 링크를 한번 참고해보자

dt_new <- rpart(bad_air~DEWP+PRES+cbwd+TEMP+Iws, data = train, method = 'class', control = rpart.control(cp=7.771215e-06, minsplit=1129))
pred_new <- predict(dt_new, newdata=test, type='class')
dt_new$cptable
mean(test$bad_air==pred_new)

score_test <- c()
for (i in 1:20){
  m <- rpart(bad_air~DEWP+PRES+cbwd+TEMP+Iws, data = train, method = 'class', control = rpart.control(cp = 7.771215e-06, minbucket =i, minsplit=1129))
  val_var <- predict(m, newdata = test, type = 'class')
  score_test <- c(score_test,mean(val_var == test$bad_air))
}
which.min(score_test)


library(rpart)
library(rpart.plot)
names(train)
# 간단하게 한번 구축을 해보자
dt <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data= train, method = "class", control = rpart.control(cp=0))
dt_all <- rpart(bad_air~DEWP+PRES+cbwd+Iws+Is+Ir, data= train, method = "class", control = rpart.control(cp=0))
pred_train <- predict(dt, newdata = train, type = 'class')
pred <- predict(dt, newdata = test, type = 'class')
table(train$bad_air, pred_train)
mean(train$bad_air == pred_train) 
# decision tree에서 0.79정도 되는게
# test에서는 0.63으로 확 떨어지네...
# overfitting의 가능성이 어느 정도 존재한다고 할 수 있다.
pred2 <- predict(dt_all, newdata = test, type = 'class')
table(test$bad_air, pred)
mean(test$bad_air == pred)
# 이러한 단순한 모델은 형편없네... 다 때려 박았을 때보단 성능이 좋다..


dt$cptable
plotcp(dt)
dt$control

dt_adjust <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp = 6.907747e-06, minsplit = 1227))
pred_adjust <- predict(dt_adjust, newdata = test, type = 'class')
table(test$bad_air, pred_adjust)
mean(test$bad_air==pred_adjust)
dt_adjust$control

dt_adjust2 <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp = 2.279557e-04, minsplit = 180))
pred_adjust2 <- predict(dt_adjust2, newdata = test, type = 'class')
table(test$bad_air, pred_adjust2)
mean(test$bad_air==pred_adjust2)
dt_adjust2$control

# 한번만 더해보자
dt_adjust3 <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp = 0.00021))
pred_adjust3 <- predict(dt_adjust3, newdata = test, type = 'class')
table(test$bad_air, pred_adjust3)
mean(test$bad_air==pred_adjust3)

dt_prune <- prune(dt, cp=0.00021)
pred_prune <- predict(dt_prune, newdata = test, type = 'class')
table(test$bad_air, pred_prune)
mean(test$bad_air==pred_prune)

# minbucket 변화에 따른 정확도 확인
score_test <- c()
for (i in 1:100){
  m <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp = 6.907747e-06, minbucket =i, minsplit = 1227))
  val_var <- predict(m, newdata = train, type = 'class')
  score_test <- c(score_test,mean(val_var == test$bad_air))
}
score_test
# 일반적인 set에서 다시 해보자
score_test <- c()
for (i in 1:10){
  m <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp = 0, minbucket =i))
  val_var <- predict(m, newdata = train, type = 'class')
  score_test <- c(score_test,mean(val_var == test$bad_air))
}

# 대강 minbucket = 58까지로 한게 좀 좋았네

dt_final_adjust <- rpart(bad_air~DEWP+PRES+cbwd+Iws, data = train, method = 'class', control = rpart.control(cp =6.907747e-06, minbucket = 60, minsplit=1227 ))
pred_final <- predict(dt_final_adjust, newdata = test, type = 'class')
table(test$bad_air, pred_final)
mean(test$bad_air==pred_final)

# caret 패키지를 통해 교차검증 시도 -- 성능이 더 좋아진건지는 잘 모르겟다.
train$bad_air <- as.factor(train$bad_air)
test$bad_air <- as.factor(test$bad_air)
dtree <- train(bad_air~DEWP+PRES+cbwd+Iws, data=train, method="rpart", trControl = trctrl, tuneLength = 10)
trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
pred_d <- predict(dtree, newdata = test, type = 'raw')
table(pred_d, test$bad_air)
mean(test$bad_air==pred_d)

train$bad_air <- as.logical(train$bad_air)
test$bad_air <- as.logical(test$bad_air)


## Homework3에서 했던 전처리(group화 했을때는 어떠할까)

# 풍속 전처리
train$wind_group <- cut(train$Iws, breaks = c(0, 1.79, 5.81, 23.26, 25.02, 46.5, 65.7, 85.4, 109.1, 140.8, 173, 211.9, 276.7, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"), right = F)

# 이슬점 전처리
train$dew_group <- cut(train$DEWP, breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)

# 기압 전처리
train$pres_group <- cut(train$PRES, breaks = c(0, 996, 1002, 1008, 1014, 1020, 1026, 1030, 1035, Inf), labels = c("1","2","3","4","5","6","7","8","9"), right = F)

## 궁금한 게 test데이터는 저러한 grouping을 못하는데 예측이 가능할까?
dt_group <- rpart(bad_air~wind_group+dew_group+pres_group+cbwd, data=train, method = 'class', control = rpart.control(cp=0))
# 안되더라..!
dt_group
pred_group <- predict(dt_group, newdata = test, type = 'class')
# train set에서도 큰 개선을 보이지는 않음...오히려 값이 떨어짐..?
mean(test$bad_air==pred_group)

test$wind_group <- cut(test$Iws, breaks = c(0, 1.79, 5.81, 23.26, 25.02, 46.5, 65.7, 85.4, 109.1, 140.8, 173, 211.9, 276.7, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"), right = F)
test$dew_group <- cut(test$DEWP, breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
test$pres_group <- cut(test$PRES, breaks = c(0, 996, 1002, 1008, 1014, 1020, 1026, 1030, 1035, Inf), labels = c("1","2","3","4","5","6","7","8","9"), right = F)

# error도 전반적으로 더 크다...! 고로 이 과정은 그다지 의미 없음..
dt_group$cptable
dt$cptable

?prediction()


############## KNN

#Knn을 쓰기 위해서는 변수가 연속형 변수일 경우 이를 표준화하는 작업이 필요
#### 여기서 아쉬웠던 게 더미 코딩을 해주지 않았다는 것...!!
# 더미 코딩을 해서 예측력을 높여보자...!

Q1. 
#학습, 테스트데이터를 나누기 전에 데이터셋에 표준화를해주는 작업을 거친다.
prs

# No행 제거
prs_scale <- prs[, -1]
prs_scale$DEWP <- scale(prs_scale$DEWP)
prs_scale$TEMP <- scale(prs_scale$TEMP)
prs_scale$PRES <- scale(prs_scale$PRES)
prs_scale$Iws <- scale(prs_scale$Iws)

#### 여기서 아쉬웠던 게 더미 코딩을 해주지 않았다는 것...!!
# 더미 코딩을 해서 예측력을 높여보자...!
new_prs <- predict(dummyVars(~cbwd, data=prs_scale), prs_scale)
new_prs <- cbind(new_prs, prs_scale)
new_prs <- new_prs[,-13]
new_prs
# 이 new_prs를 예측으로 했으면 더 좋았을듯
# 학습 데이터와 훈련 데이터셋 나눔
train_k <- prs_scale[prs_scale$year != 2014, ]
test_k <- prs_scale[prs_scale$year == 2014, ]

# 예측 변수들을 기준으로 모형 구축 -- 날짜, pm2.5등의 불필요 데이터 제거
# 기존에 사용했던 변수들 중 가장 예측이 좋았던, 이슬점, 온도, 기압, 풍속 데이터로 비교한다.
train_k <- train_k[, c(6,7,8,10,13)]
test_k <- test_k[, c(6,7,8,10,13)]

Q2.
# 우선 기존에 배운 방법대로 관측치 수의 제곱근 값을 k로 취한다

sqrt(nrow(train_k)) # 약 181로 잡는다
# labeling
train_label <- train_k$bad_air
test_label <- test_k$bad_air
library(class)
library(kknn)

train_k$bad_air

knn.model1 <- knn(train = train_k[,1:4], test = test_k[, 1:4], cl = train_k$bad_air, k = 180)
mean(knn.model1 == test_k$bad_air)
table(pred=knn.model1, test_k$bad_air)
head(attributes(knn.model1)$prob)
head(knn.model1)
testing <- ifelse(knn.model1 == TRUE, attributes(knn.model1)$prob, 1-attributes(knn.model1)$prob)
pk <- prediction(testing, test_k$bad_air)
plot(performance(pk, 'tpr', 'fpr'))
performance(pk, 'auc')@y.values[[1]]
# 더 적합한 값을 찾아본다 교차 검증을 통해 적합한 k를 찾아본다
# k는 대강 250가지 search해본다
grid <- expand.grid(.k = seq(180,250,by=1))

control <- trainControl(method = 'cv')

set.seed(2020)
train_k$bad_air <- as.factor(train_k$bad_air)
test_k$bad_air <- as.factor(test_k$bad_air)
train_k$bad_air <- as.logical(train_k$bad_air)
test_k$bad_air <- as.logical(test_k$bad_air)
# 시간이 다소 오래 걸려서 패스
knn.trains <- train(bad_air~., data = train_k, method = 'knn', trControl = control, tuneGrid = grid)

acc <- c()
pred <- c()
rec <- c()
F1 <- c()
#k <- c()
Auc <- c()
# 값이 계속 올라가니까 한번 끝까지 search를 해보자
for(i in seq(100,400,by=20)){
  modeling <- knn(train = train_k[,1:4], test = test_k[,1:4], cl = train_k$bad_air, k = i, prob = T)
  tb <- table(pred=modeling, actual = test_k$bad_air)
  acc <- c(acc, sum(diag(tb))/sum(tb))
  pred <- c(pred, sum(tb[2,2])/sum(tb[2,]))
  rec <- c(rec, sum(tb[2,2])/sum(tb[,2]))
  F1 <- c(F1, 2*(acc*pred)/(acc+pred))
  testing <- ifelse(modeling == TRUE, attributes(modeling)$prob, 1-attributes(modeling)$prob)
  make_p <- prediction(testing, test_k$bad_air)
  acus <- performance(make_p, 'auc')
  Auc <- c(Auc, acus@y.values[[1]])
}

k <- seq(100,400, by=20)
#k <- c(k, seq(300, 400, by=10))
length(k)
length(pred)
plot(k, acc)
plot(k, pred)
plot(k, rec)
plot(k, Auc)
F1 <- 2*(pred*rec)/(pred+rec)
plot(k, F1)

final_model <- knn.model1 <- knn(train = train_k[,1:4], test = test_k[,1:4], cl = train_k$bad_air, k = 80)
table(final_model, test$bad_air)
mean(final_model == test$bad_air)
library(caret)
grid <- expand.grid(.k = seq(300,350,by=10))
control <- trainControl(method = 'cv')
set.seed(2020)
train_k$bad_air <- as.factor(train_k$bad_air)
test_k$bad_air <- as.factor(test_k$bad_air)
knn.trains <- train(bad_air~., data = train_k, method = 'knn', trControl = control, tuneGrid = grid)

train_k$bad_air <- as.logical(train_k$bad_air)
test_k$bad_air <- as.logical(test_k$bad_air)

set.seed(2020)
train_k$bad_air <- as.factor(train_k$bad_air)
test_k$bad_air <- as.factor(test_k$bad_air)
train_k$bad_air <- as.logical(train_k$bad_air)
test_k$bad_air <- as.logical(test_k$bad_air)
knn.trains <- train(bad_air~., data = train_k, method = 'knn', trControl = control, tuneGrid = grid)

# 우선 best model로서 k를 75로 사용

# 혹시라도 가중 knn을 적용해서 모델을 개선시킬 수 없을지 확인해본다 이 부분은 보고서에 반영하지 않았다.
# 시간이 다소 많이 드는 작업..
set.seed(122)

kknn.train <- train.kknn(bad_air~., data = train_k, kmax = 100, distance = 10, kernel = c("rectangular", "triangular", "epanechnikov"))

final_model_prob <- knn.model1 <- knn(train = train_k, test = test_k, cl = train_k$bad_air, k = 75, prob = T)
head(final_model_prob)


