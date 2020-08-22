load("C:/Users/sec/Desktop/교과목들/데이터 과학/hw5_student.RData")

library(dplyr)
library(tidyr)
library(ggplot2)
library(reshape2)
library(caret)
library(ROCR)
library(rpart)
library(class)
library(leaps)
library(kknn)

View(student.train)
student.test.nolabel
str(student.train)
sub.fit <- regsubsets(G3~., data=student.train)
best.summary <- summary(sub.fit)
names(best.summary)
which.min(best.summary$cp)
plot(sub.fit, scale = 'Cp')
# 대충 famsize, Medu, studytime, failures, higher, class, schoolsup, school
names(student.train)
# 이렇게 하는게 맞아??
model1 <- lm(G3~famsize+Medu*school+studytime+failures+
               higher+higher*schoolsup+class+schoolsup+school+
               Fedu*school+Mjob+Fjob+Mjob*Fjob+
               famsize*Pstatus+famsize*guardian+
               address*reason+reason+address+traveltime+famsup+
               famsup*paid+paid*activities+paid+schoolsup*paid+
               activities+nursery+internet+romantic+famrel*romantic+
               romantic*traveltime+traveltime*famrel+famrel+freetime*traveltime+
               freetime+goout*freetime+goout*romantic+goout+goout*famrel+
               Dalc+Walc+Dalc*Walc+health+health*Dalc+health*Walc+absences+
               absences*health+absences*address+
               Fjob*reason+Medu*studytime+Fedu*studytime+reason*Medu + reason*Fedu+
               sex*activities+sex*Medu+sex+Fedu+sex*freetime+sex*health+sex*Dalc+
               sex*Walc+sex*goout+sex*nursery+famsup*sex+schoolsup*sex+class*studytime+
               class*higher+class*reason+failures*class+failures*studytime+failures*schoolsup+
               failures*famsup+failures*romantic+failures*famrel+failures*absences+Pstatus*Fjob+
               Pstatus*Mjob+guardian*Mjob+guardian*Fjob+traveltime*Mjob+traveltime*Fjob
              , data=student.train)
summary(model1)
# factorize 해준 경우
student.train$famrel <- as.factor(student.train$famrel)
student.train$freetime <- as.factor(student.train$freetime)
student.train$goout <- as.factor(student.train$goout)
student.train$Dalc <- as.factor(student.train$Dalc)
student.train$Walc <- as.factor(student.train$Walc)
student.train$health <- as.factor(student.train$health)
student.train$absences <- as.factor(student.train$absences)
student.train$studytime <- as.factor(student.train$studytime)
student.train$failures <- as.factor(student.train$failures)
student.train$studytime <- as.factor(student.train$studytime)
student.train$failures <- as.factor(student.train$failures)
student.train$Medu <- as.factor(student.train$Medu)
student.train$Fedu <- as.factor(student.train$Fedu)
student.train$traveltime <- as.factor(student.train$traveltime)


student.test.nolabel$famrel <- as.numeric(student.test.nolabel$famrel)
student.test.nolabel$freetime <- as.numeric(student.test.nolabel$freetime)
student.test.nolabel$goout <- as.numeric(student.test.nolabel$goout)
student.test.nolabel$Dalc <- as.numeric(student.test.nolabel$Dalc)
student.test.nolabel$Walc <- as.numeric(student.test.nolabel$Walc)
student.test.nolabel$health <- as.numeric(student.test.nolabel$health)
student.test.nolabel$absences <- as.nuemric(student.test.nolabel$absences)
student.test.nolabel$studytime <- as.numeric(student.test.nolabel$studytime)
student.test.nolabel$failures <- as.numeric(student.test.nolabel$failures)
student.test.nolabel$studytime <- as.numeric(student.test.nolabel$studytime)
student.test.nolabel$failures <- as.numeric(student.test.nolabel$failures)
student.test.nolabel$Medu <- as.numeric(student.test.nolabel$Medu)
student.test.nolabel$Fedu <- as.numeric(student.test.nolabel$Fedu)
student.test.nolabel$traveltime <- as.numeric(student.test.nolabel$traveltime)

pred_grade_test <- predict(model2, newdata=student.test.nolabel)
pred_grade_test
save(pred_grade_test, file="st21600685.RData")
# numeric 해준 경우
student.train$famrel <- as.numeric(student.train$famrel)
student.train$freetime <- as.numeric(student.train$freetime)
student.train$goout <- as.numeric(student.train$goout)
student.train$Dalc <- as.numeric(student.train$Dalc)
student.train$Walc <- as.numeric(student.train$Walc)
student.train$health <- as.numeric(student.train$health)
student.train$absences <- as.numeric(student.train$absences)
student.train$studytime <- as.numeric(student.train$studytime)
student.train$failures <- as.numeric(student.train$failures)
student.train$studytime <- as.numeric(student.train$studytime)
student.train$failures <- as.numeric(student.train$failures)
student.train$Medu <- as.numeric(student.train$Medu)
student.train$Fedu <- as.numeric(student.train$Fedu)
student.train$traveltime <- as.numeric(student.train$traveltime)

summary(student.train$age)
student.train$age_group <- cut(student.train$age, breaks = c(15,17,19,21,22), labels = c("1","2","3","4"), right=F)
hist(student.train$absences)
student.train$absence_group <- cut(student.train$absences, breaks = c(1,5,10,15,25,35), labels = c("1","2","3","4","5"), right = F)
summary(student.train$absences)

age_group_numeric <- as.factor(age_group)
absense_group_numeric <- as.factor(absence_group)

model2 <- lm(G3~famsize+Medu+studytime+failures+failures*absences+
               higher*schoolsup+higher+class+schoolsup+school+Fedu*school+
               Mjob+Fjob+Fjob*address+famsize*Pstatus+famsize*guardian+famrel*romantic+
               address+reason+address*reason+traveltime+famrel*traveltime+famsup*paid+famsup+paid+activities+
               internet+romantic+famrel+famrel*freetime+traveltime*romantic+freetime*traveltime+freetime+goout*freetime+
               goout+Dalc+Walc+health+sex*Medu+sex*Fedu+sex+health*Dalc+health*Walc+sex*activities+sex*paid+
               sex*Dalc+sex*Walc+class*reason, data=student.train)
summary(model2)
simple <- lm(G3~.,data=student.train)
summary(simple)


student.train$schoolsup_numeric <- ifelse(student.train$schoolsup=="yes", 2, 0)
student.train$famsup_numeric <- ifelse(student.train$famsup=="yes", 1, 0)
student.train$paid_numeric <- ifelse(student.train$paid =="yes", 1,0)
student.train$activities <- ifelse(student.train$activities ==1,"yes","no")
student.train$activities <- as.factor(student.train$activities)
student.train$activities_numeric <- ifelse(student.train$activities =="yes",1,0)
#student.train$nursey_numeric <- ifelse(student.train$nursery =="yes",0,1)
student.train$higher_numeric <- ifelse(student.train$higher =="yes",2,0)
student.train$internet_numeric <- ifelse(student.train$internet =="yes",1,0)
student.train$romantic_numeric <- ifelse(student.train$romantic =="yes",1,0)

model3 <- lm(G3~famsize+Medu*school+studytime+I(studytime^2)+failures+Medu+I(Medu^2)+
               higher_numeric*schoolsup_numeric+I(schoolsup_numeric^2) + higher_numeric+ I(higher_numeric^2)+ class+schoolsup_numeric+school+Fedu*school+
               Mjob+Fjob+Mjob*Fjob+famsize*Pstatus+famsize*guardian+
               address+reason+traveltime+famsup_numeric+paid_numeric+activities_numeric+
               internet_numeric +romantic_numeric+famrel+freetime*traveltime+freetime+goout*freetime+
               goout+Dalc*Walc+Dalc+Walc+health+absence_group+age+I(age^2)+age_group, data=student.train)
summary(model3)
str(student.train)


# 대충 famsize, Medu, studytime, failures, higher, class, schoolsup, school
new_model <- lm(G3~famsize+Medu+studytime+failures+higher+class+schoolsup+school, data=student.train)
summary(new_model)
