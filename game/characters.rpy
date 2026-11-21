define narrator = Character(None, callback=make_speaker_cb(None))

define kai = Character("Kai", color="#9ec2dc", callback=make_speaker_cb("kai"))
define kai_hati = Character(
    _("Kai (hati)"),
    color="#9ec2dc",
    what_italic=True,
    what_color="#d9c6ad",
    window_background=Solid("#1d1611b8"),
    callback=make_speaker_cb("kai"),
)
define kai_kaset = Character(_("Kai (dari kaset)"), color="#9ec2dc", what_italic=True, callback=make_speaker_cb("kai"))

define ageng = Character("Pak Ageng", color="#e0a55e", callback=make_speaker_cb("ageng"))
define ageng_kaset = Character(_("Pak Ageng (dari kaset)"), color="#e0a55e", what_italic=True, callback=make_speaker_cb("ageng"))

define gadis = Character(_("Gadis"), color="#e5a080", callback=make_speaker_cb("yara"))
define yara = Character("Yara", color="#e5a080", callback=make_speaker_cb("yara"))
define yara_hati = Character(
    _("Yara (hati)"),
    color="#e5a080",
    what_italic=True,
    what_color="#e8c4b0",
    window_background=Solid("#1d1611b8"),
    callback=make_speaker_cb("yara"),
)
define yara_pesan = Character(_("Yara (pesan teks)"), color="#e5a080", what_italic=True, callback=make_speaker_cb("yara"))
define yara_kaset = Character(_("Yara (dari kaset)"), color="#e5a080", what_italic=True, callback=make_speaker_cb("yara"))
define yara_surat = Character(_("Yara (suara surat)"), color="#e5a080", what_italic=True, callback=make_speaker_cb("yara"))
define yara_telepon = Character(_("Yara (dari telepon)"), color="#e5a080", what_italic=True, callback=make_speaker_cb("yara"))

define kaya = Character(_("Pria Kaya"), color="#c8c0b8", callback=make_speaker_cb("kaya"))

define bu_sarah = Character("Bu Sarah", color="#d68a7c", callback=make_speaker_cb("npc_bu_sarah"))
define bu_sarah_kaset = Character(_("Bu Sarah (dari kaset)"), color="#d68a7c", what_italic=True, callback=make_speaker_cb(None))

define ibu = Character(_("Ibu"), color="#d4b58f", callback=make_speaker_cb("npc_ibu"))
define ibu_kaset = Character(_("Ibu (dari kaset)"), color="#d4b58f", what_italic=True, callback=make_speaker_cb(None))
define ayah = Character(_("Ayah"), color="#b5a38e", callback=make_speaker_cb("npc_ayah"))
define wanita = Character(_("Wanita"), color="#e0b5c4", callback=make_speaker_cb("npc_wanita"))
define teman = Character(_("Teman Sekelas"), color="#b8c4b0", callback=make_speaker_cb("npc_teman1"))
define teman1 = Character(_("Teman 1"), color="#b8c4b0", callback=make_speaker_cb("npc_teman1"))
define teman2 = Character(_("Teman 2"), color="#a9bba4", callback=make_speaker_cb("npc_teman2"))
define ibu_penjual = Character(_("Ibu Penjual"), color="#d9b489", callback=make_speaker_cb("npc_ibu_penjual"))
define pemilik_warung = Character(_("Pemilik Warung"), color="#c9a882", callback=make_speaker_cb("npc_pemilik_warung"))
define barista = Character(_("Barista"), color="#c9a882", callback=make_speaker_cb("npc_barista"))
define pengumuman = Character(_("Pengumuman (pengeras suara)"), color="#b8c4b0", what_italic=True, callback=make_speaker_cb(None))
