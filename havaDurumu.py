#-*-coding:utf-8-*-
import requests
import time
import json
#kutuphanelerimizi dahil ettik.

#mgb web sitesinin veri servisi icin kullandigi api adresini aliyoruz
api_adresi='http://212.175.180.28/api/merkezler?il='

#kullanıcıdan sehir adını aldık.
sehir = raw_input('Sehir adini giriniz  :')

#sehir adıyla api adresimizi birlestiriyoruz.
url = api_adresi + sehir

#sehir adına göre api adresimizden , sehrimize ait değerleri getiriyoruz.
ilk_donen_json_data = requests.get(url).json() #ayrıca gelen stringi json formatına dönüştürüyoruz.




print """\n------------------------------------------------------------------------------------------------\n"""
print  ilk_donen_json_data[0]['il'] #sehrin adini yazdiriyoruz.
print "\nEnlem : {}".format(ilk_donen_json_data[0]['enlem']) #sehrin enlem degerini yazdiriyoruz.
print "Boylam: {}".format(ilk_donen_json_data[0]['boylam']) #sehrin boylam degerini yazdiriyoruz.
print """\n------------------------------------------------------------------------------------------------\n"""
#donen json formatındaki veride bulunan , son durum kodunu baska bir api adresinde kullanarak sehrimize ait son durum
#degerlerini aliyoruz.

sonDurumKodu=ilk_donen_json_data[0]['sondurumIstNo'];

#bize verilen son durum kodunu yeni apimizden veri cekmek icin kullanacagiz
yeni_api_adresi='http://212.175.180.28/api/sondurumlar?istno='+str(sonDurumKodu)
son_donen_json_data = requests.get(yeni_api_adresi).json()

print "Sicaklik : {}".format(son_donen_json_data[0]['sicaklik']) #Sıcaklık degerini yazdiriyoruz.
print "Nem : {}".format(son_donen_json_data[0]['nem']) #Nem degerini yazdiriyoruz
print "Aktuel Basinc : {}".format(son_donen_json_data[0]['aktuelBasinc']) #Aktuel basinc degerini yazdiriyoruz
print "Verinin servis edildigi tarih  : {}".format(son_donen_json_data[0]['veriZamani']) #Verinin servis edildigi tarih

#sitenin bize vermis oldugu hadise kodlarinin karsiligi olan degerleri hava durumu degiskenine atiyoruz.
havaDurumuKodu=son_donen_json_data[0]['hadiseKodu']
havaDurumu=""
if havaDurumuKodu== "A":
	havaDurumu ="Acik"
if havaDurumuKodu== "AB":
	havaDurumu ="Az bulutlu"
if havaDurumuKodu== "PB":
	havaDurumu ="Parcali Bulutlu"
if havaDurumuKodu== "CB":
	havaDurumu= "Cok Bulutlu"
if havaDurumuKodu== "HY":
	havaDurumu= "Hafif Yagmurlu"
if havaDurumuKodu== "Y":
	havaDurumu= "Yagmurlu"
if havaDurumuKodu== "KY":
	havaDurumu ="Kuvvetli Yagmurlu"
if havaDurumuKodu== "KKY":
	havaDurumu ="Karla Karisik Yagmurlu"
if havaDurumuKodu== "HKY":
	havaDurumu ="Hafif Kar Yagisli"
if havaDurumuKodu== "K":
	havaDurumu ="Kar Yagisli"
if havaDurumuKodu== "YKY":
	havaDurumu ="Yogun Kar Yagisli"
if havaDurumuKodu== "HSY":
	havaDurumu ="Hafif Saganak Yagisli"
if havaDurumuKodu== "SY":
	havaDurumu ="Saganak Yagisli"
if havaDurumuKodu== "KSY":
	havaDurumu ="Kuvvetli Saganak Yagisli"
if havaDurumuKodu== "MSY":
	havaDurumu ="Mevzi Saganak Yagisli"
if havaDurumuKodu== "DY":
	havaDurumu ="Dolu"
if havaDurumuKodu== "GSY":
	havaDurumu ="Gok Gurultulu  Saganak Yagisli"
if havaDurumuKodu== "KGY":
	havaDurumu ="Kuvvetli gokgurultulu saganak yagisli"
if havaDurumuKodu== "SIS":
	havaDurumu ="sisli"
if havaDurumuKodu== "PUS":
	havaDurumu ="puslu"
if havaDurumuKodu== "DMN":
	havaDurumu ="Dumanli"
if havaDurumuKodu== "KF":
	havaDurumu ="Toz veya kum firtinasi"
if havaDurumuKodu== "R":
	havaDurumu ="Ruzgarli"
if havaDurumuKodu== "GKR":
	havaDurumu ="Guneyli Kuvvetli Ruzgar"
if havaDurumuKodu== "KKR":
	havaDurumu ="Kuzeyli Kuvvetli Ruzgar"
if havaDurumuKodu== "SCK":
	havaDurumu= "Sicak"
if havaDurumuKodu== "SGK":
	havaDurumu ="Soguk"
if havaDurumuKodu== "HHY":
	havaDurumu ="Yagisli"

	
print "Hava Durumu : {}".format(havaDurumu) # Hava Durumu degerini ekrana yazdirdik.
