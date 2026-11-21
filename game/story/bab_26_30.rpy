label bab_26:
    $ chapter_autosave("bab_26", "Bab 26 — Barter yang Merampas Jiwa", "Ch. 26 — The Barter That Claims a Soul")

    scene bg_toko_dalam_malam with dissolve
    play music bgm_cemas loop fadein 1.5
    play sound sfx_lonceng_pintu
    show kai cemas at pos_center with dissolve

    "Lonceng pintu berbunyi lebih berat dari biasanya. Atau telinga Kai saja yang begitu. Toko Gema Masa sore ini sepi — kursi goyang Pak Ageng kosong, masih berderit pelan, lalu berhenti sendiri." id b26_001

    kai_hati "Pak Ageng nggak ada di konter. Tumben. {i}(memandang ke sudut tergelap toko){/i} …Dan mataku langsung ke sana lagi. Lemari kaca itu." id b26_002

    $ show_item("item_kaset_merah")
    "Kai melangkah mendekat. Di balik kaca yang berembun tipis, kaset-kaset merah Type IV Metal berjejer rapi. Di baris paling tengah, satu label putih tulisan tangan menatapnya langsung: {b}6 BULAN KE DEPAN (1 AGUSTUS){/b}." id b26_003

    kai_hati "Satu Agustus. Tanggal pengumuman kelulusan. Tanggal Yara berangkat ke universitas impiannya di luar kota. Tanggal yang nentuin… aku masih punya melodi, atau balik jadi cangkang kosong lagi." id b26_004

    "Telapak tangan Kai menempel ke kaca yang dingin. Napasnya membuat kaca itu berembun." id b26_005

    kai "{i}(berbisik){/i} Cuma satu menit. Aku cuma butuh dengar satu menit dari tanggal satu Agustus. Kalau yang kedengaran tawa dia… aku pulang. Aku jalanin enam bulan ini dengan tenang. Nggak cemas lagi. Janji." id b26_006

    kai_hati "Tanganku sudah di kunci lemarinya. Kunci kecil itu memang nggak pernah ditarik Pak Ageng. Satu putaran saja…" id b26_007

    show kai panik at pos_left with dissolve
    show ageng serius at pos_right with dissolve
    ageng "Kamu tahu, Kai." id b26_008

    "Kai tersentak. Tangannya menarik diri dari kunci itu seperti baru menyentuh bara. Di pintu belakang toko, Pak Ageng berdiri membawa nampan kecil — dua cangkir kopi yang masih mengepul." id b26_009

    ageng "{i}(melangkah ke konter, meletakkan cangkir-cangkir itu){/i} Pita kaset yang paling sulit diperbaiki itu yang sengaja kita kusutkan sendiri. Gara-gara kita terlalu takut dengar akhir lagunya." id b26_010

    show kai cemas at pos_left
    kai "Pak, saya— saya cuma…" id b26_011

    show ageng iba at pos_right
    ageng "Saya tahu apa yang kamu cari di balik kaca itu. {i}(menatap Kai lama, tidak marah — justru sedih){/i} Kaset merah satu Agustus itu mahal, Kai. Lebih mahal dari semua kaset yang pernah kamu beli." id b26_012

    kai "Harganya… bukan uang, kan, Pak." id b26_013

    show ageng serius at pos_right
    ageng "Bukan. Buat ngintip enam bulan ke depan, nggak cukup bayar pakai ingatan soal rasa makanan, atau kunci motor yang hilang. {i}(berdiri tepat di hadapan Kai){/i} Harganya satu kenangan terindahmu. Ditarik dari kepalamu, digulung masuk ke pita ini, hilang selamanya. Kamu nggak akan bisa ingat lagi. Sekeras apa pun kamu coba." id b26_014

    kai "{i}(menelan ludah){/i} Satu kenangan terindah…" id b26_015

    kai_hati "Dan kepalaku langsung memutar semuanya. Rawon hangat di pinggir rel pas hujan. Angin di puncak Bukit Banyak. Air mendidih di kantin. Dan yang paling atas… perpustakaan kota. Buku-buku jatuh." id b26_016
    kai_hati "Debu beterbangan kena cahaya senja. Dan Yara berdiri di sana — detik aku sadar aku nggak jadi mati. Itu jangkar hidupku. Itu yang bikin aku berubah dari hantu penakut jadi… orang." id b26_016_p2

    menu:
        "Kaset Merah. Kai menatap lemari kaca itu. Apa yang dia lakukan?"

        "\"Tukar.\"":
            $ record_major_choice(9, "A")

            play sound sfx_klik_play
            show kai sedih at pos_left
            kai "{i}(suaranya nyaris berbisik){/i} …Saya setuju, Pak." id b26_017a

            kai_hati "Takut kehilangan dia sudah menang. Aku rela buang masa laluku, asal masa depanku aman. Kedengarannya masuk akal. Kedengarannya… masuk akal." id b26_018a

            show ageng iba at pos_right
            ageng "{i}(menghela napas berat){/i} Pilihan yang sangat berani, Nak. Sekaligus sangat bodoh." id b26_019a

            "Pak Ageng membuka lemari kaca, mengambil kaset merah berlabel 1 AGUSTUS itu, dan meletakkannya di atas konter." id b26_020a

            ageng "Sebelum pitanya bekerja, kamu yang memilih. Kenangan mana yang kamu serahkan? Pita ini nggak mengambil sembarangan — dia mengambil yang kamu tunjuk." id b26_021a

            menu:
                "Kenangan mana yang ditukar Kai?"

                "\"Perpustakaan. Debu dan cahaya itu.\"":
                    $ record_cond_k1("A")

                "\"Rawon di rel kereta.\"":
                    $ record_cond_k1("B")

                "\"Bukit Banyak. Angin pertama.\"":
                    $ record_cond_k1("C")

            ageng "Letakkan tanganmu di atas kaset ini. Pikirkan momen itu. Biarkan pitanya menyerap suara, gambar, dan rasanya dari kamu." id b26_022a

            if cond_k1 == "A":
                kai_hati "Perpustakaan kota. Bau kertas lapuk. Suara debu jatuh. Pipinya yang memerah. Dan debar jantungku yang luar biasa lega — aku masih hidup. {i}(memejamkan mata){/i} Ambil. Ambil saja." id b26_k1a
            elif cond_k1 == "B":
                kai_hati "Warung rawon di pinggir rel. Kuah hitam yang masih mengepul, hujan deras di luar tenda, dia ketawa karena kepedesan sambal. Hangat. Itu sore paling hangat yang aku punya. {i}(memejamkan mata){/i} Ambil. Ambil saja." id b26_k1b
            else:
                kai_hati "Bukit Banyak. Angin pertama yang nerpa muka kami pas sampai puncak. Dia teriak kecil, megangin tripod biar nggak jatuh, terus ketawa. Dunia rasanya luas dan aku nggak takut. {i}(memejamkan mata){/i} Ambil. Ambil saja." id b26_k1c

            play sound sfx_desis_pita
            $ show_cg_and_unlock("cg_barter", dissolve)

            "Dingin yang tajam menyengat telapak tangan Kai, merambat naik ke lengan, menusuk ke tengah kepalanya. Kepalanya mendadak terasa kosong — seperti ada satu halaman di buku hidupnya yang disobek bersih. Pening sebentar. Lalu hilang." id b26_024a

            scene bg_toko_dalam_malam with dissolve
            show kai datar at pos_left with dissolve
            show ageng iba at pos_right with dissolve

            kai "{i}(membuka mata, mengerutkan kening){/i} …Sudah, Pak?" id b26_025a

            play sound sfx_klik_play
            ageng "{i}(memasukkan kaset merah ke pemutar di belakang konter){/i} Sudah selesai. Pertukarannya genap." id b26_026a

            kai_hati "Aneh. Ada ruang kosong di kepalaku. Aku tahu aku kenal Yara. Aku tahu kami dekat, dekat sekali. Tapi… gimana awalnya? Di mana pertama kali kami ngomong? Kenapa kami bisa jalan bareng keliling kota? {i}(jeda){/i} Kosong. Lembaran putih. —Nggak apa-apa. Nggak apa-apa. Yang penting sekarang: putar kasetnya." id b26_027a

        "\"Beri saya waktu.\"":
            $ record_major_choice(9, "B")

            show kai cemas at pos_left
            kai "Pak… saya… {i}(tangannya gemetar, menjauh dari lemari){/i} Beri saya waktu. Saya belum bisa mutusin sekarang. Temenan, Pak. Saya takut salah pilih." id b26_017b

            show ageng iba at pos_right
            ageng "{i}(menatap Kai lama, lalu mengangguk pelan){/i} Nggih. Waktu itu juga harga, Kai. Cuma beda cara bayarnya." id b26_018b

            "Pak Ageng membuka lemari kaca, mengambil kaset merah berlabel 1 AGUSTUS, dan — di depan mata Kai — menyimpannya di bawah meja konter, di laci yang paling gampang dijangkau." id b26_019b

            ageng "Kaset ini saya simpan di sini. Sampai Jumat. Kalau sampai Jumat kamu datang dan bilang tukar, kita tukar. Kalau tidak… ya sudah. Berarti kaset ini bukan buat kamu." id b26_020b

            kai "Kalau ada orang lain yang mau beli duluan, Pak?" id b26_021b

            ageng "{i}(tersenyum tipis, sedih){/i} Di toko ini, yang datang menawar duluan bukan selalu yang paling butuh. Tapi yang ragu terlalu lama… biasanya memang kehilangan giliran. Pulanglah, Nak. Pikir baik-baik." id b26_022b

            kai_hati "Sampai Jumat. Empat hari. Empat hari buat mutusin apakah aku berani… atau apakah aku cuma nunda-nunda jadi pengecut dengan cara yang lebih sopan." id b26_023b

        "\"Nggak, Pak. Biar saya nggak tahu.\"":
            $ record_major_choice(9, "C")

            stop music fadeout 1.0
            play music bgm_toko loop fadein 1.5
            show kai biasa at pos_left
            kai "{i}(menarik tangannya dari lemari, menggeleng){/i} Nggak, Pak. {i}(suaranya pelan, tapi berhenti gemetar){/i} Biar saya nggak tahu. Kalau harga buat tenang itu kenangan paling bahagia saya… itu bukan tenang, Pak. Itu rugi." id b26_017c

            show ageng senyum at pos_right
            ageng "{i}(mengangguk pelan, seperti sudah menduga){/i} Duduk dulu. Kopinya diminum. Tanganmu masih dingin itu." id b26_018c

            "Pak Ageng membuka lemari kaca, mengambil kaset merah berlabel 1 AGUSTUS, membungkusnya dengan kain bersih, dan menyimpannya ke sebuah laci kayu di belakang konter — laci yang sama tempat ia menyimpan kaset-kaset almarhumah istrinya. Kai melihat itu. Pak Ageng tahu Kai melihat itu." id b26_019c

            ageng "Kaset ini nggak akan ditawarkan lagi. Ke kamu, ke siapa pun. Ada hal-hal yang memang lebih baik disimpan daripada dijual." id b26_020c

            kai "Pak… makasih. {i}(jeda){/i} Saya tetap takut, Pak. Soal satu Agustus. Tetap takut setengah mati." id b26_021c

            ageng "Takut itu nggak apa-apa, Nak. Yang bahaya itu kalau takutmu yang pegang kemudi. {i}(menuang kopi){/i} Wes. Minum. Cerita yang lain saja. Katanya Yara lagi ngumpulin suara apa sekarang?" id b26_022c

    return

label bab_26_tunda:
    $ chapter_autosave("bab_26_tunda", "Bab 26 (Tunda) — Jumat Berikutnya", "Ch. 26 (Delay) — Next Friday")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop fadein 1.2
    show kai cemas at pos_center with dissolve

    "Empat hari. Kai menghitungnya seperti menghitung mundur sesuatu yang meledak." id bt_001

    kai_hati "Senin: aku yakin mau tukar. Selasa: aku yakin nggak mau. Rabu: aku yakin mau lagi — jam dua pagi, pas nggak bisa tidur. Kamis… Kamis aku sadar satu hal. Aku bukan lagi mikirin kasetnya. Aku mikirin gimana caranya mutusin tanpa nyesel. Dan itu nggak ada jawabannya." id bt_002

    play sound sfx_desis_pita
    "Kaset-kaset biasa tetap dia putar tiap malam. Enam puluh detik besok, enam puluh detik besok. Aman. Terkendali. Tapi setiap desis pita berhenti, kalimat yang sama muncul lagi di kepalanya: {i}sampai Jumat.{/i}" id bt_003

    scene bg_toko_luar with dissolve
    show kai cemas at pos_center with dissolve
    "Rabu sore, kakinya bahkan sudah membawanya sampai mulut gang. Toko itu kelihatan dari sana — papan kayunya, jendelanya yang kuning. Kai berdiri sepuluh menit penuh, seperti orang menunggu sesuatu mendorongnya dari belakang." id bt_004

    kai_hati "Masuk sekarang, tukar sekarang, selesai. Nggak usah nunggu Jumat. {i}(jeda panjang; kakinya tidak bergerak){/i} …Atau masuk sekarang, bilang nggak jadi, selesai juga. {i}(menggeleng, berbalik pulang){/i} Ternyata yang nggak bisa aku lakuin bukan milihnya. Berhenti berdiri di tengah-tengahnya ini yang nggak bisa." id bt_005

    scene bg_kamar_kai_malam with dissolve
    show kai sedih at pos_center with dissolve
    "Kamis malam, ia menulis dua kalimat di kertas sobekan, melipatnya, dan membuangnya. Kalimat pertama: {i}\"Saya tukar, Pak.\"{/i} Kalimat kedua: {i}\"Nggak jadi, Pak.\"{/i} Dua-duanya masuk tempat sampah. Dua-duanya terasa bohong." id bt_006

    scene bg_gang_hujan with dissolve
    play sound sfx_hujan_deras loop fadein 0.8
    show kai cemas at pos_center with dissolve

    kai_hati "Aku datang lebih sore dari biasanya. Separuh berharap tokonya sudah tutup. Separuh lagi… nggak tahu. Pokoknya kakiku jalan sendiri ke gang ini." id bt_007

    if get_major_choice(5) == "A":

        show kai panik at pos_left with dissolve
        show kaya senyum at pos_right with dissolve
        "Di mulut gang, seorang pria berjas rapi baru saja keluar dari arah toko, membawa kantong kertas kecil. Langkahnya berhenti waktu melihat Kai." id bt_008a

        kaya "{i}(tersenyum tipis){/i} Oh. Kita bertemu lagi." id bt_009a

        kai "{i}(membeku){/i} …Bapak… dari toko?" id bt_010a

        kaya "Urusan kecil. {i}(mengangkat kantong kertasnya sedikit){/i} Barang bagus itu nggak nunggu orang yang ragu, Nak. Ingat itu. {i}(berlalu, sepatunya berkecipak di genangan){/i}" id bt_011a

        hide kaya with dissolve
        kai_hati "Kantong kertas. Ukuran kaset. Dadaku langsung dingin." id bt_012a

    else:

        "Gang sepi. Tidak ada siapa-siapa selain kucing oranye di bawah pot, yang menatap Kai seperti biasa. Tapi pintu toko terbuka, dan dari dalam terdengar suara kursi goyang — pelan, seperti habis ada tamu penting." id bt_008b

    stop sound fadeout 0.5
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    stop music fadeout 0.8
    play music bgm_toko loop fadein 1.5
    show kai cemas at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    kai "Pak… saya datang. Soal kaset merah itu, saya—" id bt_013

    ageng "{i}(mengangkat satu tangan, pelan){/i} Duduk dulu, Kai." id bt_014

    "Pak Ageng beranjak ke konter. Ia membuka laci di bawah meja — laci tempat kaset merah 1 AGUSTUS disimpan empat hari lalu. Laci itu kosong. Ia membiarkannya terbuka, supaya Kai melihat sendiri." id bt_015

    show kai sedih at pos_left
    kai "…Kosong." id bt_016

    ageng "Sudah ada yang mengambilnya." id bt_017

    if get_major_choice(5) == "A":
        kai "Pria itu, ya, Pak. Yang di gang tadi. Yang waktu itu nawar toko ini." id bt_018a

        show ageng serius at pos_right
        ageng "Dia datang Kamis sore. Bayar tanpa tanya harga. {i}(menatap Kai){/i} Dia tahu persis kenangan mana yang dia tukar. Nggak pakai ragu sama sekali. Kadang saya mikir… orang yang nggak ragu itu bukan lebih berani. Cuma lebih nggak punya yang dipertahankan." id bt_019a

    else:
        kai "Siapa, Pak? Kenal?" id bt_018b

        show ageng serius at pos_right
        ageng "Pelanggan lama. Orang berada. Dia nggak cerita banyak — orang yang menukar kenangan memang jarang cerita. {i}(menatap Kai){/i} Dia datang, dia mutusin, dia pergi. Tiga puluh menit, selesai." id bt_019b

    kai "{i}(duduk pelan-pelan, seperti kakinya baru kehilangan tenaga){/i} Jadi… selesai? Kesempatan saya… selesai?" id bt_020

    show ageng iba at pos_right
    ageng "Kesempatan buat {i}kaset itu{/i} — selesai. {i}(menuang teh, menyodorkan cangkir){/i} Dengar, Nak. Kamu empat hari nggak bisa mutusin. Itu bukan nggak ada jawaban. Itu jawabannya yang nggak berani kamu dengar." id bt_021

    kai "Maksud Bapak?" id bt_022

    show ageng senyum at pos_right
    ageng "Kalau kamu temenan kepingin tahu isi satu Agustus, kamu sudah tukar dari Senin. Yang bikin kamu maju-mundur itu bukan takut sama kasetnya. Kamu takut sama kenangan yang harus kamu bayar. Berarti kenangan itu masih lebih mahal buatmu daripada kepastian. {i}(tersenyum kecil){/i} Itu bukan kabar buruk, Kai." id bt_023

    kai_hati "Anehnya… aku lega. Lega dan malu dan kecewa, campur jadi satu, nggak bisa dipisah. Kasetnya hilang — bukan karena aku berani nolak, bukan karena aku berani ambil. Hilang karena aku kelamaan berdiri di tengah pintu." id bt_024

    kai "Pak… {i}(ragu){/i} Dia dengar apa, Pak? Dari satu Agustus itu. Dia dengar… suara apa?" id bt_025

    show ageng biasa at pos_right
    ageng "{i}(menggeleng pelan){/i} Bukan kasetmu, bukan ceritamu. Yang dia dengar itu masa depan {i}dia{/i} — dari hidupnya, dari pilihannya. Nggak ada hubungannya sama kamu. {i}(menatap Kai lurus){/i} Dan itu pelajaran terakhir dari kaset ini, Nak: satu Agustus-mu nggak pernah dijual ke siapa-siapa. Dia masih utuh. Masih belum terjadi. Masih… bisa jadi apa saja." id bt_026

    show kai biasa at pos_left
    kai "{i}(terdiam lama){/i} …Bisa jadi apa saja. {i}(tertawa pendek, nyaris tidak percaya){/i} Saya ngabisin empat hari ketakutan setengah mati — buat sesuatu yang ternyata memang nggak bisa dibeli orang." id bt_027

    kai "Terus sekarang gimana, Pak? Satu Agustus tetap datang. Saya tetap nggak tahu apa-apa." id bt_028

    show ageng senyum at pos_right
    ageng "Ya dijalani. Kayak orang kebanyakan. Kayak Yara — dia juga nggak tahu besoknya gimana, tapi dia tetap berangkat ngumpulin suara tiap sore. {i}(berdiri, merapikan rak){/i} Wes, minum tehmu. Habis ini pulang. Kalau besok ke sini lagi, jangan bawa wajah kayak habis kehilangan kereta. Keretanya memang sudah lewat — tapi stasiunnya masih buka." id bt_029

    kai_hati "Stasiunnya masih buka. {i}(jeda){/i} Aku nggak dapat kepastianku. Tapi entah kenapa, waktu jalan pulang lewat gang itu, langkahku nggak seberat biasanya. Mungkin karena untuk pertama kalinya… besok beneran milik besok lagi. Bukan milik kaset." id bt_030

    stop music fadeout 1.2
    return

label bab_27_merah:
    $ chapter_autosave("bab_27_merah", "Bab 27 — Tangis yang Tersedot Magnetik", "Ch. 27 — Tears Drawn Into Tape")

    scene bg_toko_dalam_malam with dissolve
    stop music fadeout 0.8
    play sound sfx_klik_play
    show kai panik at pos_left with dissolve
    show ageng iba at pos_right with dissolve

    "Pak Ageng menekan tombol play. Suara mekanisnya keras sekali di toko yang sunyi. Kai memasang headphone. Jantungnya berdegup seperti mau keluar." id b27r_001

    kai_hati "Enam puluh detik. Tawa dia. Tolong, biar yang keluar tawa dia. Atau suara jalanan Malang, atau apa pun — asal bukan—" id b27r_002

    play sound sfx_desis_pita
    kai_hati "Kosong…? Sepuluh detik kok kos—" id b27r_003

    play music bgm_cemas loop fadein 1.5
    "Bukan tawa. Bukan kereta, bukan air mendidih. Itu suara orang menangis — dekat sekali, sampai Kai bisa dengar kain jaketnya bergesek. Jaket yang dia kenal." id b27r_004

    kai_hati "Itu… itu Yara. Itu suara Yara nangis." id b27r_005

    call play_cassette(
        cassette_id="kaset_tangis_yara",
        label_title=_("Kaset Merah — 1 Agustus"),
        transcript_lines=[
            (_("Yara (dari kaset)"), _("{i}(bergetar, pecah di ujung kalimat){/i} Jaga diri baik-baik ya, Kai…")),
            (None, _("[Jeda panjang — rintik hujan di latar belakang rekaman.]")),
            (_("Yara (dari kaset)"), _("Selamat tinggal.")),
        ],
        duration_sec=8,
        allow_skip=True,
    )

    play sound sfx_klik_play
    show kai menangis at pos_left with vpunch
    "Keheningan toko kembali. Kai menurunkan headphone pelan-pelan. Tangannya gemetar hebat — alat itu hampir jatuh ke konter. Wajahnya pucat. Tenaganya seperti habis disedot mesin pemutar barusan." id b27r_006

    kai "{i}(tercekat){/i} Kenapa… {i}(menatap Pak Ageng, matanya kosong){/i} Kenapa dia nangis, Pak? Kenapa harus ada kata selamat tinggal?" id b27r_007

    ageng "{i}(tidak langsung menjawab; mengeluarkan kaset merah dari pemutar, menyodorkannya ke Kai){/i} Kaset nggak pernah bohong, Kai. Tapi ingat — suara yang kamu dengar itu akibat dari jalan yang kamu pilih hari ini. Sekarang kaset ini kamu bawa. Sama lubang baru di ingatanmu itu." id b27r_008

    kai_hati "Aku bayar pakai kenangan terindahku… buat ini. Buat dengar dia nangis. Buat dengar \"selamat tinggal\". Kepastian yang aku kejar-kejar ternyata isinya begini." id b27r_009

    menu:
        "Kai masih memegang kaset merah itu. Apa yang dia lakukan di toko, sebelum pulang?"

        "Ke wastafel di belakang toko, cuci muka.":
            $ record_minor_choice("m16", "A")
            "Airnya dingin sekali. Kai membasuh wajahnya tiga kali, empat kali, sampai napasnya berhenti lompat-lompat. Di cermin kecil yang retak di sudut, wajahnya asing — tapi setidaknya sudah tidak gemetar." id b27r_010a
            ageng "{i}(dari arah konter, pelan){/i} Air memang paling jujur, Nak. Dia nggak janji apa-apa. Cuma dingin, terus lewat." id b27r_011a

        "Duduk di lantai toko, punggung bersandar ke rak.":
            $ record_minor_choice("m16", "B")
            play sound sfx_derit_kursi_goyang loop fadein 0.8
            "Kai merosot duduk di lantai kayu, di antara rak-rak kaset, memeluk lutut. Pak Ageng tidak menyuruhnya bangun. Ia hanya kembali ke kursi goyangnya dan membiarkan derit kayu itu menemani — pelan, teratur, seperti bilang: toko ini nggak buru-buru." id b27r_010b
            stop sound fadeout 0.6

        "Memutar satu kaset biasa. Asal ada suara.":
            $ record_minor_choice("m16", "C")
            play sound sfx_klik_play
            queue sound sfx_desis_pita
            "Dengan tangan masih gemetar, Kai memasukkan kaset biasa ke Walkman-nya dan menekan play. Enam puluh detik suara besok — suara kantin, suara bel, suara biasa. Anehnya, suara-suara membosankan itu yang menenangkannya. Besok masih ada. Besok yang dekat, yang kecil, masih ada." id b27r_010c

    stop music fadeout 1.0
    return

label bab_27_sehat:
    $ chapter_autosave("bab_27_sehat", "Bab 27 — Pengumuman", "Ch. 27 — The Announcement")

    scene bg_teras_toko with dissolve
    play music bgm_senja loop fadein 1.5
    show kai biasa at pos_left with dissolve

    "Sore itu tidak ada apa-apa yang istimewa. Dan justru itu yang akan diingat Kai lama sekali: hari besar ternyata sering datang dengan wajah hari biasa." id b27s_001

    show yara ceria at pos_right with dissolve
    yara "{i}(datang dengan langkah cepat, tas kanvas dan perekam di tangan, napasnya agak habis){/i} Kai. Kamu di sini. Untung. Aku mau cerita — jangan pasang muka gitu dulu, ini kabar bagus. Harusnya." id b27s_002

    kai "Kabar apa? Kamu lari dari mana, napasmu—" id b27s_003

    yara "Dari sekolah. Barusan diumumin hasil seleksi berkas. {i}(duduk di undakan teras, menatap Kai, senyumnya lebar tapi matanya waswas){/i} Portofolioku lolos, Kai. Universitas di Yogya itu… mereka nerima aku. Program studi desain suara. Kalau nggak ada halangan, aku berangkat habis kelulusan. Awal Agustus." id b27s_004

    kai_hati "Yogya. Awal Agustus. Satu Agustus. Tanggal itu tetap datang — cuma sekarang dia datang dari mulut Yara sendiri, bukan dari pita kaset. Dan anehnya… rasanya beda. Nggak dingin. Nggak kayak vonis. Lebih kayak… berita. Berita besar yang harus aku dengar dari orangnya langsung." id b27s_005

    show kai senyum at pos_left
    kai "{i}(menarik napas, lalu tersenyum — dipaksakan di detik pertama, tapi jadi beneran di detik kedua){/i} …Selamat, Yar. Serius. Itu yang kamu kejar dari dulu, kan? Suara-suara ini semua— {i}(menunjuk perekamnya){/i} —buat ini." id b27s_006

    show yara penasaran at pos_right
    yara "{i}(menatap Kai lekat-lekat){/i} Kamu nggak kaget?" id b27s_007

    kai "Kaget. {i}(jeda){/i} Tapi kamu cerita langsung ke aku. Itu… makasih. Maksudku — makasih sudah cerita langsung." id b27s_008

    show yara ceria at pos_right
    yara "Ya jelas cerita langsung. Kamu pikir aku mau ngumumin lewat apa, lewat kaset? {i}(tertawa kecil, lalu suaranya melembut){/i} Aku juga takut, Kai. Kota baru, kos sendirian, nggak ada yang aku kenal. Tapi aku kepingin banget. Kepinginnya sudah lama." id b27s_009

    kai "Aku tahu. Kelihatan kok, dari cara kamu ngumpulin suara kayak ngumpulin bekal." id b27s_010

    yara "Ngomong-ngomong soal bekal. {i}(mengangkat perekamnya){/i} Aku mau bikin satu rekaman terakhir sebelum berangkat. Semacam… peta suara Malang. Semua tempat yang kita datangi. Biar di Yogya nanti, kalau kangen, aku tinggal putar." id b27s_011

    kai "Kita?" id b27s_012

    yara "Ya kita. Kamu pikir aku kuat bawa tripod sendirian naik Bukit Banyak lagi? {i}(berdiri, menepuk celananya dari debu){/i} Mulai besok. Sore-sore, kayak biasa. Kamu temani aku sampai hari terakhir. Janji?" id b27s_013

    kai "{i}(jeda sebentar — ada rasa sesak yang datang, tapi kali ini ia tidak lari darinya){/i} …Janji." id b27s_014

    kai_hati "Enam bulan. Kurang, malah. Dia akan pergi, dan itu pasti, dan itu sakit — tapi sakitnya sakit yang wajar. Bukan tangis di dalam kaset. Bukan teka-teki. Cuma… waktu yang jalan. Dan aku masih punya sisa waktu itu buat diisi, bukan buat dicemasi." id b27s_015

    show ageng senyum at pos_center with dissolve
    "Pak Ageng keluar dari dalam toko membawa dua cangkir teh, seperti sudah mendengar dari tadi — mungkin memang sudah." id b27s_016

    ageng "Ada yang lolos seleksi, katanya. {i}(menyodorkan cangkir ke Yara){/i} Selamat, Nak. Yogya itu jauh… tapi suara di sana bagus-bagus. Kereta, pasar pagi, hujan di atap kos. Kamu bakal betah ngumpulinnya." id b27s_017

    yara "{i}(menerima cangkir, tersenyum lebar){/i} Makasih, Pak. Nanti dari sana aku kirimi rekaman, deh. Biar toko ini punya koleksi suara luar kota." id b27s_018

    ageng "{i}(melirik Kai, pelan){/i} Didengar baik-baik nanti, Kai. Ada suara yang datangnya cuma sekali." id b27s_019

    kai_hati "Aku tahu maksudnya. Dan untuk sekali ini, aku nggak lari dari maksud itu." id b27s_020

    hide ageng with dissolve
    yara "{i}(sudah berjalan beberapa langkah, menoleh){/i} Eh, jangan bengong. Pulang bareng. Sekalian mampir warung rawon, aku traktir. Merayakan." id b27s_021

    kai "{i}(berdiri, menyusul){/i} Ditraktir pakai uang beasiswa yang belum cair?" id b27s_022

    yara "Pakai uang sakuku. Makanya jangan pesan yang mahal-mahal." id b27s_023

    stop music fadeout 1.2
    return

label bab_28_merah:
    $ chapter_autosave("bab_28_merah", "Bab 28 — Lubang di Peta Ingatan", "Ch. 28 — A Hole in the Memory Map")

    scene bg_kamar_kai with dissolve
    play music bgm_cemas loop fadein 1.5
    show kai datar at pos_center with dissolve

    if cond_k1 == "A":

        "Kai terbangun dengan sentakan, seperti baru jatuh dari tempat tinggi. Kamarnya sama persis: kertas-kertas di meja, jam digital, dan wadah mika merah tergeletak di sampingnya." id b28_001a

        kai_hati "Ada yang salah. Aku tahu ada yang salah sebelum aku tahu apanya." id b28_002a

        "Dia duduk di tepi kasur, memegang kepalanya yang berdenyut ringan. Lalu ia mulai memeriksa ingatannya satu-satu, seperti orang memeriksa saku setelah kecopetan." id b28_003a

        kai_hati "Yara. Aku tahu siapa dia. Anak kelas sebelah, ngoleksi suara bising dunia. Kami jalan bareng keliling kota. Bawa tripod. Makan rawon di pinggir rel pas hujan. Semua fakta itu ada. Rapi. Logis. {i}(jeda){/i} Tapi awalnya… gimana awalnya?" id b28_004a

        "Ia mencoba mengingat perpustakaan kota. Ia tahu ia pernah ke sana. Ia tahu ada kejadian — tumpukan buku ensiklopedia jatuh berserakan di depan kakinya. Tapi kenapa buku itu jatuh? Siapa yang menjatuhkannya? Bagaimana wajah Yara waktu mata mereka pertama kali bertemu di balik debu sore itu?" id b28_005a

        kai_hati "Kosong. Nggak ada gambar. Nggak ada suara buku jatuh. Nggak ada debar itu — debar waktu aku sadar aku nggak jadi mati. {i}(menatap tangannya sendiri){/i} Logikaku tahu dia penting. Dadaku… nggak ngerasain apa-apa. Kayak baca biografi orang lain yang namanya sama denganku." id b28_006a

        "Kai beranjak ke meja belajar. Jemarinya menyentuh wadah kaset merah itu — di dalam gulungan pitanya, tersimpan potongan dirinya yang paling berharga, dibarter demi rasa aman yang ternyata berisi tangisan." id b28_007a

        kai_hati "Aku nukar rasa debar yang bikin aku hidup… sama rekaman dia bilang selamat tinggal. {i}(duduk merosot di kursi, menatap keluar jendela){/i} Mahal banget. Mahal banget, Kai." id b28_008a

    elif cond_k1 == "B":

        "Kai terbangun dengan sentakan. Wadah mika merah di samping jam digital. Dan satu kekosongan yang bentuknya aneh — bukan di awal cerita, tapi di tengah-tengahnya." id b28_001b

        kai_hati "Aku tahu kami pernah makan rawon di pinggir rel. Faktanya ada: warung tenda, hujan deras, kereta lewat bikin sendok bergetar. Yara cerita itu terus." id b28_002b
        kai_hati "{i}(jeda){/i} Tapi rasa kuahnya… hangatnya… dia ketawa kepedesan sambal… {i}(menggeleng pelan){/i} Nggak ada. Kayak ada yang motong satu adegan dari film dan nyambungin ujung-ujungnya begitu saja. Jahitannya rapi. Adegan-nya yang hilang." id b28_002b_p2

        kai "{i}(duduk merosot, menatap wadah kaset){/i} Jadi ini yang aku bayar. Sore paling hangat yang aku punya… buat dengar dia nangis. {i}(jeda panjang){/i} Pantes Pak Ageng bilang mahal." id b28_003b

    else:

        "Kai terbangun dengan sentakan. Wadah mika merah di samping jam digital. Di luar jendela, angin pagi menggerakkan tirai — dan di situlah kosongnya terasa." id b28_001c

        kai_hati "Bukit Banyak. Aku tahu kami pernah ke sana. Fotonya ada di HP-ku — aku lihat sendiri: aku, dia, tripod, kota di bawah. {i}(menatap foto itu lama){/i} Tapi anginnya… teriakan kecilnya waktu hampir jatuh, megangin tripod… rasa lega pas sadar dunia itu luas dan aku nggak takut… {i}(jeda){/i} Nggak ada. Yang tersisa cuma fotonya. Bukti tanpa rasa." id b28_002c

        kai "{i}(menatap wadah kaset di meja){/i} Aku nukar hari aku berani… sama rekaman hari dia pergi. {i}(tertawa pendek, getir){/i} Dagang yang bagus, Kai. Dagang yang bagus sekali." id b28_003c

    if get_minor_choice("m16") == "A":
        kai_hati "Semalam di toko, aku cuci muka sampai airnya habis dinginnya. Pagi ini kepalaku jernih — dan justru karena jernih, lubang ini kelihatan jelas banget bentuknya." id b28_009a
    elif get_minor_choice("m16") == "B":
        kai_hati "Semalam aku duduk lama di lantai toko, nggak ngomong apa-apa. Pak Ageng juga nggak. Pagi ini punggungku pegal — dan itu satu-satunya rasa yang jelas. Sisanya… lubang." id b28_009b
    else:
        kai_hati "Semalam aku dengar suara besok yang biasa-biasa saja, dan itu nenangin aku. Pagi ini aku bangun dan sadar: besok yang biasa itu tetap jalan. Yang hilang cuma kemarin yang paling penting." id b28_009c

    return

label bab_29_merah:
    $ chapter_autosave("bab_29_merah", "Bab 29 — Menjauh Demi Melindungi", "Ch. 29 — Pulling Away to Protect")

    scene bg_kelas with dissolve
    play music bgm_cemas loop if_changed
    show kai datar at pos_left with dissolve

    "Suara tangis di kaset merah itu berputar di kepala Kai seperti piringan rusak. Setiap isak, setiap jeda, dan dua kata itu: {i}selamat tinggal.{/i} Dan kepala Kai yang dingin menarik kesimpulan paling pahit yang bisa ia temukan." id b29r_001

    kai_hati "Aku penyebabnya. Pasti aku. Kalau aku tetap dekat dia, aku cuma nganter dia ke tangisan itu. Aku ini variabel rusak. Kalau aku minggir… dia bisa pergi dengan senyum. Bukan dengan nangis. {i}(jeda){/i} Kedengarannya kayak melindungi. Aku tahu. Aku tahu itu cuma kedengarannya saja." id b29r_002

    "Maka dimulailah rumusnya. Berangkat lebih pagi supaya tidak berpapasan di gerbang. Istirahat tidak lagi ke koridor kelas sebelah. Dan hari ini: pura-pura tidur, kepala menelungkup di meja kelas yang sepi. Lalu — langkah kaki yang dia kenal. Dan aroma sisa gerimis dan sabun tipis." id b29r_003

    show yara biasa at pos_right with dissolve
    yara "Kai. {i}(pelan){/i} Kenapa pesanku nggak dibalas? Sore ini kita mau rekam suara mesin bubut di bengkel dekat stasiun, kan? Aku sudah pinjam baterai cadangan." id b29r_004

    "Dada Kai sesak seperti dihimpit. Ia ingin mendongak. Ia ingin mengambil tas kanvas itu dan pergi merekam seperti biasa. Tapi suara tangis di kaset menamparnya bangun." id b29r_005

    kai "{i}(mengangkat kepala pelan-pelan; wajahnya datar, matanya kosong){/i} Maaf, Yara. Aku sibuk. Aku harus mulai fokus belajar buat ujian akhir. Aku nggak bisa bantuin bawa barang-barang lagi." id b29r_006

    show yara sedih at pos_right
    yara "{i}(tertegun){/i} Fokus belajar? {i}(mengulanginya dengan nada getir){/i} Kemarin kita masih ketawa di puncak bukit, Kai. Ada apa denganmu, sebenarnya?" id b29r_007

    kai "{i}(mengalihkan pandang ke papan tulis){/i} Nggak ada apa-apa. Aku cuma sadar waktu kita nggak banyak. Dan kurasa… kamu juga harus fokus sama portofoliomu sendiri. Tanpa diganggu aku." id b29r_008

    hide yara with dissolve
    "Yara mematung beberapa detik. Hening di antara mereka kali ini bukan hening yang membisukan karena kagum — ini hening yang dingin dan tajam, dan sesuatu retak pelan-pelan di dalamnya. Tanpa satu kata lagi, Yara berbalik dan pergi. Derap sepatunya berat." id b29r_009

    scene bg_gerbang_sekolah with dissolve
    play sound sfx_hujan_deras loop fadein 0.8
    show kai datar at pos_left with dissolve

    "Hari-hari berikutnya rumusnya dijalankan dengan disiplin yang kejam. Memutar balik di koridor. Bersembunyi di bilik toilet sampai bel berbunyi." id b29r_010
    "Menunduk ke HP yang tidak penting waktu berpapasan di tangga — sementara tatapan Yara mengikutinya, penuh tanda tanya, penuh luka yang mulai terbuka. Sampai sore ini, Yara menghadangnya di gerbang belakang yang sepi." id b29r_010_p2

    show yara marah at pos_right with dissolve
    yara "Kenapa kamu kayak gini, Kai? {i}(berdiri tepat di depannya, tas tersampir lunglai di satu bahu){/i} Kalau aku punya salah, bilang. Jangan diam kayak pengecut dan pura-pura nggak kenal aku. Kita sudah sejauh ini!" id b29r_011

    kai_hati "Ceritain. Ceritain saja soal kaset merah konyol itu. Ceritain, dan selesai. {i}(jeda — lalu lubang di kepalanya membuka){/i} …Tapi aku bahkan nggak ingat gimana kami mulai. Debar pertamaku saja sudah nggak ada. Yang tersisa cuma takut sama tangisnya di satu Agustus. Dan mulutku memilih kalimat yang paling aman buat rasa takut itu." id b29r_012

    kai "{i}(menatap Yara lurus, memaksa matanya tetap dingin){/i} Nggak ada yang salah, Yara. Aku cuma sadar… kita memang nggak pernah benar-benar cocok. Kamu hidup di duniamu yang penuh suara." id b29r_013
    kai "Aku… lebih suka kesunyianku yang dulu. Nemenin kamu keliling kota kemarin itu cuma pengalih perhatian yang menyenangkan. Sementara. Tapi sekarang… mulai terasa melelahkan." id b29r_013_p2

    show yara menangis at pos_right
    "Setiap kata itu mengiris dua dada sekaligus. Yara mundur satu langkah. Wajahnya memucat; matanya berkaca-kaca kena cahaya senja." id b29r_014

    yara "{i}(berbisik, pecah di ujungnya){/i} Sebuah pengalih perhatian yang menyenangkan…? {i}(tertawa getir, menghapus air mata dengan punggung tangan){/i} Kamu benar-benar orang paling egois yang pernah aku temui, Kai." id b29r_015

    hide yara with dissolve
    "Yara berbalik dan berjalan pergi menembus gerimis. Kai berdiri mematung di bawah gerbang, membiarkan hujan membasahi wajahnya yang mati rasa." id b29r_016

    show kai sedih at pos_center with dissolve
    kai_hati "Logika bodohku bilang aku barusan ngelakuin hal yang benar. Memotong benangnya lebih awal, biar perpisahan nanti nggak terlalu sakit. {i}(jeda lama){/i} Terus kenapa dadaku rasanya kayak lagi mati pelan-pelan… di dalam kesunyian yang aku bikin sendiri?" id b29r_017

    stop sound fadeout 0.8
    return

label bab_29_sehat:
    $ chapter_autosave("bab_29_sehat", "Bab 29 — Menghindari Topik Itu", "Ch. 29 — Avoiding That Topic")

    scene bg_koridor_sekolah with dissolve
    play music bgm_sekolah loop fadein 1.2
    play sound sfx_kelas loop fadein 0.6
    show kai cemas at pos_left with dissolve
    show yara ceria at pos_right with dissolve

    "Kabar Yara lolos seleksi menyebar cepat — begitulah sekolah. Dan Kai menemukan fakta menyebalkan tentang dirinya: ia bisa tersenyum dan bilang selamat di depan Yara, tapi ia tidak sanggup mendengar detailnya." id b29s_001

    yara "{i}(menenteng map berisi formulir){/i} Kai, kamu tahu kos-kosan di Yogya itu harus survei dari—" id b29s_002

    kai "{i}(terlalu cepat){/i} Eh, aku harus ke kelas. Bu Sarah nyariin. {i}(berjalan pergi){/i}" id b29s_003

    hide kai with dissolve
    show yara penasaran at pos_right
    yara "{i}(menatap punggungnya){/i} …Bu Sarah nggak ngajar hari ini." id b29s_004

    stop sound fadeout 0.5
    "Besoknya: jadwal kereta. Lusanya: formulir pendaftaran ulang. Setiap topik yang berbau Yogya, Kai punya pintu keluar. Dan Yara — yang biasanya merekam semua suara — mulai merekam juga pola yang satu ini: suara langkah Kai yang pergi." id b29s_005

    scene bg_teras_toko with dissolve
    stop music fadeout 0.8
    play music bgm_senja loop fadein 1.5
    show kai sedih at pos_left with dissolve
    show yara biasa at pos_right with dissolve

    yara "{i}(duduk di undakan, tidak membawa perekam sore ini){/i} Aku perhatiin, lho. Tiap aku bilang \"Yogya\", kamu jadi sibuk. Sibuknya mendadak. Kayak bel sekolah, tapi yang bunyi kamu." id b29s_006

    kai "{i}(terdiam; tidak membantah){/i} …" id b29s_007

    yara "Aku nggak marah. Aku cuma mau tahu. Kamu senang aku lolos, kan?" id b29s_008

    kai "Senang. Temenan senang. {i}(jeda lama){/i} Cuma… tiap kamu cerita detailnya, di kepalaku langsung kebayang peron stasiun. Dan aku belum siap kebayang itu tiap hari. Jadi aku kabur. Sepurane, Yar." id b29s_009

    show yara ceria at pos_right
    yara "{i}(menatapnya, lalu mengangguk kecil){/i} Oke. Makasih sudah bilang — yang ini jangan dikabur-kaburin lagi. {i}(berdiri, mengulurkan tangan){/i} Besok kita tetap rekam peta suara. Topik Yogya-nya… kita cicil. Sedikit-sedikit. Kayak kamu dengerin kaset. Enam puluh detik sekali dengar." id b29s_010

    show kai senyum at pos_left
    kai_hati "Enam puluh detik sekali dengar. {i}(tersenyum tipis){/i} Dia memang selalu tahu cara bikin hal besar jadi ukuran yang bisa aku telan." id b29s_011

    stop music fadeout 1.0
    return

label bab_30_merah:
    $ chapter_autosave("bab_30_merah", "Bab 30 — Rekaman yang Kehilangan Detak", "Ch. 30 — Recordings That Lost Their Pulse")

    scene bg_kamar_yara with dissolve
    play music bgm_cemas loop if_changed
    show yara sedih at pos_center with dissolve

    "Malam itu Yara memutar ulang semua rekaman mereka. Angin Bukit Banyak. Derit pintu perpustakaan. Ketukan besi kereta tua. Dan di sela-selanya, selalu ada napas Kai yang teratur di dekatnya — atau tawanya yang samar waktu mereka hampir kesandung tripod." id b30r_001

    yara "{i}(melepas headphone kasar, melemparnya ke meja; berbisik ke kamar yang sunyi){/i} Dia kaku sekali. Kayak ada bagian dari dirinya yang mendadak… hilang. {i}(jeda){/i} Orang nggak berubah sedingin itu dalam semalam. Kecuali ada yang diambil dari dia. Atau dia ngambil sesuatu." id b30r_002

    scene bg_gerbang_sekolah with dissolve
    show kai datar at pos_left with dissolve
    show yara sedih at pos_right with dissolve

    "Sepulang sekolah, Yara menunggu di dekat parkiran yang mulai sepi. Kai datang menunduk, tas tersandang. Yara melangkah menghadang — di tangan kanannya perekam portabel dan mikrofon saku." id b30r_003

    yara "Kai. {i}(menjaga suaranya tetap tenang, walau bergetar){/i} Hari ini di dekat pasar loak ada toko pandai besi tua, masih pakai palu manual. Suara benturan besinya ritmis banget — kayak detak jantung purba. Ayo berburu suara denganku. Sekali ini saja." id b30r_004

    "Kai berhenti. Ia menatap mikrofon itu, lalu wajah Yara. Yara melangkah lebih dekat, menyodorkan mikrofon ke arah dada Kai." id b30r_005

    show yara menangis at pos_right
    yara "{i}(suaranya pecah){/i} Dengar. Alat ini bisa nangkap frekuensi paling sunyi sekalipun. Tapi kenapa pas aku lihat kamu sekarang… aku nggak bisa dengar apa-apa lagi dari dirimu? Kamu kayak kaset kosong yang sudah terhapus, Kai." id b30r_006

    kai_hati "Kaset kosong yang sudah terhapus. {i}(jeda — kalimat itu menghantam tepat di lubang di kepalanya){/i} Dia nggak tahu betapa tepatnya itu. Sebagian dari aku memang sudah terhapus. Di atas konter toko itu. Pakai tanganku sendiri." id b30r_007

    kai "{i}(mengepalkan tangan di saku, melangkah melewatinya, tanpa menoleh){/i} Maaf, Yara. Rekaman kita sudah selesai." id b30r_008

    hide kai with dissolve
    "Yara berdiri mematung di tengah parkiran yang sunyi, ditemani angin sore yang hampa. Dan Kai berjalan pulang dengan kalimat gadis itu menempel di kepalanya seperti pita yang tidak mau berhenti berputar: {i}kaset kosong yang sudah terhapus.{/i}" id b30r_009

    scene bg_kamar_kai_malam with dissolve
    show kai sedih at pos_center with dissolve

    kai_hati "Kaset kosong. Terhapus. {i}(duduk lama, lalu mengambil perekam kecil pinjaman dari Yara yang belum sempat ia kembalikan){/i} …Kalau aku sudah kayak kaset kosong, harusnya gampang dibuktiin. Kosong itu bunyinya kayak apa, sih?" id b30r_010

    menu:
        "Kai dan perekam kecil itu, malam ini."

        "Merekam detak jantungnya sendiri.":
            $ record_minor_choice("m17", "A")
            play sound sfx_klik_play
            "Ia menempelkan mikrofon ke dadanya. Di headphone: {i}dug… dug… dug…{/i} — tidak teratur, terlalu cepat, seperti orang habis lari. Atau orang yang ketakutan." id b30r_011a
            kai_hati "Ada. Detaknya masih ada. Berantakan, tapi ada. {i}(jeda){/i} Berarti aku belum kosong. Berarti yang hilang itu bukan detaknya. Cuma… lagunya. —Rekaman ini aku simpan. Mungkin suatu hari aku berani kasih dengar ke dia." id b30r_012a

        "Merekam jam dinding kamarnya.":
            $ record_minor_choice("m17", "B")
            play sound sfx_klik_play
            "Tik. Tik. Tik. Enam puluh detik penuh, tidak ada yang lain. Kai memutarnya ulang dua kali." id b30r_011b
            kai_hati "Waktu jalan terus, rapi, nggak peduli. Mungkin itu bedanya aku sama jam. Jam nggak pernah takut sama menit berikutnya. {i}(jeda){/i} Rekaman ini aku simpan. Buat pengingat: diam pun ternyata berbunyi." id b30r_012b

        "Tidak merekam apa-apa.":
            $ record_minor_choice("m17", "C")
            "Kai menatap perekam itu lama, lalu meletakkannya kembali ke laci, pelan-pelan, seperti takut bunyinya kedengaran siapa-siapa." id b30r_011c
            kai_hati "Nggak. Malam ini nggak. Kalau aku rekam dan hasilnya beneran kosong… aku nggak siap dengar buktinya." id b30r_012c

    return

label bab_30_sehat:
    $ chapter_autosave("bab_30_sehat", "Bab 30 — Toko yang Sepi, Dengan Cara yang Benar", "Ch. 30 — A Shop Quiet in the Right Way")

    scene bg_gang_kering with dissolve
    play music bgm_toko loop fadein 1.5
    show kai biasa at pos_center with dissolve

    kai "{i}(berhenti di mulut gang, menatap tanah){/i} …Kering. Pak, gangnya kering. Tumben banget." id b30s_001

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    show kai senyum at pos_left with dissolve
    show ageng senyum at pos_right with dissolve

    ageng "{i}(dari dalam toko){/i} Sepurane, Nak. Kayaknya gang ini lagi libur hujan. {i}(tersenyum){/i} Masuk. Toko lagi sepi. Sepinya beneran, bukan sepi yang kamu bikin-bikin." id b30s_002

    kai "{i}(tersenyum kecil, masuk){/i} Bapak bisa saja." id b30s_003

    "Tidak ada pelanggan lain sore itu. Kai membantu Pak Ageng menata ulang rak kaset biasa — pekerjaan lambat yang tidak menuntut apa-apa dari kepalanya." id b30s_004

    ageng "Yang Type I di kiri. Yang labelnya tulisan tangan, jangan dicampur sama cetakan pabrik. {i}(jeda, menatap Kai){/i} Kamu kelihatan lebih ringan akhir-akhir ini. Masih ke sini tiap hari, tapi nggak kayak orang ngejar sesuatu." id b30s_005

    kai "Masih takut, Pak. Soal Agustus. {i}(menggeser satu kotak kaset){/i} Bedanya… sekarang takutnya nggak nyetir. Dia duduk di kursi belakang. Kadang berisik. Tapi tanganku yang di kemudi." id b30s_006

    ageng "{i}(mengangguk pelan, puas){/i} Itu kalimat paling dewasa yang pernah saya dengar dari kamu, Nak. {i}(berdiri, mengambil dua cangkir){/i} Teh. Habis ini Yara katanya mau mampir — mau nunjukin daftar suara buat peta Malangnya. Kamu tunggu, kan?" id b30s_007

    kai "Tunggu, Pak. {i}(tersenyum){/i} Sisa waktu ini… mau aku pakai buat hadir beneran. Bukan buat ngintip dari kaset." id b30s_008

    "Di luar, gang yang kering mulai diwarnai cahaya senja. Toko itu sepi — dengan cara yang benar: bukan karena ditinggalkan, tapi karena sedang menunggu, dengan tenang, orang-orangnya datang." id b30s_009

    return
