"""Senaryo listesinden videolar/NN-konu/script.json dosyalarını üretir.

python senaryo_uret.py            -> eksik olanları yazar
python senaryo_uret.py --hepsi    -> hepsini yeniden yazar

Her video 8 sahnelik aynı iskeleti izler (bkz. KANAL-REHBERI.md):
  0 kanca · 1 derinleştir · 2 araştırma (başlık kartı) · 3 bulgu · 4 neden · 5 çözüm · 6 bugün dene · 7 yorum sorusu
Açıklama metni ve carousel sayfaları sahnelerden otomatik türetilir.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
BRAND, HANDLE = "Sessiz Yük", "@sessizyuk"
VOICE, RATE = "tr-TR-EmelNeural", "+10%"
UYARI = "Bu içerik bilgilendirme amaçlıdır, terapi yerine geçmez. Kendini uzun süre kötü hissediyorsan bir uzmandan destek almak güçlü bir adımdır."


def S(say, mood, pose, props=None, **kw):
    return {"say": say, "mood": mood, "pose": pose, "props": props or [], **kw}


VIDEOS = [
    {
        "dir": "02-beyaz-ayi", "slug": "sy02-beyaz-ayi", "title": "Düşünmemeye çalıştıkça neden artıyor?",
        "cover": {"kicker": "Beyaz Ayı Deneyi", "lines": ["Düşünmemeye", "çalıştıkça *artıyor*"], "scene": 2},
        "tags": ["psikoloji", "overthinking", "düşüncebastırma", "kaygı", "zihinsağlığı", "sessizyük"],
        "sources": "D. M. Wegner, D. J. Schneider, S. R. Carter & T. L. White, \"Paradoxical effects of thought suppression\", Journal of Personality and Social Psychology 53(1), 1987; D. M. Wegner, \"Ironic processes of mental control\", Psychological Review 101(1), 1994.",
        "scenes": [
            S("Bir şeyi düşünmemeye çalıştıkça, *daha çok* mu aklına geliyor?", "heavy", "worried",
              [{"p": "words", "items": ["unut artık", "düşünme", "geçti"], "at": "düşünmemeye"}], headline="Düşünmemeye çalıştıkça *artıyor* mu?"),
            S("Bir anıyı, bir cümleyi, bir korkuyu kafandan atmaya çalışıyorsun. Ama o hep geri geliyor.", "heavy", "facepalm",
              [{"p": "thoughts", "at": "geri"}]),
            S("Psikolog Daniel Wegner katılımcılara basit bir şey söyledi: Beş dakika boyunca *beyaz bir ayıyı* düşünmeyin. Aklınıza gelirse zile basın.",
              "calm", "think", [{"p": "bear", "at": "beyaz"}], x=420, title="BEYAZ AYI DENEYİ", sub="Daniel Wegner · 1987"),
            S("Zil susmadı. Üstelik yasak kalkınca ayı, baştan serbest bırakılan gruptakinden *daha sık* akla geldi.",
              "calm", [{"p": "stand"}, {"p": "point", "at": "Üstelik"}], ["bear"], x=420),
            S("Çünkü zihin, düşünmemen gereken şeyi gelmiş mi diye sürekli kontrol eder. Kontrol ettikçe de onu *hatırlatır.*",
              "heavy", "worried", [{"p": "thoughts", "at": "kontrol"}]),
            S("Wegner'in önerisi şaşırtıcıydı: Kovmak yerine düşüncenin gelmesine *izin ver.* Onu bir bulut gibi izle, tartışma, geçip gitsin.",
              "calm", [{"p": "think"}, {"p": "breathe", "at": "izin"}], [{"p": "cloud", "at": "bulut"}], glow=0.5),
            S("O düşünce yine geldiğinde sadece şunu söyle: Seni görüyorum, *kalabilirsin.* Direnç azalınca çoğu zaman o da sessizleşir.",
              "light", [{"p": "breathe"}, {"p": "calm", "at": "sessizleşir"}], [{"p": "heart", "at": "görüyorum"}], glow=0.8),
            S("Senin kovamadığın beyaz ayın ne? Yorumlara yaz.", "light", "hug", ["heart"], glow=1),
        ],
    },
    {
        "dir": "03-sahtekar-sendromu", "slug": "sy03-sahtekar-sendromu", "title": "Bir gün anlayacaklar mı?",
        "cover": {"kicker": "Sahtekâr Sendromu", "lines": ["Bir gün", "*anlayacaklar* mı?"], "scene": 0},
        "tags": ["psikoloji", "sahtekarsendromu", "özgüven", "mükemmeliyetçilik", "zihinsağlığı", "sessizyük"],
        "sources": "P. R. Clance & S. A. Imes, \"The impostor phenomenon in high achieving women\", Psychotherapy: Theory, Research & Practice 15(3), 1978; D. M. Bravata ve ark., Journal of General Internal Medicine 35(4), 2020.",
        "scenes": [
            S("Başardıkça, bir gün herkesin senin aslında *yetersiz* olduğunu anlayacağından mı korkuyorsun?", "heavy", "shrink",
              [{"p": "spotlight", "at": "herkesin"}], headline="Bir gün *anlayacaklar* mı?"),
            S("Övüldüğünde içinden 'şanstı' diyorsun. Bunu hak etmediğini düşünüyorsun.", "heavy", "shrink",
              [{"p": "words", "items": ["şanstı", "hak etmedim", "yakında anlarlar"], "at": "Övüldüğünde"}]),
            S("Psikologlar Pauline Clance ve Suzanne Imes bunu ilk kez başarılı kadınlarda tanımladı. Diplomaları, ödülleri vardı. Ama kendilerini *sahtekâr* gibi hissediyorlardı.",
              "calm", "think", [], title="SAHTEKÂR SENDROMU", sub="Clance & Imes · 1978"),
            S("Sonraki araştırmalar bunun kadın erkek, öğrenci, doktor, pek çok insanda görüldüğünü gösterdi. Yani *yalnız değilsin.*",
              "calm", [{"p": "stand"}, {"p": "open", "at": "yalnız"}], [{"p": "crowd", "at": "öğrenci"}]),
            S("İşin garibi şu: Bu his çoğu zaman yetersizlikten değil, *çok yüksek standartlardan* doğar. Kendine, başkalarına davrandığından çok daha sertsin.",
              "heavy", "worried", [{"p": "stone", "at": "standartlardan"}]),
            S("Küçük bir öneri: Bir kanıt defteri tut. Aldığın güzel geri bildirimleri, çözdüğün sorunları *tek tek* yaz.",
              "calm", [{"p": "think"}, {"p": "reach", "at": "defteri"}], [{"p": "list", "at": "defteri"}], x=440, glow=0.5),
            S("İçindeki ses 'yetersizsin' dediğinde deftere bak. Hisler gerçektir ama her zaman *doğru* değildir.",
              "light", [{"p": "stand"}, {"p": "calm", "at": "Hisler"}], ["list", {"p": "heart", "at": "doğru"}], x=440, glow=0.8),
            S("Sen en son neyi 'şanstı' diye geçiştirdin? Yorumlara yaz.", "light", "hug", ["heart"], glow=1),
        ],
    },
    {
        "dir": "04-dislanma-acisi", "slug": "sy04-dislanma-acisi", "title": "Dışlanmak neden bu kadar acıtır?",
        "cover": {"kicker": "Siber Top Deneyi", "lines": ["Dışlanmak neden", "*acıtır?*"], "scene": 2},
        "tags": ["psikoloji", "yalnızlık", "dışlanma", "ilişkiler", "zihinsağlığı", "sessizyük"],
        "sources": "N. I. Eisenberger, M. D. Lieberman & K. D. Williams, \"Does rejection hurt? An fMRI study of social exclusion\", Science 302, 2003; K. D. Williams, \"Ostracism\", Annual Review of Psychology 58, 2007.",
        "scenes": [
            S("Bir grupta görmezden gelindiğinde göğsünde neden *gerçek bir acı* hissediyorsun?", "heavy", "sad", [],
              others=[{"x": 200, "pose": "open", "scale": 0.85, "dim": True}, {"x": 880, "pose": "open", "scale": 0.85, "dim": True}],
              headline="Dışlanmak neden *acıtır?*"),
            S("Kimse sana vurmadı. Ama canın yanıyor. Bu bir abartı değil.", "heavy", "knees", []),
            S("Araştırmacılar katılımcıları beyin tarayıcısına alıp bilgisayarda basit bir top oyunu oynattı. Bir süre sonra diğer oyuncular topu ona *hiç atmadı.*",
              "calm", [{"p": "open"}, {"p": "sad", "at": "hiç"}], [{"p": "ball"}],
              others=[{"x": 190, "pose": "open", "scale": 0.85}, {"x": 890, "pose": "open", "scale": 0.85}],
              title="SİBER TOP DENEYİ", sub="Eisenberger · 2003"),
            S("Dışlanan kişilerin beyninde, fiziksel acının rahatsızlığıyla ilişkilendirilen bir bölge *hareketlendi.*",
              "heavy", "sad", ["ball"], others=[{"x": 190, "pose": "open", "scale": 0.85, "dim": True}, {"x": 890, "pose": "open", "scale": 0.85, "dim": True}]),
            S("Bunun mantıklı bir sebebi var. İnsan binlerce yıl grupla hayatta kaldı. Gruptan kopmak, beyin için *tehlike* demekti.",
              "calm", "hug", [{"p": "crowd", "at": "grupla"}]),
            S("Yani dışlandığında bu kadar etkilenmen zayıflık değil. Sinir sisteminin seni *korumaya* çalışması.",
              "calm", [{"p": "stand"}, {"p": "calm", "at": "korumaya"}], [], glow=0.5),
            S("Kendini dışarıda hissediyorsan, güvendiğin tek bir kişiye kısa bir mesaj at. Küçük bir bağ bile *yardımcı olabilir.*",
              "light", "phone", [{"p": "phone", "at": "mesaj"}, {"p": "heart", "at": "bağ"}], glow=0.8),
            S("En son ne zaman kendini dışarıda bırakılmış hissettin? Yorumlara yaz.", "light", "hug", ["heart"], glow=1),
        ],
    },
    {
        "dir": "05-duyguyu-adlandir", "slug": "sy05-duyguyu-adlandir", "title": "İçindeki fırtınanın adı ne?",
        "cover": {"kicker": "Duyguyu Adlandırmak", "lines": ["İçindeki fırtınanın", "*adı* ne?"], "scene": 0},
        "tags": ["psikoloji", "duygular", "kaygı", "farkındalık", "zihinsağlığı", "sessizyük"],
        "sources": "M. D. Lieberman ve ark., \"Putting feelings into words: Affect labeling disrupts amygdala activity in response to affective stimuli\", Psychological Science 18(5), 2007.",
        "scenes": [
            S("İçinde bir şey kıpır kıpır ama *ne olduğunu* bilmiyorsun. Sadece kötü hissediyorsun.", "heavy", "worried",
              ["cloud", "rain"], headline="İçindeki fırtınanın *adı* ne?"),
            S("Bu belirsizlik, duygunun kendisinden bile daha yorucu olabilir.", "heavy", "shrink", ["cloud", "rain"]),
            S("Matthew Lieberman ve ekibi katılımcılara öfkeli ya da korkmuş yüzler gösterdi. Bazıları yüzdeki duyguya *bir isim* verdi.",
              "calm", "think", [{"p": "eyes", "at": "yüzler"}], title="DUYGUYU ADLANDIRMAK", sub="UCLA · 2007"),
            S("İsim verenlerde, beynin alarm merkezi olan amigdalanın tepkisi *azaldı.*", "calm",
              [{"p": "stand"}, {"p": "point", "at": "azaldı"}], [{"p": "cloud", "at": "amigdalanın"}]),
            S("Yani duyguna isim koymak, onu yönetmenin ilk adımı. Belirsiz bir fırtına, adı konunca *bir hava durumuna* dönüşür.",
              "calm", [{"p": "think"}, {"p": "calm", "at": "hava"}], [{"p": "cloud", "at": "fırtına"}], glow=0.4),
            S("Şimdi dene: Ne hissettiğini tek kelimeyle söyle. Kırgın mısın, yorgun mu, yalnız mı?",
              "light", "breathe", [{"p": "words", "items": ["kırgınım", "yorgunum", "kıskandım", "yalnızım"], "at": "Kırgın"}], glow=0.6),
            S("'Şu an kırgınım' demek kırgınlığı yok etmez. Ama artık *sen ona bakarsın,* o sana değil.",
              "light", [{"p": "breathe"}, {"p": "calm", "at": "bakarsın"}], [{"p": "heart", "at": "bakarsın"}], glow=0.8),
            S("Şu an hissettiğin şeyin adı ne? Tek kelimeyle yorumlara yaz.", "light", "hug", ["heart"], glow=1),
        ],
    },
    {
        "dir": "06-kendine-sert", "slug": "sy06-kendine-sert", "title": "Kendine böyle mi konuşuyorsun?",
        "cover": {"kicker": "Öz Şefkat", "lines": ["Kendine *böyle*", "mi konuşuyorsun?"], "scene": 1},
        "tags": ["psikoloji", "özşefkat", "içsesin", "mükemmeliyetçilik", "zihinsağlığı", "sessizyük"],
        "sources": "J. G. Breines & S. Chen, \"Self-compassion increases self-improvement motivation\", Personality and Social Psychology Bulletin 38(9), 2012; K. D. Neff, \"Self-compassion\", Self and Identity 2, 2003.",
        "scenes": [
            S("Bir hata yaptığında içinden kendine ne diyorsun? Bir *arkadaşına* asla söylemeyeceğin şeyler mi?", "heavy", "facepalm",
              [{"p": "words", "items": ["aptalsın", "yine mi", "beceriksiz"], "at": "içinden"}], headline="Kendine *böyle* mi konuşuyorsun?"),
            S("Çoğumuz sert olursak daha iyi olacağımızı düşünürüz. Kendimizi kırbaçlarsak *düzeleceğimizi.*", "heavy", "shrink",
              [{"p": "words", "items": ["aptalsın", "yine mi", "beceriksiz", "hep böylesin"]}]),
            S("İki psikolog bunu test etti. Öğrencilere zor bir sınav verdiler, sonra bir gruba başarısızlığa *şefkatle* bakmalarını söylediler.",
              "calm", "think", [{"p": "list", "at": "sınav"}], x=440, title="ÖZ ŞEFKAT", sub="Breines & Chen · 2012"),
            S("Ardından ikinci sınava hazırlanma fırsatı verildi. Şefkatli grup *daha uzun* çalıştı.", "calm",
              [{"p": "stand"}, {"p": "point", "at": "Şefkatli"}], ["list"], x=440),
            S("Çünkü kendine sert davranmak hatayı utanca çevirir. Utanç da insanı düzeltmeye değil, *saklanmaya* iter.",
              "heavy", [{"p": "worried"}, {"p": "shrink", "at": "saklanmaya"}], [{"p": "stone", "at": "utanca"}]),
            S("Bir dahaki hatanda kendine sor: Aynı şeyi en yakın arkadaşın yapsa ona ne derdin? Sonra *aynı cümleyi* kendine söyle.",
              "light", [{"p": "think"}, {"p": "hug", "at": "aynı"}], [{"p": "heart", "at": "aynı"}], glow=0.7),
            S("Şefkat kendini serbest bırakmak değil. Düştüğünde kalkabilmek için *el uzatmak.*",
              "light", [{"p": "calm"}, {"p": "open", "at": "uzatmak"}], ["heart"], glow=0.9),
            S("Kendine en sık söylediğin sert cümle ne? Yorumlara yaz, burada kimse yargılamaz.", "light", "hug", ["heart"], glow=1),
        ],
    },
    {
        "dir": "07-erteleme", "slug": "sy07-erteleme", "title": "Erteliyorsan tembel değilsin",
        "cover": {"kicker": "Erteleme", "lines": ["Erteliyorsan", "*tembel* değilsin"], "scene": 0},
        "tags": ["psikoloji", "erteleme", "motivasyon", "kaygı", "zihinsağlığı", "sessizyük"],
        "sources": "F. Sirois & T. Pychyl, \"Procrastination and the priority of short-term mood regulation\", Social and Personality Psychology Compass 7(2), 2013; M. J. A. Wohl, T. A. Pychyl & S. H. Bennett, Personality and Individual Differences 48(7), 2010.",
        "scenes": [
            S("Yapman gereken iş orada duruyor. Sen ise telefona bakıyorsun. Sonra kendine *tembel* diyorsun.", "heavy", "phone",
              ["phone", {"p": "list", "at": "iş"}], headline="Erteliyorsan *tembel* değilsin"),
            S("Ama araştırmalar bambaşka bir şey söylüyor.", "heavy", [{"p": "phone"}, {"p": "stand", "at": "bambaşka"}], ["list"]),
            S("Psikologlar Fuschia Sirois ve Tim Pychyl'e göre erteleme bir zaman sorunu değil, bir *duygu* sorunu.",
              "calm", "think", [], title="ERTELEME", sub="Sirois & Pychyl · 2013"),
            S("O iş sende sıkıntı, kaygı ya da yetersizlik hissi uyandırıyor. Ertelemek o kötü hissi *hemen* susturuyor.",
              "heavy", [{"p": "worried"}, {"p": "phone", "at": "Ertelemek"}], [{"p": "cloud", "at": "sıkıntı"}, {"p": "phone", "at": "Ertelemek"}]),
            S("Kısa vadede rahatlıyorsun. Ama iş büyüyor, suçluluk ekleniyor ve döngü *yeniden* başlıyor.",
              "heavy", [{"p": "phone"}, {"p": "facepalm", "at": "suçluluk"}], [{"p": "stone", "at": "büyüyor"}]),
            S("Çıkış yolu daha fazla disiplin değil, daha *küçük bir başlangıç.* Sadece ilk adımı belirle: dosyayı aç, ilk cümleyi yaz.",
              "calm", [{"p": "think"}, {"p": "reach", "at": "ilk"}], [{"p": "list", "at": "ilk"}], x=440, glow=0.5),
            S("Ve kendini affet. Bir çalışmada, ertelediği için kendini affeden öğrenciler bir sonraki sınavda *daha az* erteledi.",
              "light", [{"p": "breathe"}, {"p": "hug", "at": "affeden"}], [{"p": "heart", "at": "affet"}], glow=0.8),
            S("Senin şu an ertelediğin iş ne? Yorumlara yaz, ilk adımını birlikte bulalım.", "light", "open", ["heart"], glow=1),
        ],
    },
    {
        "dir": "08-olumsuzluk-yanliligi", "slug": "sy08-olumsuzluk-yanliligi", "title": "Bir eleştiri on iltifatı siler mi?",
        "cover": {"kicker": "Olumsuzluk Yanlılığı", "lines": ["Bir eleştiri", "*on iltifatı* siler"], "scene": 0},
        "tags": ["psikoloji", "eleştiri", "özgüven", "overthinking", "zihinsağlığı", "sessizyük"],
        "sources": "R. F. Baumeister, E. Bratslavsky, C. Finkenauer & K. D. Vohs, \"Bad is stronger than good\", Review of General Psychology 5(4), 2001; J. Gottman, Why Marriages Succeed or Fail, 1994; M. E. P. Seligman ve ark., American Psychologist 60(5), 2005.",
        "scenes": [
            S("Gün boyu güzel şeyler duydun. Ama gece aklında kalan, o *tek eleştiri* oldu.", "heavy", "sad",
              [{"p": "words", "items": ["harikaydın", "eline sağlık", "ama…"], "at": "güzel"}], headline="Bir eleştiri *on iltifatı* siler mi?"),
            S("Bu sende bir kusur değil. Hepimizin beyni böyle çalışıyor.", "heavy", [{"p": "sad"}, {"p": "stand", "at": "Hepimizin"}], [{"p": "crowd", "at": "Hepimizin"}]),
            S("Roy Baumeister ve ekibi yüzlerce çalışmayı inceledi. Sonuç neredeyse her alanda aynıydı: Kötü olaylar, iyilerden *daha güçlü* iz bırakıyor.",
              "calm", "think", [], title="KÖTÜ, İYİDEN GÜÇLÜDÜR", sub="Baumeister · 2001"),
            S("İlişki araştırmacısı John Gottman'a göre uzun süren çiftlerde, her olumsuz an için yaklaşık *beş* olumlu an var.",
              "calm", [{"p": "stand"}, {"p": "point", "at": "beş"}], [], others=[{"x": 820, "pose": "open", "scale": 0.85, "dim": True}], x=420),
            S("Atalarımız için bir tehlikeyi kaçırmak, güzel bir şeyi kaçırmaktan çok daha pahalıydı. Beyin bu yüzden *kötüye* odaklanır.",
              "heavy", "worried", [{"p": "eyes", "at": "tehlikeyi"}]),
            S("O zaman dengeyi elle kurmalısın. Akşamları o gün iyi giden *üç şeyi* yaz. Küçük olsun, sorun değil.",
              "calm", [{"p": "think"}, {"p": "reach", "at": "üç"}], [{"p": "list", "at": "yaz"}], x=440, glow=0.5),
            S("Seligman'ın çalışmasında bu basit alışkanlık, aylarca süren bir iyi oluş artışı sağladı. Eleştiri yine gelecek. Ama artık *tek başına* olmayacak.",
              "light", [{"p": "calm"}, {"p": "open", "at": "tek"}], [{"p": "heart", "at": "Eleştiri"}], glow=0.8),
            S("Bugün iyi giden küçük bir şey söyle. Yorumlara yaz.", "light", "arms_up", ["sun"], glow=1),
        ],
    },
    {
        "dir": "09-yapmadiklarimiz", "slug": "sy09-yapmadiklarimiz", "title": "Seni en çok ne pişman eder?",
        "cover": {"kicker": "Pişmanlık", "lines": ["Seni en çok", "ne *pişman* eder?"], "scene": 1},
        "tags": ["psikoloji", "pişmanlık", "cesaret", "hayat", "zihinsağlığı", "sessizyük"],
        "sources": "T. Gilovich & V. H. Medvec, \"The experience of regret: What, when, and why\", Psychological Review 102(2), 1995.",
        "scenes": [
            S("Gece aklına gelen pişmanlıklar, yaptıkların mı, yoksa *yapmadıkların* mı?", "heavy", "sad", ["moon"],
              headline="Seni en çok ne *pişman* eder?"),
            S("Söyleyemediğin o cümle. Gidemediğin o yer. Denemediğin o şans.", "heavy", "knees",
              ["moon", {"p": "words", "items": ["keşke söyleseydim", "keşke gitseydim", "keşke deneseydim"], "at": "Söyleyemediğin"}]),
            S("Thomas Gilovich ve Victoria Medvec insanlara hayatlarındaki en büyük pişmanlıkları sordu.",
              "calm", "think", [], title="PİŞMANLIK", sub="Gilovich & Medvec · 1995"),
            S("Kısa vadede insanlar yaptıkları hatalara üzülüyordu. Ama hayatın geneline bakınca, pişmanlıkların çoğu *yapmadıkları* şeylerdi.",
              "calm", [{"p": "stand"}, {"p": "point", "at": "yapmadıkları"}], []),
            S("Yaptığın bir hatanın sonucunu görürsün, ondan ders çıkarırsın. Yapmadığın şey ise açık bir kapı gibi *hep merak edilir.*",
              "heavy", "worried", [{"p": "door", "at": "kapı"}], x=440),
            S("Bu bir korku değil, bir pusula. Seni hâlâ düşündüren o şey, belki hâlâ *yapılabilir.*",
              "light", [{"p": "stand"}, {"p": "walk", "at": "pusula"}], ["door"], x=620, glow=0.6),
            S("Bugün o yöne tek bir küçük adım at. Bir mesaj, bir başvuru, bir telefon.",
              "light", "reach", ["door", {"p": "heart", "at": "adım"}], x=620, glow=0.8),
            S("Senin yapmadığın için pişman olduğun şey ne? Yorumlara yaz.", "light", "arms_up", ["sun"], glow=1),
        ],
    },
    {
        "dir": "10-uykusuzluk-ve-duygular", "slug": "sy10-uykusuzluk", "title": "Uykusuz gecenin ertesi neden her şey ağır?",
        "cover": {"kicker": "Uyku ve Duygu", "lines": ["Uykusuz gecenin", "*ertesi*"], "scene": 0},
        "tags": ["psikoloji", "uyku", "uykusuzluk", "duygular", "zihinsağlığı", "sessizyük"],
        "sources": "S.-S. Yoo, N. Gujar, P. Hu, F. A. Jolesz & M. P. Walker, \"The human emotional brain without sleep\", Current Biology 17(20), 2007.",
        "scenes": [
            S("Kötü uyuduğun bir gecenin ertesi, en küçük şey bile neden *gözünü dolduruyor?*", "heavy", "lying",
              ["bed", "moon", {"p": "clock", "at": "gecenin"}], x=520, headline="Uykusuz gecenin *ertesi*"),
            S("Bir mesaja alınıyorsun, bir sese sinirleniyorsun. Sonra da kendine kızıyorsun.", "heavy",
              [{"p": "sad"}, {"p": "facepalm", "at": "kendine"}], [{"p": "phone", "at": "mesaja"}]),
            S("Matthew Walker'ın ekibi bir grup gönüllüyü bir buçuk gün uykusuz bıraktı. Sonra onlara rahatsız edici görüntüler gösterdi.",
              "calm", "think", [{"p": "eyes", "at": "görüntüler"}], title="UYKU VE DUYGU", sub="Berkeley · 2007"),
            S("Uykusuz grubun beyninde amigdala, yani alarm merkezi, yaklaşık *yüzde altmış* daha güçlü tepki verdi.",
              "heavy", "worried", [{"p": "cloud", "at": "amigdala"}, {"p": "rain", "at": "güçlü"}]),
            S("Normalde bu alarmı yatıştıran ön beyin bölgesiyle bağlantı da *zayıflamıştı.* Fren tutmuyordu.",
              "heavy", "shrink", ["cloud"]),
            S("Yani o gün yaşadığın taşkın duygular karakterinden değil, *yorgunluğundan* olabilir.",
              "calm", [{"p": "stand"}, {"p": "breathe", "at": "yorgunluğundan"}], [], glow=0.5),
            S("Uykusuz bir günün ertesinde büyük kararlar verme. Kendine şunu söyle: Bugün her şey olduğundan *daha ağır* görünüyor.",
              "light", [{"p": "calm"}, {"p": "hug", "at": "Bugün"}], [{"p": "heart", "at": "Kendine"}], glow=0.8),
            S("Uykusuz kaldığında en çok neye tepki veriyorsun? Yorumlara yaz.", "light", "hug", ["heart", "moon"], glow=1),
        ],
    },
]


def tr_title(s: str) -> str:
    """'BEYAZ AYI DENEYİ' -> 'Beyaz Ayı Deneyi' (str.title() breaks İ/ı)."""
    low = s.replace("I", "ı").replace("İ", "i").lower()
    return " ".join(w[:1].replace("i", "İ").replace("ı", "I").upper() + w[1:] for w in low.split())


def plain(s: str) -> str:
    return s.replace("*", "")


def caption(v: dict) -> str:
    sc = v["scenes"]
    title = sc[2].get("title", v["cover"]["kicker"]).upper()
    return "\n\n".join([
        plain(sc[0]["say"]) + " 👇",
        f"{title} ({sc[2].get('sub', '')})\n" + plain(sc[2]["say"]) + " " + plain(sc[3]["say"]),
        "NEDEN OLUYOR?\n" + plain(sc[4]["say"]),
        "BUGÜN İÇİN\n" + plain(sc[5]["say"]) + " " + plain(sc[6]["say"]),
        plain(sc[7]["say"]),
        "Kaynaklar: " + v["sources"],
        UYARI,
    ])


def carousel(v: dict) -> list:
    sc, c = v["scenes"], v["cover"]
    return [
        {"kicker": f"Psikoloji · {c['kicker']}", "title": sc[0].get("headline", " ".join(c["lines"])), "scene": 0},
        {"kicker": sc[2].get("sub", "Araştırma"), "title": tr_title(sc[2].get("title", c["kicker"])), "body": sc[2]["say"], "scene": 2},
        {"kicker": "Ne bulundu?", "title": plain(sc[3]["say"]).split(".")[0] + ".", "body": sc[4]["say"], "scene": 4},
        {"kicker": "Bugün dene", "title": "Küçük bir adım", "body": sc[5]["say"] + "\n\n" + sc[6]["say"], "scene": 6},
        {"kicker": "Sıra sende", "title": sc[7]["say"], "body": "Kaydet, ihtiyacı olan birine gönder.", "scene": 7},
    ]


def main() -> None:
    force = "--hepsi" in sys.argv
    for v in VIDEOS:
        d = HERE / "videolar" / v["dir"]
        f = d / "script.json"
        if f.exists() and not force:
            continue
        d.mkdir(parents=True, exist_ok=True)
        data = {"slug": v["slug"], "title": v["title"], "brand": BRAND, "handle": HANDLE, "voice": VOICE, "rate": RATE,
                "cover": v["cover"], "scenes": v["scenes"],
                "post": {"caption": caption(v), "hashtags": v["tags"]}, "carousel": carousel(v)}
        f.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print("yazıldı:", f.relative_to(HERE))


if __name__ == "__main__":
    main()
