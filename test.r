library(tidyverse)
library(mtcars)

# Boxplot of mpg by class
mtcars %>%
  ggplot(aes(class, mpg)) +
  geom_boxplot()

