setwd("C:/Users/eyyup/OneDrive/Desktop/design_build/")
D0 <- read.table("data0.txt.jpg", sep=";", header=TRUE, as.is=TRUE)
D1 <- read.table("data1.txt.jpg", sep=";", header=TRUE, as.is=TRUE)
D2 <- read.table("data2.txt.jpg", sep=";", header=TRUE, as.is=TRUE)
D3 <- read.table("data3.txt.jpg", sep=";", header=TRUE, as.is=TRUE)
D4 <- read.table("data4.txt.jpg", sep=";", header=TRUE, as.is=TRUE)

data_fade <- read.table("data4.csv.jpg", sep=";", header=TRUE, as.is=TRUE)


setwd("/home/mehmet/Desktop")


################################
## Read the .csv file containing the data
D2 <- read.table("datawednesday_evening.jpg", sep=",", header=TRUE, as.is=TRUE)
#type of D: list
D2<- unlist(D2)
#to array
D2<- c(D2)
plot(D2$X844.7542)
datawednesday_evening



