## Homework 1
# 1. Data Exploration and Cleaning
load("C:/Users/sec/Downloads/homework2_2020.RData")
View(cust.df)
library(tidyr)
library(stringr)
# 1.
str(cust.df)
## 정답 : observation 수 : 1000개, variable 수 : 11개

Q2.

## state.of.res, sex, marital.stat, hosuing.type 이상 이 4가지의 변수는 그 스트링이나 수치가 단지 범주형 변수임을 
# 표현해주므로 factor형으로 변환해주어야 한다.
cust.df$state.of.res <- as.factor(cust.df$state.of.res)
cust.df$sex <- as.factor(cust.df$sex)
cust.df$marital.stat <- as.factor(cust.df$marital.stat)
cust.df$housing.type <- as.factor(cust.df$housing.type)
str(cust.df)

Q3.
cust.df$custid <- as.character(cust.df$custid)
cust.df$custid <- str_pad(cust.df$custid, width = 7, side = "left", pad = "0")
cust.df$custid <- str_pad(cust.df$custid, width = 8, side = "left", pad = "c")

cust.df$custid



Q4. 
colnames(cust.df)
colSums(is.na(cust.df))
## 변수당 총 갯수 파악
length(cust.df$is.employed)
length(cust.df$Income)
length(cust.df$health.ins)
length(cust.df$housing.type)

328*100/1000
56*100/1000
## 정답 : is.employed : 328, Income : 328, housing.type = 56, recent.move = 56, num.vehicles = 56
## : is.employed : 32.8%, Income : 32.8%, housing.type : 5.6%, recent.move = 5.6%, num.vehicles = 5.6%

Q5.

cust.dfs <- cust.df[, c(2, 8, 9, 10)]
head(cust.dfs)
count_customer <- rowSums(is.na(cust.dfs)) ## 이 경우를 보면 rowSums의 결과가 3인 고객들이 다수 분포한다. -- 동일한 고객에게 발생함을 확인할 수 있다.
count_customer <- count_customer[which(count_customer == 3)]
count_customer
length(count_customer)
## 정답 : 이 NA값들을 포함하는 고객들의 수는 56명이다
## 정답 : 동일한 고객에게 NA값 발생


Q6

cust.df$is.employed <- as.character(cust.df$is.employed)
cust.df$is.employed
str(cust.df)
cust.df$is.employed <- str_replace(cust.df$is.employed, "TRUE", "employed")
cust.df$is.employed <- str_replace(cust.df$is.employed, "FALSE", "not employed")
cust.df$is.employed <- str_replace(cust.df$is.employed, NA, ) 
## which를 쓰되 NA의 논리 값의 경우 is.na()를 써주는 게 좋다!! 이 부분 시간 다소 허비했다!!
cust.df$is.employed[which(is.na(cust.df$is.employed))] <- "missing"


Q7
cust.df$state.of.res <- as.character(cust.df$state.of.res)
str(cust.df)
## 정답 : state별 평균값 
aggregate(Income~state.of.res, data= cust.df, mean)
## 정답 : state별 중간값
aggregate(Income~state.of.res, cust.df, median)
## df 구축
avg_income <- aggregate(Income~state.of.res, data= cust.df, mean)
colnames(avg_income)[2] <- "mean.income"
avg_income$median.income <- aggregate(Income~state.of.res, data = cust.df, median)[, 'Income']
avg_income
## 정답 : avg_income

Q8 ## 노가다 말고 어떻게 효율적으로 구성할까?? -- 아직까진 솔루션을 모르겠다 ㅠㅠ 찾음!!
## merge의 all과 key의 인자를 통해 구축 가능!!

cust_income <- aggregate(Income~state.of.res, data= cust.df, mean)
head(cust_income)
cust_df2 <- merge(cust.df, cust_income, all = T, by = 'state.of.res')
cust_df2
cust_df2$Income.x <- ifelse(is.na(cust_df2$Income.x), cust_df2$Income.y, cust_df2$Income.x)
cust_df2$Income.x 
colnames(cust_df2)[5] <- "Income" # 다시 이름 변경
cust_df2 <- cust_df2[, -12]
# 정답 : 주별 평균값으로 소득 NA값 대체
head(cust_df2)

Q9.
cust_aggregate <- aggregate(Income~state.of.res, cust.df, median)
cust_df3 <- merge(cust_df2, cust_aggregate, all = T, by = 'state.of.res')
head(cust_df3)
cust_df3$income.relative <- cust_df3$Income.x/cust_df3$Income.y
cust_df3$income.relative
colnames(cust_df3)[5] <- "Income"
cust_df3 <- cust_df3[, -12]
head(cust_df3)
# 정답 : 주별 중앙값 대비 고객별 소득 비중 산출 -- income.relative

Q10.
summary(cust_df3)
# summary를 통해 살펴보면 
# age의 Max가 146.7
# Income의 경우 Min이 -8700인 경우가 있었다.
# 평균 수명을 고려하여 146살의 경우와 소득이 -8700인 경우는 outlier로 간주 할 수 있다.
## 보다 정확히 boxplot을 그려보면 Q1-1.5IQR, Q3+1.5IQR에 각각 벗어나는 이상치임을 알 수 있다.
boxplot(cust_df3$Income)
boxplot(cust_df3$age)

Q11.
# 우선 histogram을 이용하면 이를 정확히 분석할 수 있다.
hist(cust_df3$age)
# 사람의 나이의 경우 145살의 경우 현재 평균 수명을 고려하면 생존하기는 어려운 수명이다. 
cust_df3$age
# 이 외에도 123살, 126살 등 예상으로는 23살 26살을 입력하는 과정에서 1을 앞에 붙여 발생한 오류로 추정해볼 수 있다.

# 개인 소득을 산출할 경우 보통 음수의 경우는 고려하지 않는다. 
hist(cust_df3$Income)
# -8700도 8700소득을 입력하는 과정에서 발생한 오타로 추정해볼 수 있다.

## 2. Tidy data
View(bankruptcy_df)
bankruptcy_df
Q1.
# 행의 경우 보통 관측치를 의미하고 열의 경우 그 관측치에 대한 변수가 위치한다.
# 이 경우 행에는 corpID를 통해 기업의 ID를 표시하고 그 기업의 각종 리스크를 설명하고자 하는 데이터프레임이다.
# 하지만 변수가 되어야할 리스크의 종류들이 열에 위치하지 않고 행에 분포해 있으므로 tidy한 데이터 셋으로 보기 어렵다.

Q2.
bankruptcy_df <- bankruptcy_df[, -1]
bankruptcy_df <-spread(bankruptcy_df, index, rating)
bankruptcy_df
save(bankruptcy_df, file = "bankruptcy_df.RData")

Q3. ## 여기를 가속화할 수 있는 방법은 없을까?
bankruptcy_df$Class

bankruptcy_df$Class <- str_replace(bankruptcy_df$Class, 'B', 'Bankruptcy')

bankruptcy_df$Class <- str_replace(bankruptcy_df, 'NB', 'Non-Bankruptcy')

str(bankruptcy_df)

bankruptcy_df$Competitiveness

bankruptcy_df$Competitiveness <- str_replace(bankruptcy_df$Competitiveness, 'A', 'Average')
bankruptcy_df$Competitiveness <- str_replace(bankruptcy_df$Competitiveness, 'P', 'Positive')
bankruptcy_df$Competitiveness <- str_replace(bankruptcy_df$Competitiveness, 'N', 'Negative')

bankruptcy_df$Credibility
bankruptcy_df$Credibility<- str_replace(bankruptcy_df$Credibility, 'A', 'Average')
bankruptcy_df$Credibility <- str_replace(bankruptcy_df$Credibility, 'P', 'Positive')
bankruptcy_df$Credibility <- str_replace(bankruptcy_df$Credibility, 'N', 'Negative')
bankruptcy_df$`Financial Flexibility`
#bankruptcy_df$Financial Flexibility
bankruptcy_df$`Financial Flexibility`<- str_replace(bankruptcy_df$`Financial Flexibility`, 'A', 'Average')
bankruptcy_df$`Financial Flexibility` <- str_replace(bankruptcy_df$`Financial Flexibility`, 'P', 'Positive')
bankruptcy_df$`Financial Flexibility` <- str_replace(bankruptcy_df$`Financial Flexibility`, 'N', 'Negative')

bankruptcy_df$`Industrial Risk`
bankruptcy_df$`Industrial Risk`<- str_replace(bankruptcy_df$`Industrial Risk`, 'A', 'Average')
bankruptcy_df$`Industrial Risk` <- str_replace(bankruptcy_df$`Industrial Risk`, 'P', 'Positive')
bankruptcy_df$`Industrial Risk` <- str_replace(bankruptcy_df$`Industrial Risk`, 'N', 'Negative')

bankruptcy_df$`Management Risk`
bankruptcy_df$`Management Risk`<- str_replace(bankruptcy_df$`Management Risk`, 'A', 'Average')
bankruptcy_df$`Management Risk` <- str_replace(bankruptcy_df$`Management Risk`, 'P', 'Positive')
bankruptcy_df$`Management Risk` <- str_replace(bankruptcy_df$`Management Risk`, 'N', 'Negative')

bankruptcy_df$`Operating Risk`
bankruptcy_df$`Operating Risk`<- str_replace(bankruptcy_df$`Operating Risk`, 'A', 'Average')
bankruptcy_df$`Operating Risk` <- str_replace(bankruptcy_df$`Operating Risk`, 'P', 'Positive')
bankruptcy_df$`Operating Risk` <- str_replace(bankruptcy_df$`Operating Risk`, 'N', 'Negative')

bankruptcy_df

