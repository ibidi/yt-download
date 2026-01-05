# Katkıda Bulunma Rehberi

Öncelikle, bu projeye katkıda bulunmayı düşündüğünüz için teşekkür ederim! 🎉

## Katkı Süreci

### 1. Repo'yu Fork Edin

GitHub'da sağ üstteki "Fork" butonuna tıklayarak projeyi kendi hesabınıza fork edin.

### 2. Fork'unuzu Klonlayın

```bash
git clone https://github.com/ibidi/yt-download.git
cd yt-download
```

> Not: Yukarıdaki komutta `ibidi` yerine kendi GitHub kullanıcı adınızı yazın.

### 3. Upstream Repository'yi Ekleyin

```bash
git remote add upstream https://github.com/ibidi/yt-download.git
```

### 4. Yeni Bir Branch Oluşturun

```bash
git checkout -b feature/harika-ozellik
```

Branch isimlendirme önerileri:
- `feature/yeni-ozellik` - Yeni özellikler için
- `bugfix/hata-ismi` - Hata düzeltmeleri için
- `docs/dokuman-guncelleme` - Dokümantasyon güncellemeleri için
- `refactor/iyilestirme` - Kod iyileştirmeleri için

### 5. Değişikliklerinizi Yapın

- Kodunuzu yazın
- Uygun commit mesajları kullanın
- Kod stiline dikkat edin

### 6. Değişikliklerinizi Test Edin

```bash
python youtube_downloader.py
```

Hem video hem de ses indirme modlarını test edin.

### 7. Commit Yapın

```bash
git add .
git commit -m "feat: harika özellik eklendi"
```

#### Commit Mesajı Formatı

Conventional Commits formatını kullanıyoruz:

- `feat:` - Yeni özellik
- `fix:` - Hata düzeltmesi
- `docs:` - Dokümantasyon değişikliği
- `style:` - Kod formatı (kod anlamını değiştirmeyen)
- `refactor:` - Kod iyileştirmesi
- `test:` - Test ekleme veya düzeltme
- `chore:` - Bakım işleri

Örnekler:
```
feat: playlist indirme özelliği eklendi
fix: video başlığındaki özel karakterler düzeltildi
docs: README'ye kurulum adımları eklendi
refactor: indirme fonksiyonu optimize edildi
```

### 8. Push Edin

```bash
git push origin feature/harika-ozellik
```

### 9. Pull Request Oluşturun

GitHub'da fork'unuza gidin ve "Pull Request" oluşturun. PR açıklamanızda:
- Ne değiştirdiğinizi açıklayın
- Varsa ilgili issue'yu referans verin
- Ekran görüntüleri ekleyin (UI değişiklikleri için)

## Kod Stili

- Python PEP 8 standartlarına uyun
- Anlamlı değişken ve fonksiyon isimleri kullanın
- Fonksiyonlara docstring ekleyin
- Karmaşık kod bloklarına yorum ekleyin

Örnek:
```python
def download_video(url, output_path="downloads"):
    """
    YouTube videosunu indirir
    
    Args:
        url: YouTube video URL'si
        output_path: İndirilen videonun kaydedileceği klasör
    
    Raises:
        Exception: İndirme sırasında hata oluşursa
    """
    # Kod buraya
```

## Ne Tür Katkılar Arıyoruz?

### 🐛 Hata Düzeltmeleri
- Mevcut hataları düzeltin
- Edge case'leri ele alın

### ✨ Yeni Özellikler
- Playlist indirme desteği
- Çoklu video indirme
- Video kalitesi seçimi
- Altyazı indirme
- GUI arayüzü
- Farklı platformlar (Vimeo, Dailymotion, vb.)

### 📚 Dokümantasyon
- README iyileştirmeleri
- Kod yorumları
- Örnek kullanımlar
- Farklı dillerde dokümantasyon

### 🎨 Kullanıcı Deneyimi
- Daha iyi hata mesajları
- İlerleme göstergesi iyileştirmeleri
- Kullanıcı arayüzü geliştirmeleri

## Sorunlar ve Sorular

- 🐛 Bug bulduysanız, issue açın
- 💡 Öneriniz varsa, issue açın
- ❓ Sorunuz varsa, Discussions kullanın

## Davranış Kuralları

- Saygılı ve yapıcı olun
- Açık fikirli olun ve farklı görüşlere saygı gösterin
- Eleştirilerinizi yapıcı tutun
- Diğer katılımcılara yardımcı olun

## İletişim

Sorularınız için:
- 🐦 Twitter: [@ihsanbakidogan](https://x.com/ihsanbakidogan)
- 🌐 Website: [ihsanbakidogan.com](https://ihsanbakidogan.com)
- 💻 GitHub Issues: [Buradan issue açın](https://github.com/ibidi/yt-download/issues)

---

Tekrar teşekkürler! 🙏 Her türlü katkı değerlidir.

