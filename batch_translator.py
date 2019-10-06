#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Magra
#
# Created:     13/06/2019
# Copyright:   (c) Magra 2019
# Licence:     Magra Inc.
#-------------------------------------------------------------------------------


import glob
from googletrans import Translator
import os

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

subfiles = glob.glob("**/*.vtt",recursive =True)
for files in subfiles:
    os.rename(files,files+"NT")
    current_file_new_name = open(files+"NT")
    read_file = current_file_new_name.read()
    current_file_new_name.seek(0)
    for i in range(1000,len(read_file),1000):
        read_file_custom = current_file_new_name.read(i)
        if translator.detect(read_file_custom).lang != "en":
            try:
                translated_para= translator.translate(read_file_custom,dest='en').text
            except:
                print("Error in translating ",files, " around ", i,"(+-500)")
                translated_para = read_file_custom

            translated_file = open(files,"a")

            try:
                translated_file.write(translated_para)
            except:
                print("Error in Writing ",files, " around ", i,"(+-500)")
                translated_file.write(read_file_custom)
        else:
            print(files," around ", i," +-500" ," is already in english")
            break
    try:
        translated_file.close()
    except:
        pass
    current_file_new_name.close()
    print(files," Translated")

















