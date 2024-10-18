meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "KEDİ" : "En iyi ve komik hayvan",
            "GTG" : "gitmem gerek",
            "MEYUS" : "karamsar"
            }
kelime = input ("kelime girin")
if kelime in meme_dict.keys ():
    print (meme_dict[kelime])
else:
    print ("be kelime YOK!!!")
