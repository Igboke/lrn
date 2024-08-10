import re

#analyzing download folder list

#load the file into our variable
file_ = open('danke.txt','r')
asdf_ = file_.read()

#create a regular expression
film_media_ = '\w*\.mp4|\w*\.webp|\w*\.mkv'
pic_media_ = '\w*\.jpg|\w*\.png'
music_media_= '\w*\.mp3'
docu_media_ = '\w*\.pdf|\w*\.pptx|\w*\.epub|\w*\.docx|\w*\.txt|\w*\.ipynb|\w*\.PDF'

#analysis
lst_1=[film_media_,pic_media_,music_media_,docu_media_]
lst_2=[len(re.findall((a),asdf_)) for a in lst_1 ]
aly={'film':lst_2[0],'pictures':lst_2[1],'music':lst_2[2],'document':lst_2[3]}

print(aly)