# 데이터 과학 메모 노트!!

# python은 딥러닝 할때 좋아요

# Variable -- 강의 참조 - 변수명 설정 등 내용 있으니까


# 변수의 종류로는 무엇이 있을까?

# 1. Scala 타입 - 값을 하나만 저장하는 변수!! (Atomic data type!)

# 실수(double), 정수(integer), 논리값(logical), 문자(character) -- typeof()라는 함수로 확인 가능

# NA 타입(Missing Value), is.na()을 통해 NA여부 확인

# Inf -- 무한대값

typeof(Inf)

typeof(-Inf)

typeof(NA)

# 2. Vector 타입! 
# A vector is a sequence of data elements of the same basic type
# All members should be of same data type

numeric_vector <- c(1, 10, 49)

# 추가하는 방법
new_vector <- c(numeric_vector, 50)

new_vector

# vector의 indexing!
vector1 <- c(1, 2, 3)
vector1[2]
vector1[c(1,2)]

# 중복도 가능
vector1[c(1, 1, 2)]

# -인덱싱
vector1[-1]

# 크기가 다른 경우는 연산에 제한
vector2 <- c(1, 2, 3, 4)
vector1 + vector2

# vector의 요소에 이름 부여도 가능

some_vector <- c("John Doe", "Professor")
names(some_vector) <- c("Name", "Profession")
some_vector

some_vector["Name"]
some_vector[1]
# 이건 안된다. 이름이 아니잖아
some_vector["John Doe"]

# 처음 만들때부터 부여도 가능

weather_vector <- c("Mon" = "Sunny", "Tues" = "Rainy")
weather_vector
weather_vector['Mon']

# 이름들을 보고 싶을 때
names(weather_vector)

# Short-cut to make numeric vector
a_vector <- seq(1, 10, 2) # 1 부터 10까지 2 간격으로
a_vector
b_vector <- rep(1:3, 3) # 1~3까지 3번 반복
b_vector
c_vector <- rep(1:3, each = 3) # 각각을 3번 반복
c_vector
# 결합도 가능
c(b_vector, c_vector)
# 타입이 다른 두 벡터를 컴바인할 떄
differ_vector1 <- c(1, 2, 3)
differ_vector2 <- c('1', '2', '3')
merge <- c(differ_vector1, differ_vector2)
merge # differ_vector1이 char형이 됬네...

possible <- c(1, 2, 3, '1')
possible # 이 경우도 다 char형이 됬네

isit <- c(T, 1, 2, 'char')
isit # 다 char형으로 변환시킴을 알 수 있다.

# 집합의 개념

A <- c(1, 5, 2, 7, 8, 2, 3)
B <- seq(1, 10, 3)
intersect(A, B) #교집합
union(A, B) # 합집합
setdiff(A, B) # 차집합
unique(A) # 고유값 집합
# 이러한 계산들도 가능
sum(A)
mean(A)
var(A)
sd(A)
median(A)

A + 10
A > 4
sum(A>4) # 4보다 큰 것들의 갯수를 따짐, True를 1로 따지는 거죠, 이거 조심!!

A - B # 갯수(길이)가 맞지 않으면 에러

A == B # 이것도 마찬가지

#A B를 수정하고 다시 보자
A <- c(1, 5, 2, 7, 8)
B <- seq(1, 10, 2)

A -B

A == B

sum(A == B) # 같은 건 총 2개

# 이것들은 유용한 장치이다. 데이터의 갯수가 10만개라 가정해봐...

sample_vector <- c(1, 4, NA, 2, 1, NA, 4, NA)
sample_vector[c(T, T, F, T, F, T, F ,T)]
# logical을 이용한 인덱싱도 가능하다
sample_vector[c(-1, -3, -5)] # 얘네만 빼고

is.na(sample_vector)
!is.na(sample_vector)

# NA만 뽑는 법
sample_vector[is.na(sample_vector)] 

# NA값이 아닌 녀석들만 뽑는 방법
sample_vector[!is.na(sample_vector)]
# 이 논리에 대해 궁금한 게 많다!!

sample_vector['4'] # 4를 뽑고 싶다고 다음은 안된다.

# vector에서 인덱싱에 True가 들어가는 거는 전부 산출한다. 반면 False는 산출하지 않는다

sample_vector[T]

sample_vector[F]

# is.na()가 참인 경우는 True가 되므로 해당 경우의 indexing이 적용된 녀석들을 뽑은 것, 즉 NA값만 뽑게 된 것이다.


# vector는 기본적으로 1차원적인 데이터들의 나열

# Matrix (행, 열) 

# matrix('벡터') 형태의 파라미터가 주어진다.
matrix(1:9, byrow = TRUE, nrow = 3)
# byrow -- 행별로 순서대로 기입하라, 방향을 의미한다고 보면 되!
matrix(1:9, byrow = FALSE, nrow = 3)

matrix(1:9, byrow = TRUE, nrow = 9)

my_vec <- c(1, 2, 3, 4, 5, 10, 9, 8, 7, 6)

matrix(my_vec, nrow = 5)
matrix(my_vec, byrow = TRUE, nrow = 2)
 
# bycolumn으로 자동으로
my_mat <- matrix(my_vec, nrow = 2)


# element 하나하나의 naming을 하지 않고(벡터), 행렬의 naming을 할 수 있다.
rownames(my_mat) <- c("one", "two")
colnames(my_mat) <- c("1st", "2nd", "3rd", "4th", "5th")
my_mat

new_hope <- c(460, 314)
empire_strikes <- c(290, 248)
return_jedi <- c(309, 165)

star_wars <- matrix(c(new_hope, empire_strikes, return_jedi), nrow = 3, byrow = T)
star_wars

region <- c("US", "non-US")
titles <- c("A new hope", "Empire", "Return")
colnames(star_wars) <- region
rownames(star_wars) <- titles
star_wars

# 행, 렬 값들의 합을 추산해서 나타낼 수도 있다!!
rowSums(star_wars)
colSums(star_wars)

# 열 추가!! , cbind 활용해서 -- column bind (벡터를 열로 붙여주는 역할)
worldwide <- rowSums(star_wars)
star_wars_worldwide <- cbind(star_wars, worldwide) # cbind(기존 매트릭스, 새로 추가할 벡터?)
star_wars_worldwide

# 행 추가도 rbind를 이용해 가능하다. 하나의 새로운 매트릭스를 추가해보자
box_office <- c(474, 552, 310, 380, 338, 468)
# dimnames를 이용해 한번에 추가 가능!
star_wars2 <- matrix(box_office, nrow = 3, byrow = T, dimnames = list(c("Phantom", "Attack", "Revenge"), c("US", "non-US")))
star_wars2
star_wars
all_star_wars <- rbind(star_wars, star_wars2)
all_star_wars

# vector단위 추가도 해보자
testing <- c(122, 133)
star_wars_testing <- rbind(star_wars, testing)
star_wars_testing
# 추가가 됨을 알 수가 있다!!


#matrix에서의 indexing은 어떻게??
# matrix[행,열]

all_star_wars

# 예시들을 봐보자
all_star_wars[1:3, 'non-US']
all_star_wars['Empire', 'US']
all_star_wars[, 'US']
all_star_wars['Empire', ]
all_star_wars[c(1, 2, 3), ]
all_star_wars[, c(1, 2)]

A.mat <- matrix(1:9, byrow = T, nrow = 3)
B.mat <- matrix(rep(1:3, each = 3), byrow = T, nrow = 3)
C.mat <- matrix(rep(1:3,2), byrow = F, ncol = 2)
A.mat
B.mat
C.mat

#행렬의 곱셈 --- %any% 연산자는 lubridate에 정리해놓은 자료를 꼭 참고하자!!
A.mat %*% C.mat

# Factor 형 변수 
# factor는 카테고리형 변수임을 인지, 제한된 값만을 갖는다.
# ex) 혈액형은 A, B, AB, O의 범주만 갖는다.
# 성별의 경우를 예로 들어보자
sex_vector <- c("Male", "Female", "Female", "Male", "Male") # 이 경우는 char형

# factor화
factor_sex_vector <- factor(sex_vector)

print(factor_sex_vector) # Levels가 2개로 생성된다

# 우리가 기존에 알던 방법
factoring <- as.factor(sex_vector)
str(factoring)

# factor형을 쓰면 좋지 않는 경우 -- 제한되지 않는 경우
# ex) 사람 이름

# 확인 방법
typeof(factor_sex_vector) # 얘는 왜 integer가 나오지?? level이 정수값을 가져서 그런가본데..
str(factor_sex_vector)   # structure의 약자
levels(factor_sex_vector)

# level를 바꿀 수도 있다.
# 예를 들어보자

# sex_vector의 경우 'Female', 'Male'을 쓰는데 간략하게 F, M을 써보자
levels(factor_sex_vector) <- c('F', 'M')
factor_sex_vector

# 특정한 변수의 요약 정보를 보여주는 함수 summary()
summary(factor_sex_vector)
summary(sex_vector)
# 데이터의 형태에 따라 나타나는 요약 정보가 다름을 인지

## (중요!!) factor형도 관계 연산 처리가 가능하다!
# example
test_vector <- c("low", "mid", "high")
operation_vector <- factor(test_vector, ordered = T, levels = c('low', 'mid', 'high'))
operation_vector[2] > operation_vector[1]
# factor()에서 ordered라는인자가 있음을 주의하라
# 결과는 True가 나오게 된다.



# data.frame!! -- 만든 교육자료 참고 in dplyr
# table형태 

# ex) mtcars
head(mtcars)
head(mtcars, 10)

# ex) 많은 학생의 정보를 담길때, 이름, 학번, 나이, 전공 등...

# 매트릭스랑 차이가 매트릭스는 똑같은 데이터 타입만 가질 수 있는 반면 
# 데이터 프레임은 다양한 형태의 데이터 타입을 다 취할 수 있음에 그 힘이 있다.

# 한 행은 하나의 observation!을 보통 의미, 그래서 nrow를 데이터 갯수 취급하잖아

# column은 보통 feature를 보통 의미!! 변수라고도 쓰인다!

# str() -- 데이터가 뭔가, 구조가 어떻게 되어 있는가 파악하기 위한 함수
# str이 보여주는 것들
# The total number of observation
# The total number of variable
# A full list of the variable names
# The data type of each variable
# The first few observation

str(mtcars) # observa(행), varia(열) 이렇게 보면 더 쉽다!

one <- c('one', 'two', 'three')
two <- c(T, T, F)
three <- c(1, 2, 3)
four <- data.frame(one, two, three)
four
rownames(four) <- c('I', 'II', 'III')
four # 전반적으로 매트릭스랑 네이밍, 인덱싱 방법이 유사함을 확인할 수 있다!

# data.frame( A = c(..), B = c(..)..) 이런식으로 한번의 naming도 가능하다!

# data.frame의 indexing 방법, matrix와 유사!
four[1:2, 'three']
four[, 'three']

four$one # '$' 해당 변수 지정!! four라는 데이터 프레임의 one이라는 변수, 데이터프레임의 중요 성질 중 하나임을 인지!!
four$three
four$two

# four$two 즉, T, F변수인데 True인 것 중에 three 녀석들의 내용
four[four$two, 'three']

four[four$three > 2, 'two']

dim(mtcars) # 행과 열의 크기를 보여줌 dimension

# indexing 혼동하면 안된다!!
mtcars$mpg
mtcars[,'mpg']
mtcars['mpg']
mtcars$mpg > 20
mtcars['mpg'] > 20

mtcars[mtcars$mpg>20, ]
mtcars[mtcars$mpg>20, 'cyl']

mtcars$cyl == 4
mtcars[mtcars$cyl==4, ]

# 실린더가 4개 있는 차의 연비의 평균은?
mean(mtcars[mtcars$cyl == 4, 'mpg'])


# List형 데이터
# vector, matrix, data.frame 다 데이터형의 제한이 있다. 데이터 프레임의 경우 한 column에는 하나의 타입만 저장 가능
# List는 다 커버 가능, 이게 list가 갖는 굉장한 큰 장점이다
# These objects can be matrices, vectors, data frames, even other lists, etc

my_vector <- 1:10
my_matrix <- matrix(1:9, ncol = 3)
my_df <- mtcars[1:10, ]
my_vector 
my_matrix
my_df
my_list <- list(my_vector, my_matrix, my_df)
my_list

# 이름 부여도 가능
my_list <- list(name1 = my_vector, name2 = my_matrix, name3 = my_df)
my_list
# 이 방법도
my_list <- list(my_vector, my_matrix, my_df)
names(my_list) <- c('name1', 'name2', 'name3')
my_list

# list는 [[]] 이렇게 쓴다
my_list[[1]]
my_list[['name2']]
my_list$name3

# list에 요소 추가
my_list$new_vector <- c(1, 3, 5, 6, 7)
my_list[[4]]
names(my_list) <- c('name1', 'name2', 'name3', 'name4')
my_list
# list에 list 추가!! ------> 이 경우에는 어떤 식으로 추가되었나를 보자!!
new_list <- list(1, 2)
my_list$new_list <- new_list
names(my_list) <- c('name1', 'name2', 'name3', 'name4', 'name5')
my_list


##### list항목을 다음과 같이 다시 코드를 진행해보자

my_list <- list(my_vector, my_matrix, my_df)
my_list$new_vector <- c(1, 3, 5, 6, 7)
my_list$new_list <- list(1, 2)
names(my_list) <- c('name1', 'name2', 'name3', 'name4', 'name5')
my_list

# C의 2D Array의 개념을 생각하면 쉽다!
my_list[[5]] # list indexing
my_list[[5]][1] # list의 첫번째 요소 indexing
my_list[[1]][1] # vector의 첫번쨰 요소 indexing
my_list[[2]][1,] # matrix의 1번째 행
my_list[[3]][, 'mpg'] # data.frame의 mpg 항목들

# 데이터 프레임과 마찬가지로 '$' 사용 가능!
my_list$name3$mpg # 이렇게도 indexing이 가능!!
my_list$name2[,2]


########################## (여기서부터는 조금씩 복습을 해야한다!!)

## If, Else, For!!

# 조건문과 반복문이 R에도 존재한다!!

# But, 조건문 반목문을 사용하지 않아도 된다
# , 사용하지 않는 것이 오히려 좋다
# , 대신에 vectorized operation을 사용한다! 이게 더 좋으니까!!

medium <- "LinkedIn"
num_views <- 14

# 이거 실행할 때 if 안에 문장에 커서를 놓고 실행하면 nono, if에 놓고 실행해야!
if(medium == "LinkedIn"){ # 요건 True로 간주하겠지!
  print("Showing LinkedIn information")
}

if(num_views > 15){ # 요건 False겠지!
  print("You're popular!")
}

# 이런 경우도 실행 가능!!
if(num_views > 15){
  print("You're popular!")
}else {
  print("Try to be more visible!")
}

# for loop의 형태는 다음과 같다
# for(var in seq){
# var는 벡터형임을 인지!!
}
# 
cities <- c("New York", "Paris", "London", "Tokyo", "Rio de Janeiro", "Seoul")
# 파이선과 유사
for(city in cities){
  print(city)
}
# 작동방법 
# 처음에 city <- "New York"
# 두 번째에 city <- "Paris"
# 이런식으로 할당한다!

# Vectorized Operation!! 을 잠깐 봐보자

my_vectors <- c(1, 2, 3, 4, 5)
result_vector <- rep(0, 5)
result_vector

# indexing을 이용한 방법!!
for(i in 1:5){
  result_vector[i] <- my_vectors[i] + 3
}
result_vector


# 이렇게 해도 동일한 결과가 나옴을 알 수 있다! 하지만 의미가 없다!
for(i in my_vectors){
  result_vector <- my_vectors + 3
}
result_vector
# 하지만 그냥 이러면 된다. 다 필요 없어
result_vector2 <- my_vectors + 3
result_vector2

numbers_vector <- c(1, 3, 4, 2, 6, 8, 7, 5)
numbers_even_odd <- c("odd", "odd", "even", "even", "even", "even", "odd", "odd")

# How could you numbers_even_odd vector from numbers_vector??

# 이럴 때 사용하는 것이 Vectorized Operation -- 이것이 Easier! and Much more Efficient!!

# ifelse(조건문, 참일 경우 결과, 거짓일 경우 결과)
numbers_even_odd <- ifelse(numbers_vector %%2 == 0, "even", "odd")
numbers_even_odd

# table -- 뭐가 몇개 있다라는 갯수를 세어주는 함수
table(numbers_even_odd)
table(numbers_vector)
test_mt <- matrix(1:9, byrow = T, nrow= 3)
table(test_mt)
# mtcars에 "Fuel_efficiency"라는 항을 추가할 수 있다!

# 요렇게 구성
avg_mpg <- mean(mtcars$mpg)
new_var <- ifelse(mtcars$mpg >= avg_mpg, 'good', 'bad') 
# 요렇게 추가
mtcars$fuel_efficiency <- new_var
# 확인
head(mtcars)

## Function

# User-defined 에 대해 알아보자
cube <- function(n){
  return(n*n*n) # 이것도 하나의 함수처럼 기술하는가보다
}
cube(10)
cube(1:5)
# 이런식의 logical구성도 가능!
is.even.number <- function(n){
  n %% 2 == 0
}
is.even.number(10)

ifelse(is.even.number(numbers_vector), 'even', 'odd')

diff.max.min <- function(...){ # -- parameter가 다수거나 몇개인지 모를 경우는 ...으로 쓰면 됨! ...이 하나의 벡터가 됨!
 a <- c(...)
 largest <- max(a)
 smallest <- min(a)
 largest - smallest # 따로 return을 안써도 되나봄
}

diff.max.min(6,5,6,23,4,25)

# R은 데이터 분석용 프로그래밍 언어!! 빨리 분석해 결과를 내는 용도, 빅데이터를 다룰 만큼 빠른 속도가 정말 중요하다!!



## Data Loading
# 5개의 데이터 타입이 있다!!
# 1. Flat files
# 2. Excel
# 3. Databases (DB)
# 4. Web
# 5. Statistical software (SPSS) -- stata

# 우린 이 중 Flat files를 차용해 오는 것을 배워볼것

# 보통 파일 내 첫번째 줄은 Field names인 경우가 많다!!!

# 1. read.csv()
?read.csv()
# 'swimming_pools.csv' 라는 Brisbane에 있는 데이터를 가지고 올 것이다!!
pools <- read.csv("C:/Users/sec/Desktop/데이터 과학/swiming_pool.csv")
str(pools)

# 교수님 방법 -- R tool 우측에 upload눌러서 파일을 업로드, 근데 왜 난 upload가 없지..ㅜㅜ

head(pools)

# pools의 수영장 이름과 주소가 factor형으로 되어 있다! 이 거를 char형으로 바꾸는 게 필요할 듯!
# 왜냐면 read.csv()를 쓸때 대체적으로 char형을 다 factor형으로 기본적으로 전환한다
# 이것을 string으로 바꿀 필요가 있겠지

pools <- read.csv("C:/Users/sec/Desktop/데이터 과학/swiming_pool.csv", stringsAsFactors = F)
str(pools)
# 노가다의 방법도 있지
pools$Name <- as.character(pools$Name)
pools$Address <- as.character(pools$Address) 

# 2. read.table() -- Read any tabular file as a data frame, Number of arguments is huge!
# read.table("~~.txt", header = T, sep = "/", stringsAsFactors = F) -- header : first row lists variable names(디폴트는 F) , sep : 구분자
hotdog <- read.table("C:/Users/sec/Desktop/교과목들/데이터 과학/hotdogs.txt", header = T, sep = '\t', stringsAsFactors = F)
head(hotdog)
str(hotdog)

# 다음과 같이 col.names를 통해 header의 이름을 지정할 수도 있다!! 대신 이 경우는 기존에 있던 Type Calories Sodium을 데이터로 인식하는 단점이 있으니 주의!
hotdog <- read.table("C:/Users/sec/Desktop/교과목들/데이터 과학/hotdogs.txt", sep = '\t', col.names = c("type", "calories", "sodium"), stringsAsFactors = F)
head(hotdog) # 실행해보면 이상한 점을 확인할 수 있다!

# cal.type이라는 걸 추가하고 싶다!
hotdog$cal.type <- ifelse(hotdog$Calories >= 150, 'heavy', 'light')
head(hotdog)

# 해당 수정 결과를 새로운 데이터 타입으로 저 장하고 싶은 경우!
write.csv(hotdog, "newhotdog.csv", row.names = F) # row.names -- 1~50가지의 숫자는 저장하지 마라
# 다음을 실행하면 csv파일이 만들어짐을 확인할 수 있다.

# csv가 아닌 다른 파일 형태로 저장하고 싶다!
write.table(hotdog, "tablehotdog.tsv", row.names = F, sep = '\t')
# 이 경우도 tsv파일이 만들어짐을 확인할 수 있다.

# 해당 파일을 저장하고 싶은 경우는?? Save!!
my.var <- 10
my.var2 <- c(1, 4, 6, 22, 3)
my.var3 <- c('john', 'Bob', 'Alice')
my.var4 <- data.frame(A = 1:3, B = 9:11)
save(my.var, my.var2, my.var3, my.var4, file = "myVariables.RData") # R파일이 만들어짐을 확인할 수 있음!!

# 하던 걸 다 없애고 싶으면 우측 상단의 빗자루를 누르면 좋음
# 다시 가져오고 싶으면
load("myVariables.RData")

# 해당 작업하는 것을 다 가져가고 싶은 경우, 가령 다른 컴퓨터에서 작업을 해야하는 소요가 발생할 때
save(list = ls(), file = myWork.RData)
# 혹은 우측 상단의 저장 버튼을 누르면 된다!


### RData file의 경우는 용량도 훨씬 작고 R에서 사용하기 빠르다
## csv파일은 모든 text를 파싱하기에 시간이 오래 걸리고 용량도 크다!



## Apply Function

# Let me introduce apply() family

# It applies functions to manipulate slices of data (스칼라 데이터가 아닌)from matricies, arrays, lists, dataframes
# 이러한 데이터 타입에 대하여 반복적으로 여러 기능들을 수행해주는 기능을 하는 함수 
# 종류로는 apply(), lapply(), sapply(), vapply(), mapply(), rapply(), tapply()

# 1. apply(X, MARGIN, FUN, ..)

# X is martix or dataframe
# MARGIN is a variable defining how the function is applied (함수가 적용되는 방향)
# MARGIN=1, it applies over rows
# MARGIN=2, it works over columns
# FUN is the function that you want to apply to the data(적용할 함수)
# example
A <- matrix(1:6, byrow=T, nrow=3)
apply(A, 1, sum) # MARGIN이 1이므로 행 단위로 slicing해서 sum을 계산, 결과는 벡터형으로 반환하겠지
apply(A, 2, sum)
apply(iris[,1], 2, sum)
## apply(mtcars, mtcars$mpg, sum)  ----- 이런식으로 특정 조건에 맞는 연산은 안되는듯..

# 연습 한번만 더해보자

set.seed(2018) # 난수 부여할때 고정을 해주게됨! 
myMat <- matrix(runif(12), ncol = 4) # runif(n) : 0~1 사이의 수 n개를 뽑음
myMat
set.seed(2018)
myMat <- matrix(runif(12), ncol = 4)
myMat
apply(myMat, 1, mean)
apply(myMat, 2, mean)

head(iris)
apply(iris[, 1:4], 2, mean)
apply(iris[, 1:4], 1, mean)

# 이렇게도 구할 수 있었지
colMeans(iris[, 1:4])

# 2. lapply() -- (데이터프레임, 리스트, 벡터) 각 요소에 대해서 특정 함수를 적용
# 결과값은 list로 반환(list apply라고 생각하자)

myList <- list(num = 3.14, chr = "char", logi=T)
myList

lapply(myList, typeof) # 리스트 각 요소에 typeof라는 함수 적용
# typeof(3.14), typeof("char"), typeof(T) 이러한 기능을 수행하게 된다

# lapply를 데이터프레임과 벡터에도 적용해보자

lapply(mtcars, mean)
vecs <- c(1, 2, 3, 4, 5)
lapply(vecs, mean)
# 다른 예를 가져와보자
myList2 <- list(vec = 1:5, mat = matrix(runif(12), ncol = 4), df=iris)
result <- lapply(myList2, length)
result # 매트릭스의 length는 요소들의 갯수였지만, df의 경우는 column의 갯수가 반환됨을 인지!

# cf) 데이터 프레임은 list of vectors!! 꼭 알아두자
head(iris)
length(iris)

# list -> vector 기능을 하는 unlist()
unlist(result)
unlist(myList2)

lapply(c(1,4,9,16), sqrt)
lapply(mtcars, max) # 기본 열별로 계산, why? 벡터들의 리스트이니까 (벡터는 열별로 분포)
#동일한 기능을 하는 
apply(mtcars, 2, max) # 벡터형으로 반환
unlist(lapply(mtcars, max)) # 이러면 apply()랑 계산 결과가 같겠지

# 3. sapply() -- 기본적인 기능은 lapply()와 기능 동일
# 이것두 데이터 프레임, 리스트, 벡터에 적용
# 이거는 벡터랑 매트릭스형 반환
sapply(iris[, 1:4], mean)

#lapply(iris[, 1:4], mean) -- 해당 결과랑 비교해보자
sapply(iris, is.numeric)
# instance function
sapply(c(1,3,5,7,9), function(x){x**2}) # 이렇게 함수를 짬내서 만들어 적용 가능
sapply(matrix(1:12, ncol=4), function(x){x/2})

x <- sapply(iris[, 1:4], function(x){x>3}) # 이 경우 결과를 매트릭스로 반환
head(x)
colSums(x) # 이 경우, True는 1, False는 0으로 취급해서 연산, 참 혹은 거짓의 경우를 count할때 많이 쓴다

K <- sapply(iris[, c("Sepal.Width", "Petal.Width")], function(n){n > 3 & n < 5}) ## R에서 and 연산자는 &임을 기억
colSums(K)
K

# 이 경우도 매트릭스로 반환하는듯?
x <- sapply(iris[, 1:4], function(x){x/2})
head(x)

# 4. tapply(X, GRP_VAR, FUN, ...) 입력값이 벡터
# apply FUN to X after grouping with GRP_VAR
# 그니까 dplyr의 group_by개념을 생각하면 편하겠다
# 결과는 벡터형??, 리스트형??


# iris의 경우는 Species에 따라 다양한 특징들이 분포되어있다.
head(iris)
# 여기서 다음 명령을 수행해보자
# 이 경우는 종에 따른 Sepal.Length의 평균값을 산출해주는 기능을 한다.
tapply(iris$Sepal.Length, iris$Species, mean)

tapply(mtcars$mpg, mtcars$cyl, mean) 
# 이 경우 해석해볼래?
head(mtcars)

# mpg가 20이 넘는 녀석들과 그렇지 않은 녀석들의 wt의 평균값 -- 기준점이 2개가 될 수도 있다.
tapply(mtcars$wt, mtcars$mpg>20, mean)

# 이렇듯 보다 복잡한 구성의 연산을 처리해주는 기능을 하는 것이 tapply()
# dplyr, tidyr에 있는 연산들을 처리해준다

# 이 경우는 실린더의 갯수별 연비가 20보다 큰지 작은 지를 나열
# 여기서 중요한 점은 tapply의 세번쨰 인자의 함수의 parameter는 첫번째 벡터가 된다.
x <- tapply(mtcars$mpg, mtcars$cyl, function(x){x>20})
x

# Question, tapply(분류할 것들, 분류할 기준) 이렇게 되는건가?
sapply(x, sum)


## aggregate(var1 ~ var2, data = x, FUN = func, ..)
# Apply func to var1 of X after grouping by var2
# alternates to tapply
# Result is data.frame

# tapply는 벡터 2개를 주었지만
# aggregate는 df를 주고 그 중 벡터 2개 선정하는 식으로, 조금 더 유용한 녀석이다


# cyl기준 mpg를 구분한 걸 mean 적용
aggregate(mpg~cyl, data=mtcars, FUN = mean)

aggregate(Sepal.Length~Species, data=iris, FUN = mean)

# '~' : formula , y~x : y를 x기준으로 ( y는 종속변수, x는 독립변수)

# order() and sort() 정렬하는 녀석들이다!!

# order() gives a vector of index of smallest element, second smallest, .. # 해당 벡터를 정렬한 채로 해당 수들의 정렬전의 인덱싱을 반환

# sort() gives a sorted vector of numbers 정렬해준 결과 반환

# decreasing 옵션도 존재
vecs <- c(6, 12, 4, 89, 23, 35)
vecss <- c(2, 3, 1, 4)
order(vecs)
order(vecs, decreasing=T)
new_vecs <- vecs[order(vecs)] # 요렇게도 정렬 가능 order()는 생각을 좀 해야되!!
new_vecs

sort(vecs)

vecs[order(vecs, decreasing = T)]
sort(vecs, decreasing = T)
c <- c(3, 2, 4, 5)
order(c)
c[order(c)]
# 왜 order를 쓸까?

# order는 벡터를 정렬하기 위함

# df는 sort를 쓰기 어려움, 불가능하기보다는 제한이 많다

# ex) 연비순으로 데이터 프레임을 정렬하자

mtcars[order(mtcars$mpg, decreasing = T), ]

sort(mtcars$mpg, decreasing = T) # 순수 정렬은 가능은 해도 데이터 프레임 안에 한눈에 깔끔하기 보기에 제한..

# 이렇게가 같은 기능을 하겠지..

iris[order(iris$Petal.Length), ]


## 유용한 몇가지 함수

# 1. sample(X, sample, replace = F, ...)
# X는 모집단, sample은 표본, replace는 복원으로 할지(T), 비복원으로 할지(F)

set.seed(2020) # 고정해주자
X <- 1:20
sample(X, 10)
sample(X, 10, replace = T)
sample(X, 10, replace = F) # 얘는 비복원이라 제한이 되겠지

# iris의 150개의 데이터 중 10개만 보고 싶은데... head 나 tail은 데이터가 편향될 가능성이 높아
# 이경우는 다음과 같이 해준다

sample(1:150, 10) # 1~150중 임의의 수 10개를 뽑는다

# 그리고 해당 수를 인덱스로 사용한다
iris[sample(1:150, 10), ]

## 이런식으로 큰 데이터에서 일부를 랜덤하게 착출할 때 많이 사용한다

mtcars[sample(1:nrow(mtcars), 20), ]

# sample은 순서대로 배치되어 있는 데이터를 섞는대도 사용될 수 있다. --- 데이터의 편향을 방지하기 위해!!
x <- 1:10
sample(x, length(x))

# 실전 적용, sample은 indexing임을 꼭 인지하세요!! 주의해라!
women
woman_shuffle <- women[sample(1:nrow(women), nrow(women)), ]
woman_shuffle

# mtcars에서 섞는 방법을 적용해보자!!
mtcars$mpg <- sort(mtcars$mpg)
mtcars

mtcars <- mtcars[sample(1:nrow(mtcars), nrow(mtcars)), ]
mtcars

iris[sample(1:150, 150), ]

## 2. split(df, split_Var, ...) -- 데이터 프레임을 쪼개는 함수!! 반환값 리스트!!
# Split a data frame into a list of data frames with split vairable

# cyl 벡터를 기준으로 데이터 프레임 쪼갬
split(mtcars, mtcars$cyl)

split(mtcars, mtcars$mpg > 20)

mtcars["mpg"] # 한 열의 값만 df형식으로 반환하기


## 3. subset(df, condition, ...) --- 데이터의 프레임의 하위 집합을 특정 기준에 찾는 녀석
# Find a subset of dataframe with a criteria ---- 일종의 selection
subset(mtcars, mpg>25)
# 이거랑 같은 기능이다!
mtcars[mtcars$mpg>25, ]

iris[iris$Sepal.Length > 7, ] # 이런식으로 행의 indexing을 이용한 subset구하는 technique도 꼭 숙지하라

## 4. merge(df1, df2, ...) -- 두개의 데이터프레임을 공통된 변수를 갖는 하나의 데이터 프레임으로 합치는 것??
## Join two data frames into one with common variable
# cbind랑 유사하겠지!! 하지만 차이가 있다.

x <- data.frame(name = c("John", "Bob", "Carol"), math = c(70, 80, 90))
y <- data.frame(name = c("John", "Bob", "Alice"), history = c(100, 55, 75))
x
y
merge(x, y) # 공통된 이름을 갖는 녀석만 골라서 하나의 데이터 프레임 구축
merge(x, y, all = T) # 공통되든 안되는 걍 합치는 것

tol <- cbind(x, y) # 얘는 나란히 붙여주는 것, 말그래도 열을  합치는 것 뿐!
tol
y <- data.frame(name = c("John", "Bob", "Carol"), history = c(100, 55, 75))
tol <- cbind(x, y)
tol2 <- rbind(x, y)

cbind(iris, mtcars) # 이 경우 길이가 달라 에러

merge(iris, mtcars) # 이 경우에는 결과가 이상한데 어떻게 된 거지?? 중복이 되는데

# 중복이 된다 확인해보자
test1 <- data.frame(L = c(1, 2,3), W = c('a', 'b', 'c'), P = c(4, 5, 6))
test2 <- data.frame(mpg = c(12, 23, 45, 66), wt = c('g', 'h', 'j', 'k'), cyl = c(55.2, 22.3, 31.2, 1.1))
test1
test2
merge(test1, test2) 
?merge()
# 이 경우는 실행에 착오가 생긴다!
test3 <- data.frame(L = c(2, 3,4), M = c('m', 'n', 'o'), C = c(6, 5, 4))
test3
test1
merge(test1, test3)

# merge()함수는 공부를 많이 해야 한다!! key값에 따른 다양한 정렬을 할 수 있음을 참고하자
# https://rfriend.tistory.com/51 해당 링크를 참고!!
# https://m.blog.naver.com/PostView.nhn?blogId=coder1252&logNo=220953760651&proxyReferer=https:%2F%2Fwww.google.com%2F
merge(test1, test3, by = 'L')
merge(test1, test3, by = 'L', all = T)
merge(test1, test3, all.test1 = TRUE) # 왜 안되지들..
merge(test1, test3, all.test2 = TRUE)


## 5. which() --- 해당 조건을 만족하는 녀석의 인덱스 반환
# Find positions of elements that satisfy the condition

x <- c(5, 1, 2, 6, 3, 17, 8, 9, 12)
myindex <- which(x > 10)
myindex # 인덱스 반환
x[myindex] # 값 반환

# 요런 식으로 사용 가능
mtcars[which(mtcars$mpg > 30), ]


# which.max, which.min -- Find positions of maximun and minimum elements
x
# 인덱스 반환
which.max(x)  
which.min(x)
# 값 반환
x[which.max(x)]
x[which.min(x)]

## 6. cut() -- 연속형 변수보다 명목형 변수가 더 좋을 때가 있다.
mtcars$wt
mtcars
mtcars$mt_grp <- cut(mtcars$wt, breaks = c(0,2,4,6), label = c('light', 'normal', 'heavy')) # 0~2, 2~4, 4~6
# label에 따라 구간마다 naming도 가능하다!!
mtcars[, c('wt', 'mt_grp')]
# 이 경우 방향이 반대가 됨을 알 수 있다!!
mtcars$mt_grp <- cut(mtcars$wt, breaks = c(0,2,4,6), right = F)
mtcars
mtcars$mt_grp
## cut은 이렇게 분포가 어느정도 추정될 때 사용이 가능하지만, 대부분 데이터를 수집하면 수가 천차만별이라 분포를 알기 쉽지 않다.
# ex) 사람들마다 하루에 기침을 하는 수, 휴대폰을 들여다보는 시간 등...
# 제시된 명확한 기준이 없을 경우 이런 경우는 범위를 적절히 나누기가 어렵다.

### 이런 경우 우리는 quantile을 사용한다!!!! -- '분위수'를 의미한다
quantile(iris$Sepal.Length)
# Smallest, Median, Biggest
# 100명이라 가정할 떄
# 25번째 사람 -- 1 사분위수
# 75번째 사람 -- 3 사분위수

# 보고 싶은 확률만 따로 빼와서 확인도 가능하다!
quantile(iris$Sepal.Length, probs = c(0.1, 0.5, 0.9)) 
# 이 quantile함수를 통해 cut에서 구간을 자를 기준을 제시해줄 수 있다. 
#summary(iris$Sepal.Length)
hist(iris$Sepal.Length)

cut_point <- quantile(mtcars$mpg, c(0, 0.25, 0.75, 1))
mtcars$fuel_efficiency <- cut(mtcars$mpg, breaks = cut_point, include.lowest = T)
# include.lowest --> 기본 디폴트로 ( ] 식으로 형성되는데 그럼 최소값이 포함이 안될 것을 우려.. 다음과 같은 인자를 넣어준다!
mtcars[, c('mpg', 'fuel_efficiency')]
levels(mtcars$fuel_efficiency) <- c('low25perc', 'normal', 'high25perc') # label을 통한 인자도 가능하지만
# leves()함수를 통해서도 네이밍이 가능하다!!

# table()을 통해 해당 변수의 카운트?

table(mtcars$fuel_efficiency)
table(mtcars$cyl)
table(mtcars$fuel_efficiency, mtcars$cyl) # 매트릭스 형태로 만들어줌! -- 전문용어로 ConfusionMatrix!

#hist(table(mtcars$fuel_efficiency, mtcars$cyl))
 
# paste()
# to  concatenate several values into one string!            # 하나의 스트링으로 합치는 기능
# to cancatenate element by element from 2 or more vectors   # 2개 이상의 벡터를 합치는 기능 -- python의 zip이랑 같은 기능      
# to smash vector elements into one string                   # 벡터를 하나의 스트링으로 smash by collapse

# in Python, 두 스트링을 합치기 위해
# print("hellow" + "world") # 식으루
# But in R use paste()


paste('one', 1, 'three')

x <- seq(2, 20, 2)
y <- LETTERS[1:10] # 이 경우 알파벳 문자열을 순서대로 뽑음
x
y
y <- LETTERS[1:11] # 길이가 다를 경우는? 반복!!
paste(x,y)
paste(x,y,sep=":")

# need to use 'sep' and 'collapse' option properly
# useful to generate column names and row names
# paste0 equals to paste(..., sep = '')

var <- seq(2, 20, 2)
paste('var', x)
paste0('var', x)
paste('var', x, y, sep = "-")
paste(x)
# 벡터를 하나의 스트링으로 smash
paste(x, collapse = ",")
paste(x) # 하나만 하게 되면 그냥 각각의 element를 string화
x
y
paste0(x, y)
paste(paste0(x,y), collapse = ",")

# 적용!
test.df <- data.frame(year = c(2019, 2020, 2016), month = c(4, 5, 7), day = c(10, 15, 20))
test.df
test.df$date = paste(test.df$year, test.df$month, test.df$day, sep="-")
test.df
test.df$name <- c('john','Bob','Carol')
test.df
test.df$name 
paste(test.df$name, collapse=',')

names(mtcars)
# 모델링을 구축할 때를 예로 들면
#'mpg ~ cyl + disp ...' 이런식으로 하는데 변수가 겁나 많은 경우는 일일이 입력해주기 어렵다
#'이런 경우 어떻게 할까
outcome <- 'mpg'
input_vars = names(mtcars)[2:6]
# 이렇게 축약해서 나타나게 된다.
paste(outcome, paste(input_vars, collapse = '+'), sep='~')

## collapse는 하나의 벡터의 구성요소들끼리 하나의 스트링으로 smash할때
## sep는 두개 이상의 벡터를 합칠 때

## 둘의 구분법을 구분할 줄 알아야 한다!! 


### Data science Project Pipeline --- 프로젝트는 어떻게 운용되는가????
# ex)
## Turn prediction -- 카드회사, 신용회사의 고객관리 중
# churn : 고객 중 우리 서비스를 이탈하고자 하는 고객들
# 이러한 고객들에 대한 미리 예측
# 서비스의 불편한 점을 확인하여 고객 관리
# ex2)
## Data visualization
# 싱가폴의 Traffic monitoring system -- 밝게 : 교통이 혼잡, 어둡게 : 교통이 완산 실시간으로 

# 데이터 과학의 프로세스가 어떤 식으로 진행이 되는가???

# 1. Goal setup
# 
# 2. Data Collection
# 
# 3. Data Preprocessing(verification, cleaning)
#
# 4. Data analysis
#
# 5. Evaluation and Revision
#
# 6. Documentation and Presentation of Result
#
# 7. Development

# Goal setup

# Goal should be

# 1) Reasonable 2) Clear 3) Measurable

# Data collection -- client may provide the data

# To check license, privacy, and confidentiality issue

# 요즘은 오픈 데이터 프로세스들이 많다
# ex) Uniprot : http://www.uniprot.org/
# provide protein sequence and functional information
# ex) GDELT project -- daily world-wide events
# http://gdeltproject.org/
# ex) 공공 정부 데이터
# data.go.kr
# data.seoul.go.kr
# ex) EU open data portal
# https://open-data.europa.eu/en/data/
# ex) DBLP - computer science publications, authors, citations 등
# http://dplp.uni-trier.de/
# ex) weather underground -- real-time and historical world=wide weather information
# http://www.wunderground.com/

# 좋아!!
# ex) UC Irivine machine learning Repository -- 이거 공부하는 거 연습용 데이터에 많이 있으니 쓰자!!
# http://archive.ics.uci.edu/ml/


## Data 검증!!
# 데이터를 이해하고 샘플들의 수와 정보
# 변수들은 어떠한 형태인지
# 데이터의 오류 검정

## 데이터 전처리!!
# Data cleaning and Processing

# 데이터의 검증과 전처리가 전체의 80%를 차지할만큼 중요한 과정이다!!!

# 이후 데이터 분석!! -- Supervised method, Unsupervised Method

# 이후 결과를 평가!!!


#### Loading data to R
bmi_clean <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/bmi_clean.csv", header = T)
# 훗 공부한 걸 써먹기
bmi_clean[which(bmi_clean$Country == "Korea, Rep."), ]

## 이러한 web URL을 통해 긁어오는 것도 가능!!
uniCar <- read.csv('http://www.win-vector.com/dfiles/car.data.csv', header = T)
uniCar
View(uniCar)

#### Exploring Raw Data

class(bmi_clean)
dim(bmi_clean)
names(bmi_clean)
str(bmi_clean)
# str()랑 동일한 기능을 제공하는 dplyr 함수
# 개략적으로 데이터에 대한 개괄
library(dplyr)
glimpse(bmi_clean)

summary(bmi_clean) # 변수들에 대한 통계 - > char형 변수는 count, 숫자형의 경우 분포

hist(bmi_clean$Y1980)
plot(x = bmi_clean$Y1980, y = bmi_clean$Y2008)


#### Data cleaning!!! --- 수작업과 노가다!! 하지만 굉장히 중요!!


## common symptoms of messy data!!

# tidyr
library(tidyr)
test_overwatch <- data.frame(read.csv("C:/Users/sec/Desktop/개인 업무 자료/DRA/연습용 R파일.csv"), stringsAsFactors = F)
test_overwatch
# gather(df, key, value, ...) -- ...는 합칠 열
# 이렇게 wide한 데이터 형태로 바꿀 수 있다!!
test_overwatchs <- gather(test_overwatch, character, value, c(2, 3))
test_overwatchs
## spread(df, key, value) -- 다시 spread

test_overwatchss <- spread(test_overwatch, Hero, Type)
test_overwatchss
test_overwatchsss <- spread(test_overwatchs, character, value) 
test_overwatchsss

## spread에서 주의할 점!! ppt 필기 참고!!  
# 여기서 col은 분리할 열, into는 뭘로 분해?
#seperate(data, col = , sep = , into = ) sep의 디폴트는 "-"을 기준으로 나눔
# 여기서 col은 합쳐서 만들 열, ...는 합칠 열
#unite(data, col, ...) 디폴트 sep = "_"


# practice!!
head(bmi_clean)

bmi_clean_wide <- gather(bmi_clean, year, bmi_value, -1)
head(bmi_clean_wide)
bmi_clean_long <- spread(bmi_clean_wide, year, bmi_value)
head(bmi_clean_long)


bmi_cc <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/bmi_cc.csv")
head(bmi_cc)
bmi_cc_sep <- separate(bmi_cc, Country_ISO, sep="/", into = c("Country", "ISO"))
bmi_cc_uni <- unite(bmi_cc_sep, Country_ISO, sep = "/", Country, ISO)
bmi_cc_uni

## Date 와 Posict! Date 는 날짜, Posict는 날짜+시간
date <- c('2010-01-01', '2011-01-01')
summary(date)
as.Date(date)
library(lubridate)
summary(ymd('2020-04-11', '2021-12-12', '2030-02-01'))
summary((as.Date(date))) ## Date 타입으로!! x축에 날짜 데이터를 쓸 경우!!!!
range(as.Date(date))
## 이거 되게 요긴하게 사용할 수 있어!!!

library(stringr)
# 앞 뒤 공백 제거
str_trim(" John Smith ")


# 자릿수를 맞추어줌
# str_pad(스트링, 자릿수, 어디에 패팅?, 패팅할 문자)
str_pad("24493", width = 7, side = "right", pad = "0")
str_pad("24493", width = 9, side = "left", pad = "0")

#str_detect(스트링 집합 혹은 벡터, 찾을 놈) -- 많이 썼지??
#저 들어갈 자리에 df 이런건 안되는 거 같음 벡터형을 요구하네
str_detect("abcdefg", "x")
str_replace("abcdefg", "e", "x")
students <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/students2.csv", stringsAsFactors = F)
str(students)
students$dob <- as.Date(students$dob)
library(lubridate)
students$nurse_visit <- ymd_hms(students$nurse_visit)

str_detect(students$dob, "1997")
## 저장한 채로 갖기 위해서는 반드시 값을 할당해야 한다.
students$sex <- str_replace(students$sex, "F", "Female")
students$sex <- str_replace(students$sex, "M", "Male")
students$sex

## 조금 잔머리를 쓰면 이런 구성도 가능하니까 테크니컬하게 활용하자!!
cols <- colnames(bmi_clean)
colnames(bmi_clean) <- str_replace(cols, "Y", "")
bmi_clean

## 결측치를 다루는 법!!!

is.na(mtcars)
any(is.na(mtcars)) # 하나라도 있는가
sum(is.na(mtcars)) # 총 몇개 있는가
colSums(is.na(mtcars)) # 열별로
summary(mtcars)

dfs <- data.frame(A = c(1, NA, 8, NA), B = c(3, NA, 88, 23), C = c(2, 45, 3, 1))
dfs
## 행별로 NA가 없는 경우 - True, 있는 경우 - False
complete.cases(dfs)
## NA가 없는 행만 추출하는 경우 --- 이렇게 쓰는 테크닉은 반드시 숙지하자!
dfs[complete.cases(dfs), ]
## 동일한 기능으로 na.omit()이라는 함수도 있다. 얘도 NA가 없는 행들만 추출해서 df형태로 보여준다
na.omit(dfs)
drop_na(dfs)

set.seed(10)
# rnorm(sample수, 평균, 표준편차)
x <- c(rnorm(30, mean = 15, sd = 5), -5, 28, 35)
boxplot(x, horizontal = F)

# 이상치를 확인해보는 예제
set.seed(2020)
df2 <- data.frame(A = rnorm(100, 50, 10), B = c(rnorm(99, 50, 10), -500), C = c(rnorm(99, 50, 10), -1 ))
df2
summary(df2)
hist(df2$B, breaks = 20)
boxplot(df2)
df2$B[which(df2$B< -100)]

students3 <- read.csv("C:/Users/sec/Desktop/교과목들/데이터 과학/students3.csv", stringsAsFactors = F)
str(students3)

## plot에 대해
set.seed(1919)
x1 <- rnorm(1000)
y1 <- x1 + rnorm(1000)

plot(x1, y1)
abline(lm(y1~x1), col = "red")
## density에 대한 수치도 구할 수 있는데..
density(x1)
# plot을 통해서도 구할 수 있다. 분포 형태를 보여주는 거지
plot(density(x1))
density(y1)
plot(density(y1))

# 동시 표현 가능
## 이 lines는 기존 plot에 그래프를 추가해줄 때 사용
plot(density(x1)) + lines(density(y1), col="red")
plot(density(x1))+plot(density(y1)) # 이거는 안되는듯

## 축 이름 설정
plot(x1, y1, 
     main = "This is my plot", 
     xlab = "X-values", 
     ylab = "Y-values")

# 이항분포 함수들 참고 링크!
# https://m.blog.naver.com/PostView.nhn?blogId=padosori60&logNo=220755436419&proxyReferer=https:%2F%2Fwww.google.com%2F


# 그룹화하여 그래프 그림!!
group <- rbinom(1000, 1, 0.3) + 1 ## create group variable
group
plot(x1, y1,                     ## create plot with group
     main = "This is my Plot",
     xlab = "X-valeus",
     ylab = "Y-valeus",
     col = group, ## color를 통해 그룹을 구분
     pch = group) ## PCH인자는? 
## 1번째 그룹은 검은색
## 2번째 그룹은 빨간색으로 표현

## legend 함수 범례 표시
# https://thebook.io/006723/ch06/06/ 참고

legend("topleft", 
       legend =  c("Group1", "Group2"), 
       col = 1:2, 
       pch = 1:2)
x2 <- seq(-5, 5, 0.01)
y2 <- cos(x2)
y2
plot(x2, y2)

# Customizing plot!
# https://www.youtube.com/watch?v=0MrYVzPxBIc&feature=youtu.be

###### dplyr을 복습하기 위해 -- DRA 교육자료랑 같이 참고
library(hflights)
View(hflights)
# tbl_df() 조금 더 효과적으로 데이터를 보기 위해
library(dplyr)
hflights2 <- tbl_df(hflights)
View(hflights2)
# str()보다 더 많이 쓰는 glimpse()
glimpse(hflights)
glimpse(hflights2)
# tbl 데이터를 쓰기 싫으면 다시 df로 바꾸면 되!
as.data.frame(hflights2)

# select 랑 mutate는 열을 다루는 부분으로서 variable를 다룸
# filter랑 arrange 는 행을 다루는 부분으로서 observation을 다룸
# summarize는 group화 함

# select()
hflights2 %>% select(Month, ArrDelay, ActualElapsedTime, AirTime, DepDelay)
# 이렇게 걍 나란히 쓰면 되
h1 <- hflights2 %>% select(Month, ArrDelay, ActualElapsedTime, AirTime, DepDelay)
glimpse(h1)

# mutate()
mutate(hflights2, shival = ArrDelay - DepDelay)
hflights2[, "shival"]
h1 <- mutate(h1, shival = ArrDelay - DepDelay)
glimpse(h1)
mean(h1$shival, na.rm = T)
hist(h1$shival)

# filter()는 공모전때도 많이 썼던 함수이다. 알아놓자
## 그전에 알아놓으면 좋을 것!!
# 'starts_with()', 'ends_with()' 인자도 꼭 알자!!
f1 <- select(hflights, starts_with("Cancel"), DepDelay)
f1
filter(f1, Cancelled == 1) ## 이건 시험때도 쓰자!!!
f2 <- filter(f1, Cancelled == 1)
f2

# arrange()
order랑 sort보다 쉬움

library(dplyr)
mtcars %>% arrange(desc(mpg))
# contains() 인자도 있음을 알자!!!
a1 <- select(hflights, TailNum, contains("Delay"))
a1
arrange(a1, desc(DepDelay)) # 내림차순
arrange(a1, DepDelay, ArrDelay) ## 이럴 경우는 기준은 앞에 것

# summraise()
summarise(hflights, n())
summarise(hflights, n_distinct(DepDelay))
## na지워주는 습관
summarise(hflights, sum = sum(DepDelay, na.rm = T), avg = mean(DepDelay, na.rm = T), var = var(DepDelay, na.rm = T))
hflights$DepDelay
## 보다 na를 깔끔하게 처리해주기 위해
a1
a1<- filter(a1, !is.na(ArrDelay), !is.na(DepDelay))
a1 %>% summarise(sum = sum(ArrDelay), mean(DepDelay))

### pipes -- passing object 중요하다!
'%>%' 
c(1, 2, 3, NA) %>% sum(na.rm = T)
# 이런식의 연산도 가능
hflights$ArrDelay %>% hist(col = 'steelblue', border = 'white', xlim = c(-50, 400))

# group_by()
# 구조는 이렇게
group_by(df, 'column to group by')

U1 <- hflights %>% group_by(UniqueCarrier)

U1$UniqueCarrier
hflights %>% group_by(UniqueCarrier) %>%
  summarise(avgDep = mean(DepDelay, na.rm = T), 
            avgArr = mean(ArrDelay, na.rm = T)) %>%
  arrange(avgArr, avgDep)

## databases
data frame
data table -- tbl_dt
database - tbl

## R markdown에 대해서 간단히 공부해보자?


name.df <- data.frame("name" = c(1, 2, 3, 4 ,5), "A"= c(T, F, F, F, F), "B" = c(F, T,F,F,F), "C" = c(F, F, T, F, F), "D" = c(F,F,F,T,F), "E" = c(F,F,F,F,T))
name.df
library(tidyr)
name.df <- gather(name.df, type, value, A:E)
filter(name.df, value == TRUE)
library(dplyr)
