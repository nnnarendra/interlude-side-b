# Interlude / Side B (Visual Novel)

> [ID] [Bahasa Indonesia](#id-bahasa-indonesia) | [EN] [English](#en-english)

---

## [ID] Bahasa Indonesia

**Interlude / Side B** adalah visual novel Ren'Py (`1920×1080`) tentang Kai, Yara, Pak Ageng, dan **Toko Gema Masa** di ujung gang buntu Kota Malang — tempat kaset pita memutar 60 detik suara hari esok.

> **Catatan Repositori:** Versi repositori ini berisi **kode sumber & naskah lengkap** dengan **aset gambar (`bg`, `cg`, `choices`, `items`, `sprites`) berupa template polos berdimensi asli** dan **audio (`.ogg`) berupa berkas hening** agar proyek tetap dapat langsung dijalankan di Ren'Py tanpa menyertakan aset visual/audio komersial.

### Fitur Utama
- **Struktur Cerita:** 48 bab, 12 gerbang utama (`G1–G12`), 2 gerbang kondisional (`K1–K2`), 23 gerbang minor (`m01–m23`), 5 ending kanonik, 17 pencapaian, 6 CG + Adegan Bonus Bab 48, serta 44 entri glosarium Jawa & lokal.
- **UI & Kenyamanan Baca:** Kartu pilihan bergambar untuk seluruh 37 gerbang (ID & EN), *nameplate* penutur di atas kotak dialog (`Kai` & `Kai (hati)` terpisah dari narasi), spanduk judul bab, strip progres 12 gerbang, mode kecepatan `2x`, sembunyikan UI (`H`), dan dukungan bahasa ganda independen (**Indonesia / English**).

### Cara Menjalankan (Windows / macOS / Linux)
1. Pasang **Ren'Py SDK 8.3+** (disarankan **8.6.1** — Python 3).
2. Clone atau unduh repositori ini ke direktori proyek Ren'Py Anda.
3. Buka **Ren'Py Launcher**, pilih folder proyek ini, lalu klik **Launch Project**.

### Kendali Dasar
- **Klik / Spasi / Enter:** Lanjut dialog.
- **Esc / Klik kanan:** Buka menu permainan (Simpan, Muat, Riwayat, Glosarium, Pengaturan).
- **Quick Menu (bawah kotak dialog):** Riwayat, Lewati (*Skip*), Auto, kecepatan `1x/2x`, Simpan Cepat, Muat Cepat, Simpan, Glosarium, Pengaturan.
- **Mode Debug Penilai Ending:** Tekan `Shift + D` di Menu Utama atau melalui tab *Galeri Ending*.

### Mengganti Aset Placeholder
Seluruh aset merujuk pada jalur tetap di dalam `game/images/` dan `game/audio/`. Untuk mengganti template dengan aset buatan sendiri, cukup **timpa berkas yang ada dengan nama file, folder, dan format yang persis sama** tanpa perlu mengubah kode `.rpy`:

| Folder | Jumlah & Format | Keterangan |
| --- | --- | --- |
| `game/images/bg/` | 20 `.jpg` | Latar lokasi (Malang, Toko Gema Masa, sekolah, stasiun, dll.) |
| `game/images/cg/` | 16 `.jpg` | Ilustrasi CG momen kunci |
| `game/images/choices/` | 41 gambar | Kartu pilihan gerbang |
| `game/images/items/` | 13 `.png` | Ikon / item transparan |
| `game/images/sprites/` | 36 `.png` | Sprite karakter transparan |
| `game/audio/` | 29 `.ogg` | BGM, SFX, dan rekaman kaset (saat ini hening 0,5 detik) |

### 5 Ending Kanonik
1. `H1` — *Simfoni yang Kita Tulis Sendiri* (Happy-True)
2. `H2` — *Pita yang Tak Pernah Ditukar* (Happy-Healthy)
3. `G` — *Sisi B Belum Selesai* (Gantung / Open)
4. `S1` — *Desis Statis* (Sad-Pasif)
5. `S2` — *Hening Enam Puluh Detik* (Sad-Ironis)

###  Unduh Paket Siap Main / Download Playable Builds (v1.0.4)

Unduh versi rilis siap main melalui tab **[Releases](https://github.com/nnnarendra/interlude-side-b/releases/tag/v1.0.4)**:

| Platform | Format | Keterangan / Notes |
| --- | --- | --- |
| 🪟 **PC (Windows / Linux)** | `.zip` | Ekstrak lalu jalankan `interlude-side-b.exe` atau `interlude-side-b.sh` |
| 🌐 **Web (HTML5 / PWA)** | `.zip` | Ekstrak ke web server lokal / hosting static |
| 📱 **Android** | `.apk` | Pasang langsung di perangkat Android |

### Kredit
- **Cerita:** Roo
- **Engine:** Ren'Py

---

## [EN] English

**Interlude / Side B** is a bilingual (`1920×1080`) Ren'Py visual novel about Kai, Yara, Pak Ageng, and **Toko Gema Masa** at the end of a dead-end alley in Malang, Indonesia — a shop where cassette tapes play 60 seconds of tomorrow's sound.

> **Repository Note:** This repository contains the **full source code and script**, while visual assets (`bg`, `cg`, `choices`, `items`, `sprites`) are replaced with **dimension-matched plain template placeholders** and audio files (`.ogg`) are replaced with **silent placeholders**, so the project remains immediately runnable in Ren'Py without redistributing commercial art/audio assets.

### Key Features
- **Story Structure:** 48 chapters, 12 main gates (`G1–G12`), 2 conditional gates (`K1–K2`), 23 minor gates (`m01–m23`), 5 canonical endings, 17 achievements, 6 CGs + Chapter 48 Bonus Scene, and 44 Javanese & local glossary entries.
- **UI & Reading Experience:** Illustrated choice cards for all 37 gates (ID & EN), speaker nameplate above the dialogue box (`Kai` & `Kai (inner)` separated from narration), chapter title banners, 12-gate progress strip, `2x` speed mode, hide UI (`H`), and independent bilingual switching (**Indonesian / English**).

### How to Run (Windows / macOS / Linux)
1. Install **Ren'Py SDK 8.3+** (recommended **8.6.1** — Python 3).
2. Clone or download this repository into your Ren'Py projects directory.
3. Open **Ren'Py Launcher**, select this project folder, and click **Launch Project**.

### Controls
- **Click / Space / Enter:** Advance dialogue.
- **Esc / Right-click:** Open game menu (Save, Load, History, Glossary, Preferences).
- **Quick Menu (bottom of dialogue box):** History, Skip, Auto, `1x/2x` speed toggle, Quick Save, Quick Load, Save, Glossary, Preferences.
- **Ending Evaluator Debug Mode:** Press `Shift + D` on the Main Menu or open it from the *Ending Gallery* tab.

### Replacing Placeholder Assets
All assets point to fixed paths inside `game/images/` and `game/audio/`. To swap in your own art or audio, simply **overwrite the existing files using the exact same filenames, folders, and formats** — no `.rpy` code edits needed:

| Folder | Count & Format | Description |
| --- | --- | --- |
| `game/images/bg/` | 20 `.jpg` | Location backgrounds (Malang, Toko Gema Masa, school, station, etc.) |
| `game/images/cg/` | 16 `.jpg` | Key-moment CG illustrations |
| `game/images/choices/` | 41 images | Gate choice cards |
| `game/images/items/` | 13 `.png` | Transparent item graphics |
| `game/images/sprites/` | 36 `.png` | Transparent character sprites |
| `game/audio/` | 29 `.ogg` | BGM, SFX, and cassette recordings (currently 0.5s silence) |

### 5 Canonical Endings
1. `H1` — *The Symphony We Write Ourselves* (Happy-True)
2. `H2` — *The Tape Never Traded* (Happy-Healthy)
3. `G` — *Side B Unfinished* (Open)
4. `S1` — *Static Hiss* (Sad-Passive)
5. `S2` — *Sixty Seconds of Silence* (Sad-Ironic)

###  Download Playable Builds (v1.0.4)

Download the full playable builds from the **[Releases](https://github.com/nnnarendra/interlude-side-b/releases/tag/v1.0.4)** tab:

| Platform | Format | Instructions |
| --- | --- | --- |
| 🪟 **PC (Windows / Linux)** | `.zip` | Extract and run `interlude-side-b.exe` or `interlude-side-b.sh` |
| 🌐 **Web (HTML5 / PWA)** | `.zip` | Extract to any static hosting or local web server |
| 📱 **Android** | `.apk` | Install directly on your Android device |

### Credits
- **Story:** Roo
- **Engine:** Ren'Py
