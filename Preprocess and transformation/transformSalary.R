library(stringr)

data <- read.csv("Data.csv")
summary(data)

calculate_experience <- function(job) {
  str_extract(job, "(\\d+(?:-\\d+)?\\+?)\\s*(years?)")
}

n <- length(data$Job_Description)
data$experience <- NA
for (i in 1:n) {
  data$experience[i] <- calculate_experience(data$Job_Description[i])
}


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


for (i in 1:n) {
  data$exp_normailzed[i] <- normalize_exp(data$experience[i])
}


normalize_type <- function(t) {
  type_norm <- as.integer(factor(t))
  type_norm <- scale(type_norm)
  return(type_norm)
}

data$type_norm <- normalize_type(data$Type)
data$Contract_type <- gsub("(r - )?Full-time", "Full-time", data$Contract_type)
data$Contract_type <- gsub("^(?!Full-time$).*", "Contract", data$Contract_type, perl = TRUE)
data$Contract_type_norm <- ifelse(data$Contract_type == "Full-time", 1, 0)
default_salary <- "NA"
data$salary1 <- ifelse(grepl("\\$[0-9,]+ - \\$[0-9,]+", data$Salary), data$Salary, default_salary)
data$salary_min <- as.numeric(gsub("[^0-9.]+", "", sapply(strsplit(data$salary1, "-"), "[", 1)))
data$salary_max <- as.numeric(gsub("[^0-9.]+", "", sapply(strsplit(data$salary1, "-"), "[", 2)))
data$salary_avg <- trunc(data$salary_min + data$salary_max) / 2

hourly_to_yearly <- function(hourly_pay) {
  return(hourly_pay * 40 * 52)
}

n_int_digits <- function(x) {
  result <- floor(log10(abs(x))) + 1
  result[!is.finite(result)] <- 0
  result
}

calculate_sal <- function(sal) {
  li <- list()
  
  for (i in 1:length(as.numeric(sal))) {
    if (is.na(sal[i])) {
      li <- append(li, sal[i])
    } else if (n_int_digits(sal[i]) <= 3) {
      li <- append(li, hourly_to_yearly(sal[i]))
    } else {
      li <- append(li, sal[i])
    }
  }

  return(li)
}

data_raw <- data
data$salary_norm <- calculate_sal(data$salary_avg)

bin_salary <- function(sal) {
  li <- list()
  for (i in 1:length(sal)) {
    if (is.na(sal[i])) {
      li <- append(li, sal[i])
    } else if (sal[i] <= 70000) {
      li <- append(li, "Low")
    } else if (sal[i] > 70000 && sal[i] <= 120000) {
      li <- append(li, "Medium")
    } else if (sal[i] > 120000) {
      li <- append(li, "High")
    }
  }

  return(li)
}

data$label <- bin_salary(data$salary_norm)

df <- data.frame(lapply(data, as.character), stringsAsFactors = FALSE)
write.csv(df, "C:\\Users\\skalako\\Desktop\\dataLabeled.csv", row.names = FALSE)

data$annual_pay <- as.numeric(unlist(data$salary_norm))
data_final <- data[!is.na(data$annual_pay), ]
myp11 <- ggplot(data_final, aes(x = annual_pay, colour = Industry)) +
  geom_bar(size = 2.25)
ggsave("myp11.png", plot = myp11, dpi = 300)

data_final <- data_final[data_final$annual_pay <= 200000, ]

myp12 <- ggplot(data_final, aes(x = annual_pay, colour = Industry)) +
  geom_bar(size = 2.25)
ggsave("myp12.png", plot = myp12, dpi = 300)