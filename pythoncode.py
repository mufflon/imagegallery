import os
import sys

text = sys.stdin.read()

file_endings = [".jpg",".jpeg",".png"]

prefix = "prefix"

def get_first_occurence(haystack, needles):
	for i in range(len(haystack)):
		for needle in needles:
			if haystack[i:i+len(needle)].lower() == needle.lower():
				return i, needle, i+len(needle)
	return -1

start, ending, end = get_first_occurence(text[len(prefix):], file_endings)

#print("start: " + str(start) + " ending: " + str(ending) + " end: " + str(end))

image_path = text[len(prefix):len(prefix) + end].strip()

dir_path = os.path.dirname(image_path)

print(dir_path)