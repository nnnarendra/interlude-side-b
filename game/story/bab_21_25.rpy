label bab_21:
    $ chapter_autosave("bab_21", "Bab 21 — Rahasia di Balik Gulungan Pita", "Ch. 21 — Secret Behind the Spool")

    scene bg_toko_dalam with dissolve
    play music bgm_toko loop if_changed
    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    "Pria kaya itu sudah pergi. Bau parfumnya yang menyengat pelan-pelan kalah sama aroma teh melati. Di meja jati, kaset yang pitanya terputus tergeletak begitu saja — cokelat, kusut, diam." id b21_001

    "Kai masih menatap pita kusut itu. Pak Ageng sudah kembali ke kursi goyangnya, tenang, kayak badai kecil tadi nggak pernah lewat." id b21_002

    kai "Pak." id b21_003

    ageng "Hmm?" id b21_004

    kai "…Kenapa toko ini ada?" id b21_005

    menu:
        "Seberapa jauh Kai mau mendengar jawaban Pak Ageng?"

        "\"Duduk, Pak. Ceritakan semuanya. Saya nggak buru-buru.\"":
            $ record_major_choice(6, "A")

            play sound sfx_derit_kursi_goyang loop fadein 0.8
            ageng "{i}(mengambil cangkir tehnya, menyesap, memandang deretan lemari kaca){/i} Pertanyaan bagus, Kai. Menurutmu sendiri, buat apa toko ini berdiri di ujung gang buntu yang hampir nggak pernah dilewati orang?" id b21_006a

            kai "Dulu saya pikir tempat ini penyelamat. {i}(jemarinya memainkan tepi cangkir){/i} Buat orang kayak saya — yang takut setengah mati sama hari esok — kaset Bapak itu kayak pegangan. Kayak jaminan semua bakal baik-baik saja. Tapi… habis lihat pria tadi, dan habis jalan sama Yara belakangan ini… saya mulai ragu." id b21_007a

            show ageng senyum at pos_right
            ageng "{i}(tersenyum tipis; kursi goyangnya berderit pelan){/i} Manusia itu rapuh, Kai. Soalnya mereka nggak bisa lihat apa yang ada di depan. Ketidakpastian itu musuh paling besar buat pikiran yang cemas. {i}(jeda){/i} Toko ini ada bukan buat bikin manusia jadi kayak dewa. Toko ini ada sebagai cermin." id b21_008a

            kai "Cermin?" id b21_009a

            show ageng serius at pos_right
            ageng "Iya. Cermin buat lihat sejauh mana kecemasan bisa ngendalikan hidupmu. {i}(menunjuk kaset putus di meja){/i} Pria tadi itu — dia kira kalau dia bisa nguasai hari esok, dia bisa genggam dunia. Dia nggak cari tenang, Kai. Dia cari kendali. Mutlak. Padahal hidup nggak dirancang buat dikendalikan mutlak." id b21_010a

            show ageng iba at pos_right
            "Pak Ageng menghela napas panjang. Tatapannya ke Kai melembut." id b21_011a

            ageng "Coba kamu pikir. Gimana rasanya kalau kamu tahu persis, kata per kata, apa yang bakal Yara omongin besok sore? Kamu tahu persis hari apa, jam berapa, dan gara-gara apa kamu bakal ketawa bareng dia minggu depan?" id b21_012a

            "Kai diam. Dia membayangkan itu: Yara tertawa karena leluconnya — dan dia sudah tahu itu bakal terjadi." id b21_013a

            show kai sedih at pos_left
            kai "…Hambar. {i}(pelan){/i} Nggak ada kejutannya lagi." id b21_014a

            show ageng senyum at pos_right
            ageng "Tepat. {i}(mengangguk mantap){/i} Tahu masa depan itu seringnya malah ngerusak kejutannya. Indahnya hidup itu bukan di garis akhirnya yang sudah tertulis. Tapi di deg-degan-nya jantungmu waktu kamu jalan tanpa tahu di belokan depan ada apa." id b21_015a

            show kai senyum at pos_left
            kai "{i}(mengangkat wajah; matanya lebih jernih sekarang){/i} Jadi… Bapak sengaja biarin kami salah nerjemahin suara-suara di kaset itu?" id b21_016a

            ageng "{i}(terkekeh){/i} Aku cuma muter pitanya, Nak. Hatimulah yang milih mau dengar ketakutan, atau harapan. Dan hari ini… aku senang lihat kamu akhirnya berhenti dengar masa depan, dan mulai dengar detik ini." id b21_017a

            $ flag_g6_cermin = True

            "Kursi goyang itu berderit pelan. Di luar, gang buntu basah seperti biasa. Tapi untuk pertama kalinya, Kai duduk di toko itu tanpa merasa dikejar-kejar besok." id b21_018a
            stop sound fadeout 0.8

        "\"Ceritakan, Pak. Tapi… saya nggak bisa lama-lama.\"":
            $ record_major_choice(6, "B")

            ageng "{i}(menyesap tehnya, memandang lemari kaca){/i} Menurutmu, buat apa toko ini berdiri di gang buntu yang nggak pernah dilewati orang?" id b21_006b

            kai "Dulu saya pikir ini penyelamat, Pak. Buat orang cemas kayak saya, kaset-kaset itu kayak pegangan. Tapi belakangan… saya mulai ragu sendiri." id b21_007b

            show ageng senyum at pos_right
            ageng "{i}(tersenyum tipis){/i} Manusia itu rapuh karena nggak bisa lihat ke depan, Kai. Toko ini ada bukan buat bikin manusia kayak dewa. Toko ini ada sebagai cermin." id b21_008b

            kai "Cermin?" id b21_009b

            show ageng serius at pos_right
            ageng "Cermin buat lihat sejauh mana kecemasan bisa ngendalikan hidupmu. Pria tadi itu nggak cari tenang. Dia cari kendali. Padahal hidup—" id b21_010b

            show kai cemas at pos_left
            kai "{i}(melihat layar, mendesah){/i} …Ibu, Pak. Nyuruh pulang sekarang. Katanya sudah mau magrib." id b21_011b

            show ageng biasa at pos_right
            ageng "Wes, pulang sana. Ibumu nunggu." id b21_012b

            kai "Padahal baru sampai di bagian penting… Besok Bapak lanjutin, ya?" id b21_013b

            show ageng senyum at pos_right
            ageng "Besok itu urusan besok. {i}(tersenyum){/i} Pulang. Hati-hati, gangnya licin." id b21_014b

            "Kai pulang dengan kepala penuh pertanyaan. Kata \"cermin\" itu menempel terus di kepalanya — tapi cermin buat apa, persisnya, dia belum sempat dengar sampai habis." id b21_015b

        "\"…Nggak jadi, Pak. Saya cuma mau beli kaset yang biasa.\"":
            $ record_major_choice(6, "C")

            ageng "Hmm?" id b21_006c

            show kai cemas at pos_left
            kai "Nggak. Nggak jadi, Pak. {i}(menggeleng cepat){/i} Saya… saya cuma mau beli kaset yang biasa. Buat besok." id b21_007c

            show ageng iba at pos_right
            ageng "{i}(diam sebentar, lalu tersenyum){/i} Baik." id b21_008c

            "Pak Ageng bangkit, mengambil satu Kaset Biasa dari rak, dan menyerahkannya tanpa komentar apa-apa lagi. Tidak ada cerita. Tidak ada penjelasan." id b21_009c

            show kai sedih at pos_left
            kai_hati "Kenapa senyumnya kayak gitu… Kayak dia sudah tahu aku bakal kabur dari pertanyaan itu." id b21_010c

            "Sore itu toko terasa lebih dingin dari biasanya. Atau cuma perasaan Kai saja. Dia pulang lebih cepat — dan untuk pertama kalinya, cepatnya itu bukan karena dia buru-buru mendengar besok, tapi karena dia menghindari hari ini." id b21_011c

    stop music fadeout 1.2
    return

label bab_22:
    $ chapter_autosave("bab_22", "Bab 22 — Air yang Jatuh, Detik yang Singgah", "Ch. 22 — Falling Water, Lingering Seconds")

    scene bg_gang_hujan with dissolve
    play sound sfx_hujan_deras loop fadein 0.8

    "Hujan sore itu turun tanpa aba-aba. Langit yang tadinya cuma mendung mendadak tumpah — tebal, sampai ujung gang nggak kelihatan, ketutup kabut putih." id b22_001

    scene bg_teras_toko with dissolve
    show kai biasa at pos_left with dissolve
    show yara biasa at pos_right with dissolve
    "Kai dan Yara lari menembus gang, lalu berhenti terengah-engah di bawah kanopi kayu depan Toko Gema Masa. Pintu toko tertutup rapat di belakang mereka." id b22_002

    yara "{i}(napasnya memburu, menurunkan tas kanvas peralatannya ke sudut paling kering){/i} Basah semua… {i}(memeriksa tasnya){/i} Untung perekamnya nggak kena." id b22_003

    "Jaket abu-abu Yara berubah gelap kena air. Beberapa helai rambutnya yang basah menempel di dahi dan pipinya. Kai menyandarkan punggung ke dinding bata yang dingin, melepas jaketnya yang setengah basah. Dingin merayap masuk, bikin dia sedikit menggigil." id b22_004

    show kai senyum at pos_left
    "Tapi waktu dia menoleh — Yara duduk memeluk lutut di lantai teras yang sempit — dinginnya entah kenapa hilang begitu saja." id b22_005

    kai_hati "Pintunya ketutup. Kita bisa saja ngetuk. …Tapi kok rasanya nggak ada yang mau ngetuk, ya." id b22_006

    "Nggak ada yang mengetuk pintu itu. Nggak ada yang manggil Pak Ageng. Teras dua meter persegi ini — diam-diam mereka sepakat — sudah cukup. Ini seluruh dunia yang mereka butuhkan sore ini." id b22_007

    "Yara merogoh saku jaketnya, mengeluarkan perekam saku kecil. Kali ini tanpa mikrofon panjang — cuma alat kecil itu, diletakkan di lututnya yang ditekuk." id b22_008

    show yara ceria at pos_right
    yara "Hujan kayak gini sayang kalau nggak direkam. {i}(menatap sekeliling teras){/i} Menurutmu, paling enak nangkapnya dari mana?" id b22_009

    menu:
        "Rekam hujan dari mana?"

        "Di bawah talang kanopi.":
            $ record_minor_choice("m15", "A")
            yara "Talang? {i}(mengangguk, menggeser perekamnya ke dekat tetesan talang){/i} Iya sih. Airnya jatuh satu-satu, bunyinya kayak… ketukan. Rapi." id b22_010a

        "Di dekat daun tanaman di pot teras.":
            $ record_minor_choice("m15", "B")
            yara "Daun? {i}(tertawa kecil){/i} Kamu mulai ketularan aku, rek. {i}(meletakkan perekam di samping pot){/i} Dengerin — tiap tetes bunyinya beda, soalnya daunnya goyang." id b22_010b

        "Di payung lipat yang dibuka setengah.":
            $ record_minor_choice("m15", "C")
            yara "Payung? {i}(mengeluarkan payung lipat dari tasnya, membukanya setengah di lantai teras){/i} Hmm… kain payung itu kayak kulit drum. Coba dengar." id b22_010c

    show yara fokus at pos_right
    yara "{i}(memejamkan mata sebentar){/i} Nah. Ini dia." id b22_011
    $ renpy.notify(ui_tr("notify_item_hujan"))

    play music bgm_senja loop fadein 1.5
    show yara ceria at pos_right
    yara "{i}(menyodorkan satu sisi headphone besarnya, tanpa menoleh){/i} Mau dengar?" id b22_012

    "Kai tersenyum tipis. Dia menggeser duduknya lebih dekat, sampai lengan mereka yang dingin bersentuhan. Headphone itu dipasang ke telinga kirinya." id b22_013

    "Lewat rekaman Yara, hujan yang tadi liar berubah jadi sesuatu yang dekat. Ada suara tetes air dari ujung kanopi, jatuh ke genangan dengan nada jernih. Ada suara napas Yara, teratur, di sampingnya. Ada gesekan halus kain baju mereka tiap ada yang bergerak sedikit." id b22_014

    "Mereka nggak bicara. Di bawah tempias hujan yang mendinginkan Malang, kata-kata terasa sia-sia." id b22_015

    "Yara memejamkan mata, menikmati suaranya. Kai justru membuka mata — menatap profil wajah Yara yang kena cahaya kuning redup lampu teras." id b22_016

    kai_hati "Aneh. Aku nggak tahu besok bakal gimana. Nggak tahu enam bulan lagi gimana. {i}(jeda){/i} Tapi semenit ini… aku nggak takut. Sama sekali nggak takut." id b22_017

    stop sound fadeout 0.8
    return

label bab_23:
    $ chapter_autosave("bab_23", "Bab 23 — Gema untuk Masa Lalu", "Ch. 23 — Echoes for the Past")

    scene bg_teras_toko with dissolve
    play music bgm_senja loop if_changed
    show kai biasa at pos_left with dissolve
    show yara biasa at pos_right with dissolve

    "Hujan derasnya pelan-pelan melunak. Tinggal ketukan rintik yang lambat di aspal gang." id b23_001

    "Yara membuka mata. Headphone-nya digeser melingkar di leher. Dia menatap perekam kecil di lututnya, lalu menatap Kai." id b23_002

    yara "Kai." id b23_003

    kai "Ya?" id b23_004

    show yara ceria at pos_right
    yara "Ayo buat rekaman kita sendiri." id b23_005

    kai "Rekaman sendiri? Buat portofoliomu lagi?" id b23_006

    play sound sfx_klik_play
    yara "{i}(menggeleng; rambut setengah basahnya bergoyang){/i} Bukan buat portofolio. Bukan juga ramalan kayak kaset-kaset Pak Ageng yang biasa kamu beli." id b23_007
    yara "{i}(merogoh tas kanvasnya, mengeluarkan kaset kosong berbungkus mika merah — Type IV Metal, yang tempo hari dikasih Pak Ageng — dan memasukkannya ke perekam portabelnya; klik){/i} Kita rekam suara kita sekarang. Tapi bukan buat masa depan. Buat masa lalu." id b23_007_p2

    kai "Masa lalu?" id b23_008

    show yara fokus at pos_right
    yara "Kita kirim pesan buat diri kita yang dulu. Buat bukti… kalau kita berhasil lewat. {i}(menatap Kai lurus){/i} Gimana?" id b23_009

    menu:
        "Kai ikut merekam, atau tidak?"

        "\"Ikut. Buat diriku yang dulu.\"":
            $ record_major_choice(7, "A")

            play sound sfx_klik_play
            "Yara mengulurkan mikrofon kecil, diposisikan tepat di antara wajah mereka berdua. Dia menekan tombol record. Lampu indikator merah kecil berkedip — pita di dalam mulai berjalan." id b23_010a

            show yara ceria at pos_right
            yara "{i}(mendekatkan bibir ke mikrofon){/i} Buat Yara yang sebulan lalu berdiri sendirian di halte, nutup telinga rapat-rapat karena benci bisingnya dunia… {i}(tersenyum ke arah jalanan basah){/i} Jangan takut sama suara-suara berisik di sekitarmu." id b23_011a
            yara "Suatu hari, bising itu bakal ngenalin kamu ke seseorang yang mau bantuin kamu bawa tas tripod berat ini keliling kota. Tanpa ngeluh." id b23_011a_p2

            "Yara menyenggol lengan Kai pakai sikutnya. Giliranmu." id b23_012a

            kai_hati "Oke. Buat Kai yang dulu. Yang ngunci diri di kamar. Yang nulis surat-surat konyol itu. {i}(menarik napas){/i} Ngomong apa, ya…" id b23_013a

            menu:
                "Kalimat pertama rekaman Kai"

                "\"Kamu nggak akan mati hari Jumat ini. Percaya sama aku.\"":
                    $ flavor_g7_opening = "A"

                "\"Letakkan pulpenmu. Surat-surat itu nggak perlu dikirim.\"":
                    $ flavor_g7_opening = "B"

                "\"Keluar dari kamar. Di luar lagi hujan — dan itu nggak seburuk yang kamu kira.\"":
                    $ flavor_g7_opening = "C"

            show kai senyum at pos_left
            kai "{i}(berbicara ke mikrofon, tenang){/i} Buat Kai yang ngunci diri di kamar dan nulis surat-surat perpisahan konyol karena terlalu takut sama hari esok… Letakkan pulpenmu." id b23_014a
            kai "Kamu nggak akan mati hari Jumat ini. Kamu justru bakal mulai benar-benar hidup setelah tumpukan buku itu jatuh. Jalanin saja hari ini. Kejutan di depanmu jauh lebih bagus daripada ramalan apa pun." id b23_014a_p2

            play sound sfx_klik_play
            "Yara menekan tombol stop. Bunyi mekanis kecil. Suara mereka sekarang terkunci di dalam pita hitam berlapis logam itu — rekaman yang nggak menjanjikan apa-apa soal besok, tapi menyimpan rapat-rapat bahagianya detik ini." id b23_015a

            yara "{i}(tersenyum, paling tulus yang pernah Kai lihat){/i} Selesai. …Sekarang diri kita yang dulu pasti lagi dengerin ini. Dan lega." id b23_016a

            kai "{i}(mengangguk; hangat menjalar dari ujung jarinya){/i} Iya. Pasti lega." id b23_017a

        "\"Aku dengerin aja, Yar. Kamu dulu.\"":
            $ record_major_choice(7, "B")

            show kai cemas at pos_left
            kai "Aku… dengerin aja, Yar. Kamu dulu. Aku belum tahu mau ngomong apa." id b23_010b

            show yara biasa at pos_right
            yara "{i}(menatapnya sebentar, lalu mengangguk tanpa memaksa){/i} Ya sudah. Dengerin saja juga ikut, kok." id b23_011b

            play sound sfx_klik_play
            "Yara menekan tombol record dan merekam pesannya sendiri — buat Yara di halte, yang menutup telinga rapat-rapat. Suaranya lembut, dan di kalimat terakhirnya dia melirik Kai sambil tersenyum." id b23_012b

            show yara ceria at pos_right
            yara "…Suatu hari, bising itu bakal ngenalin kamu ke seseorang yang mau bantuin kamu bawa tas tripod berat ini keliling kota. Tanpa ngeluh. {i}(menekan stop){/i} Nah. {i}(menatap Kai){/i} Kalau suatu hari kamu sudah tahu mau ngomong apa, pitanya masih panjang. Kita rekam lagi." id b23_013b

            play sound sfx_klik_play
            show kai senyum at pos_left
            kai "…Makasih, Yar." id b23_014b

            "Kaset itu cuma berisi satu suara sore ini. Tapi Yara menyimpannya dengan cara yang sama hati-hatinya — kayak isinya dua." id b23_015b

        "\"Nggak. Masa lalu biar di sana.\"":
            $ record_major_choice(7, "C")

            show kai sedih at pos_left
            kai "{i}(menggeleng pelan){/i} Nggak, Yar. Masa lalu… biar di sana saja. Aku nggak mau ngomong sama dia." id b23_010c

            show yara sedih at pos_right
            yara "{i}(diam sebentar; tidak tersinggung, hanya menatapnya){/i} …Ya sudah. Nggak apa-apa." id b23_011c

            hide yara with dissolve
            scene bg_gang_hujan with dissolve
            show kai sedih at pos_center with dissolve
            "Kai berdiri, berjalan ke ujung teras, lalu turun ke mulut gang. Rintik hujan menempel di jaketnya. Dari belakang, samar-samar, dia mendengar suara Yara merekam sendirian — pelan, jauh, sesekali diselingi tawa kecil." id b23_012c

            kai_hati "Dia ketawa. Ngomong ke dirinya yang dulu… dan ketawa. {i}(jeda){/i} Kenapa aku nggak bisa?" id b23_013c

            "Kai menunggu di mulut gang sampai rekaman itu selesai — mendengarkan tawa dari teras toko yang tidak dia ikuti, sambil berdiri di bawah rintik yang sama." id b23_014c

    stop music fadeout 1.2
    return

label bab_24:
    $ chapter_autosave("bab_24", "Bab 24 — Bisikan yang Kembali Menggoda", "Ch. 24 — Whispers That Tempt Again")

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop fadein 1.5
    show kai cemas at pos_center with dissolve

    "Malam itu Kai berbaring menatap langit-langit. Kamarnya sekarang jauh lebih rapi. Di meja belajar, kaset mika merah — rekaman suara mereka buat masa lalu — tergeletak manis." id b24_001

    "Harusnya dia tenang. Tapi dadanya justru dirayapi sesak yang baru." id b24_002

    kai_hati "Aku sadar sekarang. Rasa hangat tiap lengan kami kena sentuh. Rasa… nggak enak tiap bel pulang bunyi. Caraku nyari-nyari dia di koridor. {i}(jeda panjang){/i} Aku jatuh cinta. Beneran jatuh cinta sama Yara." id b24_003

    kai_hati "Masalahnya — dia sudah bilang jelas-jelas. Semua rekaman ini buat portofolio. Buat masuk jurusan seni musik di luar kota. Mungkin luar negeri. Habis ujian akhir. Enam bulan lagi." id b24_004

    kai_hati "Enam bulan. Seratus delapan puluh hari. {i}(menelan ludah){/i} Habis itu… duniaku balik sunyi lagi?" id b24_005

    "Dan seperti biasa, kecemasan di kepala Kai mulai berbisik — menunjuk satu tempat: lemari kaca khusus di Toko Gema Masa." id b24_006

    kai_hati "Kaset merah. Enam bulan ke depan. Kalau aku beli… aku bisa dengar. Tawa Yara masih ada di sana, atau nggak. Kalau masih ada, aku bisa napas lega. Kalau nggak ada… {i}(jeda){/i} …setidaknya aku bisa siap-siap patah hati dari sekarang." id b24_007

    scene bg_toko_luar with dissolve
    show kai cemas at pos_center with dissolve

    "Sore harinya, dengan langkah ragu yang sudah terlalu akrab, Kai berdiri lagi di depan pintu kayu toko itu. Tangannya gemetar di gagang pintu." id b24_008

    menu:
        "Apa yang Kai lakukan dengan ketakutannya?"

        "Masuk. Curhat ke Pak Ageng.":
            $ record_major_choice(8, "A")

            play sound sfx_lonceng_pintu
            scene bg_toko_dalam with dissolve
            show kai cemas at pos_left with dissolve
            show ageng iba at pos_right with dissolve

            "Pak Ageng sedang menyeduh kopi hitam. Uap pahitnya memenuhi ruangan. Dia nggak kaget melihat Kai — tapi ada kilat prihatin di matanya waktu melihat cemas itu lagi di wajah Kai." id b24_009a

            ageng "Kamu balik lagi, Kai. {i}(meletakkan teko tanah liatnya){/i} Dan hari ini kamu bawa beban yang beda." id b24_010a

            "Kai nggak duduk. Dia jalan mendekati lemari kaca khusus, menatap kaset Type IV Metal berlabel enam bulan ke depan yang berkilau di bawah lampu kuning." id b24_011a

            kai "Pak… saya mau beli kaset lagi." id b24_012a

            ageng "{i}(menghela napas panjang; berjalan mendekat, berdiri di samping Kai, tidak ikut memandang lemari){/i} Buat apa, Nak? Bukannya kamu sudah belajar dengar hari ini?" id b24_013a

            show kai sedih at pos_left
            kai "Hari ini terlalu indah, Pak. {i}(matanya berkaca-kaca, tetap menatap kaset merah itu){/i} Dan gara-gara terlalu indah… saya jadi takut banget kehilangan. Saya cuma mau tahu satu hal. Enam bulan lagi — Yara masih ada di masa depan saya, atau nggak? Cuma itu. Saya cuma butuh satu kepastian." id b24_014a

            "Pak Ageng diam lama. Lalu, tanpa menjawab, dia berjalan ke rak paling belakang, mengambil satu kaset tua yang sampulnya sudah kosong, dan memasukkannya ke pemutar di konter." id b24_015a

            show ageng biasa at pos_right
            ageng "Dengerin dulu. Baru putuskan." id b24_016a

            stop music fadeout 0.8
            call play_cassette(
                cassette_id="kaset_tawa_siti",
                label_title=_("Kaset Tanpa Sampul — 1994"),
                transcript_lines=[
                    (None, _("[Desis pita tua… lalu tawa seorang perempuan muda — jernih, lepas, direkam puluhan tahun lalu.]")),
                ],
                duration_sec=12,
                allow_skip=True,
            )

            play music bgm_toko loop fadein 1.5
            "Tawa. Cuma tawa. Seorang perempuan muda tertawa karena sesuatu yang sudah nggak bisa didengar lagi sebabnya — dan tawanya berhenti di tengah, karena pitanya memang cuma menyimpan segitu." id b24_017a

            kai "…Itu siapa, Pak?" id b24_018a

            show ageng iba at pos_right
            ageng "{i}(pelan, matanya ke arah kaset yang berputar){/i} Siti. Istriku. {i}(jeda){/i} Dulu aku juga pernah berdiri di tempatmu, Nak. Bedanya, lemari kacaku waktu itu bernama radio. Aku teknisi suara. Aku pikir kalau semua suara bisa kusimpan, nggak ada yang bisa hilang dariku." id b24_019a

            ageng "Ternyata suara bisa disimpan. Orangnya nggak." id b24_020a

            "Tawa di kaset itu sudah habis. Yang tersisa cuma desis — dan Kai, untuk pertama kalinya, mendengar desis itu tanpa merasa harus mengisinya dengan ramalan." id b24_021a

            show kai biasa at pos_left
            kai "{i}(mengusap matanya, kasar){/i} …Saya nggak jadi beli, Pak. Hari ini nggak." id b24_022a

            show ageng senyum at pos_right
            ageng "{i}(mengangguk sekali, pelan){/i} Pulanglah. Bukit Banyak sore ini bagus, katanya. Ada yang nunggu kamu di sana, kan?" id b24_023a

        "Nggak jadi masuk. Besok, di Bukit Banyak, coba bicara ke Yara.":
            $ record_major_choice(8, "B")

            "Tangan Kai sudah menyentuh gagang pintu. Lonceng kecil di atasnya bergoyang sedikit — tapi nggak sampai berbunyi." id b24_009b

            kai_hati "Nggak. Nggak hari ini. {i}(melepaskan gagang pintu){/i} Kalau memang harus ngomong… ngomongnya ke orangnya langsung. Bukan ke kaset." id b24_010b

            "Kai berbalik, menyusuri gang basah itu sendirian. Di belakangnya, lampu toko tetap menyala — dan nggak ada yang tahu dia tadi hampir masuk." id b24_011b

        "Pulang. Pendam sendiri.":
            $ record_major_choice(8, "C")

            show kai sedih at pos_center
            kai_hati "Nggak. Ngapain cerita-cerita. Pak Ageng juga paling cuma bakal senyum-senyum saja. {i}(melepaskan gagang pintu){/i} Biar aku saja yang mikir. Sendiri. Kayak biasanya." id b24_009c

            "Kai berbalik, menyusuri gang basah itu sendirian. Di belakangnya, lampu toko tetap menyala — dan nggak ada yang tahu dia tadi hampir masuk." id b24_011c

    stop music fadeout 1.2
    return

label bab_25:
    $ chapter_autosave("bab_25", "Bab 25 — Bayangan di Ujung Senja", "Ch. 25 — Shadows at Dusk's Edge")

    if get_major_choice(8) in ("A", "B"):

        scene bg_bukit with dissolve
        play music bgm_senja loop fadein 1.5
        show kai cemas at pos_left with dissolve
        show yara biasa at pos_right with dissolve

        "Udara di puncak Bukit Banyak dingin menggigit. Tapi buat Kai, dingin yang sebenarnya menjalar dari tempat lain — dari dalam dadanya sendiri." id b25_001

        "Yara duduk di hamparan rumput liar yang basah oleh embun. Dia baru selesai merekam desau angin yang menyapu pucuk-pucuk pinus di bawah mereka. Headphone-nya dilepas, melingkar di leher." id b25_002

        show yara ceria at pos_right
        $ show_cg_and_unlock("cg_bukit_senja", dissolve)
        yara "{i}(menatap lampu-lampu kota yang menyala satu-satu di kejauhan){/i} Lihat itu, Kai." id b25_003

        "Jarinya menunjuk ke kaki langit, tempat jingga sisa senja melebur sama malam." id b25_004

        yara "Oh iya — dengerin ini dulu. {i}(mengeluarkan perekam sakunya, memutar dengan volume kecil){/i} Yang kemarin, di teras toko itu. Hujan yang kita rekam." id b25_005

        play sound sfx_hujan_deras loop fadein 0.5
        $ renpy.notify(ui_tr("notify_playing_rain_" + (item_file_hujan or "talang")))

        yara "{i}(tersenyum){/i} Bagus, ya. Padahal cuma hujan di teras toko orang." id b25_006

        kai "…Iya. Bagus." id b25_007

        stop sound fadeout 0.8
        yara "Enam bulan lagi, aku mungkin lihat pemandangan yang beda. Kota yang lebih besar, suara-suara yang lebih asing. {i}(matanya berbinar memantulkan cahaya senja){/i} Aku mau rekam deru kereta bawah tanah." id b25_008
        yara "Suara langkah ribuan orang asing di penyeberangan. Bising pelabuhan malam hari. Portofolioku hampir selesai, Kai. Rasanya… masa depan di depan sana kelihatan cerah banget." id b25_008_p2

        "Yara menoleh, berbinar-binar. Kai nggak mampu membalas binar itu. Buat Yara, enam bulan ke depan itu gerbang. Buat Kai, enam bulan ke depan itu tebing." id b25_009

        scene bg_bukit with dissolve
        show kai sedih at pos_left with dissolve
        show yara biasa at pos_right with dissolve
        kai "Kamu… benar-benar pengin pergi, ya?" id b25_010

        show yara sedih at pos_right
        yara "{i}(senyumnya melorot; kerutan tipis muncul di dahinya){/i} Kai, ini impianku. Aku mau belajar lebih banyak soal suara. Soal gimana ngubah bisingnya dunia jadi sesuatu yang bernyawa. {i}(tangannya menyentuh jemari Kai yang sedingin es){/i} Bukannya itu bagus?" id b25_011

        "Tangan Yara hangat. Dan kehangatan itu justru bikin hati Kai makin perih. Dia menggenggam balik jemari itu, erat — kayak dengan begitu waktu bisa ditahan supaya nggak jalan." id b25_012

        kai "Iya. Bagus. Bagus banget. {i}(suaranya serak; matanya beralih ke lampu kota yang mulai kabur){/i} Aku cuma… aku cuma takut duniaku balik sunyi habis kamu pergi. Takut nggak bisa dengar \"musik\" itu lagi kalau kamu nggak ada di sampingku." id b25_013

        if get_major_choice(8) == "B":

            "Yara menatapnya lama. Dan Kai — yang kemarin berdiri di depan pintu toko dan memilih untuk bicara ke orangnya langsung — menarik napas." id b25_014b

            kai "Yar. Ada yang mau kubilang—" id b25_015b

            show yara penasaran at pos_right
            yara "{i}(menunggu){/i} …Ya?" id b25_016b

            "Kalimatnya berhenti di tenggorokan. Di kepala Kai, kalimat itu bunyinya: {i}aku takut kehilangan kamu.{/i} Yang keluar dari mulutnya malah—" id b25_017b

            show kai cemas at pos_left
            kai "…Suara angin di sini. Kemarin pas hujan di teras itu, bunyinya mirip nggak sih?" id b25_018b

            show yara biasa at pos_right
            yara "{i}(mengerjap){/i} …Hmm? {i}(jeda; tersenyum kecil, tidak memaksa){/i} Beda. Angin di bukit lebih tipis. Kayak… napas yang ditahan." id b25_019b

            "Yara membuka buku catatannya dan menulis sesuatu. Cepat, pendek. Kai melirik — tapi Yara sudah menutup bukunya lagi." id b25_020b

            kai_hati "Dia nulis apa? {i}(jeda){/i} Kenapa aku nggak bisa ngomong satu kalimat saja, sih." id b25_021b

        show yara biasa at pos_right
        yara "{i}(menggeser duduk, merapat sampai bahu mereka bersentuhan; bersandar di bahu Kai){/i} Dunia ini nggak akan pernah sunyi, Kai. Bahkan habis aku nggak di sini, suara-suaranya tetap ada. Kamu cuma perlu janji satu hal: jangan pernah nutup telingamu lagi." id b25_022

        "Kai memejamkan mata rapat-rapat. Wangi rambut Yara yang basah oleh kabut sore tercium samar. Di bawah mereka, Malang menyala seluruhnya." id b25_023

        kai_hati "Jatuh cinta itu ternyata begini. Kecemasan paling indah… sekaligus paling nyakitin yang pernah kurekam." id b25_024

    else:

        scene bg_bukit with dissolve
        play music bgm_cemas loop fadein 1.5
        show kai sedih at pos_center with dissolve

        yara_pesan "Kai, maaf ya, aku nggak bisa ke bukit hari ini. Ada urusan keluarga mendadak. Besok ya. Kamu sudah di atas? Hati-hati pulangnya." id b25_025c

        "Kai membaca pesan itu dua kali. Lalu duduk sendirian di hamparan rumput yang basah oleh embun, di titik persis tempat mereka biasa duduk berdua." id b25_026c

        kai_hati "Lampu kotanya nyala satu-satu. Indah. {i}(jeda){/i} Dia pasti bakal bilang sesuatu soal suara angin. Atau soal… entah. Dia selalu punya komentar buat hal-hal yang menurutku biasa saja." id b25_027c

        kai_hati "Enam bulan lagi aku mungkin duduk di sini kayak sekarang. Sendirian. Bedanya, waktu itu nggak ada pesan masuk lagi yang harus kubaca dua kali." id b25_028c

        "Kai memejamkan mata. Angin pinus lewat. Dia nggak merekam apa-apa, nggak cerita ke siapa-siapa — cuma duduk, menggenggam ketakutannya sendiri, sampai lampu kota di bawah sana menyala semuanya." id b25_029c

    stop music fadeout 1.5
    return
