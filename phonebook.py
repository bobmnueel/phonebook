import os
index = 1
phonebook = {} 

#modul create/insert
def tambahKontak(name, phone):
    file = open ("phonebook.txt", "a")
    file.write(f"{index : <1}{'. ' : <1}{'nama: ' : <2}{name : <25}{'nomor: ' : <5}{phone : >1}\n")
    file.close
    print("\nKontak", name, "Dengan Nomor", phone, "Telah Ditambahkan !\n")
    

#modul read
def tampilKontak():
    if phonebook:
        f = open("phonebook.txt", "r")
        print(f.read())
    else:
        print("\nTidak Ada Kontak Tersedia !\n")
        


#modul update
def updateKontak(name, phonebook):
    pilih = input("Apakah Ingin Mengedit Nama Atau Nomor?\n1. Nama\n2. Nomor\nPilihan: ")
    if pilih == 1:
        with open("phonebook.txt",'r') as file:
            isiFile = file.read()

        baru = input ("Masukan Nama Yang Baru : ")
        isiFile = isiFile.replace(name,baru)

        with open("phonebook.txt",'w') as file:
            file.write(isiFile)
    elif pilih == 2:
        with open("phonebook.txt",'r') as file:
            isiFile = file.read()

        baru = input("masukan nomor yang baru : ")
        isiFile = isiFile.replace(phone,baru)

        with open("phonebook.txt",'w') as file:
            file.write(isiFile)


#modul delete
def hapusKontak(name):
    hapus = name
    with open("phonebook.txt",'r') as file:
        cari = file.readlines()
    
    with open("phonebook.txt",'w') as file:
        for line in cari:
            if not line.startswith(hapus):
                file.write(line)


#modul search
def cariKontak(name):
    cek = False
    with open("phonebook.txt",'r') as file:
        for line in file:
            if name in line:
                print(line)
                cek = True
    
    if cek != True:
        print("Kontak", name, "Tidak Ada\n")


#ALGORITMA
while True:

    print("=== PHONE BOOK ===\n")
    print("1. create/insert contact")
    print("2. read contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. search contact")
    print("6. EXIT")
    
    choice = input("\nMasukkan Input   : ")
    
    if choice == "1":
        name = input("Masukkan Nama    : ")
        phone = input("Masukkan Nomer   : ")
        phonebook[name] = [phone]
        tambahKontak(name, phone)
        index = index + 1

    elif choice == "2":
        tampilKontak()
            
    elif choice == "3":
        name = input("Masukkan Nama     : ")
        updateKontak(name,phonebook)
            
    elif choice == "4":
        name = input("Masukkan Nama     : ")
        hapusKontak(name)
  
    elif choice == "5":
        name = input("Masukkan Nama    : ")
        cariKontak(name)
    
    elif choice == "6":
        print("=== BYE ===")
        break
        
    else:
        print("Input Tidak Valid ")