DOSYA_ADI = "görevler.txt"

def dosyadan_oku():
    try:
        with open(DOSYA_ADI, "r") as dosya:
            return [satir.strip() for satir in dosya.readlines()]
    except FileNotFoundError:
        return []

def dosyaya_yaz(gorevler):
    with open(DOSYA_ADI, "w") as dosya:
        for gorev in gorevler:
            dosya.write(gorev + "\n")

def gorev_ekle():
    gorev = input("Eklenecek görev: ")
    gorevler.append(gorev)
    dosyaya_yaz(gorevler)
    print(f"'{gorev}' görevi eklendi.")

def gorevleri_listele():
    if not gorevler:
        print("Görev yok.")
    else:
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")

def gorev_tamamla():
    gorevleri_listele()
    try:
        secim = int(input("Tamamlanan görevin numarasını seçin: ")) - 1
        gorevler[secim] += " (Tamamlandı)"
        dosyaya_yaz(gorevler)
        print("Görev tamamlandı olarak işaretlendi.")
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

def gorev_sil():
    gorevleri_listele()
    try:
        secim = int(input("Silmek istediğiniz görevin numarasını seçin: ")) - 1
        silinen = gorevler.pop(secim)
        dosyaya_yaz(gorevler)
        print(f"'{silinen}' görevi silindi.")
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

gorevler = dosyadan_oku()

while True:
    print("\nYapılacaklar Listesi:")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamlandı Olarak İşaretle")
    print("4. Görev Sil")
    print("5. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gorev_ekle()
    elif secim == "2":
        gorevleri_listele()
    elif secim == "3":
        gorev_tamamla()
    elif secim == "4":
        gorev_sil()
    elif secim == "5":
        print("Uygulama kapatılıyor...")
        break
    else:
        print("Geçersiz seçim!")