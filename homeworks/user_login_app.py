username = "admin"
password = "user123"
counter = 3

while True :
    if (counter > 0):
        a = input("Kullanıcı adınızı giriniz: ")
        b = input("Şifrenizi giriniz: ")

        if (a == username and b == password):
            print("Tebrikler giriş başarılı")
            break

        elif (a != username and b == password):
            print("Kullanıcı adı yanlış! ")
        elif (a == username and b != password):
            print("Şifreniz yanlış")
        elif(a == username and b == password):
            print(" kullanıcı adı yada şifrenizi girmediniz.")

        counter -= 1
    else:
        print("Çok fazla deneme yaptınız çıkış yapılıyor.")