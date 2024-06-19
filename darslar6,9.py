# 6-dars
davlat_poytaxt = {
    "O'zbekiston": "Toshkent",
    "Rossiya": "Moskva",
    "AQSh": "Vashington",
    "Xitoy": "Pekin",
    "Yaponiya": "Tokio",
}
davlat = sorted(davlat_poytaxt.keys())
print("Davlatlar:")
for davlat in davlat:
    print(davlat)

foydalanuvchi_davlati = input("\nDavlat nomini kiriting: ")
if foydalanuvchi_davlati in davlat_poytaxt:
    print(f"{foydalanuvchi_davlati}ning poytaxti {davlat_poytaxt[foydalanuvchi_davlati]}")
else:
    print("Bizda bunday ma'lumot yo'q")


buyurtmalar=[]
for i in range(3):
    menu = {
        "Palov": 25000,
        "Shashlik": 12000,
        "Somsa": 10000,
        "Gamburger": 10000,
        "Lavash": 22000,
        "Pitsa": 50000,
        "Cake": 20000,
}
buyurtmalar=[]
for i in range(3):
    buyurtma=input(f"{i+1}-taom kiriting")
    buyurtmalar.append(buyurtma)
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtmalar.title()} {menu[buyurtma]} som")
    else:
        print("Kechirasz bizda buyurtma yoq")


# 7-dars
friends_movies={
    "Alin":['Poyga','Tezlik','Uchuvchi'],
    "Vali":["Yo'lchi",'Dengizchi',"Suv malikasi"],
    "Hasan":['Hovli','Chuqur','Ichkarida'],
    "Husan":['Hukmdor Usmon','Qosem','Muhtasham']
}

countries = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "hudud": "448978 kv.km",
        "aholi": "33000000",
        "pul birligi": "so'm"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "hudud": "17098246 kv.km",
        "aholi": "144000000",
        "pul birligi": "rubl"
    },
    "AQSH": {
        "poytaxt": "Vashington",
        "hudud": "9631418 kv.km",
        "aholi": "327000000",
        "pul birligi": "dollar"
    },
    "Malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hudud": "329750 kv.km",
        "aholi": "25000000",
        "pul birligi": "rinngit"
    }
}

def get_country_info(country_name):
    info = countries.get(country_name)
    if info:
        print(f"{country_name}ning poytaxti {info['poytaxt']}")
        print(f"Hududi: {info['hudud']}")
        print(f"Aholisi: {info['aholi']}")
        print(f"Pul birligi: {info['pul birligi']}")
    else:
        print("Bizda bu davlat haqida ma'lumot mavjud emas")

def get_favorite_movies(friend_name):
    movies = friends_movies.get(friend_name)
    if movies:
        print(f"{friend_name}ning sevimli kinolari:")
        for movie in movies:
            print(movie)
    else:
        print(f"{friend_name} haqida ma'lumot mavjud emas")

# 8-dars
def tugilgan_yil():
    ism = input("Ismingiz nima? ")
    yosh = int(input("Yoshingiz nechida? "))
    hozirgi_yil = 2024
    tugilgan_yil = hozirgi_yil - yosh
    print(f"{ism}, siz {tugilgan_yil}-yilda tug'ilgansiz.")



def kvadrati_va_kubi():
    son = int(input("Iltimos, biror son kiriting: "))
    kvadrati = son** 2
    kubi = son ** 3
    print(f"{son} ning kvadrati {kvadrati}, kubi esa {kubi}.")


def juft_yoki_toq():
    son = int(input("Iltimos, biror son kiriting: "))
    if number % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")


def son(x=None, y=2):
    if x is None:
        x = int(input("Birinchi sonni kiriting: "))
    y = int(input("Ikkinchi sonni kiriting: ")) if y == 2 else y
    if x > y:
        print(f"Katta son: {x}")
    elif y > x:
        print(f"Katta son: {y}")
    else:
        print("Sonlar teng.")


def toplam():
    son = int(input("Iltimos, biror son kiriting: "))
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")
        else:
            print(f"{son} {i} ga qoldiqsiz bo'linmaydi.")

# 9-dars
def foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joy,email,telefon):
    foydalanuvchi = {
        'ism': ism,
        'familiya': familiya,
        'tugilgan_yil': tugilgan_yil,
        'tugilgan_joy': tugilgan_joy
    }
    if email:
        foydalanuvchi['email'] = email
    if telefon:
        foydalanuvchi['telefon'] = telefon

    return foydalanuvchi

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
email = input("Email manzilingizni kiriting: ")
telefon = input("Telefon raqamingizni kiriting: ")

foydalanuvchi_malumotlari = foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon)

print("Foydalanuvchi ma'lumotlari:")
print(foydalanuvchi_malumotlari)


mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(foydalanuvchi_mijoz(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for foydalanuvchi_mijoz in mijozlar:
    print(f"{foydalanuvchi_mijoz['ism'].title()} {foydalanuvchi_mijoz['familiya'].title()},"
          f"{foydalanuvchi_mijoz['yoshi']} yoshda, telefoni: {foydalanuvchi_mijoz['telefon']}")



def kattasi(x,y,z):
    mx  = x
    if y>=mx:
        mx = y
    if z>=mx:
        mx = z
    return mx
print(kattasi(20,30,-5))



def aylana_r(radius,p=3.14):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*p,
              "yuza":p*radius**2}
    return aylana

print(aylana_r(15))


def tub_sonlar_t(mn, mx):
    tub_sonlar = []
    for n in range(mn, mx + 1):
        tub = True
        if (n == 1):
            tub = False
        elif (n == 2):
            tub = True
        else:
            for x in range(2, n):
                if (n % x == 0):
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar


print(tub_sonlar_t(1, 100))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(100))
