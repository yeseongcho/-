table_org <- data.frame(read.csv("C:/Users/sec/Desktop/GDP adjust.csv", stringsAsFactor =F))
str(table_org)
table <- table_org[,-9]
str(table)

colnames(table) <- c('Series_Name', 'Time', 'Cotedivoire', 'Cameroon', 'BurkinaFaso', 'Togo', 'Rwanda', 'CentralAfricanRepublic')
head(table, 9)
View(table)
install.packages("tidyr")
#install.packages("dplyr")
library("tidyr")
#library("dplyr")
table0 <- gather(table, country, value, -1, -2)
View(table0)
table1 <- cbind(filter(table0, Series_Name == 'TFP level at current PPPs ') %>% select(Time, country, value),
      filter(table0, Series_Name == 'Exports of goods and services (current US$)')%>% select(value),
      filter(table0, Series_Name == 'Foreign direct investment, net inflows (BoP, current US$)')%>% select(value),
      filter(table0, Series_Name == 'General government final consumption expenditure (current US$)')%>% select(value),
      filter(table0, Series_Name == 'Households and NPISHs Final consumption expenditure (current US$)')%>% select(value),
      filter(table0, Series_Name == 'Imports of goods and services (current US$)')%>% select(value),
      filter(table0, Series_Name == 'Net official development assistance received (current US$)')%>% select(value),
      filter(table0, Series_Name == 'Population ages 15-64, total')%>% select(value),
      filter(table0, Series_Name == 'WGDP')%>% select(value))




colnames(table1) <- c('Time', 'country', 'TFP', 'Export', 'FDI', 'GovernmentExpenditure', 'HouseExpenditure', 'Import', 'ODA', 'Population', 'WGDP')
library('plm')

pdata <- pdata.frame(table1, index = c('country', 'Time'))
pdata

fixed <- plm(TFP ~ Export +Population+ FDI + HouseExpenditure + Import + ODA + WGDP + Population+GovernmentExpenditure, data = pdata, model = 'within')
summary(fixed)
fixed <-plm(TFP ~ ODA+FDI+HouseExpenditure+GovernmentExpenditure, data=pdata, model='within')
fixed<- lm(TFP ~ Export +Population+ FDI + HouseExpenditure + Import + ODA + WGDP + Population+GovernmentExpenditure , data = pdata)
install.packages('car')
require(car)

vif(fixed)
