from iptcinfo3 import IPTCInfo
import os
import sys

path = sys.argv[1]

file_endings = ["jpeg", "jpg", "png"]

for file in os.listdir(path):
    print(file)
    try:
        file_components = file.rsplit('.', 1)
        if file_components[1] in file_endings:

            output_filename = file_components[0] + ".md"
            text = ""
            
            info = IPTCInfo(path + "/" + file, force=True)
            
            try:
                text = text + "Title: " + info["caption/abstract"].decode("utf-8") + "\n"
            except:
                text = text + "Title: " + "okänd\n"
            try:
                text = text + "Date: " + info["date created"].decode("utf-8") + "\n"
            except:
                text = text + "Date: " + "okänd\n"
            try:
                text = text + "Author: " + info["by-line"].decode("utf-8") + "\n"
            except:
                text = text + "Author: " + "okänd\n"
            
            print(output_filename)
            
            output_file = open(path + "/" + output_filename,"w+")
            output_file.write(text)
            output_file.close()
    except Exception as e:
        print(e)