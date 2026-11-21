## Interlude / Side B — Deklarasi Referensi Aset Kanonik (73 aset persis sesuai aset_manifest.json)
## Mengganti berkas placeholder pada fase berikutnya cukup menimpa file di foldernya dengan nama sama.

## --- UI (3 aset) ---
image ui_latar_menu = "images/ui/ui_latar_menu.jpg"
image ui_logo_judul = "images/ui/ui_logo_judul.png"
image ui_ikon_kaset = "images/ui/ui_ikon_kaset.png"

## --- Background (20 aset) ---
image bg_gang_hujan = "images/bg/bg_gang_hujan.jpg"
image bg_gang_kering = "images/bg/bg_gang_kering.jpg"
image bg_toko_luar = "images/bg/bg_toko_luar.jpg"
image bg_toko_dalam = "images/bg/bg_toko_dalam.jpg"
image bg_toko_dalam_malam = "images/bg/bg_toko_dalam_malam.jpg"
image bg_toko_kosong = "images/bg/bg_toko_kosong.jpg"
image bg_kafe = "images/bg/bg_kafe.jpg"
image bg_kamar_kai = "images/bg/bg_kamar_kai.jpg"
image bg_kamar_kai_malam = "images/bg/bg_kamar_kai_malam.jpg"
image bg_kamar_yara = "images/bg/bg_kamar_yara.jpg"
image bg_kelas = "images/bg/bg_kelas.jpg"
image bg_koridor_sekolah = "images/bg/bg_koridor_sekolah.jpg"
image bg_gerbang_sekolah = "images/bg/bg_gerbang_sekolah.jpg"
image bg_perpustakaan = "images/bg/bg_perpustakaan.jpg"
image bg_kantin = "images/bg/bg_kantin.jpg"
image bg_warung_rawon = "images/bg/bg_warung_rawon.jpg"
image bg_teras_toko = "images/bg/bg_teras_toko.jpg"
image bg_bukit = "images/bg/bg_bukit.jpg"
image bg_stasiun = "images/bg/bg_stasiun.jpg"
image bg_rumah_yara = "images/bg/bg_rumah_yara.jpg"

## --- Sistem Sorot Penutur Aktif (Non-penutur diberi overlay hitam 25% via TintMatrix) ---
## Memakai kelas top-level (picklable) agar proses Save/Load di PC & Android 100% aman.
init -6 python:
    _active_speaker_tag = None

    class SpeakerCallback(object):
        """Catat tag karakter yang sedang berbicara agar sprite lain otomatis meredup 25%."""
        def __init__(self, tag):
            self.tag = tag

        def __call__(self, event, interact=True, **kwargs):
            global _active_speaker_tag
            if event == "begin" and interact:
                _active_speaker_tag = self.tag

    class SpeakerDimFn(object):
        """Overlay hitam 25% (#bfbfbf = 75% kecerahan RGB) saat karakter tidak berbicara."""
        def __init__(self, tag):
            self.tag = tag

        def __call__(self, trans, st, at):
            if _active_speaker_tag == self.tag:
                trans.matrixcolor = TintMatrix("#ffffff")
            else:
                trans.matrixcolor = TintMatrix("#bfbfbf")
            return 0.05

    def make_speaker_cb(tag):
        return SpeakerCallback(tag)

    def make_speaker_dim_fn(tag):
        return SpeakerDimFn(tag)

init -5:
    transform speaker_dim(tag):
        function make_speaker_dim_fn(tag)

## --- Sprite Karakter (24 aset — tag terpisah spasi + auto-dim 25% saat tidak berbicara) ---
image kai biasa = At("images/sprites/kai_biasa.png", speaker_dim("kai"))
image kai cemas = At("images/sprites/kai_cemas.png", speaker_dim("kai"))
image kai panik = At("images/sprites/kai_panik.png", speaker_dim("kai"))
image kai senyum = At("images/sprites/kai_senyum.png", speaker_dim("kai"))
image kai sedih = At("images/sprites/kai_sedih.png", speaker_dim("kai"))
image kai datar = At("images/sprites/kai_datar.png", speaker_dim("kai"))
image kai menangis = At("images/sprites/kai_menangis.png", speaker_dim("kai"))
image kai dewasa = At("images/sprites/kai_dewasa.png", speaker_dim("kai"))

image yara ceria = At("images/sprites/yara_ceria.png", speaker_dim("yara"))
image yara biasa = At("images/sprites/yara_biasa.png", speaker_dim("yara"))
image yara penasaran = At("images/sprites/yara_penasaran.png", speaker_dim("yara"))
image yara fokus = At("images/sprites/yara_fokus.png", speaker_dim("yara"))
image yara marah = At("images/sprites/yara_marah.png", speaker_dim("yara"))
image yara sedih = At("images/sprites/yara_sedih.png", speaker_dim("yara"))
image yara menangis = At("images/sprites/yara_menangis.png", speaker_dim("yara"))
image yara senyum_perpisahan = At("images/sprites/yara_senyum_perpisahan.png", speaker_dim("yara"))
image yara dewasa = At("images/sprites/yara_dewasa.png", speaker_dim("yara"))

image ageng biasa = At("images/sprites/ageng_biasa.png", speaker_dim("ageng"))
image ageng senyum = At("images/sprites/ageng_senyum.png", speaker_dim("ageng"))
image ageng serius = At("images/sprites/ageng_serius.png", speaker_dim("ageng"))
image ageng iba = At("images/sprites/ageng_iba.png", speaker_dim("ageng"))
image ageng sakit = At("images/sprites/ageng_sakit.png", speaker_dim("ageng"))

image kaya biasa = At("images/sprites/kaya_biasa.png", speaker_dim("kaya"))
image kaya senyum = At("images/sprites/kaya_senyum.png", speaker_dim("kaya"))
image kaya marah = At("images/sprites/kaya_marah.png", speaker_dim("kaya"))

## --- Sprite NPC Pendukung (9 aset — auto-dim 25% saat tidak berbicara) ---
image npc_bu_sarah = At("images/sprites/npc_bu_sarah.png", speaker_dim("npc_bu_sarah"))
image npc_ibu = At("images/sprites/npc_ibu.png", speaker_dim("npc_ibu"))
image npc_ayah = At("images/sprites/npc_ayah.png", speaker_dim("npc_ayah"))
image npc_wanita = At("images/sprites/npc_wanita.png", speaker_dim("npc_wanita"))
image npc_teman1 = At("images/sprites/npc_teman1.png", speaker_dim("npc_teman1"))
image npc_teman1_dewasa = At("images/sprites/npc_teman1_dewasa.png", speaker_dim("npc_teman1"))
image npc_teman2 = At("images/sprites/npc_teman2.png", speaker_dim("npc_teman2"))
image npc_teman2_dewasa = At("images/sprites/npc_teman2_dewasa.png", speaker_dim("npc_teman2"))
image npc_ibu_penjual = At("images/sprites/npc_ibu_penjual.png", speaker_dim("npc_ibu_penjual"))
image npc_pemilik_warung = At("images/sprites/npc_pemilik_warung.png", speaker_dim("npc_pemilik_warung"))
image npc_barista = At("images/sprites/npc_barista.png", speaker_dim("npc_barista"))

## --- CG Kanonik (12 aset) — dipastikan nama image cocok 1:1 dengan ID Galeri CG ---
image cg_perpustakaan_debu = "images/cg/cg_perpustakaan_debu.jpg"
image cg_headphone = "images/cg/cg_headphone.jpg"
image cg_barter = "images/cg/cg_barter.jpg"
image cg_peron = "images/cg/cg_peron.jpg"
image cg_jendela_kereta = "images/cg/cg_jendela_kereta.jpg"
image cg_tombol_play = "images/cg/cg_tombol_play.jpg"
image cg_pita_kusut = "images/cg/cg_pita_kusut.jpg"
image cg_bukit_senja = "images/cg/cg_bukit_senja.jpg"
image cg_kaset_siti = "images/cg/cg_kaset_siti.jpg"
image cg_peron_sehat = "images/cg/cg_peron_sehat.jpg"
image cg_kamar_pasif = "images/cg/cg_kamar_pasif.jpg"
image cg_pita_ironis = "images/cg/cg_pita_ironis.jpg"
image cg_surat_lama = "images/cg/cg_surat_lama.jpg"
image cg_surat_perpisahan = "images/cg/cg_surat_perpisahan.jpg"
image cg_surat_yara = "images/cg/cg_surat_yara.jpg"
image cg_surat_balasan_yara = "images/cg/cg_surat_balasan_yara.jpg"

## --- Posisi Sprite Standar (1920x1080, kanvas sprite 1000x1400 bottom-anchored) ---
## Jarak lebar (0.18 / 0.50 / 0.82 @ zoom 0.70) agar 2 maupun 3 karakter tidak berdempetan.
transform pos_center:
    xpos 0.50
    xanchor 0.5
    yalign 1.0
    zoom 0.70

transform pos_left:
    xpos 0.18
    xanchor 0.5
    yalign 1.0
    zoom 0.70

transform pos_right:
    xpos 0.82
    xanchor 0.5
    yalign 1.0
    zoom 0.70

## --- Audio SFX (9 aset) ---
define audio.sfx_lonceng_pintu = "audio/sfx/sfx_lonceng_pintu.ogg"
define audio.sfx_desis_pita = "audio/sfx/sfx_desis_pita.ogg"
define audio.sfx_klik_play = "audio/sfx/sfx_klik_play.ogg"
define audio.sfx_pita_kusut = "audio/sfx/sfx_pita_kusut.ogg"
define audio.sfx_hujan_deras = "audio/sfx/sfx_hujan_deras.ogg"
define audio.sfx_kelas = "audio/sfx/sfx_kelas.ogg"
define audio.sfx_panci = "audio/sfx/sfx_panci.ogg"
define audio.sfx_kereta_lewat = "audio/sfx/sfx_kereta_lewat.ogg"
define audio.sfx_derit_kursi_goyang = "audio/sfx/sfx_derit_kursi_goyang.ogg"
define audio.sfx_kertas_surat = "audio/sfx/sfx_kertas_surat.ogg"
define audio.sfx_notifikasi_hp = "audio/sfx/sfx_notifikasi_hp.ogg"
define audio.sfx_jam_dinding = "audio/sfx/sfx_jam_dinding.ogg"
define audio.sfx_tulis_pena = "audio/sfx/sfx_tulis_pena.ogg"
define audio.sfx_cangkir_teh = "audio/sfx/sfx_cangkir_teh.ogg"

## --- Audio Kaset (5 aset) ---
define audio.kaset_besok_busarah = "audio/kaset/kaset_besok_busarah.ogg"
define audio.kaset_hening_60detik = "audio/kaset/kaset_hening_60detik.ogg"
define audio.kaset_tangis_yara = "audio/kaset/kaset_tangis_yara.ogg"
define audio.kaset_tawa_siti = "audio/kaset/kaset_tawa_siti.ogg"
define audio.kaset_ultah_kai_yara = "audio/kaset/kaset_ultah_kai_yara.ogg"
define audio.kaset_pesan_ageng = "audio/kaset/kaset_pesan_ageng.ogg"

## --- Audio BGM (6 aset) ---
define audio.bgm_toko = "audio/bgm/bgm_toko.ogg"
define audio.bgm_sekolah = "audio/bgm/bgm_sekolah.ogg"
define audio.bgm_senja = "audio/bgm/bgm_senja.ogg"
define audio.bgm_cemas = "audio/bgm/bgm_cemas.ogg"
define audio.bgm_peron = "audio/bgm/bgm_peron.ogg"
define audio.bgm_epilog = "audio/bgm/bgm_epilog.ogg"
define audio.bgm_hujan_malam = "audio/bgm/bgm_hujan_malam.ogg"
define audio.bgm_duka_siti = "audio/bgm/bgm_duka_siti.ogg"
define audio.bgm_kafe_baru = "audio/bgm/bgm_kafe_baru.ogg"
