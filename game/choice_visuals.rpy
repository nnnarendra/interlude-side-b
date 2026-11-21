init -6 python:
    CHOICE_CARD_SPECS = [

        ("Yang bergambar hujan di atap seng.", "The one with rain on a tin roof.",
         "images/bg/bg_gang_hujan.jpg", "bg", "m01", "minor", "A"),
        ("Yang bergambar keramaian pasar.", "The one with a busy market.",
         "images/bg/bg_toko_luar.jpg", "bg", "m01", "minor", "B"),
        ("Yang bergambar gang pagi hari.", "The one with a morning alley.",
         "images/bg/bg_gang_kering.jpg", "bg", "m01", "minor", "C"),

        ("Bayar penuh, tidak menawar.", "Pay in full, without haggling.",
         "images/sprites/ageng_senyum.png", "sprite", "m02", "minor", "A"),
        ("Menawar sekali.", "Haggle once.",
         "images/sprites/ageng_biasa.png", "sprite", "m02", "minor", "B"),
        ("Bertanya soal cicilan.", "Ask if he can pay in installments.",
         "images/items/item_kaset_kosong_mini.png", "icon", "m02", "minor", "C"),

        ("Lewat gang basah lagi.", "Back through the wet alley.",
         "images/bg/bg_gang_hujan.jpg", "bg", "m03", "minor", "A"),
        ("Lewat jalan besar.", "Take the main road.",
         "images/bg/bg_gerbang_sekolah.jpg", "bg", "m03", "minor", "B"),

        ("\"Besok saya ke sini lagi, Pak. Tiap hari, kalau bisa.\"",
         "\"I'll be back tomorrow, Pak. Every day, if I can.\"",
         "images/choices/choice_g01_a.jpg", "bg", "G1", "major", "A"),
        ("\"Saya batasi, Pak. Seminggu sekali saja. Janji.\"",
         "\"I'll limit myself, Pak. Just once a week. Promise.\"",
         "images/choices/choice_g01_b.jpg", "bg", "G1", "major", "B"),
        ("\"Ini yang terakhir, Pak. Saya berhenti. Ini nggak sehat.\"",
         "\"This is the last one, Pak. I'm stopping. This isn't healthy.\"",
         "images/choices/choice_g01_c.jpg", "bg", "G1", "major", "C"),

        ("Pakai headphone, seperti biasa.", "With headphones, like usual.",
         "images/items/item_kaset_biasa.png", "icon", "m04", "minor", "A"),
        ("Lewat speaker Walkman.", "Through the Walkman speaker.",
         "images/bg/bg_kamar_kai_malam.jpg", "bg", "m04", "minor", "B"),

        ("Mengambil foto langit dari jendela.", "Take a photo of the sky from the window.",
         "images/bg/bg_kamar_kai_malam.jpg", "bg", "m05", "minor", "A"),
        ("Menulis di buku kecilnya.", "Write in his small notebook.",
         "images/bg/bg_kamar_kai.jpg", "bg", "m05", "minor", "B"),
        ("Tidak melakukan apa-apa.", "Do nothing.",
         "images/sprites/kai_datar.png", "sprite", "m05", "minor", "C"),

        ("\"Itu kematianku, Pak. Saya tahu itu.\"",
         "\"That's my death, Pak. I know it is.\"",
         "images/choices/choice_g02_a.jpg", "bg", "G2", "major", "A"),
        ("\"Mungkin… mungkin itu cuma jeda, ya, Pak?\"",
         "\"Maybe… maybe it's just a pause, right, Pak?\"",
         "images/choices/choice_g02_b.jpg", "bg", "G2", "major", "B"),
        ("\"Lupakan, Pak. Anggap nggak pernah terjadi.\"",
         "\"Forget it, Pak. Pretend it never happened.\"",
         "images/choices/choice_g02_c.jpg", "bg", "G2", "major", "C"),

        ("Membaca satu surat lama itu.", "Read that one old letter.",
         "images/bg/bg_toko_dalam.jpg", "bg", "m06", "minor", "A"),
        ("Tidak menyentuh surat orang.", "Don't touch someone else's letter.",
         "images/bg/bg_toko_luar.jpg", "bg", "m06", "minor", "B"),

        ("Ikut duduk, ikut tertawa bersama.", "Sit down and laugh along with them.",
         "images/sprites/kai_senyum.png", "sprite", "m07", "minor", "A"),
        ("Memotret diam-diam.", "Quietly snap a photo.",
         "images/sprites/kai_biasa.png", "sprite", "m07", "minor", "B"),
        ("Menyingkir ke kamar.", "Slip back to his bedroom.",
         "images/bg/bg_kamar_kai_malam.jpg", "bg", "m07", "minor", "C"),

        ("Perpustakaan Kota.", "The City Library.",
         "images/bg/bg_perpustakaan.jpg", "bg", "m08", "minor", "A"),
        ("Ke UKS dulu.", "Go to the UKS first.",
         "images/bg/bg_koridor_sekolah.jpg", "bg", "m08", "minor", "B"),
        ("Ke atap sekolah.", "Head up to the school rooftop.",
         "images/bg/bg_gerbang_sekolah.jpg", "bg", "m08", "minor", "C"),

        ("Duduk dekat panci besar ibu kantin.", "Sit near the canteen lady's big boiling pot.",
         "images/bg/bg_kantin.jpg", "bg", "m09", "minor", "A"),
        ("Duduk di pojok paling sepi.", "Sit in the quietest corner.",
         "images/sprites/kai_biasa.png", "sprite", "m09", "minor", "B"),
        ("Makan sambil berdiri di luar kantin.", "Eat standing up outside the canteen.",
         "images/bg/bg_koridor_sekolah.jpg", "bg", "m09", "minor", "C"),

        ("\"Cari tahu siapa dia.\"", "\"Find out who she is.\"",
         "images/choices/choice_g03_a.jpg", "bg", "G3", "major", "A"),
        ("\"Biarin. Kalau memang ketemu lagi, ya ketemu.\"",
         "\"Leave it. If we run into each other again, we run into each other.\"",
         "images/choices/choice_g03_b.jpg", "bg", "G3", "major", "B"),
        ("\"Jangan ke perpustakaan lagi. Titik.\"",
         "\"Never go back to the library. Period.\"",
         "images/choices/choice_g03_c.jpg", "bg", "G3", "major", "C"),

        ("Diam-diam merekam suara panci itu dengan HP-nya.",
         "Secretly record the boiling pot sound on his phone.",
         "images/bg/bg_kantin.jpg", "bg", "m10", "minor", "A"),
        ("Mendengarkan saja, tanpa merekam.", "Just listen, without recording.",
         "images/sprites/kai_biasa.png", "sprite", "m10", "minor", "B"),
        ("Refleks membantu ibu penjual mengangkat panci.",
         "Instinctively help the stall vendor lift the pot.",
         "images/sprites/kai_senyum.png", "sprite", "m10", "minor", "C"),

        ("\"Suara bel masuk.\"", "\"The school bell.\"",
         "images/bg/bg_kelas.jpg", "bg", "m11", "minor", "A"),
        ("\"Suara orang berbisik.\"", "\"The sound of people whispering.\"",
         "images/bg/bg_koridor_sekolah.jpg", "bg", "m11", "minor", "B"),
        ("\"Suara diam.\"", "\"The sound of silence.\"",
         "images/bg/bg_kamar_kai_malam.jpg", "bg", "m11", "minor", "C"),

        ("\"Mulai besok, aku ikut.\"", "\"Starting tomorrow, I'm coming with you.\"",
         "images/choices/choice_g04_a.jpg", "bg", "G4", "major", "A"),
        ("\"Kalau sempat, aku ikut.\"", "\"If I have time, I'll come along.\"",
         "images/choices/choice_g04_b.jpg", "bg", "G4", "major", "B"),
        ("\"Itu duniamu. Aku dengerin aja hasilnya.\"",
         "\"That's your world. I'll just listen to the recordings.\"",
         "images/choices/choice_g04_c.jpg", "bg", "G4", "major", "C"),

        ("Makan rawon di warung rel.", "Eat rawon at the warung by the tracks.",
         "images/items/item_rawon.png", "icon", "m12", "minor", "A"),
        ("Bungkus, makan di toko.", "Get it to go, eat at the shop.",
         "images/bg/bg_toko_dalam.jpg", "bg", "m12", "minor", "B"),

        ("Beri file itu ke Yara.", "Give the file to Yara.",
         "images/sprites/yara_ceria.png", "sprite", "m13", "minor", "A"),
        ("Simpan untuk diri sendiri.", "Keep it for himself.",
         "images/sprites/kai_biasa.png", "sprite", "m13", "minor", "B"),
        ("Hapus, rekamannya jelek.", "Delete it, the recording is bad.",
         "images/sprites/kai_cemas.png", "sprite", "m13", "minor", "C"),

        ("Bantu Pak Ageng membersihkan rak.", "Help Pak Ageng clean the shelves.",
         "images/sprites/ageng_senyum.png", "sprite", "m14", "minor", "A"),
        ("Lihat-lihat saja.", "Just look around.",
         "images/bg/bg_toko_dalam.jpg", "bg", "m14", "minor", "B"),
        ("Tawar kaset rusak di pojok rak.", "Ask about the broken cassette in the corner of the shelf.",
         "images/items/item_kaset_biasa.png", "icon", "m14", "minor", "C"),

        ("Menyela, membela Pak Ageng.", "Step in and defend Pak Ageng.",
         "images/choices/choice_g05_a.jpg", "bg", "G5", "major", "A"),
        ("Diam mendengarkan.", "Stay quiet and listen.",
         "images/choices/choice_g05_b.jpg", "bg", "G5", "major", "B"),
        ("Dengarkan tawarannya sampai habis.", "Listen to his offer all the way through.",
         "images/choices/choice_g05_c.jpg", "bg", "G5", "major", "C"),

        ("\"Duduk, Pak. Ceritakan semuanya. Saya nggak buru-buru.\"",
         "\"Sit down, Pak. Tell me everything. I'm not in a hurry.\"",
         "images/choices/choice_g06_a.jpg", "bg", "G6", "major", "A"),
        ("\"Ceritakan, Pak. Tapi… saya nggak bisa lama-lama.\"",
         "\"Tell me, Pak. Just… I can't stay long.\"",
         "images/choices/choice_g06_b.jpg", "bg", "G6", "major", "B"),
        ("\"…Nggak jadi, Pak. Saya cuma mau beli kaset yang biasa.\"",
         "\"…Never mind, Pak. I just want to buy a regular cassette.\"",
         "images/choices/choice_g06_c.jpg", "bg", "G6", "major", "C"),

        ("Di bawah talang kanopi.", "Under the canopy talang.",
         "images/bg/bg_teras_toko.jpg", "bg", "m15", "minor", "A"),
        ("Di dekat daun tanaman di pot teras.", "Near the potted plant leaves on the porch.",
         "images/bg/bg_toko_luar.jpg", "bg", "m15", "minor", "B"),
        ("Di payung lipat yang dibuka setengah.", "On a half-open folding umbrella.",
         "images/bg/bg_gang_hujan.jpg", "bg", "m15", "minor", "C"),

        ("\"Ikut. Buat diriku yang dulu.\"", "\"I'm in. For my younger self.\"",
         "images/choices/choice_g07_a.jpg", "bg", "G7", "major", "A"),
        ("\"Aku dengerin aja, Yar. Kamu dulu.\"", "\"I'll just listen, Yar. You go first.\"",
         "images/choices/choice_g07_b.jpg", "bg", "G7", "major", "B"),
        ("\"Nggak. Masa lalu biar di sana.\"", "\"No. Leave the past where it is.\"",
         "images/choices/choice_g07_c.jpg", "bg", "G7", "major", "C"),

        ("\"Kamu nggak akan mati hari Jumat ini. Percaya sama aku.\"",
         "\"You're not going to die this Friday. Trust me.\"",
         "images/sprites/kai_senyum.png", "sprite", "G7", "minor", "1"),
        ("\"Letakkan pulpenmu. Surat-surat itu nggak perlu dikirim.\"",
         "\"Put your pen down. Those letters don't need to be sent.\"",
         "images/bg/bg_kamar_kai.jpg", "bg", "G7", "minor", "2"),
        ("\"Keluar dari kamar. Di luar lagi hujan — dan itu nggak seburuk yang kamu kira.\"",
         "\"Come out of your room. It's raining outside — and it's not as bad as you think.\"",
         "images/bg/bg_teras_toko.jpg", "bg", "G7", "minor", "3"),

        ("Masuk. Curhat ke Pak Ageng.", "Go inside. Talk it out with Pak Ageng.",
         "images/choices/choice_g08_a.jpg", "bg", "G8", "major", "A"),
        ("Nggak jadi masuk. Besok, di Bukit Banyak, coba bicara ke Yara.",
         "Don't go in. Tomorrow, at Bukit Banyak, try talking to Yara.",
         "images/choices/choice_g08_b.jpg", "bg", "G8", "major", "B"),
        ("Pulang. Pendam sendiri.", "Go home. Bottle it up alone.",
         "images/choices/choice_g08_c.jpg", "bg", "G8", "major", "C"),

        ("\"Tukar.\"", "\"Trade.\"",
         "images/choices/choice_g09_a.jpg", "bg", "G9", "climax", "A"),
        ("\"Beri saya waktu.\"", "\"Give me time.\"",
         "images/choices/choice_g09_b.jpg", "bg", "G9", "climax", "B"),
        ("\"Nggak, Pak. Biar saya nggak tahu.\"", "\"No, Pak. Better I don't know.\"",
         "images/choices/choice_g09_c.jpg", "bg", "G9", "climax", "C"),

        ("\"Perpustakaan. Debu dan cahaya itu.\"", "\"The library. That dust and light.\"",
         "images/choices/choice_k1_a.jpg", "bg", "K1", "cond", "A"),
        ("\"Rawon di rel kereta.\"", "\"Rawon by the train tracks.\"",
         "images/choices/choice_k1_b.jpg", "bg", "K1", "cond", "B"),
        ("\"Bukit Banyak. Angin pertama.\"", "\"Bukit Banyak. That first wind.\"",
         "images/choices/choice_k1_c.jpg", "bg", "K1", "cond", "C"),

        ("Ke wastafel di belakang toko, cuci muka.",
         "Go to the sink in the back of the shop and wash his face.",
         "images/sprites/kai_panik.png", "sprite", "m16", "minor", "A"),
        ("Duduk di lantai toko, punggung bersandar ke rak.",
         "Sit on the shop floor, back leaning against the shelf.",
         "images/bg/bg_toko_dalam_malam.jpg", "bg", "m16", "minor", "B"),
        ("Memutar satu kaset biasa. Asal ada suara.",
         "Play a regular cassette. Just to have some sound.",
         "images/items/item_kaset_biasa.png", "icon", "m16", "minor", "C"),

        ("Merekam detak jantungnya sendiri.", "Record his own heartbeat.",
         "images/sprites/kai_cemas.png", "sprite", "m17", "minor", "A"),
        ("Merekam jam dinding kamarnya.", "Record the wall clock in his room.",
         "images/bg/bg_kamar_kai_malam.jpg", "bg", "m17", "minor", "B"),
        ("Tidak merekam apa-apa.", "Don't record anything.",
         "images/sprites/kai_datar.png", "sprite", "m17", "minor", "C"),

        ("\"Suara yang Jujur.\"", "\"Honest Sounds.\"",
         "images/sprites/yara_ceria.png", "sprite", "m18", "minor", "A"),
        ("\"Kota Kecil, Bunyi Besar.\"", "\"Small Town, Big Noise.\"",
         "images/bg/bg_bukit.jpg", "bg", "m18", "minor", "B"),
        ("\"Arsip Hari Biasa.\"", "\"Archive of Ordinary Days.\"",
         "images/bg/bg_perpustakaan.jpg", "bg", "m18", "minor", "C"),

        ("Jujur soal takutnya.", "Be honest about his fear.",
         "images/choices/choice_g10_a.jpg", "bg", "G10", "major", "A"),
        ("\"Oh, bagus buatmu.\" — sambil menelan sisanya.",
         "\"Oh, good for you.\" — swallowing the rest.",
         "images/choices/choice_g10_b.jpg", "bg", "G10", "major", "B"),
        ("Berubah dingin, beralasan sibuk.", "Turn cold, make excuses about being busy.",
         "images/choices/choice_g10_c.jpg", "bg", "G10", "major", "C"),

        ("\"Yar. Ada yang harus kamu tahu. Semuanya.\"",
         "\"Yar. There's something you need to know. Everything.\"",
         "images/choices/choice_g10_a.jpg", "bg", "G10", "major", "A"),
        ("\"Maafin aku. Udah, itu aja.\"", "\"I'm sorry. That's all.\"",
         "images/choices/choice_g10_b.jpg", "bg", "G10", "major", "B"),
        ("Diam dan pergi.", "Stay silent and walk away.",
         "images/choices/choice_g10_c.jpg", "bg", "G10", "major", "C"),

        ("Memotret gang itu dengan HP.", "Take a photo of the alley on his phone.",
         "images/bg/bg_gang_kering.jpg", "bg", "m19", "minor", "A"),
        ("Merekam suara langkahnya sendiri di gang kering.",
         "Record his own footsteps in the dry alley.",
         "images/bg/bg_toko_luar.jpg", "bg", "m19", "minor", "B"),
        ("Langsung masuk, tidak berhenti.", "Walk straight in, without stopping.",
         "images/bg/bg_toko_dalam.jpg", "bg", "m19", "minor", "C"),

        ("Balas malam ini.", "Reply tonight.",
         "images/choices/choice_g11_a.jpg", "bg", "G11", "major", "A"),
        ("Balas tiga hari kemudian.", "Reply three days later.",
         "images/choices/choice_g11_b.jpg", "bg", "G11", "major", "B"),
        ("Tidak balas.", "Don't reply.",
         "images/choices/choice_g11_c.jpg", "bg", "G11", "major", "C"),

        ("Suara panci mendidih dari kantin.", "The boiling pot from the canteen.",
         "images/bg/bg_kantin.jpg", "bg", "m20", "minor", "A"),
        ("Suara hujan di talang.", "Rain on the talang.",
         "images/bg/bg_teras_toko.jpg", "bg", "m20", "minor", "B"),
        ("Desis pita kosong.", "Blank tape hiss.",
         "images/items/item_kaset_biasa.png", "icon", "m20", "minor", "C"),

        ("Kaset kosong mini dari Pak Ageng.", "The mini blank cassette from Pak Ageng.",
         "images/items/item_kaset_kosong_mini.png", "icon", "m21", "minor", "A"),
        ("Surat pendek.", "A short letter.",
         "images/items/item_surat_yara.png", "icon", "m21", "minor", "B"),
        ("Nggak usah diselipkan apa-apa. Kasetnya saja.", "Don't slip anything in. Just the cassette.",
         "images/items/item_bingkisan_yara.png", "icon", "m21", "minor", "C"),

        ("\"Lari. Bicara apa adanya.\"", "\"Run. Speak honestly.\"",
         "images/choices/choice_g12_a.jpg", "bg", "G12", "climax", "A"),
        ("\"Lari — tapi yang keluar malah menyalahkan.\"", "\"Run — but what comes out is blame.\"",
         "images/choices/choice_g12_b.jpg", "bg", "G12", "climax", "B"),
        ("Tidak datang.", "Don't show up.",
         "images/choices/choice_g12_c.jpg", "bg", "G12", "climax", "C"),

        ("Telepon tiap Jumat, jam 16.00.", "Call every Friday at 4:00 PM.",
         "images/bg/bg_stasiun.jpg", "bg", "m22", "minor", "A"),
        ("Telepon bebas — kapan pun kangen.", "Call anytime — whenever they miss each other.",
         "images/sprites/yara_ceria.png", "sprite", "m22", "minor", "B"),
        ("Tukar surat suara.", "Swap voice letters.",
         "images/items/item_kaset_biasa.png", "icon", "m22", "minor", "C"),

        ("\"Putar sekarang.\"", "\"Play it now.\"",
         "images/choices/choice_k2_a.jpg", "bg", "K2", "cond", "A"),
        ("\"Simpan. Belum.\"", "\"Keep it. Not yet.\"",
         "images/choices/choice_k2_b.jpg", "bg", "K2", "cond", "B"),

        ("Kopi hitam.", "Black coffee.",
         "images/bg/bg_kafe.jpg", "bg", "m23", "minor", "A"),
        ("Teh.", "Tea.",
         "images/items/item_teh_melati.png", "icon", "m23", "minor", "B"),
        ("Tidak pesan, hanya duduk.", "Don't order anything, just sit.",
         "images/bg/bg_toko_kosong.jpg", "bg", "m23", "minor", "C"),
    ]

    CHOICE_CARD_LOOKUP = {}
    for _id_cap, _en_cap, _img, _kind, _gid, _gtype, _letter in CHOICE_CARD_SPECS:
        _meta = {
            "img": _img,
            "kind": _kind,
            "gate_id": _gid,
            "gate_type": _gtype,
            "letter": _letter,
        }
        CHOICE_CARD_LOOKUP[_id_cap] = _meta
        CHOICE_CARD_LOOKUP[_en_cap] = _meta

    CHOICE_CARD_DEFAULT = {
        "img": "images/ui/ui_ikon_kaset.png",
        "kind": "icon",
        "gate_id": "",
        "gate_type": "minor",
        "letter": "",
    }

    def get_choice_card_meta(caption, fallback_index=0):
        """Kembalikan metadata visual kartu pilihan untuk caption ID maupun EN."""
        meta = CHOICE_CARD_LOOKUP.get(caption)
        if meta is not None:
            return meta
        letters = ("A", "B", "C", "D")
        return {
            "img": CHOICE_CARD_DEFAULT["img"],
            "kind": CHOICE_CARD_DEFAULT["kind"],
            "gate_id": "",
            "gate_type": "minor",
            "letter": letters[fallback_index] if fallback_index < len(letters) else "",
        }

    def get_menu_gate_banner(items):
        """Kembalikan tuple `(label_text, accent_hex)` untuk tajuk atas layar pilihan bergambar."""
        if not items:
            return (ui_tr("choice_banner_minor"), "#b59876")
        first = get_choice_card_meta(items[0].caption, 0)
        gid = first.get("gate_id") or ""
        gtype = first.get("gate_type") or "minor"
        if gtype == "climax":
            return (ui_tr("choice_banner_climax", gate=gid), "#d96252")
        elif gtype == "major":
            return (ui_tr("choice_banner_major", gate=gid), "#e0a55e")
        elif gtype == "cond":
            return (ui_tr("choice_banner_cond", gate=gid), "#d48a58")
        elif gid:
            return (ui_tr("choice_banner_minor_id", gate=gid), "#b59876")
        return (ui_tr("choice_banner_minor"), "#b59876")
