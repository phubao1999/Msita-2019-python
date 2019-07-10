import random

hi_list = ['Hello', 'Hi', 'Xin Chao']
name = 'Hùng'
gender = 'anh'
current = ['Heo', 2019]
birthday = 1994

con_giap_list = ['Chuột', 'Trâu', 'Hổ', 'Mèo', 'Rồng',
                 'Rắn', 'Ngựa', 'Dê', 'Khỉ', 'Gà', 'Chó', 'Heo']

r_hi = random.choice(hi_list)
calc_age_tay = (current[1] - birthday)
age_tay = '%s Tuổi' % calc_age_tay
calc_age_ta = con_giap_list[(
    con_giap_list.index(current[0]) - calc_age_tay) % 12]
age_ta = 'Tuổi Con %s' % calc_age_ta
r_age = random.choice([age_tay, age_ta])

say_hello = '%s %s %s, %s %s à.' % (r_hi, gender, name, gender, r_age)

print(say_hello)
print(age_tay)
