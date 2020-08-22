load("C:/Users/sec/Desktop/교과목들/데이터 과학/hw5_student.RData")

str(student.train)

# 대충 famsize, Medu, studytime, failures, higher, class, schoolsup, school

student.train.used <- student.train


student.train.used$age_group <- cut(student.train.used$age, breaks=c(15,16,17,18,22),labels = c("1","2","3","4"), right=F)
student.train.used$absence_group <- cut(student.train.used$absences, breaks = c(1,5,10,15,25,35), labels = c("1","2","3","4","5"), right = F)
student.test.nolabel$age_group <- cut(student.test.nolabel$age, breaks=c(15,16,17,18,22),labels = c("1","2","3","4"), right=F)
student.test.nolabel$absence_group <- cut(student.test.nolabel$absences, breaks = c(1,5,10,15,25,35), labels = c("1","2","3","4","5"), right = F)


student.train.used$age_group
#student.train.used$ages <- ifelse(student.train.used$age >20, 1, 0)
student.train.used
# factor 형 전환
student.train.used$studytime <- as.factor(student.train.used$studytime)
student.test.nolabel$studytime <- as.factor(student.test.nolabel$studytime)

student.train.used$famrel <- as.factor(student.train.used$famrel)
student.test.nolabel$famrel <- as.factor(student.test.nolabel$famrel)

student.train.used$freetime <- as.factor(student.train.used$freetime)
student.test.nolabel$freetime <- as.factor(student.test.nolabel$freetime)

student.train.used$failures <- as.factor(student.train.used$failures)
student.test.nolabel$failures <- as.factor(student.test.nolabel$failures)

student.train.used$goout <- as.factor(student.train.used$goout)
student.test.nolabel$goout <- as.factor(student.test.nolabel$goout)

student.train.used$Dalc <- as.factor(student.train.used$Dalc)
student.test.nolabel$Dalc <- as.factor(student.test.nolabel$Dalc)

student.train.used$Walc <- as.factor(student.train.used$Walc)
student.test.nolabel$Walc <- as.factor(student.test.nolabel$Walc)

student.train.used$health <- as.factor(student.train.used$health)
student.test.nolabel$health <- as.factor(student.test.nolabel$health)

student.train.used$absences <- as.numeric(student.train.used$absences)
student.test.nolabel$absences <- as.numeric(student.test.nolabel$absences)

# numeric 전환
student.train.used$studytime <- as.numeric(student.train.used$studytime)
student.test.nolabel$studytime <- as.numeric(student.test.nolabel$studytime)

student.train.used$famrel <- as.numeric(student.train.used$famrel)
student.test.nolabel$famrel <- as.numeric(student.test.nolabel$famrel)

student.train.used$freetime <- as.numeric(student.train.used$freetime)
student.test.nolabel$freetime <- as.numeric(student.test.nolabel$freetime)

student.train.used$failures <- as.numeric(student.train.used$failures)
student.test.nolabel$failures <- as.numeric(student.test.nolabel$failures)

student.train.used$goout <- as.numeric(student.train.used$goout)
student.test.nolabel$goout <- as.numeric(student.test.nolabel$goout)

student.train.used$Dalc <- as.numeric(student.train.used$Dalc)
student.test.nolabel$Dalc <- as.numeric(student.test.nolabel$Dalc)

student.train.used$Walc <- as.numeric(student.train.used$Walc)
student.test.nolabel$Walc <- as.numeric(student.test.nolabel$Walc)

student.train.used$health <- as.numeric(student.train.used$health)
student.test.nolabel$health <- as.numeric(student.test.nolabel$health)

student.train.used$absences <- as.numeric(student.train.used$absences)
student.test.nolabel$absences <- as.numeric(student.test.nolabel$absences)

str(student.test.nolabel)
test_lm <- lm(G3~famsize+Medu+studytime+failures+higher+class+schoolsup+school+health*Dalc+health*Walc+health
              +failures*studytime, data=student.train.used)
summary(test_lm)

test_lm2 <- lm(G3~ famsize+Medu+Medu*higher+studytime+failures+higher+class+schoolsup+higher+school, data=student.train.used)
summary(test_lm2)

simple <- lm(G3~., data=student.train.used)

str(student.train.used)
str(student.test.nolabel)
names(student.test.nolabel)
names(student.train.used)
pred_grade_test <- predict(simple, newdata=student.test.nolabel)

save(pred_grade_test, file="st21600685.RData")
