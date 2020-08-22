# decision tree 구축 연습!!

bankruptcy_train_dt
bankruptcy_test_dt

library(caret)
library(rpart)
library(rpart.plot)
library(InformationValue)

str(loans)
View(loans)

loan_index <- createDataPartition(loans$outcome, p =.75, list = F)
loan_train <- loans[loan_index, ]
loan_test <- loans[-loan_index, ]


table(loan_train$outcome)
table(loan_test$outcome)

# rpart()
# decision tree를 이용한 예측 모델링 구성
loan_model <- rpart(outcome~. , data = loan_train, method = 'class', control = rpart.control(cp = 0))

# 시각화를 통해 확인할 수 있지만 지금처럼 변수가 많은 모델은 별로 시각화의 의미가 없다.
rpart.plot(loan_model)

# 만든 모델을 학습 데이터에 적용해봅시다..!

loan_train$pred <- predict(loan_model, newdata = loan_train, type = 'class') # type이 class임을 유념한다

# ~. 을 사용할 때 반드시 이 과정을 거쳐 주어야 한다!!
loan_train <- loan_train[, -15]
loan_test <- loan_test[, -15]

# decision tree의 예측결과 - 가급적 confusionMatrix를 활용하자
# error의 이유가 뭐지..? < 기호 때문인가..
#confusionMatrix(loan_train$outcome, loan_train$pred)
tb1 <- table(loan_train$pred, loan_train$outcome)

sum(diag(tb1))/sum(tb1)

# 동일한 모형을 test 데이터에도 적용해보자

loan_test$pred <- predict(loan_model, newdata = loan_test, type = 'class')
tb2 <- table(loan_test$pred, loan_test$outcome)

sum(diag(tb2))/sum(tb2)


#confusionMatrix(loan_test$pred, loan_test$outcome)

# 우선 이러한 방향으로 decision tree를 구축하는 연습을 한다!!

# 과적합의 문제가 있으므로 2가지 방법을 생각해본다..!

1. pre-pruning!! -- maxdepth 나 minsplit 을 통해

loan_model_maxdepth <- rpart(outcome~. , data = loan_train, method = 'class', control = rpart.control(cp = 0, maxdepth=6))

loan_test$pred <- predict(loan_model_maxdepth, newdata = loan_test, type = 'class')

tb3 <- table(loan_test$pred, loan_test$outcome)
sum(diag(tb3))/sum(tb3)

# 조금은 더 개선되었다.

loan_model_minsplit <- rpart(outcome~. , data = loan_train, method = 'class', control = rpart.control(cp = 0, minsplit=500))

loan_test$pred <- predict(loan_model_minsplit, newdata = loan_test, type = 'class')

tb4 <- table(loan_test$pred, loan_test$outcome)
sum(diag(tb4))/sum(tb4)

# 조금 더 개선됨

2. post_pruning!! -- prune함수를 사용한다!
  
loan_model_prune <- rpart(outcome~. , data = loan_train, method = 'class', control = rpart.control(cp = 0))
# plot을 그려주는 과정을 거친다
plotcp(loan_model_prune) 
# 이 plot을 통해 0.0012을 채택해본다
loan_model_prune <- prune(loan_model_prune, cp = 0.0012)
loan_test$pred <- predict(loan_model_prune, newdata = loan_test, type = 'class')
tb5 <- table(loan_test$pred, loan_test$outcome)
sum(diag(tb5))/sum(tb5)

# 조금 더 개선됨!!

############### 이제 앞서서 했던 방식을 bankruptcy 데이터에 활용해보자!!
bankruptcy_train_dt
bankruptcy_test_dt
View(bankruptcy_train_dt)
bank_model <- rpart(Class~., data = bankruptcy_train_dt, method = 'class', control = rpart.control(cp=0))

rpart.plot(bank_model)

bankruptcy_train_dt$pred <- predict(bank_model, newdata = bankruptcy_train_dt, type = 'class')

table(bankruptcy_train_dt$pred, bankruptcy_train$Class)

bankruptcy_test_dt$ pred <- predict(bank_model, newdata = bankruptcy_test_dt, type = 'class')

table(bankruptcy_test_dt$pred, bankruptcy_test$Class)


# knn practice

cancer <- read.csv("https://github.com/hbchoi/SampleData/raw/master/wisc_bc_data.csv", stringsAsFactors = F)

library(class)
library(caret)
library(kknn)

cancer <- cancer[, -1]

## Knn에서 중요한 것은! 변수 간의 정규화이다

summary(cancer[c("radius_mean", "area_mean", "smoothness_mean")])

# 나는 정규화를 scale()을 이용하여 해본다
cancer.scale <- data.frame(scale(cancer[,-1]))
cancer.scale$diagnosis <- cancer$diagnosis

summary(cancer.scale[c("radius_mean", "area_mean", "smoothness_mean")])

index <- createDataPartition(cancer.scale$diagnosis, p = .7, list = F)
train <- cancer.scale[index, ]
test <- cancer.scale[-index, ]

# knn에서는 label을 지정해주는 작업이 필요한가?

train.label <- train[, 31]
test.label <- test[,31]

# 이 적합한 k를 뽑는 결과
grid <- expand.grid(.k = seq(2, 25, by=1))

control <- trainControl(method = 'cv')

set.seed(502)

knn.train <- train(diagnosis~., data = train, method = 'knn', trControl = control, tuneGrid = grid)
knn.train

#k는 9를 뽑으로가 하네요

# 교수님 모델과 비교해보자

prof.model <- knn(train = train[, -31], test = test[, -31], cl = train.label, k = 21)
my.model <- knn(train = train[, -31], test = test[, -31], cl = train.label , k = 9)

mean(prof.model == test.label)
mean(my.model == test.label)

table(prof.model , test.label)
table(my.model, test.label)

prof.model <- knn(train = train[,-31], test = test[, -31], cl = train.label, k = 21, prob = T)
my.model <- knn(train = train[, -31], test = test[, -31], cl = train.label, k = 9, prob = T)

head(attributes(prof.model)$prob)

prof.model.prob <- ifelse(prof.model == "M", attributes(prof.model)$prob, 1-attributes(prof.model)$prob)

my.model.prob <- ifelse(my.model == "M", attributes(my.model)$prob, 1- attributes(my.model)$prob)

prof.model.prob
my.model.prob
library(ROCR)

p <- prediction(prof.model.prob, test.label == "M")
plot(performance(p, 'tpr', 'fpr'))
AUC1 <- performance(p, 'auc')
AUC1@y.values[[1]]

p2 <- prediction(my.model.prob, test.label == "M")
plot(performance(p2, 'tpr', 'fpr'))
AUC2 <- performance(p2, 'auc')
AUC2@y.values[[1]]


# precision을 높이기 위해!!
threshold <- 0.11
prof.model.new <- ifelse(prof.model.prob > threshold, "M", "B")
my.model.new <- ifelse(my.model.prob > threshold, "M", "B")

table(prof.model.new, test.label)
table(my.model.new, test.label)

#### 가중값 이웃법을 이용해 다른 응용을 해보자!! -- 유클리디안만 있지 않음을 명심하자
set.seed(2123)

# 빌어먹을 response가 뭔데
kknn.train <- train.kknn(diagnosis~. , data = train, kmax = 25, distance = 2, kernel = c("rectangular", "triangular"))
