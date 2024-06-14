# 1-dars
# print(5**4)
# print(22%4)
# print("kvadrat yuzi",125*125)
# print("kvadrat yuzi",125*4)
# print('doira yuzi',3.14*(6*6))



# 2-dars
# kocha="Al-Xorazmiy"
# mahalla="Tinchlik"
# tuman="Urganch"
# viloyat="Xorazm"
# print(kocha,"ko'chasi,",mahalla,"mahallasi,",tuman,"tumani,",viloyat,"viloyati,")

# kocha=input("Kochani kiriting")
# mahalla=input("Mahallani kiriting")
# tuman=input("Tumanni kiriting")
# viloyat=input("Viloyatni kiriting")
# print(kocha,"ko'chasi,"+mahalla,"mahallasi,"+tuman,"tumani,"+viloyat,"viloyati")

# kocha=input("Kochani kiriting")
# mahalla=input("Mahallani kiriting")
# tuman=input("Tumanni kiriting")
# viloyat=input("Viloyatni kiriting")
# print(kocha,"ko'chasi,"+'\n'+mahalla,"mahallasi,"+'\n'+tuman,"tumani,"+'\n'+viloyat,"viloyati")

# kocha=input("Kochani kiriting")
# mahalla=input("Mahallani kiriting")
# tuman=input("Tumanni kiriting")
# viloyat=input("Viloyatni kiriting")
# manzil=kocha,mahalla,tuman,viloyat
# print(f"Adress {manzil}")
#
# kocha=input("Kochani kiriting")
# mahalla=input("Mahallani kiriting")
# tuman=input("Tumanni kiriting")
# viloyat=input("Viloyatni kiriting")
# manzil=kocha+mahalla+tuman+viloyat
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
#
# a=input("Yoshingizni kiriting:")
# b=2024-int(a)
# print("Yilingiz:" + str(b))
#
# a=input("1-sonni kiriting:")
# b=input("2-sonni kiriting:")
# x=int(a)+int(b)
# y=int(a)-int(b)
# z=int(a)*int(b)
# d=int(a)/int(b)
# print("Yig`indisi:" +str(x),'\nAyirmasi:' + str(y),"\nKo`paytmasi:" + str(z),"\nBo`linmasi:"+ str(d))

# 3-dars
# ismlar = ['ali', 'vali', 'soli']
# yigitlar = "Assalomu aleykum, " + ismlar[0].title()
# print(yigitlar)
# yigitlar = "Nerda yashab yurbsilar, " + ismlar[1].title()
# print(yigitlar)
# yigitlar = "Akang ishdami, " + ismlar[2].title()
# print(yigitlar)
#
# sonlar=[1,-2,3,4.5]
# sonlar[0]=2
# sonlar[1]=-6
# sonlar[2]=8
# sonlar[3]=6.3
# print(sonlar)
#
# t_shaxslar=['Amir Temur']
# z_shaxslar=['Abror Muxtor aliy']
# print(t_shaxslar)
# print(z_shaxslar)
#
# friends=[]
# friends.append('Anvar',)
# friends.append('Lochin')
# friends.append('Yoqub')
# print(friends)
#
# friends=['Anvar', 'Lochin', 'Yoqub','Doniyor','Asadbek']
# friends.remove('Yoqub')
# friends.remove('Anvar')
# print(friends)
#
# friends=['Anvar', 'Lochin', 'Yoqub','Doniyor','Asadbek']
# friends.insert(0,'Jasur')
# friends.insert(4,'Islom')
# friends.insert(7,'Rasul')
# print(friends)

# 4-dars
# ismlar=['ali','vali','akbar','abror','asror','tohir']
# for ism in ismlar:
#     print(f"Assalomu alaykum {ism}")
# print("Xush kelibsizlar")
#
# sonlar = list(range(11,101,2))
# sonlar_kubi = []
# for son in sonlar:
#     sonlar_kubi.append(son**3)
# # print(sonlar)
# print(sonlar_kubi)

# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)
#
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)

# 5-dars

yangi_cars=['tayota','mazda','hyundai','gm','kia']
for yangi_car in yangi_cars:
    if yangi_car == 'gm':
        print(yangi_car.upper())
    else:
        print(yangi_car.title())

yangi_cars=['tayota','mazda','hyundai','gm','kia']
for yangi_car in yangi_cars:
    if yangi_car != 'gm':
        print(yangi_car.title())
    else:
        print(yangi_car.upper())

ism = input('Login ismingiz kiriting?\n')
if ism.lower() !='Admin':
   print(f"Uzr,{ism} biz Adminni kutyapmiz.")
else:
   print("Xush kelibsiz,Admin.Foydalanuvchilar royhatini koraszmi?")

son = int(input('Istalgan ikkita son kiriting?'))
if son==4545:
    print("Sonlar teng!")
else:
    print("Sonlar teng emas!")

son = int(input("Sonni kiriting!"))
if son > 0:
    print('Musbat son')
else:
    print('Manfiy son')

son = int(input("Sonni kiriting!"))
if son >= 0:
    # ildiz = math.sqrt(son)
    print(son**2)
else:
    print('Musbat son kiriting')
















































