#!/usr/bin/env python3
"""
YouTube Video İndirme Aracı
yt-dlp kütüphanesi kullanarak YouTube videolarını indirir
"""

import yt_dlp
import sys
import os


def download_video(url, output_path="downloads"):
    """
    YouTube videosunu indirir
    
    Args:
        url: YouTube video URL'si
        output_path: İndirilen videonun kaydedileceği klasör
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'quiet': False,
            'no_warnings': False,
        }
        
        print(f"Video indiriliyor: {url}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Başlık: {info['title']}")
            print(f"Süre: {info['duration']} saniye")
            print(f"Görüntülenme: {info['view_count']:,}\n")
            
            ydl.download([url])
        
        print(f"\n✓ Video başarıyla indirildi!")
        
    except Exception as e:
        print(f"\n✗ Hata oluştu: {str(e)}")
        sys.exit(1)


def download_audio(url, output_path="downloads"):
    """
    YouTube videosundan sadece ses indirir
    
    Args:
        url: YouTube video URL'si
        output_path: İndirilen sesin kaydedileceği klasör
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'no_warnings': False,
        }
        
        print(f"Ses indiriliyor: {url}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Başlık: {info['title']}\n")
            
            ydl.download([url])
        
        print(f"\n✓ Ses başarıyla indirildi!")
        
    except Exception as e:
        print(f"\n✗ Hata oluştu: {str(e)}")
        sys.exit(1)


def main():
    """Ana program"""
    print("=" * 50)
    print("YouTube Video İndirme Aracı")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
        mode = sys.argv[2] if len(sys.argv) > 2 else "video"
    else:
        url = input("\nYouTube video URL'sini girin: ").strip()
        print("\nİndirme modu:")
        print("1. Video (varsayılan)")
        print("2. Sadece ses (MP3)")
        choice = input("Seçiminiz (1/2): ").strip()
        mode = "audio" if choice == "2" else "video"
    
    if mode == "audio":
        download_audio(url)
    else:
        download_video(url)


if __name__ == "__main__":
    main()
