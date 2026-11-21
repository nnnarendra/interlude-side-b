label bab_31_inti_siti:

    play sound sfx_klik_play
    $ show_item("item_kaset_siti")
    "Pak Ageng berjalan ke lemari kayu tua di sudut ruangan. Bukan lemari kaca tempat kaset merah — lemari pribadi, yang selalu terkunci. Kunci kuningannya sudah berkarat. Dari dalamnya dia mengeluarkan satu kaset usang, labelnya menguning. Tulisannya tinta hitam yang sudah pudar: {i}Siti, 1994{/i}." id b31_005
    $ show_cg_and_unlock("cg_kaset_siti", dissolve)
    play music bgm_duka_siti loop fadein 1.5

    ageng "Dulu, puluhan tahun lalu, saya teknisi suara. Di stasiun radio lokal, di kota ini juga. Saya suka pekerjaan itu. Tapi saya jauh lebih suka istri saya. Siti namanya." id b31_006

    ageng "Tawanya… aduh. Tawa paling enak yang pernah saya dengar. Hari paling mendung di Malang pun, kalau dia tertawa, rasanya jadi hangat." id b31_007

    "Mata Pak Ageng berkaca-kaca, memantulkan lampu gantung kuning toko." id b31_008

    ageng "Terus suatu hari dia pergi. Sakit. Cepat sekali. Saya bahkan belum sempat merekam suaranya baik-baik di kaset. Habis dia nggak ada, rumah kami jadi sunyi. Sunyi banget. Sampai saya hampir— {i}(berhenti, menggeleng pelan){/i} …ya, segitunya." id b31_009

    "Dia kembali ke balik konter, meletakkan kaset bernama Siti itu di meja, di depan Kai." id b31_010

    ageng "Habis itu saya jadi terobsesi. Semua ilmu rekayasa frekuensi yang saya punya saya pakai. Sirkuit perekam saya modifikasi. Pita magnetik terbaik saya cari ke mana-mana. Buat satu tujuan yang sebenarnya gila: saya mau menangkap sisa getaran suara Siti yang masih tertinggal di dunia ini. Dengar suaranya sekali lagi. Sekali saja." id b31_011

    ageng "Bertahun-tahun, Kai. Di ruangan gelap. Menyaring bising. Menguatkan frekuensi yang sunyi. Nyoba membalikkan waktu lewat gelombang." id b31_012

    ageng "Sampai akhirnya saya sadar satu hal yang kejam. Suara yang sudah hilang itu nggak akan pernah balik utuh. Yang ketangkap di kaset ini bukan Siti. {i}(menepuk kaset itu pelan){/i} Ini gema duka saya sendiri. Muter terus, nggak ada habisnya." id b31_013

    kai_hati "…" id b31_014

    ageng "Toko ini berdiri karena saya mau bikin ruang buat orang-orang yang tersesat di kecemasannya sendiri. Kaset-kaset itu saya modifikasi biar bisa menangkap proyeksi pikiran orang — ketakutan terdalamnya soal hari esok. Karena ketakutan itu frekuensi paling kuat yang dipancarkan otak kita." id b31_015

    ageng "{i}(menatap Kai lurus){/i} Tapi ujung-ujungnya, Kai, kaset-kaset itu cuma alat. Yang mereka rekam itu kecemasanmu sendiri. Bukan takdir yang mutlak." id b31_016

    return

label bab_31_merah:
    $ chapter_autosave("bab_31_merah", "Bab 31 — Dari Duka yang Mengendap", "Ch. 31 — From Settled Grief")

    scene bg_toko_dalam_malam with dissolve
    play music bgm_toko loop fadein 1.5
    show kai sedih at pos_left with dissolve
    show ageng iba at pos_right with dissolve

    "Toko Gema Masa sore itu sepi dengan cara yang beda. Nggak ada kaset ramalan yang berputar. Nggak ada dengung apa pun. Cuma angin dingin dari celah pintu, dan kopi hitam di konter yang mulai dingin. Pak Ageng sedang mengelap pemutar piringan hitam tua — pelan sekali, kayak tiap usapan itu berat." id b31r_001

    ageng "Kamu tahu, Kai… Banyak orang mengira tempat ini ada sihirnya. Mereka datang ke sini cari keajaiban. Mengira saya punya kunci buat membuka takdir." id b31r_002

    "Dia meletakkan kain lapnya. Menatap pemutar piringan hitam itu kosong." id b31r_003

    ageng "Padahal toko ini nggak lahir dari sihir. Toko ini lahir dari duka." id b31r_004

    kai_hati "…Duka? Pak Ageng nggak pernah cerita soal dirinya sendiri. Nggak pernah." id b31r_005

    call bab_31_inti_siti

    scene bg_toko_dalam_malam with dissolve
    show kai menangis at pos_left with dissolve
    show ageng iba at pos_right with dissolve
    "Kai menatap kaset Siti di meja. Lalu menatap tangannya sendiri — yang sedang menggenggam kaset merah tanggal 1 Agustus." id b31r_006

    kai "{i}(pelan, air matanya jatuh){/i} Saya mengorbankan masa lalu saya, Pak… karena saya takut menghadapi duka di masa depan." id b31r_007

    ageng "{i}(meletakkan tangannya di pundak Kai){/i} Dan kalau kamu teruskan, Nak, kamu sedang bikin duka yang sama persis kayak yang saya rasakan dulu. Bedanya, kamu bikin sendiri." id b31r_008

    show ageng serius at pos_right
    ageng "Jangan biarkan toko ini merampas hidupmu, kayak dia merampas sisa hidup saya. Perbaiki pitamu… selagi durung putus." id b31r_009

    stop music fadeout 1.2
    return

label bab_31_sehat:
    $ chapter_autosave("bab_31_sehat", "Bab 31 — Dari Duka yang Mengendap", "Ch. 31 — From Settled Grief")

    scene bg_toko_dalam with dissolve
    play music bgm_toko loop if_changed
    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    "Sore itu Kai nggak cuma beli kaset. Rak bagian belakang berantakan habis dibongkar Pak Ageng pagi tadi, dan Kai menawarkan diri membantu menata ulang. Pak Ageng mengelap pemutar piringan hitam tua di sela-sela mereka bekerja — pelan sekali, kayak tiap usapan itu berat." id b31s_001

    kai "Pak, piringan hitam ini masih bisa bunyi?" id b31s_002

    show ageng iba at pos_right
    ageng "Kadang bisa, kadang nggak. Kayak yang punya. {i}(jeda; meletakkan kain lapnya){/i} Kamu tahu, Kai… Banyak orang mengira tempat ini ada sihirnya. Mereka datang cari keajaiban. Mengira saya punya kunci buat membuka takdir. Padahal toko ini nggak lahir dari sihir. Toko ini lahir dari duka." id b31s_003

    kai_hati "…Duka? Pak Ageng nggak pernah cerita soal dirinya sendiri. Nggak pernah." id b31s_004

    call bab_31_inti_siti

    scene bg_toko_dalam with dissolve
    show kai cemas at pos_left with dissolve
    show ageng iba at pos_right with dissolve
    "Kaset bernama Siti itu sekarang tergeletak di meja, di antara tumpukan kaset yang belum selesai ditata. Kai menatapnya lama. Tangannya kosong — nggak ada kaset merah di tangannya di rute ini. Tapi kata-kata Pak Ageng barusan menempel di kepalanya dengan cara lain." id b31s_005

    kai "Pak… kalau kaset-kaset itu cuma merekam kecemasan saya sendiri… berarti selama ini yang saya dengar tiap malam itu…" id b31s_006

    ageng "Suaramu sendiri, Nak. Yang lagi ketakutan. {i}(menepuk pundak Kai pelan){/i} Makanya saya bilang: jangan biarkan toko ini merampas hidupmu, kayak dia merampas sisa hidup saya. Kamu masih sering ke sini buat beli yang biasa, kan? Itu pun, kalau keterusan, sama saja." id b31s_007

    show ageng serius at pos_right
    ageng "Perbaiki pitamu… selagi durung putus." id b31s_008

    stop music fadeout 1.2
    return

label bab_32:
    $ chapter_autosave("bab_32", "Bab 32 — Kabar Gembira di Tengah Sunyi", "Ch. 32 — Good News in the Quiet")

    scene bg_koridor_sekolah with dissolve
    play music bgm_sekolah loop fadein 1.2
    play sound sfx_kelas loop fadein 0.6
    show kai biasa at pos_left with dissolve
    show yara ceria at pos_right with dissolve

    "Pagi itu, sebelum pengumuman apa pun beredar, Yara menahan Kai di koridor. Di tangannya ada map berisi berkas portofolio — sekolah minta satu salinan final buat diarsipkan, lengkap dengan judul resminya." id b32_001

    yara "Kai, bentar. Bantuin aku milih, dong. Buat berkas final ini aku harus nentuin satu judul. Aku buntu. Tiga-tiganya aku suka, tapi alasannya beda-beda semua." id b32_002

    kai "Kamu nanya aku? Aku kan cuma tukang gotong tripod." id b32_003

    yara "Justru itu. Kamu dengar semua rekamannya dari yang paling mentah. Udah, pilih satu. Yang paling \"aku\", menurutmu." id b32_004

    menu:
        "Judul portofolio Yara:"

        "\"Suara yang Jujur.\"":
            $ record_minor_choice("m18", "A")
            yara "{i}(tersenyum){/i} …Iya. Itu sih emang yang dari awal aku kejar. Oke. Itu." id b32_005a

        "\"Kota Kecil, Bunyi Besar.\"":
            $ record_minor_choice("m18", "B")
            yara "Hah, itu judul kesayanganku sebenarnya. Malang kedengaran kecil, tapi bunyinya… {i}(mengangguk){/i} Oke, itu." id b32_005b

        "\"Arsip Hari Biasa.\"":
            $ record_minor_choice("m18", "C")
            yara "Hari biasa, ya. {i}(tertawa kecil){/i} Padahal nggak ada hari yang beneran biasa kalau didengerin baik-baik. Oke. Itu aja." id b32_005c

    yara "Makasih, ya. {i}(berbalik, setengah berlari){/i} Aku ke ruang guru dulu— eh, nanti siang aku kabari sesuatu. Tunggu aja!" id b32_006

    hide yara with dissolve
    stop sound fadeout 0.5

    if get_major_choice(9) == "A":

        stop music fadeout 0.8
        play music bgm_cemas loop fadein 1.2
        scene bg_koridor_sekolah with dissolve
        show kai datar at pos_center with dissolve

        "Di papan pengumuman dekat ruang bimbingan konseling, selembar kertas baru ditempel. Kop surat resmi, dari universitas seni ternama di Yogyakarta. Daftar nama calon mahasiswa yang diterima. Di baris ketiga belas, tercetak tebal: {b}Yara Kirana — Seni Musik (Desain Suara).{/b}" id b32r_001

        kai_hati "Diterima. Portofolionya diterima. Tripod yang kugotong keliling kota itu… beneran nganterin dia sampai sana." id b32r_002

        "Yara melihat namanya di kertas itu dan tidak berteriak. Dia cuma terpaku sebentar — lalu senyum lebar yang sangat tulus merekah di wajahnya. Langkah pertamanya bukan ke ruang guru. Dia berlari menyusuri koridor." id b32r_003

        kai_hati "Dia nyari aku. Aku tahu dia nyari aku." id b32r_004

        show kai panik at pos_left with dissolve
        show yara ceria at pos_right with dissolve

        yara "{i}(dari jauh, setengah terengah){/i} Kai!" id b32r_005

        "Kai menoleh sekilas. Dari jarak dua puluh meter, Yara berlari ke arahnya — wajahnya berseri-seri, selembar kertas tergenggam di tangan yang gemetar karena gembira. Di saku celana Kai, kaset merah 1 Agustus terasa seperti logam panas." id b32r_006

        kai_hati "1 Agustus. Hari dia ngucapin selamat tinggal sambil nangis. {i}(menelan ludah){/i} Kalau dia sebahagia ini hari ini… gara-gara aku… nanti pas pisah dia bakal sehancur apa? Nggak. Nggak bisa. Jauhi sekarang. Sekarang, mumpung belum makin—" id b32r_007

        hide kai with dissolve
        "Sebelum Yara sempat mendekat, Kai memutar tubuhnya cepat. Langkah lebar, lalu setengah berlari — menuruni tangga darurat menuju halaman belakang yang sepi." id b32r_008

        show yara penasaran at pos_right
        yara "Kai! Tunggu!" id b32r_009

        "Yara mempercepat larinya, mengabaikan tatapan heran adik-adik kelas yang berpapasan. Tapi Kai lebih cepat. Di belokan koridor bawah, jaket abu-abu itu menghilang." id b32r_010

        scene bg_gerbang_sekolah with dissolve
        show yara sedih at pos_center with dissolve

        "Yara sampai di dasar tangga. Koridornya kosong. Cuma angin dingin yang menyapu daun-daun kering di paving halaman. Kertas pengumuman di genggamannya perlahan lemas, kena remas tangannya sendiri. Senyum yang baru mekar tadi luruh, menyisakan bingung yang kosong." id b32r_011

        yara "{i}(pelan, pada koridor yang sepi){/i} Kenapa, Kai? …Kenapa pas duniaku akhirnya mulai terdengar indah, kamu justru milih jadi tuli?" id b32r_012

    else:

        scene bg_koridor_sekolah with dissolve
        show kai biasa at pos_left with dissolve
        show yara ceria at pos_right with dissolve

        "Di rute ini, kertas di papan pengumuman itu sama: {b}Yara Kirana — Seni Musik (Desain Suara), Yogyakarta.{/b} Diterima. Dan sama seperti seharusnya, langkah pertama Yara bukan ke ruang guru — dia berlari menyusuri koridor, nyari Kai. Bedanya cuma satu: di rute ini, Kai tidak lari." id b32s_001

        yara "{i}(berlari mendekat, terengah, kertas terangkat tinggi){/i} Kai! Kai, lihat— aku diterima! Yogya! Desain Suara! Beneran diterima!" id b32s_002

        kai_hati "Yogya. Jauh. Dia bakal pergi. {i}(jeda){/i} Dadaku langsung sesak — tapi dia berdiri di depanku, sebahagia ini, dan dia lari ke aku duluan. Bukan ke ruang guru. Ke aku." id b32s_003

        menu:
            "Apa yang keluar dari mulut Kai?"

            "Jujur soal takutnya.":
                $ record_major_choice(10, "A")
                show kai senyum at pos_left
                kai "Yar… selamat. Selamat banget. {i}(tersenyum, lalu pelan){/i} Aku bohong kalau aku bilang aku cuma senang. Aku takut. Kamu pergi jauh, aku di sini… aku takut kita jadi orang asing. Tapi itu urusanku. Hari ini hari kamu. Selamat, ya." id b32s_004a
                yara "{i}(terdiam sebentar, senyumnya berubah lebih lembut){/i} …Makasih udah bilang jujur. Kebanyakan orang cuma bilang \"selamat\" terus diem. {i}(menepuk lengan Kai){/i} Kita omongin soal jarak itu nanti. Pelan-pelan. Sekarang… traktir aku susu stroberi, dong. Perayaan." id b32s_005a

            "\"Oh, bagus buatmu.\" — sambil menelan sisanya.":
                $ record_major_choice(10, "B")
                show kai cemas at pos_left
                kai "Oh— Yogya? Wah. Bagus buatmu. Selamat, ya." id b32s_004b
                show yara sedih at pos_right
                yara "{i}(senyumnya sedikit turun){/i} …Cuma \"bagus buatmu\"? {i}(tertawa kecil, dipaksakan){/i} Ya udah. Makasih, ya. Aku… aku ke ruang guru dulu, lapor." id b32s_005b
                hide yara with dissolve
                kai_hati "Ada seribu kalimat di kepalaku barusan. Yang keluar cuma tiga kata. Dan mukanya langsung berubah. Aku lihat itu. Aku lihat, dan aku tetap diem." id b32s_006b

            "Berubah dingin, beralasan sibuk.":
                $ record_major_choice(10, "C")
                show kai datar at pos_left
                kai "{i}(melihat kertas itu sekilas){/i} Oh. Selamat. {i}(melirik jam){/i} Aku ada urusan di kelas, Yar. Nanti aja, ya." id b32s_004c
                show yara sedih at pos_right
                yara "{i}(berhenti, kertas di tangannya turun perlahan){/i} …Urusan? {i}(jeda){/i} Oke. Oke, Kai. Sana." id b32s_005c
                hide yara with dissolve
                kai_hati "\"Urusan\". Urusan apa? Nggak ada. Aku cuma… nggak sanggup lihat dia sebahagia itu buat sesuatu yang bakal ngambil dia dari sini. Jadi aku yang pergi duluan. Biar gampang." id b32s_006c

    stop music fadeout 1.2
    return

label bab_33:
    $ chapter_autosave("bab_33", "Bab 33 — Benang-Benang yang Kusut", "Ch. 33 — Tangled Threads")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop fadein 1.2
    show kai sedih at pos_center with dissolve

    "Malam itu Kai nggak bisa tidur. Kamar yang biasanya jadi tempat sembunyi terasa kayak ruang interogasi. Tiap memejamkan mata, yang muncul wajah Yara di koridor tangga — wajah yang harusnya berhak merayakan impiannya, tapi malah layu gara-gara sikap dinginnya." id b33_001

    kai_hati "Aku ngerusak masa kini… buat ngantisipasi satu menit tangisan tanggal 1 Agustus. Satu menit. Yang bahkan belum tentu— {i}(menyentuh dadanya yang terasa hampa){/i} \"Melindungi\". Melindungi siapa? Yang kulindungi cuma rasa takutku sendiri." id b33_002

    kai "{i}(bisik, ke kegelapan){/i} Aku harus perbaiki ini." id b33_003

    scene bg_koridor_sekolah with dissolve
    play sound sfx_kelas loop fadein 0.6
    show kai cemas at pos_left with dissolve
    show yara sedih at pos_right with dissolve

    "Besoknya, Kai menunggu di depan loker kelas XI-Sosial. Di tangannya: sebotol susu stroberi, kesukaan Yara. Yara muncul dengan headphone hitam melingkar erat di lehernya. Kai melangkah maju, kaku." id b33_004

    kai "Yara. {i}(mencoba tersenyum){/i} Selamat ya, atas… kelulusan seleksinya. Universitas barumu. Ini— {i}(menyodorkan botol){/i} buat kamu." id b33_005

    yara "{i}(menatap botol itu, lalu wajah Kai; tidak ada marah di matanya — cuma lelah){/i} Terima kasih, Kai. Tapi aku lagi nggak pengin minum susu." id b33_006

    if get_minor_choice("m17") == "A":
        yara "{i}(sebelum berbalik, pelan){/i} Rekaman detak jantungmu itu… kudengar semalam. Kedengarannya kayak orang yang lagi lari dari sesuatu. {i}(jeda){/i} Ternyata beneran lari, ya." id b33_007a
    elif get_minor_choice("m17") == "B":
        yara "{i}(sebelum berbalik, pelan){/i} Jam dinding toko itu… kamu rekam buat aku, kan? Detaknya lebih pelan dari yang kukira. {i}(jeda){/i} Nggak kayak kamu akhir-akhir ini. Kamu buru-buru terus. Entah mau ke mana." id b33_007b

    show kai panik at pos_left
    kai "{i}(cepat, panik){/i} Yara, soal kemarin— aku cuma bingung, aku— dengerin dulu. Sore ini kita ke pasar loak, yuk? Aku bawain semua peralatanmu, semua. Aku pengin dengar suara palu pandai besi tua itu. Sama kamu." id b33_008

    yara "{i}(menghela napas pendek; senyum getir yang sangat tipis){/i} Palu pandai besi itu udah berhenti menempa sejak dua hari lalu, Kai. Dan aku udah merekamnya sendiri, kemarin lusa. Sendirian." id b33_009

    hide yara with dissolve
    stop sound fadeout 0.5
    "Yara melangkah melewati Kai begitu saja. Kai mematung, botol susu stroberi di genggamannya perlahan mendingin." id b33_010

    show kai sedih at pos_center with dissolve
    kai_hati "Semua kata yang kuucapin hari ini kedengaran sumbang. Semua usahaku buat dekat malah kedengaran kayak gangguan." id b33_011

    scene bg_kamar_kai_malam with dissolve
    show kai panik at pos_center with dissolve
    play sound sfx_pita_kusut

    "Malamnya, Kai pulang dengan kepala berdenyut. Dan begitu masuk kamar, pemandangan di meja belajar menyambutnya: kaset-kaset ramalan yang selama ini tersimpan di laci — yang sudah lama berdebu dan dia abaikan — sekarang keluar dari wadah mikanya. Pita cokelat gelapnya mencuat keluar. Tidak wajar." id b33_012

    play sound sfx_pita_kusut
    "Di bawah lampu meja, pita-pita itu mulai berputar sendiri. Pelan. Kusut. Saling melilit satu sama lain di atas meja jati — membentuk jaring hitam yang rusak, kayak benang takdir yang kehilangan polanya. Kaset merah 1 Agustus di dalam wadahnya ikut bergetar hebat. Pita logamnya menegang, kayak siap putus." id b33_013

    show kai menangis at pos_center with vpunch
    kai "{i}(jatuh terduduk di lantai, napas memburu){/i} …" id b33_014

    kai_hati "Aku nyoba ngatur masa depan. Aku ngerusak masa kiniku sendiri buat itu. Dan sekarang… takdirku kehilangan melodinya. Tinggal bising. Bising yang ngerusak semuanya." id b33_015

    return

label bab_34_merah:
    $ chapter_autosave("bab_34_merah", "Bab 34 — Musik Tanpa Nyawa", "Ch. 34 — Lifeless Music")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop if_changed
    show kai datar at pos_center with dissolve
    play sound sfx_klik_play

    "Kamarnya terasa kayak kuburan suara. Jalinan pita kusut di meja masih berserakan, kayak jaring laba-laba mati. Dengan tangan gemetar, Kai merogoh laci terdalam. Keluar: walkman perak usangnya." id b34r_001
    "Di dalamnya sudah terpasang kaset mika merah — mixtape rekaman mereka berdua, dibuat di bawah tempias hujan di teras toko Pak Ageng. Pesan suara buat diri mereka di masa lalu." id b34r_001_p2

    "Earphone terpasang. Ibu jarinya yang dingin menekan play." id b34r_002

    play sound sfx_klik_play
    queue sound sfx_desis_pita
    yara_kaset "Untuk Yara yang sebulan lalu berdiri sendirian di halte bus sambil nutup telinga rapat-rapat karena benci bisingnya dunia… Jangan takut sama suara-suara berisik di sekitarmu…" id b34r_003

    "Kai memejamkan mata rapat-rapat. Dia menunggu rasa hangat yang biasa menjalar ke dadanya tiap dengar suara Yara. Menunggu debar. Rindu. Atau setidaknya sesak — apa pun yang membuktikan dia masih punya jiwa." id b34r_004

    "Nggak ada apa-apa. Suara Yara jernih, indah — tapi datar. Kayak lagu asing di radio pusat perbelanjaan. Indah, tapi nggak ada hubungannya sama dia." id b34r_005

    if cond_k1 == "B":

        kai_kaset "Untuk Kai yang ngunci diri di kamar dan nulis surat-surat perpisahan konyol… Letakkan pulpenmu. Kamu nggak akan mati hari Jumat ini. Kamu justru akan mulai benar-benar hidup setelah kuah hitam dan bunyi rel itu…" id b34r_006b

        kai_hati "\"Kuah hitam dan bunyi rel itu\". Aku tahu itu maksudnya sore penting. Aku tahu — secara logika tahu — kami pernah duduk makan rawon di pinggir rel bersama." id b34r_007b

        kai_hati "Tapi aku nggak bisa ngebayanginnya. Nggak ingat hangat kuah rawonnya waktu hujan deras itu. Nggak ingat dia tertawa kepedesan di sampingku. Kosong. Kayak ada halaman yang disobek dari tengah buku." id b34r_008b

    elif cond_k1 == "C":

        kai_kaset "Untuk Kai yang ngunci diri di kamar dan nulis surat-surat perpisahan konyol… Letakkan pulpenmu. Kamu nggak akan mati hari Jumat ini. Kamu justru akan mulai benar-benar hidup setelah angin pertama di Bukit Banyak itu…" id b34r_006c

        kai_hati "\"Angin pertama di Bukit Banyak\". Aku tahu tempat itu. Aku tahu — secara logika tahu — kami pernah naik ke sana membawa tripod." id b34r_007c

        kai_hati "Tapi aku nggak bisa ngebayanginnya. Nggak ingat pernah duduk bersamanya di puncak itu. Nggak ingat teriakan kecilnya atau rasa lega di dadaku hari itu. Kosong. Kayak ada halaman yang disobek dari tengah buku." id b34r_008c

    else:

        kai_kaset "Untuk Kai yang ngunci diri di kamar dan nulis surat-surat perpisahan konyol… Letakkan pulpenmu. Kamu nggak akan mati hari Jumat ini. Kamu justru akan mulai benar-benar hidup setelah tumpukan buku itu jatuh…" id b34r_006a

        kai_hati "\"Tumpukan buku itu jatuh\". Aku tahu itu maksudnya peristiwa penting. Aku tahu — secara logika tahu — itu yang mempertemukan aku sama Yara." id b34r_007a

        kai_hati "Tapi aku nggak bisa ngebayanginnya. Nggak ingat cahaya senja di perpustakaan hari itu. Nggak ingat ekspresi paniknya waktu dia njatuhin buku-buku itu. Kosong. Kayak ada halaman yang disobek dari tengah buku." id b34r_008a

    show kai menangis at pos_center
    "Kai melepas earphone-nya pelan. Air matanya menetes — tapi dia bahkan nggak bisa merasakan sedih yang utuh. Yang tersisa cuma hampa. Dingin. Mengerikan." id b34r_009

    kai_hati "Gini rasanya ngelepas awal sebuah cerita. Bab-bab sesudahnya… nggak akan pernah kedengaran sama lagi." id b34r_010

    stop music fadeout 1.2
    return

label bab_34_sehat:
    $ chapter_autosave("bab_34_sehat", "Bab 34 — Mixtape yang Utuh", "Ch. 34 — The Intact Mixtape")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_senja loop fadein 1.5
    show kai biasa at pos_center with dissolve
    play sound sfx_klik_play
    queue sound sfx_desis_pita

    "Di rute ini, laci terdalam Kai berisi walkman perak yang sama, dan kaset mika merah yang sama — mixtape dari teras toko Pak Ageng, di bawah tempias hujan. Bedanya: nggak ada pita kusut di meja. Dan ingatan Kai utuh." id b34s_001

    yara_kaset "Untuk Yara yang sebulan lalu berdiri sendirian di halte bus sambil nutup telinga rapat-rapat karena benci bisingnya dunia… Jangan takut sama suara-suara berisik di sekitarmu…" id b34s_002

    kai_kaset "Untuk Kai yang ngunci diri di kamar dan nulis surat-surat perpisahan konyol… Letakkan pulpenmu. Kamu nggak akan mati hari Jumat ini. Kamu justru akan mulai benar-benar hidup setelah tumpukan buku itu jatuh…" id b34s_003

    show kai senyum at pos_center
    kai_hati "Tumpukan buku itu. {i}(tersenyum kecil, sendirian di kamar){/i} Aku ingat. Cahaya senja di perpustakaan. Dia panik, buku-buku jatuh, dan aku — bukannya pergi — malah bantuin mungut. Hari itu aneh banget. Hari itu… awal semuanya." id b34s_004

    "Rasa hangat yang dia tunggu-tunggu datang beneran. Suara Yara di rekaman itu bukan lagu asing di radio mal. Itu Yara-nya. Yang tawanya dia kenal. Yang bakal pergi ke Yogya — dan untuk pertama kalinya, pikiran itu terasa sedih dengan cara yang normal. Bukan hampa. Sedih yang punya isi." id b34s_005

    kai_hati "Dulu aku kira kaset-kaset ramalan itu yang bikin aku tenang. Ternyata bukan. {i}(menatap kaset mika merah){/i} Yang ini nggak ngasih tahu masa depan sama sekali. Isinya cuma masa lalu. Dan anehnya… ini yang bikin aku tenang." id b34s_006

    stop music fadeout 1.2
    return

label bab_35:
    $ chapter_autosave("bab_35", "Bab 35 — Debu di Gang yang Kering", "Ch. 35 — Dust in the Dry Alley")

    scene bg_koridor_sekolah with dissolve
    play sound sfx_kelas loop fadein 0.6
    show kai biasa at pos_center with dissolve

    "Siang itu selebaran pameran karya siswa ditempel di papan pengumuman dan dibagikan ke kelas-kelas. Di halaman daftar portofolio siswa, satu judul tercetak resmi:" id b35_001

    if get_minor_choice("m18") == "A":
        "\"Suara yang Jujur\" · karya Yara Kirana." id b35_002a
    elif get_minor_choice("m18") == "B":
        "\"Kota Kecil, Bunyi Besar\" · karya Yara Kirana." id b35_002b
    else:
        "\"Arsip Hari Biasa\" · karya Yara Kirana." id b35_002c

    kai_hati "Judul itu… aku yang milih. {i}(jeda){/i} Kecil sih. Tapi namaku — maksudku, pilihanku — ikut tercetak di jalannya dia. Aneh rasanya. Senang, tapi ada sesaknya juga." id b35_003

    stop sound fadeout 0.5
    scene bg_gang_kering with dissolve
    play music bgm_cemas loop fadein 1.5
    show kai cemas at pos_center with dissolve

    "Sore itu, ada yang ganjil. Gang menuju Toko Gema Masa — yang selama ini selalu basah, selalu beraroma tanah habis hujan — hari ini kering. Beneran kering. Matahari sore terik tanpa awan. Tanah semennya pecah-pecah halus, debunya beterbangan tiap angin panas lewat. Pertama kalinya Kai melihat gang ini seperti ini." id b35_004

    kai_hati "…Kok kering? Gang ini nggak pernah kering. {i}(mempercepat langkah){/i} Pak Ageng…" id b35_005

    menu:
        "Di tengah gang yang kering itu, Kai berhenti sebentar. Apa yang dia lakukan?"

        "Memotret gang itu dengan HP.":
            $ record_minor_choice("m19", "A")
            "Klik. Gang kering, debu beterbangan, toko tua di ujungnya. Foto yang rasanya salah — kayak memotret orang yang dikenal tanpa senyumnya." id b35_006a

        "Merekam suara langkahnya sendiri di gang kering.":
            $ record_minor_choice("m19", "B")
            play sound sfx_klik_play
            "Dia menyalakan perekam di HP. Krak… krak… Langkah di atas semen berdebu. Nggak ada bunyi air. Nggak ada tempias. Cuma kering." id b35_006b

        "Langsung masuk, tidak berhenti.":
            $ record_minor_choice("m19", "C")
            "Nggak ada waktu buat gang. Ada firasat buruk yang lebih keras dari rasa penasaran, dan kaki Kai memilih lari." id b35_006c

    scene bg_toko_luar with dissolve
    show kai panik at pos_center with dissolve

    "Kai sampai di depan toko, setengah berlari, ujung sepatunya kotor kena debu. Dan jantungnya mencelos. Pintu kayu Toko Gema Masa tertutup rapat. Gembok besi besar — sudah berkarat — menguncinya dari luar. Papan kecil yang biasanya bertuliskan \"Buka\" sudah dibalik. Sisi sebaliknya, tinta merah kusam: {b}TUTUP{/b}." id b35_007

    show kai panik at pos_center with vpunch
    kai "Pak Ageng… {i}(menggedor pintu dengan telapak tangan yang gemetar){/i} Pak Ageng! Ini saya, Kai! Tolong buka pintunya, Pak!" id b35_008

    "Nggak ada jawaban. Sunyi dari dalam toko terasa pekat dan mati — beda dengan hening hangat yang biasa menyelimuti ruangan penuh kaset itu. Kai menempelkan telinganya ke celah pintu. Nggak ada derit kursi goyang. Nggak ada langkah lambat. Nggak ada apa-apa." id b35_009

    "Lalu terdengar: batuk. Kering, berat, dari jendela samping yang terhubung ke rumah tinggal Pak Ageng di belakang toko. Lemah sekali. Tiap tarikan napasnya kedengaran kayak perjuangan." id b35_010

    kai "{i}(beralih ke jendela, mengetuk kacanya panik){/i} Pak Ageng? Bapak sakit? Pak, tolong buka jendelanya!" id b35_011

    show kai panik at pos_left with dissolve
    show ageng sakit at pos_right with dissolve
    "Gordennya bergerak sedikit. Dari balik kaca berdebu, ruangan dalam yang temaram terlihat sayup-sayup: Pak Ageng terbaring lemah di ranjang tuanya, diselimuti kain sarung tebal. Wajahnya pucat sekali. Matanya — yang biasanya tenang dan tajam — meredup, kelelahan." id b35_012

    "Pak Ageng menoleh lambat ke arah jendela. Dia melihat Kai yang panik di luar. Tapi dia cuma menggeleng — lemah sekali. Tangannya yang gemetar terangkat, menunjuk ke arah gembok pintu toko. Lalu jarinya bergerak, memberi isyarat: pergi. Toko ini tidak bisa membantumu hari ini." id b35_013

    hide ageng with dissolve
    show kai sedih at pos_center with dissolve
    kai "{i}(mundur satu langkah; tangannya jatuh lunglai){/i} …" id b35_014

    kai_hati "Tempat perlindunganku… runtuh. Pak Ageng terbaring sakit, nggak berdaya, dan tokonya tutup. Aku sendirian di luar sini. Di antara masa lalu yang udah kehapus… dan masa depan yang terus ngejar aku tanpa ampun." id b35_015

    stop music fadeout 1.2
    return
