label bab_09:
    $ chapter_autosave("bab_09", "Bab 9 — Bahagia yang Menikam Dada", "Ch. 9 — Joy That Pierces the Chest")

    scene bg_gang_hujan with dissolve
    stop music fadeout 1.0
    play sound sfx_hujan_deras loop fadein 0.8

    "Sore itu langit di atas gang Gema Masa abu-abu semua, seperti kanvas ketumpahan cat. Gerimis masih setia menyiram aspal. Kai berdiri mematung di depan pintu kayu toko — tangannya sudah setengah terangkat mau meraih gagang pintu — waktu pintu itu tiba-tiba terbuka dari dalam." id b09_001

    play sound sfx_lonceng_pintu
    "Seorang wanita muda keluar dengan langkah terhuyung, seperti dunia di bawah kakinya baru saja berubah jadi awan. Bahunya berguncang hebat. Ia menangis sesenggukan, mendekap sebuah kaset erat-erat di dadanya — seperti benda plastik itu adalah jantungnya yang baru saja kembali berdetak." id b09_002

    show kai cemas at pos_center with dissolve
    kai "{i}(tersentak mundur, memberi jalan){/i} Eh— silakan, Mbak…" id b09_003

    "Kai sudah siap melihat wajah penuh duka — ekspresi yang rasanya akan sangat akrab dengan nasibnya sendiri. Tapi saat wanita itu melewatinya, yang ia lihat beda: di balik air mata yang tumpah, wanita itu tersenyum. Cerah sekali. Murni sekali. Seperti gang sempit ini mendadak dapat matahari tambahan." id b09_004

    show kai cemas at pos_left with ease
    show npc_wanita at pos_right with dissolve
    wanita "{i}(berbisik pelan, seperti bicara pada dirinya sendiri){/i} Dia ada, Mas… Dia benar-benar ada. Aku mendengarnya. Dia menangis… suaranya kencang sekali." id b09_005

    hide npc_wanita with dissolve
    "Wanita itu berjalan terus, masih terisak, masih tersenyum. Lewat pintu yang belum tertutup rapat, Kai melihat Pak Ageng berdiri di balik konter, menatap punggung wanita itu — diam, dengan binar mata orang yang sudah tahu semuanya." id b09_006

    kai_hati "Dia habis dengar kaset. Dan dia nangis… bahagia. Dua-duanya barengan. Gimana bisa?" id b09_007

    play music bgm_cemas loop fadein 1.5
    play sound sfx_hujan_deras loop fadein 0.5
    show kai sedih at pos_center with ease

    "Belakangan Kai tahu kisah wanita itu. Bertahun-tahun ia menunggu sebuah keajaiban yang tak kunjung datang. Hampir menyerah pada rahimnya yang sunyi." id b09_008
    "Lalu di toko ini — lewat kaset yang dibayar dengan harga yang cuma ia dan Pak Ageng yang tahu — ia mendengar suara dari masa depan: tangisan pertama seorang bayi. Bayinya. Beberapa bulan lagi." id b09_008_p2

    kai_hati "Dia dengar suara kehidupan yang baru mau mulai. Lagu paling indah yang pernah dia dengar, katanya. Terus aku? Aku dengar… nggak ada apa-apa. Hening. Total. Yang oleh kepalaku diterjemahkan jadi: tamat." id b09_009

    kai_hati "Toko yang sama. Kaset yang sama-sama enam puluh detik. Buat dia surga, buat aku neraka. {i}(jeda){/i} Kontrasnya… nyesek banget. Bahagia orang lain kok bisa kerasa kayak ditikam, ya." id b09_010

    "Kai tidak jadi masuk. Ia tidak sanggup menghadapi tenangnya Pak Ageng sore ini. Ia berbalik dan berjalan menembus hujan yang mulai deras." id b09_011

    stop sound fadeout 0.8
    scene bg_kamar_kai_malam with dissolve
    show kai sedih at pos_center with dissolve

    "Di rumah, ruang keluarga lagi hangat-hangatnya. Ibu dan Ayah tertawa menonton acara di TV. Bau makan malam masih tertinggal di udara. Pemandangan yang biasa sekali — dan malam ini, rasanya jauh sekali dari Kai." id b09_012

    menu:
        "Kai berdiri di ambang ruang keluarga. Apa yang dia lakukan?"

        "Ikut duduk, ikut tertawa bersama.":
            $ record_minor_choice("m07", "A")
            show npc_ibu at pos_left with dissolve
            ibu "Eh, Kai pulang. Basah semua itu bajunya. Makan dulu, gih. Acara ini lucu banget — Ayahmu tadi sampai—" id b09_013a
            show npc_ayah at pos_right with dissolve
            ayah "{i}(tertawa){/i} Sampai keselek kerupuk. Nggak usah dilanjutin." id b09_014a
            "Kai duduk di ujung sofa. Ia ikut tertawa — kecil, telat setengah detik dari yang lain, tapi tertawa. Ibu menyodorkan piring tanpa banyak tanya." id b09_015a
            show kai biasa at pos_center
            kai_hati "Ketawa. Buat mereka gampang. {i}(jeda){/i} Buat aku… harusnya juga bisa. Harusnya." id b09_016a

        "Memotret diam-diam.":
            $ record_minor_choice("m07", "B")
            "Dari ambang pintu, Kai mengangkat ponselnya. Satu foto: Ibu dan Ayah lagi tertawa, candid, tidak tahu sedang difoto." id b09_013b
            kai_hati "Buat jaga-jaga. Kalau Jumat nanti aku… {i}(menggeleng cepat){/i} Kalau aku nggak sempat lihat pemandangan kayak gini lagi, paling nggak ada buktinya. Pernah ada malam kayak gini." id b09_014b

        "Menyingkir ke kamar.":
            $ record_minor_choice("m07", "C")
            ibu "{i}(dari ruang keluarga){/i} Kai? Kamu pulang? Makan dulu, Nak—" id b09_013c
            kai "{i}(dari jauh){/i} Udah, Bu. Kenyang. Mau istirahat aja." id b09_014c
            "Bohong. Perutnya kosong sejak siang. Tapi kakinya sudah membawanya masuk kamar sebelum ada yang sempat menahan." id b09_015c

    scene bg_kamar_kai_malam with dissolve
    show kai sedih at pos_center with dissolve

    "Kamarnya sudah rapi. Terlalu rapi untuk kamar anak tujuh belas tahun: buku tersusun, meja bersih — dan di atas meja, sebuah amplop putih tertutup rapat. Kai duduk di lantai kamarnya, bersandar, menatap langit-langit dengan mata lelah." id b09_017

    if get_minor_choice("m05") == "A":
        "Ia membuka galeri ponselnya. Foto langit sore dari beberapa hari lalu masih ada di sana — oranye, tenang, tidak tahu apa-apa soal hari Jumat." id b09_018a
        kai_hati "Langitnya masih sama. Yang berubah cuma aku." id b09_019a
    elif get_minor_choice("m05") == "B":
        "Dari laci meja, ia mengambil buku kecilnya dan membukanya ke halaman yang ia tulis beberapa hari lalu. Tulisan tangannya sendiri, pendek saja." id b09_018b
        kai_hati "\"Hari ini aku masih di sini.\" {i}(jeda){/i} …Iya. Hari ini masih." id b09_019b
    else:
        "Tidak ada foto. Tidak ada catatan. Meja bersih, ingatan kosong dari hal-hal baik. Kai menatap langit-langit, mencoba memanggil satu hal bagus dari minggu ini — dan yang datang malah hening dari kaset itu." id b09_018c
        kai_hati "Kosong. Kayak kasetku." id b09_019c

    "Ia membayangkan tangisan bayi yang didengar wanita tadi — kencang, hidup, baru saja dimulai. Lalu membandingkannya dengan keheningan di kasetnya sendiri. Tiba-tiba keheningan itu terasa jauh lebih bising daripada teriakan apa pun." id b09_020

    show kai cemas at pos_center
    kai_hati "Jumat. Jam empat sore. {i}(menelan ludah){/i} Langkah kaki raksasa. Pelan, tapi pasti. Datang buat nginjak aku." id b09_021

    return

label bab_10:
    $ chapter_autosave("bab_10", "Bab 10 — Pelarian ke Ruang Sunyi", "Ch. 10 — Escape to a Quiet Room")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop if_changed
    show kai cemas at pos_center with dissolve

    if get_minor_choice("m07") == "A":
        kai_hati "Tawa Ibu sama Ayah semalam masih nempel di kepala. Hangat. …Terus aku ingat hari ini hari apa." id b10_001a
    elif get_minor_choice("m07") == "B":
        kai_hati "Foto semalam masih kebuka di ponselku. Ibu, Ayah, lagi ketawa. …Terus aku ingat hari ini hari apa." id b10_001b
    else:
        kai_hati "Sunyi. Dari semalam sampai bangun, sunyi terus. …Dan hari ini Jumat." id b10_001c

    "Hal pertama yang Kai rasakan saat terbangun adalah detak jantungnya sendiri — memukul-mukul keras tulang rusuknya, napasnya memburu. Tangannya meraba dada. Masih berdetak. Ia menoleh ke meja: jam digital menyala merah. 05.00. Matahari bahkan belum sepenuhnya mengusir malam." id b10_002

    kai "{i}(berbisik){/i} …Hidup. Aku masih hidup." id b10_003

    "Lega itu cuma bertahan tiga detik. Karena Kai tahu persis jam berapa \"kejadian\" di kaset itu: pukul 16.00. Masih ada sebelas jam membentang di depannya — seperti lorong eksekusi." id b10_004

    scene bg_kelas with dissolve
    stop music fadeout 0.8
    play music bgm_sekolah loop fadein 1.2
    play sound sfx_kelas loop fadein 0.8
    show kai sedih at pos_center with dissolve

    "Pagi itu Kai memaksakan diri berangkat ke sekolah dengan langkah diseret. Di koridor, di kelas, tatapannya kosong. Badannya duduk di bangku, tapi jiwanya sudah berdiri di ujung tebing. Suara tawa teman-temannya, derit kursi, coretan kapur guru — semua cuma dengungan lebah di telinganya." id b10_005

    show kai sedih at pos_left with ease
    show npc_teman1 at pos_right with dissolve
    teman "Kai, kamu nggak apa-apa? Pucet banget, lho." id b10_006

    kai "…Nggak apa-apa. Kurang tidur aja." id b10_007

    teman "Oh. Ya udah, istirahat yang cukup, ya. {i}(pergi){/i}" id b10_008

    hide npc_teman1 with dissolve
    show kai cemas at pos_center with ease
    kai_hati "Makin siang, kepalaku makin nggak karuan. Skenarionya muter terus: kalau memang hari ini, pasti di tempat ramai. Kecelakaan di jalan raya yang padat. Atap gedung olahraga runtuh. Bahaya bisa datang dari arah mana saja kalau orangnya banyak." id b10_009

    kai_hati "Aku nggak mau matiku jadi tontonan. Kalau memang harus pergi hari ini… aku mau menghilang dengan tenang." id b10_010

    stop sound fadeout 0.6
    scene bg_gerbang_sekolah with dissolve
    show kai cemas at pos_center with dissolve

    "Bel pulang berbunyi. Kegiatan ekskul hari ini bolos — Kai sudah memutuskan. Ia berjalan cepat menyusuri trotoar, matanya awas mengamati setiap mobil yang melintas, setiap tiang listrik yang kelihatan rapuh. Ia butuh satu tempat: yang paling minim risiko, tanpa benda berbahaya, tanpa kerumunan." id b10_011

    menu:
        "Ke mana Kai bersembunyi menunggu jam 16.00?"

        "Perpustakaan Kota.":
            $ record_minor_choice("m08", "A")
            kai_hati "Perpustakaan Kota. Gedung lama. Sore-sore sepi pengunjung — anak muda mending ke kafe atau mal. Nggak ada kendaraan, nggak ada kerumunan. Di sana." id b10_012a
            "Ia melangkah lurus ke sana, tidak menoleh-noleh lagi." id b10_013a

        "Ke UKS dulu.":
            $ record_minor_choice("m08", "B")
            scene bg_koridor_sekolah with dissolve
            show kai cemas at pos_center with dissolve
            "Kai berbaring di ranjang UKS dengan alasan pusing. Sepuluh menit pertama tenang. Lalu datang dua anak kelas sebelah yang heboh, perawat yang bolak-balik, bel yang bunyi, tawa dari koridor." id b10_012b
            kai_hati "Nggak bisa. Di sini terlalu banyak orang. Terlalu banyak suara. Kalau terjadi sesuatu… semua bakal lihat." id b10_013b
            "Ia pamit dengan alasan sudah mendingan — lalu berjalan cepat ke satu tempat yang dari tadi ada di kepalanya: Perpustakaan Kota." id b10_014b

        "Ke atap sekolah.":
            $ record_minor_choice("m08", "C")
            scene bg_koridor_sekolah with dissolve
            show kai cemas at pos_center with dissolve
            "Atap sekolah kosong. Anginnya kencang. Kota membentang di bawah — dan kepala Kai langsung mengisinya dengan semua cara buruk untuk terjatuh." id b10_012c
            kai_hati "…Tempat terbuka. Tinggi. Angin. Bodoh. Ini bukan tempat sembunyi. Ini undangan." id b10_013c
            "Ia turun lagi dengan napas pendek-pendek, lalu berjalan cepat ke Perpustakaan Kota." id b10_014c

    stop music fadeout 1.0
    scene bg_perpustakaan with dissolve
    play music bgm_cemas loop fadein 1.5
    show kai cemas at pos_center with dissolve

    "Kai mendorong pintu kaca perpustakaan. Udara sejuk beraroma kertas usang dan debu halus menyambutnya. Di dalam sini begitu senyap, seolah waktu berjalan lebih lambat." id b10_015

    "Ia menyusuri lorong di antara rak-rak kayu jati yang menjulang tinggi hingga hampir menyentuh langit-langit. Terus berjalan, sampai sudut paling tersembunyi di perpustakaan ini: di balik barisan rak ensiklopedia yang jarang disentuh orang." id b10_016

    if get_minor_choice("m08") == "A":
        "Dalam perjalanan ke sudut itu, matanya sempat menangkap sesuatu di dekat jendela kaca besar di ujung ruangan: sebuah kursi kayu — dan di sampingnya, sebuah tas peralatan terbuka, tergeletak rapi. Seperti ada yang sudah lebih dulu menandai tempat itu." id b10_017a
        kai_hati "Ada orang lain…? {i}(menggeleng){/i} Biarin. Selama dia jauh dari sudutku, bukan urusanku." id b10_018a

    "Di sana Kai duduk meringkuk di sebuah kursi kayu. Menjauh dari jendela, dari rak buku yang berpotensi menimpanya, dari segala kemungkinan buruk. Ia mengunci pandangannya pada jam di pergelangan tangannya." id b10_019

    kai_hati "15.30. {i}(menelan ludah){/i} Tiga puluh menit lagi. Tiga puluh menit menuju hening total. …Oke. Di sini aku. Tempat paling aman yang bisa kupikirkan. Kalau memang harus datang — datang saja." id b10_020

    return

label bab_11:
    $ chapter_autosave("bab_11", "Bab 11 — Gema Jatuh yang Membisukan", "Ch. 11 — The Falling Echo That Silences")

    scene bg_perpustakaan with dissolve
    play music bgm_cemas loop if_changed
    show kai cemas at pos_center with dissolve

    "Lantai kayu perpustakaan yang tua berderit pelan setiap Kai bergeser, seperti ikut memprotes gerakannya. Di antara barisan rak ensiklopedia yang tebal dan berdebu, waktu terasa seperti cairan kental — sulit mengalir. Udara dingin dan bau kertas lapuk membungkus tubuhnya, memberi perlindungan semu dari dunia luar yang ia anggap berbahaya." id b11_001

    kai_hati "15.50. Sepuluh menit lagi. {i}(menekan tombol ponselnya sekali lagi — layarnya tetap gelap){/i} Udah mati. Nggak ada getaran, nggak ada suara mendadak. Cuma aku sama jam." id b11_002

    kai_hati "Di kepalaku, aku sudah bilang selamat tinggal ke semuanya. Berulang-ulang. {i}(jeda){/i} Anehnya yang paling kusesali malah hal-hal kecil. Amplop putih itu — surat wasiat konyol yang kutulis sendiri. Umur tujuh belas, nulis surat wasiat. Kalau ada yang tahu, aku diketawain seumur hidup. …Kalau aku masih punya sisa umur, maksudnya." id b11_003

    "Sebuah pergerakan di ujung lorong rak menarik perhatiannya. Beberapa meter dari tempatnya duduk, seorang gadis sebaya berdiri dengan posisi yang sangat aneh." id b11_004

    show kai biasa at pos_left with dissolve
    show yara fokus at pos_right with dissolve

    "Gadis itu memakai headphone besar yang menutupi telinganya. Tangannya memegang sebuah tongkat panjang dengan mikrofon berbulu di ujungnya — boom mic — yang ia arahkan teliti sekali ke jendela kaca besar di ujung ruangan." id b11_005
    "Jendela itu sedang bergetar hebat: di luar, sebuah truk besar baru saja melintas, meninggalkan gemuruh yang menggetarkan fondasi bangunan tua ini." id b11_005_p2

    "Gadis itu tidak tampak takut. Ia justru sangat fokus — seolah sedang memburu sesuatu yang sangat berharga dari getaran kaca tersebut." id b11_006

    if get_minor_choice("m08") == "A":
        kai_hati "…Kursi dekat jendela itu. Tas peralatan yang tadi kulihat. Punya dia. Dia sudah di sini dari tadi — sama kayak aku, \"bersembunyi\" di perpustakaan. Bedanya, dia nggak kelihatan takut sama sekali." id b11_007a

    kai_hati "Siapa dia? Di saat aku lagi hitung mundur detik-detik terakhirku, dia malah sibuk sama dunianya sendiri — penuh alat rekam. {i}(jeda){/i} Orang bisa beda banget, ya." id b11_008

    hide yara with dissolve
    show kai panik at pos_center with dissolve
    stop music fadeout 1.0

    "Jam tangan Kai menunjukkan pukul 16.00. Tepat." id b11_009

    kai_hati "Ini dia. {i}(memejamkan mata rapat-rapat; mencengkeram pinggiran kursi sampai buku-buku jarinya memutih){/i} Selamat tinggal. Selamat—" id b11_010

    show kai panik at pos_center with vpunch
    "Kai tersentak hebat di kursinya. Matanya terbuka cepat — dan ia masih bisa melihat cahaya matahari sore yang masuk lewat celah rak. Masih bisa merasakan dinginnya udara. Jantungnya berdegup begitu kencang hingga telinganya berdenging. Berdegup. Masih berdegup." id b11_011

    kai "{i}(berbisik, gemetar){/i} …Aku masih… masih bisa lihat. Masih bisa napas. Aku masih—" id b11_012

    "Di depan tempatnya duduk, tumpukan buku-buku tebal berserakan di lantai. Rupanya tumpukan itu jatuh dari meja di sampingnya — karena getaran truk tadi, atau tersenggol tanpa sengaja. Dan di balik tumpukan buku itu, berdiri gadis dengan boom mic tadi." id b11_013

    $ show_cg_and_unlock("cg_perpustakaan_debu", dissolve)

    "Gadis itu membeku. Tangannya masih memegang tongkat mikrofon, tapi matanya yang jernih kini menatap langsung ke arah Kai. Waktu seolah benar-benar berhenti berputar. Debu-debu halus menari di udara dalam sorot cahaya jingga yang menyelinap di antara rak — pemandangan yang hampir terasa tidak nyata." id b11_014

    "Kai membuka mulutnya. Ia ingin bertanya apakah gadis itu baik-baik saja. Ingin mengeluarkan suara apa saja, untuk membuktikan ia masih bernapas. Tidak ada satu kata pun yang keluar. Tenggorokannya terkunci — bukan oleh rasa takut, melainkan oleh sesuatu yang jauh lebih kuat." id b11_015

    play music bgm_senja loop fadein 2.0
    kai_hati "Dia nggak ngomong. Aku nggak ngomong. Nggak ada suara sama sekali. {i}(jeda panjang){/i} …Enam puluh detik. Ini. Ini dia. Hening di kaset hari Jumatku — ini. Bukan karena aku mati." id b11_016
    kai_hati "Bukan karena dunia kosong. Karena aku… nggak bisa berkata-kata. Terpesona. Ada orang kayak dia, berdiri di cahaya sore, hidup di temponya sendiri yang lambat dan tenang — dan kepalaku berhenti total." id b11_016_p2

    kai_hati "Aku masih hidup. Aku benar-benar masih hidup." id b11_017

    scene bg_perpustakaan with dissolve
    show kai senyum at pos_left with dissolve
    show yara marah at pos_right with dissolve

    "Tiba-tiba tawa mulai meledak dari dada Kai. Awalnya hanya kekehan kecil yang tertahan. Lama-lama berubah jadi tawa histeris yang memenuhi ruangan sunyi itu. Ia tertawa karena lega. Tertawa karena betapa bodohnya ia — menyiapkan surat wasiat untuk sesuatu yang ternyata adalah sebuah pertemuan." id b11_018

    gadis "Hei! Kamu gila, ya?!" id b11_019

    show kai cemas at pos_left
    "Tawa Kai berhenti seketika. Gadis itu kini menatapnya dengan kening berkerut, wajahnya memerah karena kesal. Headphone-nya sudah ia turunkan ke leher." id b11_020

    gadis "Kamu merusak semuanya! Aku sudah menunggu berjam-jam untuk merekam suara \"debu jatuh\" setelah getaran truk, dan kamu malah tertawa seperti orang tidak waras! {i}(melotot){/i} Tatapanmu juga aneh sekali tadi. Kamu mau merampok atau apa?" id b11_021

    "Kai terdiam. Wajahnya mendadak ikut merah padam. Ia menatap buku-buku yang berserakan, lalu menatap gadis itu — yang kini mulai memunguti peralatannya dengan kasar." id b11_022

    kai_hati "Ngomong. Ngomong sesuatu, Kai. Apa saja. Sebelum dia pergi dan kamu nggak pernah ketemu dia lagi—" id b11_023

    show kai biasa at pos_left
    kai "{i}(tiba-tiba, memberanikan diri){/i} Namaku Kai." id b11_024

    "Gadis itu berhenti sejenak. Menoleh sekilas, dengan tatapan sinis yang masih tersisa." id b11_025

    gadis "Aku tidak tanya namamu, Laki-laki Penunggu Mati." id b11_026

    hide yara with dissolve
    "Ia menyampirkan tas peralatannya dan melangkah pergi — meninggalkan Kai yang tertegun, sekaligus merasa… hidup." id b11_027

    show kai senyum at pos_center with dissolve
    kai_hati "\"Laki-laki Penunggu Mati\". {i}(jeda; lalu tersenyum kecil sendirian){/i} Julukan terburuk yang pernah kudapat. Dan entah kenapa… aku pengin dengar dia ngomong lagi." id b11_028

    scene bg_perpustakaan with fade
    show kai senyum at pos_center with dissolve

    "Di luar perpustakaan, matahari sore mulai meredup. Tapi bagi Kai, hari Jumat ini baru saja dimulai — dengan cara yang paling tidak terduga. Takdir tidak memberinya kematian. Takdir memberinya sebuah suara baru, yang sama sekali tidak ada di dalam kasetnya." id b11_029

    kai_hati "Kaset itu nggak bohong. Enam puluh detik hening, jam empat, hari Jumat — semua benar. Cuma artinya… {i}(menggeleng, tersenyum){/i} artinya yang aku salah baca. Jauh banget salahnya." id b11_030

    $ hook_chapter_completed("bab_11")

    return

label bab_12:
    $ chapter_autosave("bab_12", "Bab 12 — Manis di antara Kenyataan", "Ch. 12 — Sweetness Between Realities")

    scene bg_kantin with dissolve
    play music bgm_sekolah loop fadein 1.2
    show kai biasa at pos_center with dissolve

    "Keluar dari perpustakaan, perut Kai berbunyi. Wajar — seharian ia terlalu sibuk takut mati sampai lupa makan. Di kantin dekat perpustakaan yang hampir tutup, ia membeli minum dan sesuatu untuk mengganjal perut." id b12_001

    menu:
        "Di mana Kai duduk?"

        "Duduk dekat panci besar ibu kantin.":
            $ record_minor_choice("m09", "A")
            play sound sfx_panci loop fadein 0.6
            "Di sampingnya, panci besar ibu kantin mendidih pelan. Tutup pancinya bergetar halus setiap gelembung naik. Anehnya, suara itu menenangkan. Suara hari ini. Suara sekarang." id b12_002a
            show kai senyum at pos_center
            kai_hati "Mendidih. Berisik — tapi hidup. {i}(tersenyum kecil){/i} Enak juga didengar, ternyata." id b12_003a
            stop sound fadeout 0.8

        "Duduk di pojok paling sepi.":
            $ record_minor_choice("m09", "B")
            "Kai duduk di pojok, jauh dari siapa pun. Kebiasaan lama. Ia makan pelan-pelan sambil memandangi tangannya sendiri — tangan yang ternyata masih bisa memegang sendok." id b12_002b
            show kai senyum at pos_center
            kai_hati "Masih bisa makan. Masih bisa duduk di kantin. Hal-hal kecil begini… ternyata mewah, ya." id b12_003b

        "Makan sambil berdiri di luar kantin.":
            $ record_minor_choice("m09", "C")
            "Kai makan berdiri di depan kantin, menghadap jalan. Motor lewat, orang lewat, hidup lewat — semua bergerak biasa saja, tidak tahu bahwa beberapa menit lalu ada seorang anak yang mengira hidupnya selesai jam empat sore ini." id b12_002c
            show kai senyum at pos_center
            kai_hati "Dunia nggak berhenti tadi. Cuma aku yang berhenti. …Dan sekarang jalan lagi." id b12_003c

    stop music fadeout 1.0
    scene bg_gang_hujan with dissolve
    show kai biasa at pos_center with dissolve

    "Langkah kaki Kai terasa berat saat ia kembali menyusuri gang buntu yang selalu basah itu. Wajahnya masih terasa panas — rona merah di pipinya enggan memudar meski udara sore cukup dingin. Sisa malu karena tertawa histeris di depan gadis itu, dan karena surat wasiat konyolnya, masih menghantam harga dirinya." id b12_004

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.5
    show kai cemas at pos_left with dissolve
    show ageng senyum at pos_right with dissolve

    "Lonceng di atas pintu Gema Masa berbunyi. Pak Ageng tidak perlu mendongak untuk tahu siapa yang datang — ia sudah bisa menebak dari cara pintu itu dibuka: sedikit ragu, tapi ada sisa-sisa energi yang meledak di baliknya. Pria tua itu sedang menata beberapa butir kudapan di atas piring keramik kecil." id b12_005

    ageng "{i}(nada tenang, dengan geli terselip){/i} Kembali secepat ini, Nak?" id b12_006

    "Kai tidak langsung menjawab. Ia menjatuhkan dirinya di kursi kayu depan konter, lalu menelungkupkan wajahnya di atas meja jati yang dingin." id b12_007

    kai "{i}(suara teredam meja){/i} Bapak tahu, kan? Bapak pasti tahu kalau keheningan itu bukan karena saya mati." id b12_008

    "Pak Ageng tertawa terkekeh — suara tawanya terdengar seperti gesekan pita kaset tua: hangat, dan penuh kenangan. Ia menggeser piring keramik itu ke hadapan Kai." id b12_009
    "Di atasnya tersaji beberapa butir cenil berwarna-warni — merah muda, hijau, dan putih — diselimuti parutan kelapa segar dan siraman gula merah yang kental. Sebuah garpu kecil diletakkan di samping piring." id b12_009_p2

    ageng "Sudah kubilang — kaset ini nggak pernah bohong, tapi telinga manusia itu sering salah dengar." id b12_010

    show kai biasa at pos_left
    $ show_item("item_cenil")
    "Kai mengangkat wajahnya perlahan. Matanya menatap lekat cenil yang berkilau terkena cahaya lampu toko yang kuning redup." id b12_011

    show ageng biasa at pos_right
    ageng "Kaset itu merekam apa yang akan terjadi, Kai. Ia tidak pernah salah mencatat frekuensi. Yang salah adalah bagaimana hatimu menerjemahkan suara-suara itu." id b12_012

    "Pak Ageng menatap ke arah jendela toko yang masih menyisakan bekas tetesan air hujan. Tatapannya menerawang, seolah melihat sesuatu yang jauh melampaui tembok gang buntu ini." id b12_013

    ageng "{i}(berbisik pelan){/i} Kadang, diam itu lebih keras dari teriakan. Ada momen di mana suara di sekitarmu mendadak hilang — bukan karena duniamu berhenti, tapi karena hatimu sedang dipaksa untuk mendengarkan sesuatu yang lebih nyaring daripada kata-kata." id b12_014

    "Kai mengambil sepotong cenil dan memasukkannya ke mulut. Teksturnya kenyal, berpadu dengan gurihnya kelapa dan manisnya gula merah. Rasa manis itu seolah perlahan membasuh rasa malu dan sisa-sisa ketakutan yang mengendap di dadanya." id b12_015
    "Ia teringat kembali wajah gadis itu di perpustakaan — dan tumpukan buku yang jatuh itu, yang terdengar seperti lonceng penanda bahwa hidupnya baru saja dimulai kembali." id b12_015_p2

    kai "Diam yang itu… rasanya sangat sesak, Pak." id b12_016

    show ageng senyum at pos_right
    ageng "{i}(tersenyum tipis){/i} Memang begitu rasanya saat kita terpesona, Kai. Itu adalah jenis keheningan yang paling jujur. Tidak ada manipulasi, tidak ada kepura-puraan. Hanya kamu dan apa yang ada di depan matamu." id b12_017

    ageng "{i}(menggodanya){/i} Jadi, apa rencana kamu untuk esok hari? Masih mau membeli kaset lagi?" id b12_018

    show kai senyum at pos_left
    $ hide_item()
    kai "{i}(menggeleng perlahan, menghabiskan butir cenil terakhir){/i} Tidak untuk sekarang, Pak. Saya rasa… saya ingin mencoba mendengar suara-suara yang ada hari ini saja dulu." id b12_019

    ageng "{i}(mengangguk puas){/i} Pilihan yang bijak. Karena kaset-kaset di rak ini tidak akan lari ke mana-mana — tapi momen di perpustakaan tadi mungkin tidak akan terulang dengan cara yang sama." id b12_020

    "Kai menatap rak-rak kaset itu lama-lama. Untuk pertama kalinya, rak itu tidak terlihat seperti jawaban atas apa pun. Cuma rak. Dan itu terasa… ringan." id b12_021

    kai_hati "Hari ini saja dulu. Suara-suara hari ini. {i}(jeda){/i} …Namanya siapa, ya? Aku bahkan nggak sempat tanya. Yang aku tahu cuma julukan yang dia kasih ke aku. {i}(tersenyum){/i} Nggak apa-apa. Besok-besok aku cari tahu." id b12_022

    stop music fadeout 1.5
    return
