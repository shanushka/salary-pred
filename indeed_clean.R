data<- read.csv("Indeed_JD_SoftwareDeveloper.csv")
summary(data)
calculate_experience <- function(job){
  str_extract(job, '(\\d+(?:-\\d+)?\\+?)\\s*(years?)')
}
data$experience <- NA
data$experience<- calculate_experience(data$Job_Description)


normalize_exp <- function(exp) {
  exp_value <- as.numeric(gsub("[^0-9\\.]", "", exp))
  if (is.na(exp_value)) {
    warning("Unable to extract numeric value from experience string")
    return(NA)
  }
  
  min_exp <- 0
  max_exp <- 10
  
  exp_norm <- (exp_value - min_exp) / (max_exp - min_exp)
  return(exp_norm)
}

n = length(data$Job_Description)
for(i in 1:n){ data$exp_normailzed[i] <- normalize_exp(data$experience[i])}
  
  
  normalize_type <- function(t)
  {
    type_norm <- as.integer(factor(t))
    type_norm <- scale(type_norm)
    return (type_norm)
  }
  
data$type_norm <- normalize_type(data$Type)
data$Contract_type <- gsub("(r - )?Full-time", "Full-time", data$Contract_type)
data$Contract_type <- gsub("^(?!Full-time$).*", "Contract",data$Contract_type , perl = TRUE)
data$Contract_type_norm <- ifelse(data$Contract_type == "Full-time", 1, 0)
default_salary <- "NA"
data$salary1 <- ifelse(grepl("\\$[0-9,]+ - \\$[0-9,]+", data$Salary), data$Salary, default_salary)
data$salary_min <- as.numeric(gsub("[^0-9.]+", "", sapply(strsplit(data$salary1, "-"), "[", 1)))
data$salary_max <- as.numeric(gsub("[^0-9.]+", "", sapply(strsplit(data$salary1, "-"), "[", 2)))
data$salary_norm <- trunc(data$salary_min + data$salary_max)/2

#data$salary_norm1 <- scale(data$salary_min + data$salary_max)/2

#hourly_to_yearly <- function(hourly_pay) {
#      pay <- hourly_pay * 40 *52
#      return(pay)
#}
#yearly_to_yearly <- function(hourly_pay) {
#  pay <- hourly_pay
#  return(pay)
#}

#calculate_sal<- function(sal)
#{
 # if(length(sal) < 5)
  #  cal_pay<-hourly_to_yearly(sal)
  #else
   # cal_pay<-yearly_to_yearly(sal)
  
#  return (cal_pay)
 # }
#data$salary_norm12 <- hourly_to_yearly(as.numeric(data$salary_norm))
#if (any(is.na(data$salary_norm1))) {
 # warning("Unable to extract numeric value from experience string")
  #data$salary_norm1[is.na(data$salary_norm1)] <- NA
#}
#data$salary_norm1 <- ifelse(as.numeric(data$salary_norm) < 5, 
 #                           hourly_to_yearly(as.numeric(data$salary_norm)), 
#                            as.numeric(data$salary_norm))


