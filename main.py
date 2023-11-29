from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
              "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %'50''den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
              "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.'2019''da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor",
              "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.","Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
              "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
              "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

@app.route("/")
def bagimlilik():
    return f'<a href="/rastgele_gercekler"> goruntule </a>'
    return f'<a href="/ADRES"> oyun </a>'

@app.route("/rastgele_gercekler")
def aaa():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/ADRES")
def FONKSIYON_ADI():
    print("ŞİFRE OLUŞTURUCU")

    def gen_pass(pass_length):
        elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = ""

        for i in range(8):
            password += random.choice(elements)
        return password

app.run(debug=True)