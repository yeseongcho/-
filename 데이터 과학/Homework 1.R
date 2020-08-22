## 은행 데이터 프레임 불러오기
bank <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/bank_hw.csv", stringsAsFactors = T)
## 모든 string이 factor형으로 변환되었는지를 확인하는 절차
str(bank)

## Q1.

## 고객 수를 파악
nrow(bank)
# 정답 : 4521명

# 30살보다 어린 고객 데이터 프레임 반환
bank_under_thiry <- subset(bank, bank$age<30)
# 50살보다 많은 고객 데이터 프레임 반환
bank_over_fifty <- subset(bank, bank$age>50)
# 고객수 병합
result <- nrow(bank_under_thiry) + nrow(bank_over_fifty)
result
# 정답 : 1409명

## Q2. 
# 유로 원화 변환
bank$balance_kw <- bank$balance * 1200
bank$balance_kw


## Q3. 
# 정기 예금 상품에 가입한 고객 수
bank_yes <- subset(bank, bank$y == "yes")
nrow(bank_yes)

probability <- nrow(bank_yes)/nrow(bank)
probability
# 정답 : 521명, 0.11524

## Q4.
# 변환할 NA의 갯수
length(bank$pdays[which(bank$pdays == -1)])
# 정답 : 3705

## NA 변환
bank$pdays[which(bank$pdays == -1)] <- NA

## Q5.
# 직업군에 속한 고객 수 구하기
summary(bank$job)

## Q6.
# 가장 나이가 많은 케이스를 고려하기 위해.. 최고령의 경우 87세
summary(bank$age)
# 87세를 포함하기 위한 범위 구성
bank$age_group <- cut(bank$age, breaks = c(0, 20, 30, 40, 50, 60, 88), right = F)
bank$age_group
# 연령대에 따른 고객군 분포
summary(bank$age_group)

## 정답 : "30~39" 연령대 즉 30대가 가장 고객이 많았다.

# Q7.
# 연령대에 따른 고객군 벡터화
age_groups <- c(4, 478, 1808, 1203, 854, 174)
# 가입 했는지의 여부를 수치화하기 위해 yes값을 1로 변환
bank$y_int <- ifelse(bank$y == "yes", 1, 0)
bank$y_int
# 연령대 대비 가입자 수 구하기
aggregate(y_int~age_group, data = bank, FUN = sum)
# 위에서 구했던 고객 군 분포를 이용해 계산
age_group_yes <- c(2, 72, 185, 123, 84, 55)
results <- age_group_yes / age_groups
names(results) <- c("under 20s", "20s", "30s", "40s", "50s", "over 60s")
results
## 정답 : 연령대 대비 가입자의 비율이 가장 높은 곳은 20대 이하

# Q8.
aggregate(duration~contact, data = bank, FUN = mean)
# 정답 : 
# celluar : 267.1126
# telephone : 243.3555
# unknown : 261.7530

# Q9. 고객의 나이 오름차순으로 정렬
bank$age <- sort(bank$age)
head(bank)

# Q10.
save(bank, file = "Homework.RData")
load("Homework.RData")
