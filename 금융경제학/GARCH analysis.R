library(rugarch)
#install.packages("rugarch")
#install.packages("fGarch")
library(fGarch)
#install.packages("tseries")
library(tseries)
library(zoo)
library(e1071)
#install.packages("FinTS")
library(FinTS)

# 요녀석들 중에 알맞는 건 무얼까?
?ugarchspec()
?garch()
?garchFit()


# garch 모형을 만들기 어려우면 직접 선형회귀로 돌려볼까

treasury <- read.csv("C:/Users/sec/Desktop/testgarch.csv", stringsAsFactors = F)
View(treasury)
str(treasury)
names(treasury)[1] <- "date"

treasury$date <- as.Date(treasury$date)

treasury2 <- treasury[, 2]
plot.ts(treasury2)
# garch를 사용할 수 있는 조건 -- p-value를 통해 귀무가설 기각
ArchTest(treasury2)

garch(treasury2, grad = "numerical", trace = F)

x <- ugarchspec(variance.model = list(garchorder = c(1,1)), mean.model = list(armaOrder = c(0, 0)))
x_fit <- ugarchfit(x, data = treasury2)
x_fit

######################### 직접 linear regression을 수행해본다
treasury_3year <- read.csv("C:/Users/sec/Desktop/교과목들/금융경제학/국고채 3년물 변화량.csv")
str(treasury_3year)

# linear regression으로 취해도 괜찮은걸까...?
model_fit <- lm(delta_yt~delta_yt.1 + delta_v, data = treasury_3year)
summary(model_fit)
var(treasury_3year$delta_v)
mean(treasury_3year$delta_v)
nrow(credit_spread)
treasury_1year <- read.csv("C:/Users/sec/Desktop/교과목들/금융경제학/국고채 1년물 변화량.csv")
str(treasury_1year)
model_fit2 <- lm(delta_yt~delta_yt.1 + delta_v, data = treasury_1year)
summary(model_fit2)
credit_spread <- read.csv("C:/Users/sec/Desktop/교과목들/금융경제학/신용 스프레드 수정본.csv")

str(credit_spread)
View(credit_spread)
names(credit_spread)[1] <- "AAAt"
credit_fit <- lm(deltaAAA.t. ~deltaAAA.t.1.+delta_v, data = credit_spread)
summary(credit_fit)


## 이러한 접근이 맞는가?? 의문이 든다..