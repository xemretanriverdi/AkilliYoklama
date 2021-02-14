import cv2
import time
dosya = open("yoklama.txt","a")#a her var olana ekler
dershafta=1
ogrenciID = 0
DersID=0



def yuzTanima():
    i=0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    a= False
    print("5 saniye bekleyin")
    while (True and i<5):
        _, img = cap.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)
        cv2.imshow('img',img) 
        
        for (x,y,w,h) in faces:
        
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
            a= True
            break
    
        time.sleep(1)
        i += 1
        k=cv2.waitKey(30) & 0xff
        if k==27:
            break
        
    return a

def sistemeYukle(ogrenciId):
    time2=time.strftime("%H %M")
    if(yuzTanima()):
        output=str(ogrenciId)+" "+str(DersId)+" "+str(dershafta)+" " +str(1)+" " +str(time2)+"\n"
 
    else:
        output=str(ogrenciId)+" "+str(DersId)+" "+str(dershafta)+" " +str(0)+"\n"

    dosya.write(output)
    dosya.close()

def dersBaslangici():
    dersID= int(input("Baslamak istediginiz Ders idsini giriniz giriniz "))
    while(dersID<100 or dersID>104):
        print("Boyle bir dersimiz bulunmamaktadır..\n Fakülte Derslerimiz:\n100\n101\n102\n103\n104")
        dersID = int(input("Baslamak istediginiz Ders idsini Tekrar giriniz: "))
    return dersID

def dersSonlandir(id):
    print("{} nolu ders sonlanmistir".format(id))
    dershafta=+1

def yoklama():
    ogrenciID= int(input("Yüz taraması yapılacak ogrenci no "))
    while(ogrenciID<10000 or ogrenciID>10002):
        print("Boyle numaraya sahip ogrencimiz bulunmamaktadır..\n")
        ogrenciID = int(input(" Tekrar deneyiniz: "))
    return ogrenciID

DersId = (dersBaslangici())
sistemeYukle(yoklama())


sonuc =input("Yeni bir yoklama almak istiyorsanız Yes: \nDersi sonlandırmak istiyorsanız No tusuna basın: ")

while(sonuc != ("Yes" and "No")):
    sonuc =input("Yanlıs cevap verdiniz.........\nYeni bir yoklama almak istiyorsanız Yes \nDersi sonlandırmak istiyorsanız No tusuna basın")

if(sonuc=="Yes"):
    sistemeYukle(yoklama())
10
if(sonuc=="No"):

    dersSonlandir(DersId)






