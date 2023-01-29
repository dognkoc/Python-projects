from tkinter import messagebox as msgb
from tkinter import *
import sqlite3
# from PIL import ImageTk, Image  


window = Tk()
window.title("Kütüphane Verilerim")
window.geometry("400x300")
window.resizable(FALSE,FALSE)

etiket = Label(text="Veri Kontrol Sistem Ekranı",font="Stencil")
etiket.place(x=80,y=20)





data = sqlite3.connect("kutuphane.db")
cursor = data.cursor()
table = "CREATE TABLE IF NOT EXISTS kütüphane (isim TEXT, yayınevi TEXT, sayfa TEXT)"
cursor.execute(table)




def veri_gir():
    global isim,yayınevi,sayfa, cursor, data
    top = Toplevel()
    top.geometry("300x200")
    top.resizable(FALSE,FALSE)

    etiket = Label(top,text="""Kütüphane Kitap Kayıt Otomasyonu""",font="Arial 10 bold")
    etiket.grid(row=0,column=1)

    data.commit()

    kitap_adı = Label(top,text="Kitap Adı: ")
    kitap_adı.grid(row=2,column=0)

    kitap_adı_input = Entry(top,width=20)
    kitap_adı_input.grid(row=2,column=1)


    kitap_yayınevi = Label(top,text="Yayınevi: ")
    kitap_yayınevi.grid(row=3,column=0)

    kitap_yayınevi_input = Entry(top,width=20)
    kitap_yayınevi_input.grid(row=3,column=1)


    kitap_sayfa = Label(top,text="Sayfa: ")
    kitap_sayfa.grid(row=4,column=0)

    kitap_sayfa_input = Entry(top,width=20)
    kitap_sayfa_input.grid(row=4,column=1)

    
    
    

    def kaydet():
        isim = kitap_adı_input.get()
        yayınevi = kitap_yayınevi_input.get()
        sayfa = kitap_sayfa_input.get()
        cursor.execute("INSERT INTO kütüphane VALUES (?,?,?)",(isim,yayınevi,sayfa))
        data.commit()
        kitap_adı_input.delete(0,END)
        kitap_sayfa_input.delete(0,END)
        kitap_yayınevi_input.delete(0,END)

        def showMessage(message, timeout=2500):
            root = Tk()
            root.withdraw()
            try:
                root.after(timeout, root.destroy)
                msgb.showinfo('Info', message, master=root)
                
            except:
                pass
        showMessage("kayıt yapıldı")


    kaydet = Button(top,text="Kaydet",width=18,command=kaydet)
    kaydet.grid(row=6,column=1)

    data.commit()

    kapat = Button(top,text="Çıkış",width=18,command=top.destroy)
    kapat.grid(row=7,column=1)
    
gir = Button(window,text="Veri Girişi",width=10,height=3,command=veri_gir)
gir.place(x=20,y=120)








def tum_veri_goster():

    

    cursor.execute("SELECT COUNT (*) FROM kütüphane")
    rowcount = cursor.fetchone()[0]
    
    a = f"Kütüphanenizde kayıtlı {rowcount} sayıda kitap gözükmektedir."
    msgb.showinfo(title="Kitap Sayısı",message = a)
    


veri_goster = Button(window,text="Kitap Sayısı?",width=10,height=3,command=tum_veri_goster)
veri_goster.place(x=300,y=120)




def kitap_bilgileri():
    top2 = Toplevel()
    top2.title("Kitap Adıyla Bilgileri Sunma Paneli")
    top2.geometry("300x100")
    
    
    kitap_adı = Label(top2,text="Aramak İstediğiniz Kitap: ")
    kitap_adı.place(x=80,y=0)
    

    kitap_adı_input = Entry(top2)
    kitap_adı_input.place(x=80,y=30)

    

    

    
    def goster():
        ad = kitap_adı_input.get()
        cursor.execute("SELECT * FROM kütüphane WHERE isim=(?)",(ad,))
        liste = cursor.fetchall()
        liste2 = []
        for i in liste:
            info = f"Kitabın adı: {i[0]}\nKitabın Yayınevi: {i[1]}\nKitabın sayfa sayısı: {i[2]}"
        msgb.showinfo(title=ad,message=info) 
        
    bilgileri_goster = Button(top2,text="Bilgileri Göster",command=goster)
    bilgileri_goster.place(x=80,y=60)
    

    



bilgileri_Ara = Button(window,text="Kitap Bilgileri",width=10,height=3,command=kitap_bilgileri)
bilgileri_Ara.place(x=160,y=120)





mainloop()
data.close()