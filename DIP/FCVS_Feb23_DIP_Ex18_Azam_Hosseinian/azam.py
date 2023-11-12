# برنامه برای شمارش تکرار هر کاراکتر در یک متن

def char_frequency(str1):
    # ایجاد یک دیکشنری برای نگهداری تعداد تکرار هر کاراکتر
    dict = {}
    
    # حلقه برای بررسی هر کاراکتر
    for n in str1:
        # چک کردن اینکه کاراکتر فاصله نباشد
        if n != ' ':
            keys = dict.keys()
            # اگر کاراکتر قبلا در دیکشنری وجود داشت, افزایش تعداد تکرار
            if n in keys:
                dict[n] += 1
            # اگر کاراکتر جدید است, اضافه کردن به دیکشنری
            else:
                dict[n] = 1
    return dict

# دریافت متن از کاربر
user_input = input('لطفا یک متن انگلیسی وارد کنید: ')

# چاپ تعداد تکرار هر کاراکتر
frequency = char_frequency(user_input)
for char, count in frequency.items():
    print(f'کاراکتر "{char}" {count} بار تکرار شده است.')
