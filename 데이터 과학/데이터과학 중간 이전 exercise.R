### Exercise1


#Q1.
mtcars$kpl <- (mtcars$mpg)*1.609344/3.785412 
mtcars$kpl
mtcars$kpl
mtcars[,c('mpg', 'kpl')]
#Q2
mtcars$mpg <- sort(mtcars$mpg)
head(mtcars, 3)
tail(mtcars, 3)
## answer : 연비가 가장 좋은 것 : Merc 280c, Lincoln Continental, Fial 128, 연비가 가장 나쁜것 : Merc 230, Lotus Europa, Maserati Bora
# 하지만 문제는 3개만 뽑으라는 것에 주목!!


#Q3
## ifelse 이후 부분부터 체화 안된 것들이 너무 많다. 이들을 체화할 시간이 필요하다!!
aggregate(mpg~cyl, data=mtcars, FUN = mean )
library(dplyr)
mtcars %>% group_by('cyl' = cyl) %>% summarise('means' = mean(mpg))

#Q4
Genesis <- c(19.99324, 6, 120, 95, 3.89, 5.12, 23.4, 1,0, 4, 2) # 새로만든 fuel_efficiency, mt_grp, kpl은 추후에 또 실행해 주어야 우선 NA로 저장
mtcars <- rbind(mtcars, 'Genesis' = Genesis) # 이렇게 naming을 해준다!!
mtcars ## rbind에서 바로 naming을 할 수 있음을 확인!!

rm()## 이 명령어는 지워주는 기능도 있다!!

# 이 다음 새로 만들어진 행을 새로 만든 열의 공식을 똑같이 적용해준다.
mtcars$fuel_efficiency<-cut(mtcars$mpg, breaks = quantile(mtcars$mpg, c(0, 0.25, 0.5, 0.75, 1), include.lowest = T),  labels = c('So Bad', 'Bad', 'Soso', 'Good'))
mtcars$mt_grp <- cut(mtcars$wt, breaks = c(0, 4, 8, 12), include.lowest = T, labels = c('bad', 'good', 'So good'))
# 행 이름 변경
rownames(mtcars)[33] <- 'Genesis' ## 이런 방식두!!
dimnames(mtcars)[[1]][33] <- "Genesis" ## 이런 방식두!!
mtcars

#Q5
vectors <- (mtcars$hp > 100)
vectors
aggregate(mpg~vectors, data=mtcars, FUN = mean)
tapply(mtcars$mpg, mtcars$hp>100, mean)
quantile(mtcars$wt)
#Q6
mtcars$mpg <- sort(mtcars$mpg)
mtcars$hp <- sort(mtcars$hp, decreasing = T)
mtcars

#Q7 --- 이 부분 교수님이랑 나랑 구한 방법이 달랐다 참고하자!!
mtcars$kg <- mtcars$wt / 0.453592
mtcars$wt

mtcars$wt <- sort(mtcars$wt)
head(mtcars) # mtcars$wt <= 4.850174
tail(mtcars) # mtcars$wt >= 8.476781

low_mtcars <- split(mtcars, mtcars$wt <= 4.850174)[['TRUE']]
low_mtcars
high_mtcars <- split(mtcars, mtcars$wt >= 8.476781)[['TRUE']]
high_mtcars

#Q8
mean(low_mtcars$mpg)
mean(low_mtcars$hp)
mean(high_mtcars$mpg)
mean(high_mtcars$hp)

mtcars$price <- seq(252, 350,3)
mtcars$price
mtcars
#Q9
write.csv(mtcars, "mtcars_test.csv")
#Q10
save(mtcars, file = "mtcars_test.RData")

my_vector <- c(6, 12, 4, 89, 23, 35)
-my_vector


### Excercise 2
load("C:/Users/sec/Desktop/교과목들/데이터 과학/weather.RData")
head(weather)
tail(weather)
View(weather)
str(weather)
## 1번. tidy하게 하세요
library(tidyr)
library(stringr)
weather1 <- gather(weather, day, values, 5:35) # gather(weather, day, value, X1:X35) 이렇게 바로 col이름을 입력해도 가능!!
# 교수님의 경우 gather(weather ,day, values, X1:X35) -- 이렇게 바로 colnames로 적용!!!
weather1$day <- str_replace(weather1$day, "X", "")
View(weather1)
weather2 <- unite(weather1, date, year, month, day, sep = "-")
#weather2$date <- as.Date(weather2$date)
View(weather2)
View(weather3)
head(weather3)
weather3 <- weather2[ , -1] ## spread에 있어서 중요!!
str(weather3)
weather3
## as.Date를 안하니까 spread가 된다????
f_weather <- spread(weather3, measure, values)
View(f_weather)

### 2번. 불필요한 column제거
colnames(f_weather)
# X제거한게 불필요한 column 아닐까??

## 3번은 위에서 수행
library(dplyr)
f_weather$date <- as.Date(f_weather$date)
f_weather$date <- ymd(f_weather$date)
## sort가 못한 일을 order는 하네... 이래서 많이 쓰나 보다!!!
f_weather$date <- f_weather[order(f_weather$date), ]
# 심심하니까 plot을 그려볼까 -- 줄형 식으로 표현 가능
plot(x = f_weather$date, y =f_weather$Mean.TemperatureF, type = 'l')
### 여기 안되는 이유...
drop_na(f_weather, 'Mean.TemperatureF')
fill(f_weather, 'Mean.TemperatureF')
fill(f_weather, f_weather$Mean.TemperatureF)
replace_na(f_weather, list(Mean.TemperatureF = 50)) ### 얘네 왜 안되지??
f_weather$Mean.TemperatureF
str(f_weather)
View(f_weather)
## 4번

f_weather$PrecipitationIn <- str_replace(f_weather$PrecipitationIn, "T", "0")
f_weather$PrecipitationIn <- as.numeric(f_weather$PrecipitationIn)
## 교수님 방법
# f_weather$PrecipitationIn <- ifelse(f_weather$PrecipitationIn == 'T', 0, f_weather$PrecipitationIn)


## 5번 --- 여기 sapply()로 한다?? 강의 참고!!
# 1) 노가다
f_weather$Events <- as.factor(f_weather$Events)
f_weather$Events
table(f_weather$Events) ## 효율적으로 확인 가능!!
### str_replace가 안될 수도 있어
f_weather$Events <- str_replace(f_weather$Events, "", "Clear")
### 내가 사랑하는 which를 쓰자!!
f_weather$Events[which(f_weather$Events == "")] <- "Clear"

f_weather$Events <- as.character(f_weather$Events)
f_weather$CloudCover <- as.numeric(f_weather$CloudCover)
f_weather$Max.Dew.PointF <- as.numeric(f_weather$Max.Dew.PointF)
f_weather$Max.Gust.SpeedMPH <- as.numeric(f_weather$Max.Gust.SpeedMPH)
f_weather$Max.Humidity <- as.numeric(f_weather$Max.Humidity)
f_weather$Max.Sea.Level.PressureIn <- as.numeric(f_weather$Max.Sea.Level.PressureIn)
f_weather$Max.TemperatureF <- as.numeric(f_weather$Max.TemperatureF)
f_weather$Max.VisibilityMiles <- as.numeric(f_weather$Max.VisibilityMiles)  
f_weather$Max.Wind.SpeedMPH <- as.numeric(f_weather$Max.Wind.SpeedMPH)
f_weather$Mean.Humidity <- as.numeric(f_weather$Mean.Humidity)
f_weather$Mean.Sea.Level.PressureIn <- as.numeric(f_weather$Mean.Sea.Level.PressureIn)
f_weather$Mean.TemperatureF <- as.numeric(f_weather$Mean.TemperatureF)
f_weather$Mean.VisibilityMiles <- as.numeric(f_weather$Mean.VisibilityMiles)
f_weather$Mean.Wind.SpeedMPH <- as.numeric(f_weather$Mean.Wind.SpeedMPH)
f_weather$MeanDew.PointF <- as.numeric(f_weather$MeanDew.PointF)
f_weather$Min.DewpointF <- as.numeric(f_weather$Min.DewpointF)
f_weather$Min.Humidity <- as.numeric(f_weather$Min.Humidity)
f_weather$Min.Sea.Level.PressureIn <- as.numeric(f_weather$Min.Sea.Level.PressureIn)
f_weather$Min.TemperatureF <- as.numeric(f_weather$Min.TemperatureF)
f_weather$Min.VisibilityMiles <- as.numeric(f_weather$Min.VisibilityMiles)
f_weather$WindDirDegrees <- as.numeric(f_weather$WindDirDegrees)
f_weather[, 2]
f_weather[, c(4:23)] <- as.numeric(f_weather[, 2])
# 2) for문 사용하지마!!!
for(i in (4:23)) {
  f_weather[, i] <- as.numeric(f_weather[, i])
}
str(f_weather)
# 교수님의 sapply()
## 우선 factor랑 date빼고 나머지 바꿔야지!
# str(f_weather[, c(-1, -3)]) -- 바꾸어야할 모든 놈들 파악!!
# sapply(f_weather[, c(-1, -3)], as.numeric) --- 이렇게 하는 거야!!!! 
## 이래서 apply() 이후의 함수들이 체화가 되어야 한다!! 주일에 조지자!
sapply(f_weather[, c(-1, -3)], as.numeric)
## 6번
colSums(is.na(f_weather))
## 테크닉!!!
f_weather[is.na(f_weather$date), ] ## NA가 있는 행들!!
drop_na(f_weather) ## 너무 극단적인 케이스!!
f_weather
View(f_weather[!complete.cases(f_weather), ]) ## 어떻게 쓰냐에 따라 다르다!!

## 7번 outlier 확인 및 제거
boxplot(f_weather$Max.Humidity)
f_weather$Max.Humidity[which(f_weather$Max.Humidity > 100)]
f_weather$Max.Humidity
f_weather$Max.Humidity 
f_weather$Max.Humidity[231] <- 100
boxplot(f_weather$Mean.VisibilityMiles) ## 평균 시야 거리가 -일수 있나??

## 8번
f_weather$Mean.VisibilityMiles[which(f_weather$Mean.VisibilityMiles == -1)] <- NA
f_weather$Mean.VisibilityMiles
## 9 번
## str_replace가 이게 안되더라 ""일때
f_weather$Events <- str_replace(f_weather$Events, " " , "None")
## 내가 사랑하는 which를 사용하자!
f_weather$Events[which(f_weather$Events == "")] <- "None" ## 야매
f_weather$Events
View(f_weather)
## 10번
colnames(f_weather) <- tolower(colnames(f_weather))
colnames(f_weather)


### Excercise 3

car_df <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/cars04.csv")
str(car_df)
View(car_df)
load("C:/Users/sec/Desktop/교과목들/데이터 과학/anscombe.RData")

## 3번 -- factor가 나을까 char가 나을까??
# factor가 아니라 각각이 unique한 값을 갖기에
car_df$name <- as.character(car_df$name)
class(car_df$name)

## 4번
mean(car_df$msrp)
mean(car_df$dealer_cost)
## 조금 성의를 기울이자
car_df$price_dff <- car_df$msrp - car_df$dealer_cost
summary(car_df$price_dff)

## 기억하자! which.max!! 그냥 max()는 이런 용도가 아닌듯!
car_df[which.max(car_df$city_mpg), ]


car_df[which(car_df$city_mpg == 60), ]
car_df$city_mpg[order(car_df$city_mpg)]
car_df$hwy_mpg[order(car_df$hwy_mpg)]

# 5번살짝 노가다
colSums(car_df[, 2:6])
## 교수님 모범답안, sapply(car_df[, 2:6], sum)
dim(car_df[which((car_df$sports_car == F) & (car_df$suv == F) & (car_df$wagon == F) & (car_df$minivan== F) & (car_df$pickup == F)), ])
## omitted된거 잊지마라!!!! --- 이런거 실수하는게 씹손해 .. 수는 실제로 나는 195+50 = 245정도 나온다
## row나 col갯수 count할 때 사용하는 dim 테크닉도 잊지 말고!!

## 교수님 모범 답안 
apply(car_df[,2:6], 1, sum) ## 행의 합!!
sum(apply(car_df[, 2:6], 1, sum)==0)


# 7번
SUV <- car_df[which(car_df$suv ==T), ]
MINIVAN <- car_df[which(car_df$minivan == T), ]
mean(SUV$weight)
mean(MINIVAN$weight)
## 교수님 모범답안
mean(car_df[car_df$suv, 'weight'])
mean(car_df[car_df$minivan, 'weight'])

# 저런 함수들도 사용 가능!! 
tapply(car_df$weight, car_df$suv, mean)
aggregate(weight~suv == TRUE, car_df, mean)
### 음... 별로 비효율적인 코드인가??

## 질문!!! -- 한번만 쓰고 7번문제를 쓸 수 있을까? 생각 생각 생각 생각 신한카드
tapply(car_df$weight, car_df[, c(3, 5)], mean)
aggregate(weight~suv+minivan, car_df, mean)

## gathering을 통해 간단히 만들어 풀 수도 있다.
car_mini <- car_df[, c(1:6, 16)]
car_tidy <- gather(car_mini, car_type, value, sports_car:pickup)
car_tidy <- car_tidy[car_tidy$value == TRUE, ]
car_tidy <- car_tidy[, -4]
#car_tidy <- car_tidy[, 1:4]
View(car_tidy)
car_tidy
aggregate(weight~car_type, car_tidy, mean)


# 8번
car_df$avg_mpg <- (car_df$city_mpg + car_df$hwy_mpg)/2
car_df$avg_mpg
# 9번
na.omit(car_df$avg_mpg)
quantile(na.omit(car_df$avg_mpg), c(0, 0.2, 0.8))
car_df$eco_grade <- cut(car_df$avg_mpg, breaks = c(0, 11.0, 20.0, 26.5), include.lowest = T, labels = c("bad", "normal", "good"))
car_df$eco_grade
quantile(car_df$avg_mpg)


### 9번의 경우 풀이를 봐보자!!
## na.rm = T 이렇게 na항목을 자동으로 없애주는 기능이 있음을 알자!! 시간을 절약하자!
cuts <- quantile(car_df$avg_mpg, probs = c(0, 0.2, 0.8, 1), na.rm = T)
car_df$eco_grade <- cut(~)


# 10번
tapply(car_df$horsepwr, car_df$all_wheel, mean)
tapply(car_df$horsepwr, car_df$rear_wheel, mean)

### 요기는?
anscombe
for(i in (1:4)){
  print(mean(anscombe[, i]))
  print(mean(anscombe[, i+4]))
  print(var(anscombe[, i]))
  print(var(anscombe[, i+4]))
  print("next")
}
mean(anscombe$x1)
mean(anscombe$y1)
var(anscombe$x1)
var(anscombe$y1)
mean(anscombe$x2)
mean(anscombe$y2)
var(anscombe$x2)
var(anscombe$y2)
mean(anscombe$x3)
mean(anscombe$y3)
var(anscombe$x3)
var(anscombe$y3)
mean(anscombe$x4)
mean(anscombe$y4)
var(anscombe$x4)
var(anscombe$y4)
### 이런 걸 이렇게 길게 쓰지 말고 sapply()를 애용하자!!
sapply(anscombe, mean)
sapply(anscombe, var)

## 데이터의 분산 정도를 값만 가지고는 알 수 없다. 시각화를 해보아야 한다.
plot(x = anscombe$x1, y = anscombe$y1)
plot(x = anscombe$x2, y = anscombe$y2)
plot(x = anscombe$x3, y = anscombe$y3)
plot(x = anscombe$x4, y = anscombe$y4)

## 재미로 해본 부분
anscombe_x <- anscombe[, 1:4]
anscombe_x
anscombe_x <- gather(anscombe_x, x, x_values, 1:4)
anscombe_y <- anscombe[, 5:8]
anscombe_y
anscombe_y <- gather(anscombe_y, y, y_values, 1:4)
library(ggplot2)
library(tidyr)
anscombe_all <- merge(anscombe_x, anscombe_y) ## 이렇게 하면 ㄴㄴ
anscombe_all <- cbind(anscombe_x, anscombe_y) ## cbind많이 애용하자
anscombe_all
ggplot(data = anscombe_all, aes(x = anscombe_all[which(anscombe_all$x == x1), x_values], y= anscombe_all[which(anscombe_all$y==y1), y_values]))+ geom_point()
## 잊어!


library(dplyr)
library(tidyr)

iris
str(iris)
View(iris)

iris_g <- iris %>% gather(charcter, value, 1:4) 
iris_g
iris_s <- iris_g %>% spread(charcter, value)
iris_g_s <- iris_g[, 2:3]
iris_g_s <- iris_g_s %>% spread(charcter, value)
iris_g_s

iris_g_s$id <- 1:150
iris_g_s$Species <- iris$Species
iris_g_s
testsdf <- data.frame("A" = c(1, 2, 3, 4), "B" = c(2, 23, 4, NA), "C" = c(3, NA, NA, 6))
testsdf
testsdf %>% fill(C) -> testsdf

testsdf %>% replace_na(list(C = 8))

test_iris <- iris
test_iris
test_iris$Sepal.Length
test_iris$Petal.Length
test_iris$average.Length <- (test_iris$Sepal.Length + test_iris$Petal.Length)/2
test_iris

iris %>% mutate(average.Width = (iris$Sepal.Width + iris$Petal.Width)/2) 
iris

filter(iris, Species == "virginica")
