# Psikoloji Reels Ãœretici

Ã‡Ã¶p adam (stickman) tarzÄ± psikoloji/felsefe videolarÄ±nÄ± **senaryodan videoya** otomatik Ã¼reten hat: senaryo â†’ seslendirme â†’ animasyonlu sahne â†’ altyazÄ± â†’ dikey video.

## Dosyalar
- `senaryo_uret.py`: senaryo ve sahne metinleri (marka/yazar adÄ± Ã¼st deÄŸiÅŸkenlerde)
- `ses_al.py`: metinden seslendirme (edge-tts)
- `hepsini_uret.py`: tÃ¼m videolarÄ± sÄ±rayla Ã¼retir
- `marka/`: logo ve gÃ¶rsel kimlik varlÄ±klarÄ±

```bash
pip install edge-tts
python hepsini_uret.py
```

> ÃœretilmiÅŸ videolar boyut nedeniyle depoda yok.

**Teknolojiler:** Python Â· edge-tts Â· ffmpeg Â· HTML/CSS animasyon