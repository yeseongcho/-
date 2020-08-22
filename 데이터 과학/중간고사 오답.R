iris
library(tidyr)
## 중간고사 오답노트
iris.wide

iriss <- iris
iriss$id <- 1:150

iriss <- gather(iriss, Char, value, 1:4)

iriss <- separate(iriss, Char, into = c("Part", "char"))
spread(iriss, char, value)


pums.sample
load("C:/Users/sec/Downloads/midterm2020.RData")
pums.sample
###############
SCHL
COW
merge를 써도 안되던데...
중간고사 7번 오답정리 해야한다.
네가 앞으로 데이터를 공부하고 알려면 이런 분석은 당연히 해야되는거야
빨리 공부해 오늘(시험친 날)은 멘탈관리하고
내일부터 미친듯이 하자
문해방만 하지말고
데이터과학 경히 여기지 말자
역전할 수 있다.
미친듯이 하자
화이팅

pums.sample
hist(pums.sample$SCHL, pums.sample$COW)
table(pums.sample$COW)


### 네가 어려워하는 이런 파트를 group_by를 잘 써먹어보자

library(dplyr)
group_by(pums.sample$SCHL) %>% summarise(pums.sample$COW, n())
?summarise
str(pums.sample)
pums.sample$SCHL <- as.factor(pums.sample$SCHL)
pums.sample$COW <- as.factor(pums.sample$COW)
aggregate(COW ~ SCHL, pums.sample, table)

pums.sample %>% group_by(SCHL, COW) %>% summarise(n()) -> result
result$`n()`
result$SCHL
result$COW
str(result)
result
?prop.table
result2 <- split(result, result$SCHL)
result2
names(result2)
#  "Associate's degree"
sum(result2[[1]]$`n()`)
sapply(result2[[1]]$`n()`, function(x){x/216})
sum(result2[[2]]$`n()`)
sapply(result2[[2]]$`n()`, function(x){x/486})
sum(result2[[3]]$`n()`)




result3 <- split(pums.sample, pums.sample$SCHL)
result3[[1]]
