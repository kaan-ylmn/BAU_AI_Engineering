import os
import logging
# Google hata verdiği için Bing modülünü import ediyoruz
from icrawler.builtin import BingImageCrawler

def gorsel_indir(isim_listesi, adet=5):
    """
    Verilen listedeki isimler için Bing üzerinden fotoğraf indirir.
    """
    
    ana_klasor = "indirilen_fotograflar"
    if not os.path.exists(ana_klasor):
        os.makedirs(ana_klasor)

    # Gereksiz logları kapatarak terminali temiz tutalım
    logging.getLogger("icrawler").setLevel(logging.WARNING)

    for isim in isim_listesi:
        print(f"\n--- '{isim}' aranıyor (Bing)... ---")
        
        kayit_yolu = os.path.join(ana_klasor, isim)

        # BingImageCrawler kullanıyoruz
        crawler = BingImageCrawler(
            downloader_threads=4, # İndirme hızı
            storage={'root_dir': kayit_yolu}
        )

        # İndirmeyi başlat
        crawler.crawl(keyword=isim, max_num=adet)
        
        print(f"-> '{isim}' tamamlandı.")

aranacaklar = [
    "Afrodisias Antik Kenti (Aydın)",
    "Akdamar Kilisesi (Van)",
    "Alanya Kalesi (Antalya)",
    "Alman Çeşmesi (İstanbul)",
    "Amasya Kral Kaya Mezarları (Amasya)",
    "Ani Harabeleri (Kars)",
    "Anıtkabir (Ankara)",
    "Ankara Kalesi (Ankara)",
    "Aspendos Antik Tiyatrosu (Antalya)",
    "Assos Antik Kenti (Çanakkale)",
    "Balıklıgöl (Şanlıurfa)",
    "Bandırma Vapuru (Samsun)",
    "Bergama Asklepion (İzmir)",
    "Bodrum Kalesi (Muğla)",
    "Bursa Ulu Camii (Bursa)",
    "Celsus Kütüphanesi (İzmir)",
    "Cumalıkızık Evleri (Bursa)",
    "Cunda Taksiyarhis Kilisesi (Balıkesir)",
    "Çanakkale Şehitler Abidesi (Çanakkale)",
    "Çatalhöyük Neolitik Kenti (Konya)",
    "Çifte Minareli Medrese (Erzurum)",
    "Didyma Apollon Tapınağı (Aydın)",
    "Divriği Ulu Camii (Sivas)",
    "Efes Antik Kenti (İzmir)",
    "Fatih Camii (İstanbul)",
    "Galata Kulesi (İstanbul)",
    "Gordion Antik Kenti (Ankara)",
    "Göbeklitepe (Şanlıurfa)",
    "Göreme Açık Hava Müzesi (Nevşehir)",
    "Hadrian Kapısı (Antalya)",
    "Ihlara Vadisi (Aksaray)",
    "İshak Paşa Sarayı (Ağrı)",
    "İzmir Saat Kulesi (İzmir)",
    "İznik Ayasofya Camii (Bursa)",
    "Kapalıçarşı (İstanbul)",
    "Kaunos Kaya Mezarları (Muğla)",
    "Kayaköy (Muğla)",
    "Kızkalesi (Mersin)",
    "Knidos Antik Kenti (Muğla)",
    "Koza Han (Bursa)",
    "Mardin Evleri (Mardin)",
    "Mevlana Müzesi (Konya)",
    "Nemrut Dağı (Adıyaman)",
    "Olympos Antik Kenti (Antalya)",
    "Rumeli Hisarı (İstanbul)",
    "Safranbolu Evleri (Karabük)",
    "Selimiye Camii (Edirne)",
    "St. Antuan Kilisesi (İstanbul)",
    "St. Pierre Kilisesi (Hatay)",
    "Sultanhanı Kervansarayı (Aksaray)",
    "Sümela Manastırı (Trabzon)",
    "Taşköprü (Adana)",
    "Topkapı Sarayı (İstanbul)",
    "Varda Köprüsü (Adana)",
    "Yerebatan Sarnıcı (İstanbul)",
    "Yeşil Türbe (Bursa)"
]
# Fonksiyonu çalıştır
gorsel_indir(aranacaklar, adet=30)