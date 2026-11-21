label bab_05:
    $ chapter_autosave("bab_05", "Bab 5 — Hening", "Ch. 5 — Silence")

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.2

    "Kamis sore. Gerimis lagi. Kai menyusuri gang buntu yang sama, jaketnya basah di bagian bahu. Rutinitas ini sudah hafal di luar kepala: masuk, serahkan uang, terima kaset, pulang." id b05_001

    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve
    ageng "Yang biasa?" id b05_002

    kai "Yang biasa, Pak. {i}(menyerahkan uang){/i} Buat besok." id b05_003

    ageng "{i}(mengambil kaset berlabel hari Jumat, menyerahkan){/i} Ini. Jumatmu." id b05_004

    show kai senyum at pos_left
    kai "Makasih, Pak. {i}(memasukkan kaset ke tas, setengah tersenyum){/i} Kalau sudah pegang ini, pulangnya agak tenang." id b05_005

    show kai cemas at pos_left
    kai_hati "Agak. Nggak pernah benar-benar tenang, sih. Tapi ya… lumayan. Kayak pegang payung. Besok mau hujan kayak apa pun, seenggaknya aku sudah tahu duluan." id b05_006

    stop music fadeout 1.0
    scene bg_kamar_kai_malam with dissolve
    show kai biasa at pos_center with dissolve

    "Hujan sudah berhenti total. Di luar cuma ada suara jangkrik. Kai duduk di tepi kasur, kaset hari Jumat di tangan. Ritualnya mulai: eject, masukkan kaset, klik." id b05_007

    kai_hati "Oke. Besok Jumat. Bakal ada apa, ya? Paling-paling omelan Ibu. Atau Bu Sarah lagi. Atau… ya sudah, dengar saja." id b05_008

    menu:
        "Kai memutar kaset itu bagaimana?"

        "Pakai headphone, seperti biasa.":
            $ record_minor_choice("m04", "A")
            "Bantalan headphone yang retak menutup kedua telinganya. Dunia luar hilang. Tinggal dia dan pita itu." id b05_009a

        "Lewat speaker Walkman.":
            $ record_minor_choice("m04", "B")
            "Kai tidak memasang headphone. Biar suara kaset itu mengisi kamar, pikirnya. Biar nggak sendirian dengarnya — walaupun yang menemani cuma speaker kecil yang cempreng." id b05_009b

    "Jarinya menekan tombol play." id b05_010

    call play_cassette(
        cassette_id="kaset_hening_60detik",
        label_title=_("Kaset Hari Jumat — 60 Detik"),
        transcript_lines=[
            (None, _("[60 detik hening]")),
            (None, _("[Desis pita… white noise… lima detik… sepuluh detik… detik kelima belas desis berhenti — lalu tidak ada suara apa pun.]")),
        ],
        duration_sec=60,
        allow_skip=True,
    )

    play music bgm_cemas loop fadein 1.5
    show kai cemas at pos_center
    kai_hati "Desis dulu, biasa. Satu… lima… sepuluh detik. Kok belum ada suara orang, ya?" id b05_011

    "Detik kelima belas, desis itu putus. Dan yang menggantikannya bukan percakapan. Bukan bising jalan. Bukan apa-apa." id b05_012

    kai "{i}(membuka mata, mengerutkan kening){/i} …Eh?" id b05_013

    "Dia menekan kabel headphone-nya, memutar colokannya di Walkman. Barangkali longgar. Tapi lampu indikator masih menyala merah. Roda pitanya masih berputar, konstan, di balik kaca plastik." id b05_014

    show kai panik at pos_center
    kai "Volumenya… {i}(memutar roda volume sampai mentok){/i} …Nggak ada. Kok nggak ada?!" id b05_015

    "Tidak ada deru angin. Tidak ada gesekan kain. Tidak ada klakson jauh, tidak ada daun, tidak ada apa pun. Dan yang paling bikin perutnya dingin: tidak ada suara napas. Di kaset mana pun sebelumnya, mikrofon ajaib itu selalu menangkap napasnya. Selalu. Bukti dia masih ada." id b05_016

    "Kali ini: ruang hampa. Kosong. Beku." id b05_017

    if get_minor_choice("m04") == "B":
        "Keheningan itu tumpah ke seluruh kamar — dan anehnya terasa lebih keras daripada suara mana pun yang pernah keluar dari speaker kecil itu." id b05_018b

    kai_hati "Jangan berhenti muter. Jangan— maksudku, terus saja, nanti juga ada suara. Nanti juga—" id b05_019

    play sound sfx_klik_play
    "Empat puluh lima detik keheningan terasa seperti selamanya. Kai mencabut headphone-nya dengan tangan bergetar hebat dan melemparnya ke kasur, seperti benda itu baru saja menyetrumnya." id b05_020

    show kai panik at pos_center with vpunch
    kai "{i}(terengah-engah){/i} Hah… hah… nggak. Nggak, nggak, nggak." id b05_021

    "Udara kamar tiba-tiba terasa tipis. Keringat dingin turun di pelipisnya. Kepalanya yang memang selalu ramai kini berpacu liar, menyusun satu-satunya kesimpulan yang masuk akal buat remaja yang sedang kalut." id b05_022

    kai_hati "Kaset itu selalu merekam besok. Selalu. Kalau besok nggak ada suaraku… nggak ada napasku… {i}(menelan ludah){/i} …berarti besok aku sudah nggak ada. Besok aku mati." id b05_023

    return

label bab_06:
    $ chapter_autosave("bab_06", "Bab 6 — Bukti Kehidupan", "Ch. 6 — Proof of Life")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop if_changed
    show kai panik at pos_center with dissolve

    "Kamar itu mendadak terasa seperti ruang kedap udara. Kata \"mati\" berdengung di kepala Kai, berulang-ulang, seperti pita yang tersangkut." id b06_001

    kai_hati "Mati. Besok. Gimana caranya? Kecelakaan di jalan? Jantungku berhenti di kelas? Atau langit-langit kamar ini runtuh pas aku tidur? Yang mana? Yang mana?!" id b06_002

    play sound sfx_klik_play
    "Dia butuh jangkar. Sesuatu buat menambatkan kepalanya yang mau lepas. Dengan gerakan patah-patah, Kai menyambar Walkman di kasur. Kaset hari esok itu dia eject dengan kasar dan dia buang ke sudut ruangan, seperti selongsong plastik itu memancarkan radiasi." id b06_003

    kai "{i}(mengais laci meja){/i} Kaset kosong… kaset kosong… di mana— nah. Ini." id b06_004

    "Pita cadangan usang, yang biasa dia pakai merekam lagu acak dari radio. Dia harus memastikan alat rekamnya masih berfungsi. Dia harus dengar napasnya sendiri. Sekarang. Sebagai bukti dia masih hidup." id b06_005

    "Tangannya gemetar terlalu hebat. Jari-jarinya kaku dan dingin. Kaset itu meleset dari Walkman dan membentur lantai. Kai ikut jatuh berlutut, memungutnya dengan napas memburu. Matanya perih — bukan sedih, tapi frustrasi dan takut yang sudah nggak tertampung." id b06_006

    show kai menangis at pos_center
    kai "{i}(berbisik, memaksa tangannya diam){/i} Diam… diam, tanganku. Sekali ini saja. Diam." id b06_007

    play sound sfx_klik_play
    "Napas dalam. Kali ini pintu Walkman tertutup. Ibu jarinya menekan tombol merah REC dan PLAY bersamaan. Klik, keras." id b06_008

    play sound sfx_desis_pita
    "Kai mendekatkan Walkman itu ke bibirnya. Dia membuka mulut lebar-lebar. Maksudnya meneriakkan namanya sendiri. Atau menyanyikan lagu apa saja. Apa pun, asal ada suaranya di dunia ini." id b06_009

    "Tidak ada yang keluar." id b06_010

    "Pita suaranya seperti tercekat. Bibirnya bergetar, rahangnya kaku. Yang lolos cuma napas putus-putus dan isakan tertahan." id b06_011

    kai_hati "Nggak bisa. Aku nggak bisa ngomong. {i}(memeluk Walkman itu){/i} Aku takut. Kalau aku paksa bersuara, terus aku putar balik… dan yang kudengar tetap hening kayak kaset tadi… aku nggak sanggup. Aku nggak sanggup dengarnya." id b06_012

    show kai sedih at pos_center
    "Walkman itu berhenti direkam. Kai masih di lantai. Kepalanya berputar mencari satu hal — satu saja — yang bisa membuktikan malam ini dia benar-benar ada." id b06_013

    menu:
        "Apa yang Kai lakukan?"

        "Mengambil foto langit dari jendela.":
            $ record_minor_choice("m05", "A")
            "Dengan tangan masih gemetar, Kai mengangkat HP-nya ke jendela. Langit malam Malang bersih sehabis hujan, bintangnya kelihatan satu-satu. Klik. Foto itu tersimpan — bergetar sedikit, tapi nyata. Ada tanggal dan jamnya di sudut layar." id b06_014a
            kai_hati "Ini. Ini buktinya. Malam ini, jam segini, aku masih di sini. Aku yang memotret ini." id b06_015a

        "Menulis di buku kecilnya.":
            $ record_minor_choice("m05", "B")
            "Kai meraih buku catatan kecil di meja dan pulpen yang tintanya hampir habis. Dia menulis besar-besar, hurufnya miring dan berantakan: {i}\"Aku masih di sini. Kamis malam. Tanganku gemetar, tapi ini tulisan tanganku.\"{/i}" id b06_014b
            kai_hati "Tulisanku. Nggak ada orang lain yang nulis ini. Berarti aku… masih ada. Masih." id b06_015b

        "Tidak melakukan apa-apa.":
            $ record_minor_choice("m05", "C")
            "Kai tidak meraih apa-apa. Dia hanya memeluk lututnya lebih erat. Biarlah. Kalau memang tidak ada bukti yang bisa dia pegang, setidaknya rasa takut ini nyata — dan orang mati tidak bisa takut." id b06_014c
            kai_hati "…Takut ini buktinya, kan? Aku takut, berarti aku masih hidup. Iya, kan?" id b06_015c

    "Malam itu terasa panjang sekali. Kai meringkuk di lantai kamarnya, memeluk lutut erat-erat. Mengetahui jadwal kematian sendiri, ternyata, adalah kutukan paling kejam yang pernah dia beli — dan dia membelinya pakai uang saku." id b06_016

    return

label bab_07:
    $ chapter_autosave("bab_07", "Bab 7 — Tafsir Bisu Sebuah Jeda", "Ch. 7 — Silent Reading of a Pause")

    scene bg_gang_hujan with dissolve
    play music bgm_cemas loop if_changed

    "Pagi belum benar-benar datang waktu Kai sudah berlari menembus sisa embun. Napasnya tersengal, dadanya mau meledak — dia tidak peduli. Pintu toko didorongnya kasar sampai loncengnya berdenting panik." id b07_001

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    show kai panik at pos_left with vpunch
    show ageng biasa at pos_right with dissolve

    kai "Pak! Ini maksudnya apa?!" id b07_002

    "Suaranya pecah, bergema di antara rak-rak yang sunyi. Kaset berlabel hari Jumat itu dia banting ke meja kasir. Tangannya masih gemetar. Wajahnya sembap — dia tidak tidur semalaman." id b07_003

    kai "Kenapa kaset ini hening, Pak?! Kenapa nggak ada suara apa pun setelah detik kelima belas?! Bapak jual kaset rusak ke saya, ya?!" id b07_004

    "Pak Ageng tidak terkejut. Dia bahkan tidak berhenti mengelap pemutar pita tua di belakang konter. Tatapannya tenang sekali, seperti kemarahan Kai cuma riak kecil di permukaan telaga." id b07_005

    stop music fadeout 1.2
    play music bgm_toko loop fadein 1.5
    show ageng senyum at pos_right

    $ show_item("item_lemper")
    ageng "{i}(mengeluarkan bungkusan daun pisang dari wadah bambu di bawah meja, menyodorkan){/i} Makan dulu." id b07_006

    show kai cemas at pos_left
    kai "Pak, saya nggak—" id b07_007

    show ageng biasa at pos_right
    ageng "Makan dulu. Perut kosong itu bikin kepala tambah berisik." id b07_008

    "Kai ingin menolak. Dia ingin terus berteriak. Tapi aroma gurih daun pisang yang hangat dan ketenangan orang tua itu melucuti amarahnya satu per satu. Dengan tangan gemetar dia membuka bungkusan itu: lemper ayam, masih sangat hangat." id b07_009

    show kai sedih at pos_left
    kai "{i}(menggigit; ketan pulen dan ayam manis-gurih memenuhi mulutnya){/i} …" id b07_010

    "Untuk sejenak, teror semalam mereda. Ada rasa nyata di lidahnya. Kakinya masih berpijak di bumi." id b07_011

    $ hide_item()
    "Setelah gigitan terakhir ditelan, Pak Ageng mengambil kaset itu dan memutarnya di jari-jarinya yang keriput." id b07_012

    show ageng serius at pos_right
    ageng "Kaset nggak pernah bohong, Nak. {i}(menatap lurus ke mata Kai){/i} Tapi telinga manusia sering salah dengar. Kamu dengar keheningan itu sebagai akhir. Padahal keheningan bisa berarti banyak hal." id b07_013

    show kai cemas at pos_left
    kai "Banyak hal gimana, Pak? Itu kosong. Kosong total. Nggak ada napas saya, nggak ada—" id b07_014

    show ageng biasa at pos_right
    ageng "Keheningan nggak selalu berarti nggak ada apa-apa. Kadang dia jeda. Kadang… dia puncak." id b07_015

    "Kai menatap kaset di tangan Pak Ageng. Kepalanya masih menolak. Tapi beban di dadanya — sedikit saja — bergeser. Sekarang giliran Kai yang memutuskan: keheningan itu apa?" id b07_016

    menu:
        "Apa kata Kai?"

        "\"Itu kematianku, Pak. Saya tahu itu.\"":
            $ record_major_choice(2, "A")
            "Pak Ageng tidak membantah. Tidak juga mengiyakan. Dia hanya beranjak, berjalan ke pemutar radio di sudut toko, dan mematikannya." id b07_017a
            stop music fadeout 0.3
            play sound sfx_klik_play
            ageng "{i}(pelan){/i} Hening juga, kan, toko ini? Tapi kita masih di sini." id b07_018a
            "Kai tidak menjawab. Hening toko dan hening kaset itu kini menumpuk di telinganya jadi satu." id b07_019a

        "\"Mungkin… mungkin itu cuma jeda, ya, Pak?\"":
            $ record_major_choice(2, "B")
            show ageng senyum at pos_right
            ageng "{i}(tersenyum tipis){/i} Nah. Coba dengarkan lagi. Hening itu bukan akhir lagu, Nak. Lagu yang bagus pun punya jeda — di situ justru orang menahan napas." id b07_017b
            play sound sfx_klik_play
            queue sound sfx_desis_pita
            "Pak Ageng memasukkan kaset itu ke pemutar toko dan menekan play. Desis… lalu hening. Tapi kali ini Kai tidak menutup telinga. Untuk pertama kalinya, dia mendengarkan keheningan itu sampai habis — dan tidak takut." id b07_018b
            play sound sfx_klik_play
            show kai biasa at pos_left
            kai "{i}(menghela napas panjang){/i} …Selesai juga. Ternyata bisa didengar sampai selesai." id b07_019b

        "\"Lupakan, Pak. Anggap nggak pernah terjadi.\"":
            $ record_major_choice(2, "C")
            show kai sedih at pos_left
            kai "Saya nggak mau mikirin itu lagi. Beneran. Saya capek." id b07_017c
            "Kai mengambil kaset itu dari konter… lalu, tanpa berkata apa-apa, berjalan ke rak paling belakang toko dan menyelipkannya di antara kaset-kaset yang paling berdebu. Paling jauh dari jangkauan mata." id b07_018c
            show ageng iba at pos_right
            ageng "{i}(mengamati, tidak melarang){/i} Wes. Kalau itu yang kamu butuhkan sekarang." id b07_019c
            "Tapi Kai tahu — dan Pak Ageng juga tahu — dia akan menghindari rak itu berminggu-minggu." id b07_020c

    show ageng biasa at pos_right
    play music bgm_toko loop if_changed
    if get_major_choice(2) == "C":
        ageng "Pulanglah. Jalani Jumatmu. Jangan sampai ketakutanmu bikin kamu tuli duluan — sebelum suaranya benar-benar datang." id b07_021c
        kai "{i}(setengah membungkuk){/i} …Iya, Pak. Makasih lempernya." id b07_022c
    else:
        ageng "Pulanglah. Jalani Jumatmu. {i}(menyerahkan kembali kaset itu){/i} Jangan sampai ketakutanmu bikin kamu tuli duluan — sebelum suaranya benar-benar datang." id b07_021
        kai "{i}(memasukkan kaset ke saku, setengah membungkuk){/i} …Iya, Pak. Makasih lempernya." id b07_022

    play sound sfx_derit_kursi_goyang loop fadein 0.5
    "Di belakang Kai, kursi goyang Pak Ageng berderit lagi. Pelan. Teratur. Seperti waktu di toko itu memang bergerak dengan tempo sendiri — dan untuk pagi ini, tempo itu cukup untuk membuat Kai bisa melangkah pulang." id b07_023

    return

label bab_08:
    $ chapter_autosave("bab_08", "Bab 8 — Surat-Surat yang Tak Sempat Terbaca", "Ch. 8 — Letters Never Read")

    scene bg_toko_dalam with dissolve
    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve
    play music bgm_toko loop if_changed
    play sound sfx_derit_kursi_goyang loop if_changed

    "Sebelum benar-benar pulang, langkah Kai terhenti di dekat rak rendah samping kasir. Di sana, diikat tali rafia yang sudah rapuh, ada seikat surat-surat tua. Kertasnya menguning, amplopnya ditulis tangan. Satu amplop paling atas terbuka sedikit." id b08_001

    menu:
        "Apa yang Kai lakukan?"

        "Membaca satu surat lama itu.":
            $ record_minor_choice("m06", "A")
            "Kai melirik Pak Ageng — orang tua itu pura-pura sibuk dengan kursi goyangnya. Pelan-pelan, Kai menarik amplop teratas. Surat di dalamnya ditulis dengan huruf tegak yang rapi, oleh tangan yang jauh lebih muda." id b08_002a
            call show_letter(
                cg_id="cg_surat_lama",
                letter_title=_("Surat Tua — Toko Gema Masa"),
                paragraphs=[
                    _("Radionya baru selesai diperbaiki sore ini. Suaranya sudah jernih lagi, tidak berdesis seperti kemarin."),
                    _("Hujan di kota ini belum juga reda sejak minggu lalu, tapi entah kenapa rasanya tidak terlalu dingin."),
                    _("\"Tunggu aku pulang. Nanti kita dengarkan sama-sama.\""),
                    _("— S."),
                ],
                paper_bg="#f2e4c4df",
            )
            "Tidak ada nama pengirim selain satu huruf di ujung surat. Kai melipatnya kembali dengan hati-hati, persis seperti semula. Mendadak Pak Ageng terasa bukan cuma pemilik toko aneh — dia pernah muda, pernah menunggu, pernah ditunggu." id b08_002a_p3
            kai_hati "…Siapa yang nulis ini? Atau… buat siapa? {i}(menggeleng){/i} Bukan urusanku. Tapi anehnya, toko ini jadi terasa lebih… manusiawi." id b08_003a

        "Tidak menyentuh surat orang.":
            $ record_minor_choice("m06", "B")
            kai_hati "Itu surat orang. Bukan buatku. {i}(menarik tangannya){/i} Aku saja nggak mau surat-suratku dibaca orang." id b08_002b
            stop sound fadeout 0.4
            "Kai membetulkan ikatan rafia yang miring itu — hanya itu — lalu berbalik ke pintu. Di belakangnya, derit kursi goyang berhenti sebentar. Pak Ageng tidak bilang apa-apa. Tapi sepertinya dia memperhatikan." id b08_003b

    stop sound fadeout 0.4
    stop music fadeout 1.2
    scene bg_kamar_kai_malam with dissolve
    play music bgm_hujan_malam loop fadein 1.5
    play sound sfx_jam_dinding
    show kai sedih at pos_center with dissolve

    "Sejak pulang dari toko, waktu terasa seperti hitung mundur yang berdetak di dalam kepala. Debu yang menari di bawah lampu, retakan kecil di langit-langit, detak jam — semuanya seperti saksi bisu. Kai memandang kamarnya bukan lagi sebagai tempat aman. Ini museum kecil, dan dia akan segera meninggalkannya." id b08_004

    kai_hati "Kalau besok aku beneran nggak ada… aku nggak mau Ibu nemu kamarku berantakan kayak gini. Nggak mau orang lihat… potongan-potongan aku yang acak-acakan ini." id b08_005

    "Tengah malam, dia mulai. Kardus-kardus besar ditarik dari kolong kasur. Satu per satu, tujuh belas tahun hidupnya dipilah." id b08_006

    kai "{i}(mengangkat tumpukan majalah game yang menguning){/i} Ini… buang. {i}(mengambil koleksi bungkus permen dari toples){/i} Ini juga. Dulu kupikir berharga banget. Ternyata cuma sampah yang kusimpan rapi." id b08_007

    "Kertas coretan berisi lirik lagu galau yang tak pernah selesai — masuk kantong hitam. Buku harian SMP yang penuh keluhan kekanak-kanakan — masuk. Foto-foto lama berekspresi konyol — masuk. Dan di dasar laci: tumpukan surat cinta yang tidak pernah dia berani kirimkan ke siapa pun, selama ini." id b08_008

    kai "{i}(memegang tumpukan surat itu lama){/i} …Yang ini juga. Nggak akan pernah terkirim juga, kan. {i}(memasukkannya ke kantong hitam, pelan){/i} Setidaknya… aku ingin diingat sebagai versi yang lebih rapi." id b08_009

    scene bg_kamar_kai_malam with dissolve
    play sound sfx_tulis_pena
    show kai sedih at pos_center with dissolve

    "Kamarnya sekarang lebih luas. Lebih kosong. Kai duduk di meja belajar, mengeluarkan beberapa lembar kertas putih bersih dan pulpen tinta hitam yang masih penuh. Dia mulai menulis. Bukan tugas. Bukan catatan harian. Surat perpisahan — yang tidak akan pernah dia kirimkan." id b08_010

    call show_letter(
        cg_id="cg_surat_perpisahan",
        letter_title=_("Surat yang Tidak Akan Terkirim — Kai"),
        paragraphs=[
            _("Bu, maaf aku sering terlalu tertutup. Susah dimengerti. Terlalu sibuk sama benda-benda kuno yang Ibu anggap nggak penting…"),
            _("Terima kasih sudah membiarkanku hidup dalam duniaku sendiri, meski Ibu tidak pernah benar-benar paham isinya."),
            _("— — —"),
            _("Dan buat Kai yang dulu: maaf kita kebanyakan takutnya soal masa depan, sampai lupa caranya bernapas lega di masa sekarang. Padahal hari-hari biasa itu… lumayan, sebenarnya."),
        ],
        paper_bg="#f6f1e6e0",
    )

    "Surat-surat itu dilipat rapi dan dimasukkan ke laci meja paling bawah, di balik tumpukan kaset kosong. Mungkin tidak akan pernah dibaca siapa pun. Mungkin membusuk di sana. Tapi bagi Kai, menulis adalah cara terakhir meninggalkan jejak suara di atas kertas — sebelum keheningan yang dia dengar itu benar-benar datang menjemput." id b08_016

    kai_hati "{i}(merebahkan kepala ke meja){/i} …Sudah. Kamarku rapi. Suratku selesai. Kalau besok memang hari terakhirku… {i}(memejamkan mata){/i} …setidaknya aku sudah pamit. Diam-diam." id b08_017

    "Malam itu, untuk pertama kalinya setelah sekian lama, Kai tertidur dengan kamar yang rapi. Tapi hatinya tetap sesak oleh gema yang tak kunjung reda." id b08_018

    return
