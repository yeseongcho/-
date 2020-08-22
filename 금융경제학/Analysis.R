finance <- read.csv("C:/Users/sec/Desktop/교과목들/금융경제학/피드백 이후 분석용.csv")
str(finance)
names(finance)[1] <- "delta_v"
names(finance)

View(finance)
# treasury_3year는 별다른 영향을 보이지 않음
treasury_3year <- lm(delta_trea3.t.~delta_trea3.t.1.+delta_Av, data=finance)
summary(treasury_3year)

### 1년 국채는 전기가 영향을 크게 미쳤지만 수익률이 주가변동성에 그다지 큰 영향을 받지는 않았다.
treasury_1year <- lm(delta_trea1.t. ~ delta_trea1.t.1.+delta_Av, data=finance)
summary(treasury_1year)

### 회사채는 결과가 전반적으로 비슷했다.
AAA <- lm(delta_AAA.t.~ delta_AAA.t.1.+delta_Av, data=finance)
summary(AAA)
names(finance)
summary(finance)
AAplus <- lm(deltaAAp.t. ~deltaAAp.t.1. +delta_Av, data=finance)
summary(AAplus)

AA <- lm(deltaAA.t. ~deltaAA.t.1. +delta_Av, data=finance)
summary(AA)

AAminus <- lm(deltaAAm.t.~ deltaAAm.t.1. +delta_Av, data=finance)
summary(AAminus)

Aplus <- lm(deltaAp.t. ~deltaAp.t.1.+delta_Av, data=finance)
summary(Aplus)

A <- lm(deltaA.t.~deltaA.t.1.+delta_Av, data=finance)
summary(A)

Aminus <- lm(deltaAm.t. ~deltaAm.t.1. +delta_Av, data=finance)
summary(Aminus)

mean(finance$delta_v)


