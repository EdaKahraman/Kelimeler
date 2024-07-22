while True:
  meme_dict = {
      "CRINGE": "Garip ya da utandırıcı bir şey",
      "LOL": "Komik bir şeye verilen cevap",
      "ROFL" : "Bir şakaya karşılık verilen cevap",
      "SHEESH" : "Onaylamamak",
      "CREEPY" : "Korkunç",
      "AGGRO" : "Agresifleşmek/sinirlenmek"
}

  word = input("Anlamını bilmediğiniz bir kelime yazın (lütfen hepsini büyük harflerle yazın): ")
  if word in meme_dict.keys():
    print(meme_dict[word])   
  else:
    print("Bu kelime sözlüğümüzde bulunmamaktadır.Lütfen başka bir kelime yazın.")
