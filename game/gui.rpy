## Interlude / Side B — Konfigurasi GUI (1920x1080)
## Palet warna hangat bernuansa kayu jati & pita kaset (Malang, senja),
## dengan kontras teks >= 4.5:1 tanpa menambah berkas aset di luar aset_manifest.json.

init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True
define gui.main_menu_background = "images/ui/ui_latar_menu.jpg"
define gui.game_menu_background = "images/ui/ui_latar_menu.jpg"
define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "i", "b" }

## Palet utama (warm muted palette, kontras tinggi untuk aksesibilitas PC & Android).
define gui.accent_color = "#e0a55e"
define gui.idle_color = "#cbbca8"
define gui.idle_small_color = "#b8a792"
define gui.hover_color = "#fff5e6"
define gui.selected_color = "#f6c987"
define gui.insensitive_color = "#7a6d6088"
define gui.muted_color = "#5c4a3b"
define gui.hover_muted_color = "#8c6d4e"
define gui.text_color = "#f5ebdc"
define gui.interface_text_color = "#f5ebdc"

## Warna panel & permukaan antarmuka.
define UI_BG_DARK = "#1a130fe6"
define UI_BG_PANEL = "#241b15f0"
define UI_BG_CARD = "#2e221af2"
define UI_BG_CARD_LOCKED = "#1e1612e6"
define UI_BG_CARD_HOVER = "#3d2d22f5"
define UI_BORDER_SUBTLE = "#6b523c"
define UI_BORDER_ACCENT = "#e0a55e"
define UI_TEXT_MUTED = "#b8a792"
define UI_TEXT_DIM = "#8c7d6e"

## Tipografi bawaan Ren'Py (portabel di Windows & Android tanpa berkas font ekstra).
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## Ukuran teks dasar di 1920x1080 (>= 26px untuk keterbacaan PC & Android).
define gui.text_size = 32
define gui.name_text_size = 36
define gui.interface_text_size = 28
define gui.label_text_size = 34
define gui.notify_text_size = 26
define gui.title_text_size = 56

## Tata letak kotak dialog.
define gui.textbox_height = 280
define gui.textbox_yalign = 1.0
define gui.name_xpos = 140
define gui.name_ypos = 24
define gui.dialogue_xpos = 140
define gui.dialogue_ypos = 84
define gui.dialogue_width = 1640

## Tata letak slot save/load (3 halaman x 6 slot manual = grid 3x2).
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

init -2 python:
    def scaled_font_size(base_px):
        scale = persistent.font_size_scale
        if scale is None:
            scale = 1.0
        scale = max(0.85, min(1.40, float(scale)))
        return int(round(base_px * scale))
