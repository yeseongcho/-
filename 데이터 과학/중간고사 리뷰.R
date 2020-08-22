#중간고사 리뷰!!
#중간은 망했으나 끝난 게 아니다!
#역전의 여지는 충분히 있다!! 프1을 생각하자...ㅂㄷㅂㄷ
load("C:/Users/sec/Downloads/midterm2020.RData")
pum <- pums.sample

Q2. 
sex_map <- c('Male', 'Female')
pum$SEX <- 
  factor(sex_map[pum$SEX], levels = sex_map)
head(pum$SEX)
# 이렇게 쉽게 바꿀 수 있다... ifelse도 써두 되구!

Q3. # factor 변환을 못했다...ㅠㅠㅠ 여기두 감점이 있을 듯!

marital_map <- c("Married", ....)

pum$MAR <- factor(marital_map[pum$MAR], levels = marital_map)

Q4. # COW를 고려 못함.. 아마 감점이 있을듯..

colSums(is.na(pum))
# 이렇게 간단하게... ㄷㄷ
(colSums(is.na(pum))[colSums(is.na(pum)) != 0]/ nrow(pum)) %>% round(3)

Q5. 

sum(!is.na(subset(pum, SEX == 'Male')[, 'FER']))
# 이런식이 가능!!
sum(is.na(subset(pum, SEX == 'Female' & AGEP >= 15 & AGEP <= 50)[, 'FER']))

Q6. (이상치 판별 문제) # 우선 나는 1개만 적었는데 크게 감점 요소는 없을 듯
summary(pum)
sum(pum$PINCP <0)
pum[pum$PINCP<0, ] # 조건 indexing
# 이렇게 세부 사항을 확인하면서...!!! 깊게 보는 것을 확인할 수 있다.
# 논리적 근거를 들어야 한다. 아 자영업이라 그럴 수도 있겠다!!
hist(pum$PINCP) 
# Max는 뭐지 이 인간은 왜이리 수익이 크노 이런 거는 아웃라이어??
# 그럴 수도 아닐 수도..
pum[which.max(pum$PINCP), ]
# 또한 가능성 있는 것! 
summary(pum$WKHP)
# 1시간??, 99시간?? 이러한 것으로 이상치를 찾아볼 수 있다. 실제 데이터 조사할 땐!

# 얘는 뭔데 일을 1시간 하냐.. 알바인가? 그런데 income은 높네.... 씹새끼
pum[which.min(pum$WKHP), ]

# 99시간은..대신 수익은 개높네..
pum[which.max(pum$WKHP), ]

Q7. # 이 문제가 너한테 주는 교훈

## 아는 만큼 보인다. 알려면 공부를 해야된다. 어떻게? 혼자서 공부를 해야한다.
prop.table(table(pums.sample$SCHL, pums.sample$COW))
prop.table(table(pums.sample$SCHL, pums.sample$COW))
# 혼자서 merge다 뭐다 생각이 갇히면 안된다!

# 이렇게만 구하면 되는 걸까??

# 교수님이 풀이는 어떠할까? 
# 우선 동일하게 접근을 하셨다.
x <- prop.table(table(pums.sample$COW, pums.sample$SCHL))
x
general.ratio <- prop.table(table(pum$COW))

plot(x[,1],xlab = 'COW') # no high school diploma

# 이렇게 대강의 시각화를 해보자

Q8.
# 한 방식이 맞는 듯..

Q9. (해석 문제) 
# 우선 plot 그래프 그린 방식은 맞음!
plot(pum$WKHP, log10(pum$PINCP)) # log를!!

# correlation을 구하는 거는 잘못되었나? 상관 없다!!
hist(pum$WKHP)
Q2-1. # 이문제가 너한테 주는 교훈 .. 아는 게 다가 아니다. 겸손해라
# 내 풀이 1번
iris.wide
iris
iriss <- iris
iriss
# 이렇게 id를 붙여주는 테크닉이 반드시 필요하다!! 이게 spread의 에러를 막아준다!!
# id 테크닉은 알았지만.... 겸손하지 못했다..!
iriss$id <- 1:150

iriss <- gather(iriss, Char, value, 1:4)

iriss <- separate(iriss, Char, into = c("Part", "char"))
iriss
iriss <- spread(iriss, char, value)
iriss

# 교수님 풀이
# 2번
x<-gather(iris, Measurement, Value, Sepal.Length:Petal.Width)
separate(x, Measurement, into = c('Part', 'Mesure'))

# 1번은??
# 교수님의 풀이와 내 풀이와 동일하다!
# id를 쓰는게 핵심이었엉!
