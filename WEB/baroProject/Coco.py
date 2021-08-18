# gender, age, health = input( ).split(' ')
# print(gender)
# print(age)
# print(health)
# gender = gender.replace('#', '')
# age = age.replace('#', '')
# health = health.replace('#', '')
# print(gender)
# print(age)
# print(health)

FITERLIST=[(1, 'age1_M_B'),(2, 'age1_M_W'),(3, 'age1_M_G'),
                    (4, 'age1_W_B'),(5, 'age1_W_W'),(6, 'age1_W_G'),
                    (7, 'age2_M_B'),(8, 'age2_M_W'),(9, 'age2_M_G'),
                    (10, 'age2_W_B'),(11, 'age2_W_W'),(12, 'age2_W_G'),
                    (13, 'age3_M_B'),(14, 'age3_M_W'),(15, 'age3_M_G'),
                    (16, 'age3_W_B'),(17, 'age3_W_W'),(18, 'age3_W_G'),
                    (19, 'age4_M_B'),(20, 'age4_M_W'),(21, 'age4_M_G'),
                    (22, 'age4_W_B'),(23, 'age4_W_W'),(24, 'age4_W_G'),]
                    
fkey=FITERLIST[6-1][1]
print(fkey)