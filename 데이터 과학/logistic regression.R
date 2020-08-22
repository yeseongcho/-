Logistic regression

library(dplyr)
library(tidyr)
library(stringr)
library(caret)
library(ggplot2)
library(reshape2)
library(class)
library(kknn)
library(rpart)

load(url('https://github.com/hbchoi/SampleData/raw/master/NatalRiskData.rData'))

str(sdata)
 
train <- sdata[sdata$ORIGRANDGROUP <=5, ]
test <- sdata[sdata$ORIGRANDGROUP>5, ]

complications <- c("ULD_MECO", "ULD_PRECIP", "ULD_BREECH")
riskfactors <- c("URF_DIAB", "URF_CHYPER", "URF_PHYPER", "URF_ECLAM")
y <- "atRisk"
x <- c("PWGT", "UPREVIS", "CIG_REC", "GESTREC3", "DPLURAL", complications, riskfactors)

fmla <- paste(y, paste(x, collapse='+'), sep='~')

model <- glm(fmla, data=train, family = binomial(link='logit'))

train$pred <- predict(model, newdata=train, type='response')
test$pred <- predict(model, newdata=test, type='response')

test[20:40, c('pred', 'atRisk')]

aggregate(pred~atRisk, data = train, mean)
aggregate(pred~atRisk, data = test, mean)
 
ggplot(train, aes(x=pred, color=atRisk, linetype=atRisk)) + geom_density()

# 다음과 같이 table 구성하는 테크닉 참고!
ctab.test <- table(pred=test$pred>0.02, atRisk=test$atRisk)
ctab.test <- table(pred=test$pred>0.02, acutual=test$atRisk)
ctab.test

precision <- ctab.test[2,2]/sum(ctab.test[2,])
precision
recall <- ctab.test[2,2]/sum(ctab.test[,2])
recall
# 코드의 의미를 이해할 수 있겠니?
enrich <- precision/mean(as.numeric(test$atRisk))
enrich

coefficients(model)
