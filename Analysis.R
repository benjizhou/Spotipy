setwd("C:/Users/benzh/Desktop/Spotipy")
dat <- read.table("Analysis.xlsx", sep=",", header=TRUE, stringsAsFactors=FALSE)

library(rio) #in case you didn't activate the library earlier
dat<-import("Analysis.xlsx",which=1)
subDat <- dat[,c(4:15)]
subDatSc<-scale(subDat)
#3. Calculate all pairwise distances
distDat <- dist(subDatSc)
k<-5
km5<-kmeans(subDatSc,k, nstart = 20)
distDat <- dist(subDatSc)
fit<-cmdscale(distDat, k=2) # k is the number of dim to PLOT
plot(fit, xlab="Coordinate 1",ylab="Coordinate 2", pch=16, col=km5$cluster)
studCodes<-as.character(dat[,1])
text(fit+.3, labels = studCodes, cex=.7)
legend("topright", legend=as.character(1:k), col=1:k, pch=16,
       title="Cluster", horiz = TRUE)