import wikipediaapi
import json
import re

# 1. AYARLAR
# Türkçe Wikipedia'yı kullanacağız ('tr')
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='HistoryLensProject/1.0 (senin.mailin@ogrenci.edu.tr)',
    language='tr', 
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

# Senin Listen (Klasör İsimleri)
aranacaklar = [
    'Rumeli Hisarı',
    'Topkapı Sarayı',
    'Kız Kulesi',
    'Sultan Ahmet Camii',
    'Galata Kulesi',
    'Mevlana Müzesi',
    'Anıtkabir',
    'Sumela Manastırı',
    'İzmir Saat Kulesi',
    'Ayasofya Camii',
    'Yerebatan Sarnıcı'
 ]

# 2. YARDIMCI FONKSİYONLAR
def clean_search_term(raw_name):
    """
    'Afrodisias Antik Kenti (Aydın)' -> 'Afrodisias Antik Kenti'
    Parantez içindeki şehir isimlerini siler.
    """
    # Parantez ve içindekileri sil, sondaki boşlukları temizle
    clean_name = re.sub(r'\s*\(.*?\)', '', raw_name).strip()
    return clean_name

def clean_wiki_text(text):
    """Metindeki [1], [2] gibi atıfları ve gereksiz boşlukları temizler."""
    text = re.sub(r'\[\d+\]', '', text)
    return text.strip()

# 3. VERİ ÇEKME DÖNGÜSÜ
dataset = []
bulunamayanlar = []

print(f"Toplam {len(aranacaklar)} tarihi eser taranıyor...\n")

for i, folder_name in enumerate(aranacaklar):
    # 1. İsim Temizliği: (Aydın) kısmını atıyoruz
    search_term = clean_search_term(folder_name)
    
    print(f"[{i+1}] Aranıyor: '{search_term}' ...", end=" ")
    
    page = wiki_wiki.page(search_term)
    
    # Eğer direkt isimle bulamazsa, bazen tam ismi denemek gerekebilir
    # Ama %90 ihtimalle temiz isim çalışacaktır.
    
    if page.exists():
        entry = {
            "id": i,
            "folder_name": folder_name, # Senin klasör ismin (Eşleştirme için kritik)
            "wiki_title": page.title,
            "url": page.fullurl,
            "summary": clean_wiki_text(page.summary),
            "full_text": clean_wiki_text(page.text)
        }
        dataset.append(entry)
        print("✅ BULUNDU")
    else:
        print("❌ BULUNAMADI")
        bulunamayanlar.append(folder_name)

# 4. KAYDETME
output_file = "turkish_landmarks_knowledge_base.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print(f"\n🎉 İşlem Tamamlandı! {len(dataset)} eser kaydedildi.")
if bulunamayanlar:
    print(f"⚠️ Şu eserler Wikipedia'da bulunamadı (Manuel kontrol gerekebilir):")
    for b in bulunamayanlar:
        print(f" - {b}")