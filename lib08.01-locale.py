'''
locale 模块

locale 模块提供了 C 本地化( localization )函数的接口.

同时提供相关函数, 实现基于当前 locale 设置的数字, 字符串转换.

(而 int , float , 以及 string 模块中的相关转换函数不受 locale 设置的影响.)
'''
import locale

print('locale', '=>', locale.setlocale(locale.LC_ALL,''))

value = 4711
print(locale.format('%d',value,1),'==','',end='')
print(locale.atoi(locale.format('%d',value,1)))

value = 47.11
print(locale.format('%f',value,1),'==','',end='')
print(locale.atof(locale.format('%f',value,1)))

info = locale.localeconv()
print(info)
print(info['int_curr_symbol'])
'''
locale => Chinese (Simplified)_People's Republic of China.936
4,711 == 4711
47.110000 == 47.11
{'frac_digits': 2, 'p_sep_by_space': 0, 'n_sign_posn': 4, 'mon_decimal_point': '.', 'int_frac_digits': 2, 'currency_symbol': '￥', 'int_curr_symbol': 'CNY', 'positive_sign': '', 'mon_thousands_sep': ',', 'thousands_sep': ',', 'negative_sign': '-', 'decimal_point': '.', 'p_sign_posn': 4, 'n_cs_precedes': 1, 'grouping': [3, 0], 'p_cs_precedes': 1, 'mon_grouping': [3, 0], 'n_sep_by_space': 0}
CNY
'''




# 使用 locale 模块获得当前平台 locale 设置
import locale

language, encoding = locale.getdefaultlocale()
print('language:',language)
print('encoding:',encoding)



