str(Water_Quality_Testing) #similar a un .info() en Pandas

mean(Water_Quality_Testing$pH)
quantile(Water_Quality_Testing$pH, 0.25)
quantile(Water_Quality_Testing$pH)
median((Water_Quality_Testing$pH))
table(Water_Quality_Testing$pH)
var(Water_Quality_Testing$pH)
sd(Water_Quality_Testing$pH)
sqrt(var(Water_Quality_Testing$pH))
range(Water_Quality_Testing$pH)
max(Water_Quality_Testing$pH) - min(Water_Quality_Testing$pH)
IQR(Water_Quality_Testing$pH)

summary((Water_Quality_Testing$pH)) #similar a un .describe() en Pandas

lapply(Water_Quality_Testing, mean) #promedio de todos los campos del dataset
tapply(Water_Quality_Testing$pH, Water_Quality_Testing$`Temperature (°C)`> 22, mean) #promedio sobre un campo que cumple una determinada condicion
