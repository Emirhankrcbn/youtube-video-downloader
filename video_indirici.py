import yt_dlp

def video_indir(url):
    # İndirme ayarları: En iyi kaliteyi seç ve videonun orijinal adıyla kaydet
    ayarlar = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' 
    }
    
    print("Videonuz aranıyor, indirme işlemi birazdan başlayacak...")
    
    try:
        # İndirme işlemini başlatan kısım
        with yt_dlp.YoutubeDL(ayarlar) as ydl:
            ydl.download([url])
        print("Tebrikler! İndirme başarıyla tamamlandı.")
    except Exception as hata:
        print(f"Maalesef bir hata oluştu: {hata}")

# ---------------------------------------------------------
# Kullanım Kısmı:
# Aşağıdaki tırnak işaretleri içine indirmek istediğin videonun linkini yapıştır.

video_linki = "https://www.youtube.com/shorts/LpXhZctFCt8"

video_indir(video_linki)