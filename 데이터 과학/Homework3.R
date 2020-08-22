load("C:/Users/sec/Desktop/교과목들/데이터 과학/bankruptcy.RData")
prs <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/PRSA_data.csv")

library(dplyr)
library(tidyr)
library(stringr)
library(caret)
library(ROCR)
library(ggplot2)
library(reshape2)
library(kknn)
install.packages('tidyr')
install.packages('dplyr')
install.packages('caret')
#install.packages('ggplot2')
#remove.packages('ggplot2')

str(prs)
View(prs)

prs$pm2.5

prs <- prs[!is.na(prs$pm2.5), ]

str(prs)
View(prs)

prs.test <- prs[prs$year == 2014, ]
prs.train <- prs[prs$year != 2014, ]

prs.2010 <- prs.train[prs$year == 2010, ]
prs.2011 <- prs.train[prs$year == 2011, ]
prs.2012 <- prs.train[prs$year == 2012, ]
prs.2013 <- prs.train[prs$year == 2013, ]
# 구성은 대개 비슷함을 확인할 수 있다.
plot(density(prs.train$pm2.5))
plot(density(prs.test$pm2.5))

# 3분위수도 오바야
dew_quant <- tapply(prs.train$pm2.5, prs.train$dew_group, function(x){ return(quantile(x)[4]) })
prs.train$predic_quant_dew <- dew_quant[prs.train$dew_group]
prs.train$error_quant_dew <- prs.train$pm2.5 - prs.train$predic_quant_dew
RMSE_quant_dew <- sqrt(mean(prs.train$error_quant_dew**2))
RMSE_quant_dew


boxplot(prs.train$pm2.5~prs.train$month)

# 월별 평균 미세먼지 농도
tapply(prs.train$pm2.5, prs.train$month, mean)
# 2010년부터 2013년까지 전체 월별 미세먼지 농도의 평균은 대체적으로 10월~2월, 가을에서 겨울 시점이 높았음
tapply(prs.2010$pm2.5, prs.2010$month, mean)
# 2010년의 경우 10~11월이 높게 나타남 이례적으로 7월도 높게 나타남
tapply(prs.2011$pm2.5, prs.2011$month, mean)
# 2011년의 경우 여전히 10월 중이 높게 나타나고 2월이 가장 높게 나타남
tapply(prs.2012$pm2.5, prs.2012$month, mean)
# 2012년의 경우 전반적으로 미세먼지 농도의 수치가 낮았으나 12~1월 겨울 중의 미세먼지 농도가 높았음
tapply(prs.2013$pm2.5, prs.2013$month, mean)
# 2013년 전반적으로 1~3월 겨울철의 미세먼지 농도가 높았는데 1월의 경우가 압도적으로 미세먼지 농도가 높았음

# 월별 미세먼지 농도를 ggplot을 이용하여 시각화
ggplot(data = prs.train, aes(x = as.factor(month), y = pm2.5)) + geom_boxplot()
# 시각화 결과
# 전반적으로 가을, 겨울철의 미세먼지 농도가 봄 여름 같이 비교적 따뜻한 날보다는 더 미세먼지 농도가 높았으며, 
# 겨울철에는 미세먼지 농도가 매우 높은 날이 있었음을 확인 -- outlier 존재
ggplot(data = prs.train, aes(x = as.factor(month), y = pm2.5)) + geom_boxplot() + facet_wrap(~prs.train$year)

table(prs.train$TEMP)

# 온도에 따라 미세먼지 농도의 비중은 어떻게 될까 ggplot을 이용해 시각화를 해보면
ggplot(data = prs.train, aes(x = as.numeric(TEMP), y = pm2.5)) + geom_line()
# 뚜렷이 구분이 되지는 않지만, 평균적으로 기온이 높을 때보다는 기온이 낮았을 때, 보다 더 미세 먼지 농도가 높음을 확인할 수 있다.
# 년도별로도 확인해보자
ggplot(data = prs.train, aes(x = as.numeric(TEMP), y = pm2.5)) + geom_line() + facet_wrap(~prs.train$year)

# tapply를 이용하여 수치를 그래프로 표현하여 확인을 해보면 
plot(names(tapply(prs.train$pm2.5, prs.train$TEMP, mean)), tapply(prs.train$pm2.5, prs.train$TEMP, mean))

# 보다 기온이 낮을 때 (그렇다고 낮을수록 무조건 높은 것이 아니라) 우리나라 평균적인 겨울철 온도인 -10~0도 사이의 겨울철과 0~10도의 가을철 온도 때의 
# 경우가 가장 미세먼지 농도가 높았음을 확인할 수 있다


# 바람의 방향의 경우 cv일 때 평균적으로 미세 먼지의 농도가 높음을 확인할 수 있다!
tapply(prs.train$pm2.5, prs.train$cbwd, mean)

ggplot(data = prs.train, aes(x = cbwd, y = pm2.5)) + geom_boxplot() + facet_wrap(~prs.train$year)

# 풍속의 경우 풍속이 작을 때 미세 먼지의 농도가 높음을 확인할 수 있다! 이는 직관하고 굉장히 비슷한 결과임을 알 수 있다!
plot(prs.train$Iws,prs.train$pm2.5) 

# 혹시라도 변수간의 상관관계가 있는 지를 확인한다. 이는 regression 실행 시 다중 공선성의 우려를 막기 위함이다.
# 상관관계분석이 가능한 이슬점, 온도, 기압, 적설량, 강우량, 풍속을 통해 확인한다.
library(corrplot)
cors <- cor(prs.train[, c(6, 7, 8, 9, 11, 12 ,13)])
corrplot.mixed(cors)

# 분석 결과 이슬점과 온도간 상관관계가 높으며 온도랑 기압, 기압과 이슬점 간의 상관관계가 다소 분포함을 확인할 수 있다. 이는 추후에 vif 다중공선성 검정을 통해 적합 후에 확인하도록 한다.

# 우선 미세먼지 농도를 예측하는데 년도랑 일수는 중요하지 않은 변수고 계절성을 띠는 월 데이터만 따로 가지고 온다.
names(prs.train)
prs.train.adjust <- prs.train[,c(3, 6, 7, 8, 9, 10,11,12,13)]
str(prs.train.adjust)
# 그 다음 월 데이터를 factor형으로 바꾸어 준다.
prs.train.adjust$month <- as.numeric(prs.train.adjust$month)

# 최량 부분집합 회귀분석을 통해 유의미한 변수를 가리는 과정을 밟아보자
library(leaps)
subset <- regsubsets(pm2.5~., data = prs.train.adjust)
best_summary <- summary(subset)
names(best_summary)
which.min(best_summary$rss)
# 8개의 변수를 선택하는 것이 가장 모형이 최적화된 것 같다.
# 멜로의 cp 통계치를 이용하여 정확히 확인을 해보면 
plot(subset, scale = 'Cp')

# 이슬점, 온도, 기압, 풍향, 풍속, 적설, 강우, 월 다 비교를 해봐야겠다.

# 우선 월별 데이터가 중요하되 이것을 계절로 변경을 해보자

prs.train$season <- cut(prs.train$month, breaks = c(3, 7, 9, 11), right = F, labels = c("spring", "summer", "fall"))
prs.train$season <- ifelse(is.na(prs.train$season), "winter", prs.train$season)
prs.train$season <- as.factor(prs.train$season)
table(prs.train$season)
prs.train$season <- ifelse(prs.train$season==3, "fall", prs.train$season)

## 그렇다면 이제 계절별 평균 미세먼지 농도를 확인해보자

sv_models_season <- tapply(prs.train$pm2.5, prs.train$season, mean)

prs.train$prediction_season <- sv_models_season[prs.train$season]

prs.train[prediction_season]

prs.train$error <- prs.train$pm2.5 - prs.train$prediction_season

RMSE <- sqrt(mean(prs.train$error**2))
RMSE     
# 표준편차랑 큰 차이가 없어서 예측률 꽝!
sd(prs.train$pm2.5)

# 그냥 월별로 하면 어떻게 될까? -- 더 안 좋은 결과를 초래한다.
sv_models_month <- tapply(prs.train$pm2.5, prs.train$month)
prs.train$prediction <- sv_models_month[prs.train$month]
prs.train$error2 <- prs.train$pm2.5 - prs.train$prediction
RMSE <- sqrt(mean(prs.train$error2**2))
RMSE

# 온도로 한번 가보자!!
# 키, 온도, 체중의 경우 num형태이지만, 그대로 regression을 돌리기에는 적당한 변수는 아니다.
# grouping을 통해 factor type으로 변환시키는 것이 중요할 듯
boxplot(prs.train$pm2.5~prs.train$TEMP)
summary(prs.train$TEMP)
quantile(prs.train$TEMP)
prs.train$temp_group <- cut(prs.train$TEMP, breaks = c(-19, -11, -4, 2, 7, 13, 20, 27, 34, 41, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), right = F)

sv_models_temp <- tapply(prs.train$pm2.5, prs.train$temp_group, mean)
prs.train$temp_group

prs.train[, c(6, 18)]

prs.train$prediction <- sv_models_temp[prs.train$temp_group]
prs.train$error3 <- prs.train$pm2.5 - prs.train$prediction
prs.train$error3
RMSE <- sqrt(mean(prs.train$error3**2))
RMSE

# 온도, 계절 등이 그다지 좋은 변수는 아닌 것 같다.
#### 온도랑 계절을 나누는 적절한 cutpoint르 잘 못찾아서 그럴 수도 있다. 이를 잘 발견해주는 것이 중요할 수도 있다.

# 기압도 절차상 확인을 해보자
table(prs.train$PRES)
boxplot(prs.train$pm2.5~prs.train$PRES)

prs.train$pres_group <- cut(prs.train$PRES, breaks = c(0, 996, 1002, 1008, 1014, 1020, 1026, 1030, 1035, Inf), labels = c("1","2","3","4","5","6","7","8","9"), right = F)
sv_models_pres <- tapply(prs.train$pm2.5, prs.train$pres_group, mean)
prs.train$prediction <- sv_models_pres[prs.train$pres_group]
prs.train$error4 <- prs.train$pm2.5 - prs.train$prediction
RMSE <- sqrt(mean(prs.train$error4**2))
RMSE

# 바람 방향으로 해보자
table(prs.train$cbwd)

sv_models_cbwd <- tapply(prs.train$pm2.5, prs.train$cbwd, mean)
prs.train$prediction <- sv_models_cbwd[prs.train$cbwd]
prs.train$error5 <- prs.train$pm2.5 - prs.train$prediction
RMSE <- sqrt(mean(prs.train$error5**2))
RMSE

# 풍속 같은 경우는 역의 관계를 갖는 게 조금 보이는 데 어떻게 변수를 조정해줄까?
summary(prs.train$Iws)
boxplot(prs.train$pm2.5~prs.train$Iws)
boxplot(prs.train$Iws)


############ 이게 안되는 이유가 궁금하다
sv_models_fool <- tapply(prs.train$pm2.5, prs.train$Iws, mean)
sv_models_fool
table(prs.train$Iws)
prs.train$prediction_fool <- sv_models_fool[prs.train$Iws]


# 이렇게 되어있는 것을 어떻게 factorize하지?
# 우선 저 boxplot에 나와있는 것을 기준으로 해보자

prs.train$wind_group <- cut(prs.train$Iws, breaks = c(0, 1.79, 5.81, 23.26, 25.02, 46.5, 65.7, 85.4, 109.1, 140.8, 173, 211.9, 276.7, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"), right = F)
prs.train$wind_group2 <- cut(prs.train$Iws, breaks = c(0, 1.79, 5.81, 23.26, 25.02, 42, 55, 70.2, 88.5, 111.3, 140.8, 173, 208.3, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"), right = F)
sv_models_wind <- tapply(prs.train$pm2.5, prs.train$wind_group, mean)
prs.train$prediction <- sv_models_wind[prs.train$wind_group2]
prs.train$error6 <- prs.train$pm2.5 - prs.train$prediction
RMSE <- sqrt(mean(prs.train$error6**2))
RMSE
RSS_w <- sum((prs.train$error6)**2)
SST_w <- sum((prs.train$pm2.5 - mean(prs.train$pm2.5))**2)
RSQ_w <- 1 - (RSS_w/SST_w)
RSQ_w

# 마지막으로 이슬점 확인해보자 얘도 유의미해보이네..!

summary(prs.train$DEWP)
plot(density(prs.train$DEWP))
hist(prs.train$DEWP)
boxplot(prs.train$pm2.5~prs.train$DEWP)

#Error in sv_models_fake[prs.train$DEWP] : 
#  only 0's may be mixed with negative subscripts
# 이 에러 메세지가 잘 이해가 가지 않는다....ㅠㅠㅠ
sv_models_fake <- tapply(prs.train$pm2.5, prs.train$DEWP, mean)
prs.train$fake <- sv_models_fake[prs.train$DEWP]


prs.train$dew_group <- cut(prs.train$DEWP, breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
prs.train$dew_group <- cut(prs.train$DEWP, breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, 28, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"), right = F)
sv_models_dew <- tapply(prs.train$pm2.5, prs.train$dew_group, mean)
prs.train$prediction <- sv_models_dew[prs.train$dew_group]
prs.train$error7 <- prs.train$pm2.5 - prs.train$prediction
RMSE <- sqrt(mean(prs.train$error7**2))
RMSE
RSS <- sum((prs.train$error7)**2)
SST <- sum((prs.train$pm2.5 - mean(prs.train$pm2.5))**2)
RSQ <- 1 - (RSS/SST)
RSQ


############ 이게 안되는 이유가 궁금하다
sv_model_dew2 <- tapply(prs.train$pm2.5, prs.train$DEWP, mean)
prs.train$prediction <- sv_model_dew2[prs.train$DEWP]


# 전체 변수를 다 선형회귀 돌린 모델의 성능
summary(lm(pm2.5~TEMP + Iws + cbwd+ as.factor(month) + PRES +DEWP, data=prs.train))


# 이슬점 데이터가 가장 유력해보이니까 걔를 사용하자!

prs.test$dew_group <- cut(prs.test$DEWP,  breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
prs.test$prediction <- sv_models_dew[prs.test$dew_group]
prs.test$error <- prs.test$pm2.5 - prs.test$prediction
RMSE <- sqrt(mean(prs.test$error**2))
RMSE
RSS1 <- sum((prs.test$error)**2)
SST1 <- sum((prs.test$pm2.5-mean(prs.test$pm2.5))**2)
RSQ1 <- 1 - (RSS1/SST1)
RSQ1

plot(pm2.5~prediction, data=prs.train, xlab = "pred", ylab = "actual")
plot(pm2.5~prediction, data=prs.test, xlab = "pred2", ylab = "actual2")

# 우선 그래프만 보면 예측 값이 형편없다 아마 평균값을 기준으로 예측을 잡아서, outlier가 대거 분포해있는 경우 예측력이 몹시 떨어졌다
# 그래프를 보면 예측 값의 max는 136인데 기본적으로 200이 넘어가는 분포수가 생각보다 많음을 알 수 있다.
# grouping을 다시 해주던가 평균이 아닌 다른 값을 사용해야 할 거 같다.
table(prs.test$pm2.5)
table(prs.test$prediction)


########## 여기까지가 Memorization method를 사용했으니 이제 lm을 돌려서 확인해보자, 오히려 예측력이 떨어지네

# 가장 유의미한 변수처럼 보였던, Dew point와 풍속, 풍향 3개를 살펴본다

summary(lm(pm2.5~DEWP, data=prs.train))
summary(lm(pm2.5~Iws, data=prs.train))
summary(lm(pm2.5~cbwd, data=prs.train))

# R2가 가장 높게 나오는 Iws로 우선 해보자

iws_fit <- lm(pm2.5~Iws, data=prs.train)
errors <- prs.train$pm2.5 - iws_fit$fitted.values  
rmse <- sqrt(mean(errors**2))
rmse

dew_fit <- lm(pm2.5~DEWP, data=prs.train)
errors2 <- prs.train$pm2.5 - dew_fit$fitted.values
rmse2 <- sqrt(mean(errors2**2))
rmse2

#### 결국 데이터를 직접 핸들링해서 R2를 높이는 수 밖에 없겠다.

# 우선 그 방법으로 y값에 logarithm을 취하는 방식을 생각해본다!!

# 만일 이곳에 등장하는 Inf값은 어떻게 통제하는 것이 좋을까?
# 0으로 그냥 하는 이 방법도 다만 위험한 값이 되지 않을까..?
# 이 부분도 논의점이 될 수 있을 거 같다...!
prs.train$log <- log(prs.train$pm2.5)
prs.test$log <- log(prs.test$pm2.5)
prs.train$log <- ifelse(prs.train$log == -Inf, 0, prs.train$log)
prs.test$log <- ifelse(prs.test$log == -Inf, 0, prs.test$log)

# logarithm을 이렇게 통제하는 것도 정확하지는 않다..

prs.train$log2 <- ifelse(prs.train$log < 0, prs.train$pm2.5, prs.train$log)
prs.test$log2 <- ifelse(prs.test$log < 0, prs.test$pm2.5, prs.test$log)

## 이슬점의 경우?
sv_model_dew_up <- tapply(prs.train$log, prs.train$dew_group, mean)
prs.train$dew_group2 <- sv_model_dew_up[prs.train$dew_group]
prs.train$error_dewlog <- prs.train$log - prs.train$dew_group2 
RMSE_dewlog <- sqrt(mean(prs.train$error_dewlog**2))
RMSE_dewlog

sv_model_dew_up2 <- tapply(prs.train$log2, prs.train$dew_group, mean)
prs.train$dew_group3 <- sv_model_dew_up2[prs.train$dew_group]
prs.train$error_dewlog2 <- prs.train$log2 - prs.train$dew_group3 
RMSE_dewlog <- sqrt(mean(prs.train$error_dewlog2**2))
RMSE_dewlog

RSS_dewlog <- sum((prs.train$error_dewlog)**2)
SST_dewlog <- sum((prs.train$log-mean(prs.train$log))**2)
RSQ_dewlog <- 1 - (RSS_dewlog/SST_dewlog)
RSQ_dewlog

## 풍향의 경우??
sv_model_wind_up <- tapply(prs.train$log, prs.train$wind_group, mean)
prs.train$prediction_wind <- sv_model_wind_up[prs.train$wind_group]
prs.train$error_wind <- prs.train$log - prs.train$prediction_wind
RMSE_wind <- sqrt(mean(prs.train$error_wind**2))
RMSE_wind
RSS_wind <- sum((prs.train$error_wind)**2)
SST_wind <- sum((prs.train$log-mean(prs.train$log))**2)
RSQ_wind <- 1 - (RSS_wind/SST_wind)
RSQ_wind

# 조금 더 안좋다..
sv_models_cbwd_log <- tapply(prs.train$log, prs.train$cbwd, mean)
prs.train$prediction_cbwd <- sv_models_cbwd_log[prs.train$cbwd]
prs.train$error_cbwd <- prs.train$log - prs.train$prediction_cbwd
RMSE_cbwd <- sqrt(mean(prs.train$error_cbwd**2))
RMSE_cbwd

## 일단은 logarithm을 통해 조금 더 개선됨을 확인할 수 있다!!

# 그럼 Is, Ir 데이터는 어떠할까??

# Is데이터는 사용하기 어렵겠다....
plot(density(prs.train$Is))
table(prs.train$Is)

# Ir데이터도 마찬가지...
table(prs.train$Ir)


sv_models_pres_log <- tapply(prs.train$log, prs.train$pres_group, mean)
prs.train$prediction_pres <- sv_models_pres_log[prs.train$pres_group]
prs.train$error_pres <- prs.train$log - prs.train$prediction_pres
RMSE_pres <- sqrt(mean(prs.train$error_pres**2))
RMSE_pres

######################!!!!! 변수 간의 grouping을 해보자!!!

#1) 기압과 온도를 grouping해보자

pr <- tapply(prs.train$pm2.5, prs.train$pres_group, mean)
te <- tapply(prs.train$pm2.5, prs.train$temp_group, mean)
pr_te <- pr+te
pr_te <- (pr_te)/2
# 이거를 model에 써보면 어떨까..?
pr_te

prs.train$temp_group <- cut(prs.train$TEMP, breaks = c(-19, -11, -4, 2, 7, 13, 20, 27, 34, 41, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), right = F)
prs.train$pres_group <- cut(prs.train$PRES, breaks = c(0, 996, 1002, 1008, 1014, 1020, 1026, 1030, 1035, 1041, Inf), labels = c("1","2","3","4","5","6","7","8","9", "10"), right = F)

prs.train$pr_te <- pr_te[prs.train$temp_group]
prs.train$pr_te <- pr_te[prs.train$pres_group]

prs.train$error.pr_te <- prs.train$pm2.5 - prs.train$pr_te 
RMSE_pr_te <- sqrt(mean(prs.train$error.pr_te**2))
RMSE_pr_te


#2) 이슬점과 온도를 grouping해보자

#prs.test$dew_group <- cut(prs.test$DEWP,  breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
prs.train$dew_group <- cut(prs.train$DEWP,  breaks = c(-Inf, -28, -23, -18, -13,  -9, -5, -1, 3, 6, 9, 13, 17, 21, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
prs.train$temp_group2 <- cut(prs.train$TEMP, breaks = c(-19, -11, -4, 2, 7, 10, 13, 18, 20, 25, 27, 31, 34, 41, Inf), labels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), right = F)
boxplot(prs.train$pm2.5~prs.train$TEMP)
# 둘의 cutoff group수를 같게 해주어 비교를 수행해본다!!!
tapply(prs.train$pm2.5, prs.train$dew_group, mean)
tapply(prs.train$pm2.5, prs.train$temp_group2, mean)



###################################################################3 Classification
str(bankruptcy_train)
str(bankruptcy_test)
bankruptcy_train
sapply(bankruptcy_train[, -1], as.factor)
bankruptcy_test$Class <- as.factor(bankruptcy_test$Class)
bankruptcy_test$Competitiveness <- as.factor(bankruptcy_test$Competitiveness)
bankruptcy_test$Credibility <- as.factor(bankruptcy_test$Credibility)
bankruptcy_test$`Financial Flexibility` <- as.factor(bankruptcy_test$`Financial Flexibility`)
bankruptcy_test$`Industrial Risk` <- as.factor(bankruptcy_test$`Industrial Risk`)
bankruptcy_test$`Management Risk` <- as.factor(bankruptcy_test$`Management Risk`)
bankruptcy_test$`Operating Risk` <- as.factor(bankruptcy_test$`Operating Risk`)

bankruptcy_train$Class <- as.factor(bankruptcy_train$Class)
bankruptcy_train$Competitiveness <- as.factor(bankruptcy_train$Competitiveness)
bankruptcy_train$Credibility <- as.factor(bankruptcy_train$Credibility)
bankruptcy_train$`Financial Flexibility` <- as.factor(bankruptcy_train$`Financial Flexibility`)
bankruptcy_train$`Industrial Risk` <- as.factor(bankruptcy_train$`Industrial Risk`)
bankruptcy_train$`Management Risk` <- as.factor(bankruptcy_train$`Management Risk`)
bankruptcy_train$`Operating Risk` <- as.factor(bankruptcy_train$`Operating Risk`)


# 학습 데이터와 테스트 데이터의 종속 변수 분포확인
table(bankruptcy_train$Class)
table(bankruptcy_test$Class)
# 음... 다소 학습 데이터가 부도의 경우가 굉장히 높았구먼.. 조금 데이터 분포의 차이가 존재

# 우선 corpID는 예측에 그다지 쓰이지 않으므로 제거

bankruptcy_trains <- bankruptcy_train[, -1]
bankruptcy_tests <- bankruptcy_test[, -1]

Q1.

table(bankruptcy_trains$Competitiveness, bankruptcy_trains$Class)
# 경쟁력은 나름 유의미한 차이를 보이는 것 같다

# 신용성은 적당히 잘 분포해 있는 것 같다. 
table(bankruptcy_trains$Credibility, bankruptcy_trains$Class)

# 재무 건전성도 비슷한 유의성을 가지지만 경쟁력이 보다 더 괜찮은 변수처럼 보인다. 
table(bankruptcy_trains$`Financial Flexibility`, bankruptcy_trains$Class)

# 비슷하게 다른 변수들도 개략적인 것을 관찰해보자

# 얘는 조금 명확하게 구분하는 것 같지는 않죠
table(bankruptcy_trains$`Industrial Risk`, bankruptcy_trains$Class)

# 얘도 그래 보인다
table(bankruptcy_trains$`Management Risk`, bankruptcy_trains$Class)

table(bankruptcy_trains$`Operating Risk`, bankruptcy_trains$Class)

# 얼핏 보았을 때는 경쟁력과 재무 건전성이 실제로 부도를 예측하기에 적합한 변수로 판단되나 정확한 분석을 위해 모델링을 하나씩 만들어보기로 한다.

prop.table(table(bankruptcy_trains$Competitiveness, bankruptcy_trains$Class), margin = 1)

# 실행 결과 경쟁력이 평균 정도의 해당하는 기업은 0.09의 확률로 부도를 겪었다. 

# 그 말은 평균 정도의 기업이 0.9 정도는 부도를 겪지 않은 것이다.

# 기업들이 부도를 겪지 않음을 예측하기 위해서 모델링을 해보면

sv_mdel_com <- prop.table(table(bankruptcy_trains$Competitiveness, bankruptcy_trains$Class), margin = 1)[,2]
bankruptcy_trains$prob <- sv_mdel_com[bankruptcy_trains$Competitiveness]
bankruptcy_trains$prediction <- bankruptcy_trains$prob > 0.9
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
bankruptcy_trains[, c('prediction', 'Class')]

tble1 <- table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)

acc1 <- sum(diag(tble1))/sum(tble1)
prec1 <- sum(tble1[1,1])/sum(tble1[1,])  
rec1 <- sum(tble1[1,1])/sum(tble1[,1]) 
acc1
prec1
rec1

p1 <- prediction(bankruptcy_trains$prob, bankruptcy_trains$Class)
AUC1 <- performance(p1, 'auc')
AUC1@y.values[[1]]
plot(performance(p1, 'tpr', 'fpr'))

# 높게 나왔으나 과적합의 우려가 있다



# 테스트 케이스의 모든 케이스에서 예측이 성공함을 알 수가 있다.

# 신용성은 어떠할까
prop.table(table(bankruptcy_trains$Credibility, bankruptcy_trains$Class), margin=1)
# 대략 threshold를 0.7로 잡아본다

sv_mdel_cre <- prop.table(table(bankruptcy_trains$Credibility, bankruptcy_trains$Class), margin=1)[, 2]
bankruptcy_trains$prob_c <- sv_mdel_cre[bankruptcy_trains$Credibility]
bankruptcy_trains$prediction <- bankruptcy_trains$prob_c > 0.75438596
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble3 <-  table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)
tble3
acc3 <- sum(diag(tble3))/sum(tble3)
prec3 <- sum(tble3[1,1])/sum(tble3[1,])
rec3 <- sum(tble3[1,1])/sum(tble3[,1])
acc3
prec3
rec3
p <- prediction(bankruptcy_trains$prob_c, bankruptcy_trains$Class)
AUC2 <- performance(p, 'auc')
AUC2@y.values
plot(performance(p, 'tpr', 'fpr'))

# 재무 건전성은 ?
prop.table(table(bankruptcy_trains$`Financial Flexibility`, bankruptcy_trains$Class), margin=1)
sv_mdel_fin <- prop.table(table(bankruptcy_trains$`Financial Flexibility`, bankruptcy_trains$Class), margin=1)[,2]
bankruptcy_trains$prob_f <- sv_mdel_fin[bankruptcy_trains$`Financial Flexibility`]
bankruptcy_trains$prediction <- bankruptcy_trains$prob_c > 0.9
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble4 <-  table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)
acc4 <- sum(diag(tble4))/sum(tble4)
prec4 <- sum(tble4[1,1])/sum(tble4[1,])
rec4 <- sum(tble4[1,1])/sum(tble4[,1])
acc4
prec4
rec4
p <- prediction(bankruptcy_trains$prob_f, bankruptcy_trains$Class)
AUC3 <- performance(p, 'auc')
AUC3@y.values
plot(performance(p, 'tpr', 'fpr'))

# 산업 리스크는? 그닥 좋은 예측력을 보이지는 않았다.
prop.table(table(bankruptcy_trains$`Industrial Risk`, bankruptcy_trains$Class), margin=1)
sv_mdel_ind<-prop.table(table(bankruptcy_trains$`Industrial Risk`, bankruptcy_trains$Class), margin=1)[,2]
bankruptcy_trains$prob_i <- sv_mdel_ind[bankruptcy_trains$`Industrial Risk`]
bankruptcy_trains$prediction <- bankruptcy_trains$prob_i > 0.63
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble5 <-  table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)
acc5 <- sum(diag(tble5))/sum(tble5)
prec5 <- sum(tble5[1,1])/sum(tble5[1,])
rec5 <- sum(tble5[1,1])/sum(tble5[,1])
acc5
prec5
rec5
p <- prediction(bankruptcy_trains$prob_i, bankruptcy_trains$Class)
AUC4 <- performance(p, 'auc')
AUC4@y.values
plot(performance(p, 'tpr', 'fpr'))

# 경영 리스크는? 
prop.table(table(bankruptcy_trains$`Management Risk`, bankruptcy_trains$Class), margin=1)
sv_mdel_man <- prop.table(table(bankruptcy_trains$`Management Risk`, bankruptcy_trains$Class), margin=1)[,2]
bankruptcy_trains$prob_m <- sv_mdel_man[bankruptcy_trains$`Management Risk`]
bankruptcy_trains$prediction <- bankruptcy_trains$prob_m > 0.6
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble6 <-  table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)
tble6
acc6 <- sum(diag(tble6))/sum(tble6)
prec6 <- sum(tble6[1,1])/sum(tble6[1,])
rec6 <- sum(tble6[1,1])/sum(tble6[,1])
acc6
prec6
rec6
p <- prediction(bankruptcy_trains$prob_m, bankruptcy_trains$Class)
AUC5 <- performance(p, 'auc')
AUC5@y.values
plot(performance(p, 'tpr', 'fpr'))

# 영업 리스크는?
prop.table(table(bankruptcy_trains$`Operating Risk`, bankruptcy_trains$Class), margin=1)
sv_mdel_op <- prop.table(table(bankruptcy_trains$`Operating Risk`, bankruptcy_trains$Class), margin=1)[,2]
bankruptcy_trains$prob_o <- sv_mdel_op[bankruptcy_trains$`Operating Risk`]
bankruptcy_trains$prediction <- bankruptcy_trains$prob_o > 0.5
bankruptcy_trains$prediction <- ifelse(bankruptcy_trains$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble7 <-  table(pred = bankruptcy_trains$prediction, actual = bankruptcy_trains$Class)
tble7
acc7 <- sum(diag(tble7))/sum(tble7)
prec7 <- sum(tble7[1,1])/sum(tble7[1,])
rec7 <- sum(tble7[1,1])/sum(tble7[,1]) 
acc7
prec7
rec7
p <- prediction(bankruptcy_trains$prob_m, bankruptcy_trains$Class)
AUC6 <- performance(p, 'auc')
AUC6@y.values
plot(performance(p, 'tpr', 'fpr'))

## 여기서는 train set에서 가장 결과가 좋았던 경쟁력 지표를 단일 변수로 선정한다.

Q2.
# test case에서 확인해보자

bankruptcy_tests$prob1 <- sv_mdel_com[bankruptcy_tests$Competitiveness]
bankruptcy_tests$prediction <- bankruptcy_tests$prob1 > 0.9
bankruptcy_tests$prediction <- ifelse(bankruptcy_tests$prediction==TRUE,'Non-Bankruptcy', 'Bankruptcy')
tble2 <- table(pred = bankruptcy_tests$prediction, actual = bankruptcy_tests$Class)
tble2
acc2 <- sum(diag(tble2))/sum(tble2)
prec2 <- sum(tble2[1,1])/sum(tble2[1,])  
rec2 <- sum(tble2[1,1])/sum(tble2[,1]) 
acc2
prec2
rec2
tble2

final_p <- prediction(bankruptcy_tests$prob1, bankruptcy_tests$Class)
Final_AUC <- performance(final_p, 'auc')
Final_AUC@y.values[[1]]
plot(performance(final_p, 'tpr', 'fpr'))

Q3.
# 명확하게 일치함을 확인할 수 있다. train 데이터, 테스트 데이터 전부 예측을 잘 했으므로 과적합이 있다고 보기는 어렵다.


Q4. # 0.9가 바람직하겠네 그 이유까지 보고서에 작성하자
plot(performance(final_p,'prec'))
plot(performance(final_p, 'rec'))

Q5.
plot(performance(final_p, 'f'))
performance(final_p, 'f')

Q6.
plot(performance(p1, 'tpr', 'fpr'))
plot(performance(final_p, 'tpr','fpr'))

Q7.
plot(performance(p1, 'acc'))
plot(performance(final_p, 'acc'))

Q8.
