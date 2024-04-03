from googletrans import Translator
translator = Translator()
#print(translator.translate('안녕하세요.'))
#print(translator.translate('안녕하세요.',dest='en'))
#print(translator.translate("hello",dest='ja'))
#print(translator.translate("eritas lux mea.",dest='en'))
#Language detection
print(translator.detect("이 문장은 한글로 쓰여졌습니다.'"))
print(translator.translate("This sentence is written in English."))
#https://github.com/ssut/py-googletrans

