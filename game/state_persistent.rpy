## Interlude / Side B — Variabel Persisten & Katalog Kanonik (PRD §2, §4.5, §4.6, §4.7)
## Semua data lintas-playthrough memakai `default persistent.*`.

## --- Bahasa Ganda Independen (bawaan: id + id) ---
default persistent.ui_lang = "id"
default persistent.story_lang = "id"

## --- Progres Persisten: Ending, Pencapaian, CG ---
## unlocked_endings: { "H1": {"unlocked_at": "YYYY-MM-DD", "sample_choices": "AAAAAAAAAAAA"}, ... }
default persistent.unlocked_endings = {}

## achievements: { "ach_first_tape": {"unlocked_at": "YYYY-MM-DD"}, ... }
default persistent.achievements = {}

## seen_cgs: set berisi ID CG kanonik yang pernah tampil (mis. "cg_perpustakaan_debu")
default persistent.seen_cgs = set()

## Bonus Bab 48 di galeri CG bila tamat dengan K2 = B (PRD §4.7)
default persistent.bonus_ch48_unlocked = False

## --- Preferensi Mode Baca & Perangkat (PRD §4.4, §4.5) ---
default persistent.base_text_cps = 45
default persistent.base_afm_time = 5
default persistent.afm_v2_migrated = False
default persistent.read_speed_2x = False
default persistent.font_size_scale = 1.0
default persistent.android_vibration = False

## --- Katalog Kanonik (konstanta, bukan state yang disimpan) ---
define ENDINGS_CATALOG = [
    {"id": "H1", "ach_id": "ach_ending_h1", "title_key": "ending_h1_title", "tag_key": "ending_h1_tag"},
    {"id": "H2", "ach_id": "ach_ending_h2", "title_key": "ending_h2_title", "tag_key": "ending_h2_tag"},
    {"id": "G",  "ach_id": "ach_ending_g",  "title_key": "ending_g_title",  "tag_key": "ending_g_tag"},
    {"id": "S1", "ach_id": "ach_ending_s1", "title_key": "ending_s1_title", "tag_key": "ending_s1_tag"},
    {"id": "S2", "ach_id": "ach_ending_s2", "title_key": "ending_s2_title", "tag_key": "ending_s2_tag"},
]

define ACHIEVEMENTS_CATALOG = [
    "ach_first_tape",
    "ach_kusut",
    "ach_hening",
    "ach_penunggu_mati",
    "ach_telinga_kedua",
    "ach_kolektor_suara",
    "ach_barter",
    "ach_penunda",
    "ach_penolak",
    "ach_jujur",
    "ach_ending_h1",
    "ach_ending_h2",
    "ach_ending_g",
    "ach_ending_s1",
    "ach_ending_s2",
    "ach_gema_bahagia",
    "ach_kaset_terakhir",
    "ach_dua_sisi_kaset",
    "ach_semua_ending",
]

## 12 CG kanonik persis sesuai aset_manifest.json (plus slot bonus Bab 48 di layar galeri).
define CG_CATALOG = [
    {"id": "cg_perpustakaan_debu", "file": "images/cg/cg_perpustakaan_debu.jpg", "title_key": "cg_perpustakaan_debu"},
    {"id": "cg_headphone",         "file": "images/cg/cg_headphone.jpg",         "title_key": "cg_headphone"},
    {"id": "cg_barter",            "file": "images/cg/cg_barter.jpg",            "title_key": "cg_barter"},
    {"id": "cg_peron",             "file": "images/cg/cg_peron.jpg",             "title_key": "cg_peron"},
    {"id": "cg_jendela_kereta",    "file": "images/cg/cg_jendela_kereta.jpg",    "title_key": "cg_jendela_kereta"},
    {"id": "cg_tombol_play",       "file": "images/cg/cg_tombol_play.jpg",       "title_key": "cg_tombol_play"},
    {"id": "cg_pita_kusut",        "file": "images/cg/cg_pita_kusut.jpg",        "title_key": "cg_pita_kusut"},
    {"id": "cg_bukit_senja",       "file": "images/cg/cg_bukit_senja.jpg",       "title_key": "cg_bukit_senja"},
    {"id": "cg_kaset_siti",        "file": "images/cg/cg_kaset_siti.jpg",        "title_key": "cg_kaset_siti"},
    {"id": "cg_peron_sehat",       "file": "images/cg/cg_peron_sehat.jpg",       "title_key": "cg_peron_sehat"},
    {"id": "cg_kamar_pasif",       "file": "images/cg/cg_kamar_pasif.jpg",       "title_key": "cg_kamar_pasif"},
    {"id": "cg_pita_ironis",       "file": "images/cg/cg_pita_ironis.jpg",       "title_key": "cg_pita_ironis"},
    {"id": "cg_surat_lama",        "file": "images/cg/cg_surat_lama.jpg",        "title_key": "cg_surat_lama"},
    {"id": "cg_surat_perpisahan",  "file": "images/cg/cg_surat_perpisahan.jpg",  "title_key": "cg_surat_perpisahan"},
    {"id": "cg_surat_yara",        "file": "images/cg/cg_surat_yara.jpg",        "title_key": "cg_surat_yara"},
    {"id": "cg_surat_balasan_yara","file": "images/cg/cg_surat_balasan_yara.jpg","title_key": "cg_surat_balasan_yara"},
]

## 6 BGM kanonik persis sesuai aset_manifest.json untuk Ruang Musik (PRD §4.7).
define BGM_CATALOG = [
    {"id": "bgm_toko",    "file": "audio/bgm/bgm_toko.ogg",    "title_key": "bgm_toko",    "loop": True},
    {"id": "bgm_sekolah", "file": "audio/bgm/bgm_sekolah.ogg", "title_key": "bgm_sekolah", "loop": True},
    {"id": "bgm_senja",   "file": "audio/bgm/bgm_senja.ogg",   "title_key": "bgm_senja",   "loop": True},
    {"id": "bgm_cemas",   "file": "audio/bgm/bgm_cemas.ogg",   "title_key": "bgm_cemas",   "loop": True},
    {"id": "bgm_peron",       "file": "audio/bgm/bgm_peron.ogg",       "title_key": "bgm_peron",       "loop": False},
    {"id": "bgm_epilog",      "file": "audio/bgm/bgm_epilog.ogg",      "title_key": "bgm_epilog",      "loop": True},
    {"id": "bgm_hujan_malam", "file": "audio/bgm/bgm_hujan_malam.ogg", "title_key": "bgm_hujan_malam", "loop": True},
    {"id": "bgm_duka_siti",   "file": "audio/bgm/bgm_duka_siti.ogg",   "title_key": "bgm_duka_siti",   "loop": True},
    {"id": "bgm_kafe_baru",   "file": "audio/bgm/bgm_kafe_baru.ogg",   "title_key": "bgm_kafe_baru",   "loop": True},
]

init -15 python:
    import datetime

    def _ensure_persistent_containers():
        if persistent.ui_lang not in ("id", "en"):
            persistent.ui_lang = "id"
        if persistent.story_lang not in ("id", "en"):
            persistent.story_lang = "id"
        if not isinstance(persistent.unlocked_endings, dict):
            persistent.unlocked_endings = {}
        if not isinstance(persistent.achievements, dict):
            persistent.achievements = {}
        if not isinstance(persistent.seen_cgs, set):
            persistent.seen_cgs = set(persistent.seen_cgs) if persistent.seen_cgs else set()
        if persistent.bonus_ch48_unlocked is None:
            persistent.bonus_ch48_unlocked = False
        if persistent.base_text_cps is None:
            persistent.base_text_cps = 45
        if persistent.base_afm_time is None:
            persistent.base_afm_time = 15
        if persistent.read_speed_2x is None:
            persistent.read_speed_2x = False
        if persistent.font_size_scale is None:
            persistent.font_size_scale = 1.0
        if persistent.android_vibration is None:
            persistent.android_vibration = False

    def is_ending_unlocked(ending_id):
        _ensure_persistent_containers()
        return ending_id in persistent.unlocked_endings

    def get_ending_record(ending_id):
        _ensure_persistent_containers()
        return persistent.unlocked_endings.get(ending_id)

    def unlock_ending(ending_id, choice_string=""):
        """Catat ending yang dibuka secara persisten beserta tanggal & string contoh."""
        _ensure_persistent_containers()
        today = datetime.date.today().isoformat()
        if ending_id not in persistent.unlocked_endings:
            persistent.unlocked_endings[ending_id] = {
                "unlocked_at": today,
                "sample_choices": choice_string or "",
            }
        renpy.save_persistent()
        for entry in ENDINGS_CATALOG:
            if entry["id"] == ending_id:
                unlock_achievement(entry["ach_id"], notify=True)
                break
        if all(e["id"] in persistent.unlocked_endings for e in ENDINGS_CATALOG):
            unlock_achievement("ach_semua_ending", notify=True)

    def is_achievement_unlocked(ach_id):
        _ensure_persistent_containers()
        return ach_id in persistent.achievements

    def get_achievement_record(ach_id):
        _ensure_persistent_containers()
        return persistent.achievements.get(ach_id)

    _achievement_toast_queue = []

    def _show_next_achievement_toast():
        if not _achievement_toast_queue:
            renpy.hide_screen("achievement_toast")
            return
        next_id = _achievement_toast_queue.pop(0)
        renpy.show_screen("achievement_toast", ach_id=next_id)

    def unlock_achievement(ach_id, notify=True):
        """Buka pencapaian persisten; antrekan toast kecil agar unlock bersamaan tidak saling menimpa."""
        _ensure_persistent_containers()
        if ach_id not in ACHIEVEMENTS_CATALOG:
            return False
        if ach_id in persistent.achievements:
            return False
        persistent.achievements[ach_id] = {
            "unlocked_at": datetime.date.today().isoformat(),
        }
        renpy.save_persistent()
        if notify:
            if renpy.get_screen("achievement_toast"):
                if ach_id not in _achievement_toast_queue:
                    _achievement_toast_queue.append(ach_id)
            else:
                renpy.show_screen("achievement_toast", ach_id=ach_id)
        return True

    def is_cg_seen(cg_id):
        """Cek apakah CG sudah pernah tampil (dari set persisten atau `renpy.seen_image`)."""
        _ensure_persistent_containers()
        if cg_id in persistent.seen_cgs:
            return True
        try:
            if renpy.seen_image(cg_id):
                persistent.seen_cgs.add(cg_id)
                renpy.save_persistent()
                return True
        except Exception:
            pass
        return False

    def mark_cg_seen(cg_id):
        """Tandai CG sudah pernah terlihat secara persisten."""
        _ensure_persistent_containers()
        if cg_id not in persistent.seen_cgs:
            persistent.seen_cgs.add(cg_id)
            renpy.save_persistent()

    def show_cg_and_unlock(cg_id, transition=None):
        """
        Tampilkan CG kanonik layar penuh tanpa sprite karakter & tanpa UI terlebih dahulu
        agar pemain bisa menikmati CG secara utuh; klik sekali untuk memunculkan dialog lagi.
        """
        mark_cg_seen(cg_id)
        try:
            hide_item()
        except Exception:
            pass
        if renpy.get_screen("chapter_banner"):
            renpy.hide_screen("chapter_banner")
        prev_qm = getattr(store, "quick_menu", True)
        store.quick_menu = False
        try:
            _window_hide(dissolve)
        except Exception:
            pass
        renpy.scene()
        renpy.show(cg_id)
        if transition is not None:
            renpy.with_statement(transition)
        renpy.pause()
        store.quick_menu = prev_qm
        try:
            _window_show(dissolve)
        except Exception:
            pass

    def apply_read_speed():
        """Sinkronkan kecepatan teks & jeda auto-play dengan pengali 1x / 2x (PRD §4.4)."""
        _ensure_persistent_containers()
        if not getattr(persistent, "afm_v2_migrated", False):
            persistent.base_afm_time = 5
            persistent.afm_v2_migrated = True
        base_cps = int(persistent.base_text_cps or 0)
        base_afm = max(1, min(15, int(persistent.base_afm_time or 5)))
        persistent.base_afm_time = base_afm
        if persistent.read_speed_2x:
            _preferences.text_cps = 0 if base_cps == 0 else min(240, base_cps * 2)
            _preferences.afm_time = max(1, int(round(base_afm / 2.0)))
        else:
            _preferences.text_cps = base_cps
            _preferences.afm_time = base_afm
        ## Pastikan skip selalu berhenti di setiap pilihan (PRD §4.4).
        _preferences.skip_after_choices = False

    class ToggleAutoForward(Action, DictEquality):
        """Toggle Auto-Forward Mode dengan jaminan `afm_time >= 1` agar selalu berjalan mulus."""
        def __call__(self):
            _ensure_persistent_containers()
            apply_read_speed()
            _preferences.afm_enable = not bool(_preferences.afm_enable)
            renpy.restart_interaction()

        def get_selected(self):
            return bool(_preferences.afm_enable)

    class ToggleSpeed2x(Action, DictEquality):
        def __call__(self):
            _ensure_persistent_containers()
            persistent.read_speed_2x = not persistent.read_speed_2x
            apply_read_speed()
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            _ensure_persistent_containers()
            return bool(persistent.read_speed_2x)

    class SetSpeed2x(Action, DictEquality):
        def __init__(self, enabled):
            self.enabled = bool(enabled)

        def __call__(self):
            _ensure_persistent_containers()
            persistent.read_speed_2x = self.enabled
            apply_read_speed()
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            _ensure_persistent_containers()
            return bool(persistent.read_speed_2x) == self.enabled

    class SetInstantText(Action, DictEquality):
        def __init__(self, instant):
            self.instant = bool(instant)

        def __call__(self):
            _ensure_persistent_containers()
            if self.instant:
                persistent.base_text_cps = 0
            else:
                if persistent.base_text_cps == 0:
                    persistent.base_text_cps = 45
            apply_read_speed()
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            _ensure_persistent_containers()
            return (persistent.base_text_cps == 0) == self.instant

    class BaseTextCPSBarValue(BarValue, DictEquality):
        def __init__(self):
            self.min_val = 15
            self.max_val = 120

        def get_style(self):
            return "slider", "vslider"

        def get_adjustment(self):
            _ensure_persistent_containers()
            cur = persistent.base_text_cps
            if cur <= 0:
                cur = self.max_val
            val = max(0, min(self.max_val - self.min_val, cur - self.min_val))
            return ui.adjustment(
                range=self.max_val - self.min_val,
                value=val,
                changed=self._changed,
                step=5,
            )

        def _changed(self, v):
            _ensure_persistent_containers()
            persistent.base_text_cps = int(self.min_val + round(v))
            apply_read_speed()
            renpy.save_persistent()
            renpy.restart_interaction()

    class BaseAFMTimeBarValue(BarValue, DictEquality):
        def __init__(self):
            self.min_val = 1
            self.max_val = 15

        def get_style(self):
            return "slider", "vslider"

        def get_adjustment(self):
            _ensure_persistent_containers()
            cur = max(self.min_val, min(self.max_val, int(persistent.base_afm_time)))
            return ui.adjustment(
                range=self.max_val - self.min_val,
                value=cur - self.min_val,
                changed=self._changed,
                step=1,
            )

        def _changed(self, v):
            _ensure_persistent_containers()
            persistent.base_afm_time = int(self.min_val + round(v))
            apply_read_speed()
            renpy.save_persistent()
            renpy.restart_interaction()

    class FontSizeScaleBarValue(BarValue, DictEquality):
        def __init__(self):
            self.min_pct = 85
            self.max_pct = 140

        def get_style(self):
            return "slider", "vslider"

        def get_adjustment(self):
            _ensure_persistent_containers()
            pct = int(round(float(persistent.font_size_scale) * 100))
            pct = max(self.min_pct, min(self.max_pct, pct))
            return ui.adjustment(
                range=self.max_pct - self.min_pct,
                value=pct - self.min_pct,
                changed=self._changed,
                step=5,
            )

        def _changed(self, v):
            _ensure_persistent_containers()
            pct = int(self.min_pct + round(v))
            persistent.font_size_scale = pct / 100.0
            renpy.save_persistent()
            renpy.restart_interaction()

    class SetAndroidVibration(Action, DictEquality):
        def __init__(self, enabled):
            self.enabled = bool(enabled)

        def __call__(self):
            _ensure_persistent_containers()
            persistent.android_vibration = self.enabled
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            _ensure_persistent_containers()
            return bool(persistent.android_vibration) == self.enabled

    def trigger_haptic(duration_ms=35):
        """Getaran halus di Android hanya bila pemain mengaktifkannya di Pengaturan (PRD §4.5)."""
        _ensure_persistent_containers()
        if not persistent.android_vibration:
            return
        if renpy.variant("android"):
            try:
                renpy.vibrate(max(0.01, float(duration_ms) / 1000.0))
            except Exception:
                pass

    class PlayGalleryBGM(Action, DictEquality):
        def __init__(self, track_file, loop=True):
            self.track_file = track_file
            self.loop = loop

        def __call__(self):
            current = renpy.music.get_playing(channel="music")
            if current == self.track_file:
                renpy.music.stop(channel="music", fadeout=0.4)
            else:
                renpy.music.play(self.track_file, channel="music", loop=self.loop, fadein=0.4)
            renpy.restart_interaction()

        def get_selected(self):
            return renpy.music.get_playing(channel="music") == self.track_file
