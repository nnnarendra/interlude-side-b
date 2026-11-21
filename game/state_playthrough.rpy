## Interlude / Side B — Variabel State Per-Playthrough & Hook Gerbang/Pencapaian (Fase 2)
## Semua variabel state permainan memakai `default` (bukan `define`) agar tersimpan otomatis di save.
## Flag minor `m01`–`m23` dan kondisional `K1`/`K2` dipisahkan penuh dari penilai ending.

define SAVE_SCHEMA_VERSION = 1

## Registri mesin 23 gerbang minor persis sesuai `minor_gates.json` (read-only).
define MINOR_GATES_CATALOG = {
    "m01": ("A", "B", "C"),
    "m02": ("A", "B", "C"),
    "m03": ("A", "B"),
    "m04": ("A", "B"),
    "m05": ("A", "B", "C"),
    "m06": ("A", "B"),
    "m07": ("A", "B", "C"),
    "m08": ("A", "B", "C"),
    "m09": ("A", "B", "C"),
    "m10": ("A", "B", "C"),
    "m11": ("A", "B", "C"),
    "m12": ("A", "B"),
    "m13": ("A", "B", "C"),
    "m14": ("A", "B", "C"),
    "m15": ("A", "B", "C"),
    "m16": ("A", "B", "C"),
    "m17": ("A", "B", "C"),
    "m18": ("A", "B", "C"),
    "m19": ("A", "B", "C"),
    "m20": ("A", "B", "C"),
    "m21": ("A", "B", "C"),
    "m22": ("A", "B", "C"),
    "m23": ("A", "B", "C"),
}

define RAIN_SOUND_BY_M15 = {
    "A": "talang",
    "B": "daun",
    "C": "payung",
}

## Metadata bab berjalan untuk ditampilkan di slot save/load (PRD §4.2).
default current_chapter_id = ""
default current_chapter_name_id = ""
default current_chapter_name_en = ""

## 12 gerbang utama (G1..G12): daftar 12 slot + string 12 huruf yang tersinkronisasi di save.
default major_choices = [None, None, None, None, None, None, None, None, None, None, None, None]
default choice_string = "------------"

## 23 gerbang minor (m01..m23) — namespace terpisah, TIDAK pernah dibaca penilai ending.
default minor_flags = {
    "m01": None, "m02": None, "m03": None, "m04": None, "m05": None,
    "m06": None, "m07": None, "m08": None, "m09": None, "m10": None,
    "m11": None, "m12": None, "m13": None, "m14": None, "m15": None,
    "m16": None, "m17": None, "m18": None, "m19": None, "m20": None,
    "m21": None, "m22": None, "m23": None,
}

## 2 gerbang kondisional (K1 bila G9=A; K2 di epilog Happy-True Bab 45) — tidak mengubah ending.
default cond_k1 = None
default cond_k2 = None

## Flag item kosmetik (rantai item gerbang minor, tersimpan di save):
## - m02=A -> item_kaset_kosong_mini (dipakai opsi ekstra m21)
## - m10=A -> item_file_panci (dipakai m13, m20, dan syarat ach_kolektor_suara)
## - m13=A -> item_panci_di_portofolio (daftar portofolio Yara di Bab 22)
## - m14=C -> item_kaset_rusak (kosmetik dari rak pojok di Bab 19)
## - m15   -> item_file_hujan ("talang" | "daun" | "payung", dipakai Bab 25, m20, ach_kolektor_suara)
default item_kaset_kosong_mini = False
default item_file_panci = False
default item_panci_di_portofolio = False
default item_kaset_rusak = False
default item_file_hujan = None

## Flag modal dialog G6=A ("toko ini cermin") untuk membuka pengakuan penuh di G10 (Bab 29/36).
default flag_g6_cermin = False

## Sub-pilihan rasa kalimat rekaman Kai di G7=A (Bab 23-2 — BUKAN gerbang, tidak menyentuh ending).
default flavor_g7_opening = None

init -5 python:
    def _rebuild_choice_string():
        choices = getattr(store, "major_choices", None)
        if not choices or len(choices) != 12:
            store.choice_string = "------------"
            return store.choice_string
        chars = [c if c in ("A", "B", "C") else "-" for c in choices]
        store.choice_string = "".join(chars)
        return store.choice_string

    def get_choice_string():
        """Kembalikan string 12 huruf pilihan gerbang utama (mis. 'ACB---------')."""
        return _rebuild_choice_string()

    def get_major_choice(gate_num):
        """Ambil pilihan gerbang utama G1..G12 (indeks 1-based)."""
        if not (1 <= int(gate_num) <= 12):
            raise ValueError("Nomor gerbang utama harus 1..12")
        return store.major_choices[int(gate_num) - 1]

    def record_major_choice(gate_num, choice):
        """
        Catat pilihan gerbang utama G1..G12 ('A'/'B'/'C'), perbarui string 12 huruf,
        dan jalankan hook pencapaian yang terkait gerbang tersebut (PRD §4.6).
        """
        idx = int(gate_num) - 1
        c = str(choice).strip().upper()
        if not (0 <= idx < 12):
            raise ValueError("Nomor gerbang utama harus 1..12")
        if c not in ("A", "B", "C"):
            raise ValueError("Pilihan gerbang utama harus A, B, atau C")

        store.major_choices[idx] = c
        _rebuild_choice_string()

        ## Hook pencapaian & flag terkait gerbang utama (PRD §4.6 & Route Map):
        if gate_num == 4 and c == "A":
            unlock_achievement("ach_telinga_kedua", notify=True)
        elif gate_num == 6:
            store.flag_g6_cermin = (c == "A")
        elif gate_num == 9:
            if c == "A":
                unlock_achievement("ach_barter", notify=True)
            elif c == "B":
                unlock_achievement("ach_penunda", notify=True)
            elif c == "C":
                unlock_achievement("ach_penolak", notify=True)
        elif gate_num == 10 and c == "A":
            unlock_achievement("ach_jujur", notify=True)

        return store.choice_string

    def get_minor_choice(gate_id):
        """Ambil nilai flag gerbang minor m01..m23."""
        if gate_id not in MINOR_GATES_CATALOG:
            raise ValueError("ID gerbang minor tidak dikenal: " + str(gate_id))
        return store.minor_flags.get(gate_id)

    def check_minor_achievement_hooks():
        """Periksa syarat pencapaian yang berasal dari koleksi suara minor (PRD §4.6)."""
        if store.item_file_panci and store.item_file_hujan is not None:
            unlock_achievement("ach_kolektor_suara", notify=True)

    def record_minor_choice(gate_id, choice):
        """
        Catat pilihan gerbang minor `m01`–`m23`, perbarui flag item kosmetik terkait,
        dan jalankan hook pencapaian minor. Tidak pernah menyentuh `major_choices`.
        """
        if gate_id not in MINOR_GATES_CATALOG:
            raise ValueError("ID gerbang minor tidak dikenal: " + str(gate_id))
        c = str(choice).strip().upper()
        valid_opts = MINOR_GATES_CATALOG[gate_id]
        if c not in valid_opts:
            raise ValueError("Pilihan tidak valid untuk " + gate_id + ": " + c)

        store.minor_flags[gate_id] = c

        ## Rantai item kosmetik sesuai `GERBANG-MINOR-Interlude-Side-B.md` & `minor_gates.json`:
        if gate_id == "m02":
            store.item_kaset_kosong_mini = (c == "A")
        elif gate_id == "m10":
            store.item_file_panci = (c == "A")
        elif gate_id == "m13":
            store.item_panci_di_portofolio = (c == "A")
        elif gate_id == "m14":
            store.item_kaset_rusak = (c == "C")
        elif gate_id == "m15":
            store.item_file_hujan = RAIN_SOUND_BY_M15.get(c)

        check_minor_achievement_hooks()
        return c

    def record_cond_k1(choice):
        """Catat gerbang kondisional K1 (kenangan yang ditukar, hanya bila G9=A): A/B/C."""
        c = str(choice).strip().upper()
        if c not in ("A", "B", "C"):
            raise ValueError("Pilihan K1 harus A, B, atau C")
        store.cond_k1 = c
        return c

    def record_cond_k2(choice):
        """
        Catat gerbang kondisional K2 (putar kaset kosong di Bab 45 Happy-True): A/B.
        - A: buka pencapaian `ach_kaset_terakhir`.
        - B: buka adegan bonus Bab 48 di galeri setelah tamat (PRD §4.7).
        """
        c = str(choice).strip().upper()
        if c not in ("A", "B"):
            raise ValueError("Pilihan K2 harus A atau B")
        store.cond_k2 = c
        if c == "B":
            _ensure_persistent_containers()
            persistent.bonus_ch48_unlocked = True
            renpy.save_persistent()
        return c

    ## --- Hook Pencapaian Berbasis Adegan/Bab (siap dipanggil di fase naskah) ---

    def hook_cassette_played(cassette_id):
        """Dipanggil saat kaset mulai diputar (PRD §4.6: ach_first_tape di Bab 3, plus Side A & Side B epilog)."""
        if cassette_id == "kaset_besok_busarah":
            unlock_achievement("ach_first_tape", notify=True)
        elif cassette_id == "kaset_ultah_kai_yara":
            unlock_achievement("ach_gema_bahagia", notify=True)
            if is_achievement_unlocked("ach_kaset_terakhir"):
                unlock_achievement("ach_dua_sisi_kaset", notify=True)
        elif cassette_id == "kaset_pesan_ageng":
            unlock_achievement("ach_kaset_terakhir", notify=True)
            if is_achievement_unlocked("ach_gema_bahagia"):
                unlock_achievement("ach_dua_sisi_kaset", notify=True)

    def hook_cassette_finished(cassette_id, completed_unskipped=False):
        """Dipanggil saat kaset selesai diputar (PRD §4.6: ach_hening bila tanpa skip)."""
        if cassette_id == "kaset_hening_60detik" and completed_unskipped:
            unlock_achievement("ach_hening", notify=True)

    def hook_tape_jammed():
        """Dipanggil saat adegan pita kusut pertama di Bab 4 (PRD §4.6: ach_kusut)."""
        trigger_haptic(45)
        unlock_achievement("ach_kusut", notify=True)

    def hook_chapter_completed(chapter_id):
        """Dipanggil di akhir bab tertentu (PRD §4.6: ach_penunggu_mati saat Bab 11 selesai)."""
        if chapter_id == "bab_11":
            unlock_achievement("ach_penunggu_mati", notify=True)

    ## --- Kendali Skip, Auto-Play, & Autosave Awal Bab ---

    def stop_skip_and_auto():
        """Hentikan skip dan auto-play secara paksa (wajib di menu pilihan & adegan kaset — PRD §4.4)."""
        config.skipping = None
        _preferences.afm_enable = False

    def stop_skip_for_cassette():
        """Alias untuk kompatibilitas: hentikan skip & auto-play saat masuk adegan kaset."""
        stop_skip_and_auto()

    def chapter_autosave(chapter_id, name_id, name_en):
        """Setel metadata bab berjalan, tampilkan spanduk bab, dan simpan autosave di awal bab (PRD §4.2)."""
        hide_item()
        store.current_chapter_id = chapter_id
        store.current_chapter_name_id = name_id
        store.current_chapter_name_en = name_en
        renpy.show_screen("chapter_banner", title_id=name_id, title_en=name_en)
        renpy.force_autosave(take_screenshot=True)

    def _write_save_slot_metadata(d):
        """Sisipkan metadata versi, nama bab, dan string 12 huruf ke JSON setiap save."""
        d["save_schema_version"] = SAVE_SCHEMA_VERSION
        d["chapter_id"] = getattr(store, "current_chapter_id", "")
        d["chapter_name_id"] = getattr(store, "current_chapter_name_id", "")
        d["chapter_name_en"] = getattr(store, "current_chapter_name_en", "")
        d["choice_string"] = get_choice_string()

    config.save_json_callbacks.append(_write_save_slot_metadata)
