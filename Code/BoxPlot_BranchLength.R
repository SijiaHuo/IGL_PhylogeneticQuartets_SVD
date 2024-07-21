simphy.10tax.1000gen.100000su =as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-10tax-1000gen-100000su.csv", header=FALSE))
simphy.10tax.1000gen.100000su= as.vector(simphy.10tax.1000gen.100000su[,-ncol(simphy.10tax.1000gen.100000su)])

simphy.10tax.1000gen.500000su= as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-10tax-1000gen-500000su.csv", header=FALSE))
simphy.10tax.1000gen.500000su= as.vector(simphy.10tax.1000gen.500000su[,-ncol(simphy.10tax.1000gen.500000su)])

simphy.10tax.1000gen.1000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-10tax-1000gen-1000000su.csv", header=FALSE))
simphy.10tax.1000gen.1000000su= as.vector(simphy.10tax.1000gen.1000000su[,-ncol(simphy.10tax.1000gen.1000000su)])

simphy.10tax.1000gen.5000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-10tax-1000gen-5000000su.csv", header=FALSE))
simphy.10tax.1000gen.5000000su= as.vector(simphy.10tax.1000gen.5000000su[,-ncol(simphy.10tax.1000gen.5000000su)])

simphy.10tax.1000gen.10000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-10tax-1000gen-10000000su.csv", header=FALSE))
simphy.10tax.1000gen.10000000su= as.vector(simphy.10tax.1000gen.10000000su[,-ncol(simphy.10tax.1000gen.10000000su)])

simphy.25tax.1000gen.100000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-25tax-1000gen-100000su.csv", header=FALSE))
simphy.25tax.1000gen.100000su= as.vector(simphy.25tax.1000gen.100000su[,-ncol(simphy.25tax.1000gen.100000su)])

simphy.25tax.1000gen.500000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-25tax-1000gen-500000su.csv", header=FALSE))
simphy.25tax.1000gen.500000su= as.vector(simphy.25tax.1000gen.500000su[,-ncol(simphy.25tax.1000gen.500000su)])

simphy.25tax.1000gen.1000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-25tax-1000gen-1000000su.csv", header=FALSE))
simphy.25tax.1000gen.1000000su= as.vector(simphy.25tax.1000gen.1000000su[,-ncol(simphy.25tax.1000gen.1000000su)])

simphy.25tax.1000gen.5000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-25tax-1000gen-5000000su.csv", header=FALSE))
simphy.25tax.1000gen.5000000su= as.vector(simphy.25tax.1000gen.5000000su[,-ncol(simphy.25tax.1000gen.5000000su)])

simphy.25tax.1000gen.10000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-25tax-1000gen-10000000su.csv", header=FALSE))
simphy.25tax.1000gen.10000000su= as.vector(simphy.25tax.1000gen.10000000su[,-ncol(simphy.25tax.1000gen.10000000su)])

simphy.50tax.1000gen.100000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-50tax-1000gen-100000su.csv", header=FALSE))
simphy.50tax.1000gen.100000su= as.vector(simphy.50tax.1000gen.100000su[,-ncol(simphy.50tax.1000gen.100000su)])

simphy.50tax.1000gen.500000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-50tax-1000gen-500000su.csv", header=FALSE))
simphy.50tax.1000gen.500000su= as.vector(simphy.50tax.1000gen.500000su[,-ncol(simphy.50tax.1000gen.500000su)])

simphy.50tax.1000gen.1000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-50tax-1000gen-1000000su.csv", header=FALSE))
simphy.50tax.1000gen.1000000su= as.vector(simphy.50tax.1000gen.1000000su[,-ncol(simphy.50tax.1000gen.1000000su)])

simphy.50tax.1000gen.5000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-50tax-1000gen-5000000su.csv", header=FALSE))
simphy.50tax.1000gen.5000000su= as.vector(simphy.50tax.1000gen.5000000su[,-ncol(simphy.50tax.1000gen.5000000su)])

simphy.50tax.1000gen.10000000su = as.matrix(read.csv("~/Documents/Research Projects/IGL SVD/Branch Lengths/simphy-50tax-1000gen-10000000su.csv", header=FALSE))
simphy.50tax.1000gen.10000000su= as.vector(simphy.50tax.1000gen.10000000su[,-ncol(simphy.50tax.1000gen.10000000su)])

##Merge the dataset
BL=list(simphy.10tax.1000gen.100000su,simphy.10tax.1000gen.500000su,simphy.10tax.1000gen.1000000su,simphy.10tax.1000gen.5000000su,simphy.10tax.1000gen.10000000su,
        simphy.25tax.1000gen.100000su,simphy.25tax.1000gen.500000su,simphy.25tax.1000gen.1000000su,simphy.25tax.1000gen.5000000su,simphy.25tax.1000gen.10000000su,
        simphy.50tax.1000gen.100000su,simphy.50tax.1000gen.500000su,simphy.50tax.1000gen.1000000su,simphy.50tax.1000gen.5000000su,simphy.50tax.1000gen.10000000su)
names(BL)=c("10_100000","10_500000","10_1000000","10_5000000","10_10000000",
            "25_100000","25_500000","25_1000000","25_5000000","25_10000000",
            "50_100000","50_500000","50_1000000","50_5000000","50_10000000")
##Extract the part with same length
BLSL=matrix(ncol=15,nrow=20000)
for (i in 1:15){
    BLSL[,i]=BL[[i]][1:20000]
}
BLSL=as.data.frame(BLSL)
colnames(BLSL)=c("10_100000","10_500000","10_1000000","10_5000000","10_10000000",
                 "25_100000","25_500000","25_1000000","25_5000000","25_10000000",
                 "50_100000","50_500000","50_1000000","50_5000000","50_10000000")
##BoxPlot

library(reshape2)
change1=c("25_100000","25_500000","25_1000000","25_5000000","25_10000000",
          "10_100000","10_500000","10_1000000","10_5000000","10_10000000")
Reshape_a <- melt(BLSL,id.vars = change1)

change2=c("10_100000","10_500000","10_1000000","10_5000000","10_10000000",
          "50_100000","50_500000","50_1000000","50_5000000","50_10000000")
Reshape_b <- melt(BLSL,id.vars = change2)

change3=c("25_100000","25_500000","25_1000000","25_5000000","25_10000000",
          "50_100000","50_500000","50_1000000","50_5000000","50_10000000")
Reshape_c <- melt(BLSL,id.vars = change3)
Reshape=cbind(as.matrix(Reshape_a)[,11:12],as.matrix(Reshape_b)[,11:12],as.matrix(Reshape_c)[,11:12])
Reshape=as.data.frame(Reshape)

BLSLClass=as.data.frame(matrix(nrow=300000,ncol=3))
BLSLClass[,1]=factor(rep(c("50","25","10"),each=100000))
BLSLClass[,2]=factor(rep(rep(c("100000","500000","1000000","5000000","10000000"),each=20000),times=3))
BLSLClass[,3]=c(as.numeric(as.character(Reshape[,2])),as.numeric(as.character(Reshape[,4])),as.numeric(as.character(Reshape[,6])))
options(scipen = 999)
colnames(BLSLClass)=c("Taxa","Substitution","Branch_Length")

##Plotting
library(ggplot2)
ggplot(BLSLClass, aes(x = Taxa, y = Branch_Length, fill = Substitution))+geom_boxplot(alpha = .6,size = 1, outlier.shape = NA)+ scale_y_continuous(limits = c(0, 3))+
    ggtitle("Branch Length Comparison") + theme(plot.title = element_text(size = 25, face = "bold"))+labs(fill="substitution rate")

ggplot(BLSLClass, aes(x = Taxa, y = Branch_Length, fill = Substitution))+geom_boxplot(alpha = .6,size = 1)+
    ggtitle("Branch Length Comparison") + theme(plot.title = element_text(size = 25, face = "bold"))+labs(fill="substitution rate")

write.csv(BLSLClass,file="Brench Length Statistics.csv",row.names=FALSE)
