# 🎬 YouTube Video İndirici

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-red.svg)](https://github.com/yt-dlp/yt-dlp)

Python ile yazılmış kullanımı kolay, güçlü bir YouTube video indirme aracı. `yt-dlp` kütüphanesi kullanılarak geliştirilmiştir.

## ✨ Özellikler

- 🎥 **Yüksek Kalite Video İndirme** - En yüksek kalitede (1080p'ye kadar) video indirme
- 🎵 **MP3 Ses Dönüştürme** - Videoları otomatik olarak MP3 formatına dönüştürme
- 📊 **Video Bilgileri** - Başlık, süre ve görüntülenme sayısı gösterimi
- 📈 **İndirme İlerlemesi** - Gerçek zamanlı ilerleme takibi
- 📁 **Otomatik Klasör Yönetimi** - İndirilen dosyalar için otomatik klasör oluşturma
- 💻 **İki Kullanım Modu** - İnteraktif ve komut satırı modları
- 🚀 **Hızlı ve Güvenilir** - yt-dlp'nin gücü ile hızlı indirme

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- FFmpeg (ses dönüştürme için)

### FFmpeg Kurulumu

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
[FFmpeg resmi sitesinden](https://ffmpeg.org/download.html) indirip PATH'e ekleyin.

## 🚀 Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/ibidi/yt-download.git
cd yt-download
```

2. Gerekli Python kütüphanesini yükleyin:
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

### İnteraktif Mod

Program parametresiz çalıştırıldığında interaktif mod başlar:

```bash
python youtube_downloader.py
```

Program sizden URL isteyecek ve video/ses seçimi yapmanızı sağlayacaktır.

### Komut Satırı Modu

#### Video İndirme

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Sadece Ses İndirme (MP3)

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" audio
```

### Örnekler

```bash
# Video indirme
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# MP3 olarak ses indirme
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" audio
```

## 📁 İndirilen Dosyalar

Tüm dosyalar otomatik olarak `downloads/` klasörüne kaydedilir. Klasör yoksa otomatik oluşturulur.

```
yt-download/
├── downloads/
│   ├── Video Başlığı 1.mp4
│   ├── Video Başlığı 2.mp4
│   └── Ses Dosyası.mp3
├── youtube_downloader.py
├── requirements.txt
└── README.md
```

## 🛠️ Teknik Detaylar

- **Video Kalitesi**: 1080p'ye kadar en iyi kalite (MP4 formatında)
- **Ses Kalitesi**: 192 kbps MP3
- **Kütüphane**: yt-dlp (youtube-dl'in gelişmiş forku)

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyorum! Lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

1. Bu repoyu fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/harika-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Harika özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/harika-ozellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## ⚠️ Yasal Uyarı

Bu araç yalnızca eğitim amaçlıdır. YouTube'un hizmet şartlarına ve telif hakkı yasalarına saygı gösterin. İndirdiğiniz içeriğin kullanım haklarına sahip olduğunuzdan veya uygun izinlere sahip olduğunuzdan emin olun.

## 👨‍💻 Geliştirici

**İhsan Bakı Doğan**
- 🌐 Website: [ihsanbakidogan.com](https://ihsanbakidogan.com)
- 🐦 Twitter/X: [@ihsanbakidogan](https://x.com/ihsanbakidogan)
- 💻 GitHub: [@ibidi](https://github.com/ibidi)

## 🙏 Teşekkürler

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Harika video indirme kütüphanesi
- [FFmpeg](https://ffmpeg.org/) - Video/ses işleme

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
