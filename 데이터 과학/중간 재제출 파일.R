library(dplyr)
library(tidyr)
library(stringr)

Q1.
str(pums.sample)

Q2.
pums.sample$SEX <- as.character(pums.sample$SEX)
pums.sample$SEX <- str_replace(pums.sample$SEX, "1", "Male")
pums.sample$SEX <- str_replace(pums.sample$SEX, "2", "Female")
pums.sample$SEX <- as.factor(pums.sample$SEX)
head(pums.sample$SEX)

Q3.
pums.sample$MAR <- as.character(pums.sample$MAR)
#pums.sample$MAR
named_vector <- c("1" = "Married", "2" = "Widowed", "3"= "Divorced", "4" = "Separated", "5" = "Never married or under 15 years old")

pums.sample$MAR <- sapply(pums.sample$MAR, function(x){named_vector[x]})

pums.sample$MAR <- as.factor(pums.sample$MAR)
head(pums.sample)

Q4.
colSums(is.na(pums.sample))
nrow(pums.sample)

Q5.
pums.sample.male <- pums.sample[which(pums.sample$SEX == "Male"), ]
nrow(pums.sample.male)
colSums(is.na(pums.sample.male))
pums.sample.female <- pums.sample[which(pums.sample$SEX == "Female"), ]
pums.sample.young_f <- filter(pums.sample.female, AGEP<15)
pums.sample.young_f
pums.sample.old_f <- filter(pums.sample.female, AGEP>50)
nrow(pums.sample.old_f)
colSums(is.na(pums.sample.old_f))

Q6.
summary(pums.sample)
pums.sample[which.min(pums.sample$PINCP), ]


Q7.

table(pums.sample$COW, pums.sample$SCHL)
tble <- prop.table(table(pums.sample$COW, pums.sample$SCHL))
tble

tble[, 1]
plot(tble[, 1], xlab = 'COW')
Q8.
cut_point <- cut(pums.sample$AGEP, breaks = c(20,30,40,50,60,84), right = F, labels = c("20s", "30s", "40s", "50s", "over 60s"))
#cut_point
cut_point[is.na(cut_point)] <- "20s" 

pums.sample$age_group <- cut_point
tapply(pums.sample$PINCP, pums.sample$age_group, mean)

Q9.
plot(pums.sample$WKHP, pums.sample$PINCP)
cor(pums.sample$WKHP, pums.sample$PINCP)
hist(pums.sample$WKHP)
pums.sample$W_group <- cut(pums.sample$WKHP, breaks = c(0, 20, 40, 60, 80, 100), right = F, labels = c('low', 'semi low', 'middle', 'semi high', 'high'))
summary(lm(pums.sample$PINCP~pums.sample$W_group))
plot(pums.sample$W_group, log10(pums.sample$PINCP))

Q10.
save(pums.sample, file = "21600685.retry.RData")

Q1.
iriss <- iris
iriss

iriss$id <- 1:150
iriss
iriss <- gather(iriss, Part, value, 1:4)
iriss

iriss <- separate(iriss, Part, into = c('Part', 'Char'))
iriss

iriss <- spread(iriss, Char, value)
iriss

iris.tidy <- iriss[, c('Species', 'Part', 'Length', 'Width')]
iris.tidy

Q2.

iriss2 <- iris
iriss2$id <- 1:150
iriss2

iriss2 <- gather(iriss2, Part, value, 1:4)
iriss2

iriss2 <- separate(iriss2, Part, into = c('Part', 'Measure'))
iriss2

iris.wide <- iriss2[, c('Species', 'Part', 'Measure', 'value')]
iris.wide
save(pums.sample, iris.tidy, iris.wide, file = "21600685.retry.RData")

install.packages('InformationValue')
?predict()

library(caret)
?confusionMatrix()


