import re #import regularEx

in_file, out_file  = input("Masukan nama file input dan output: ").split(" ") #meminta output dan input
file_in = open(in_file, 'r') #membuat file input object

file_out = open(out_file, 'w') #membuat file output object
my_str = file_in.read() #membuat string dari file input

my_list = re.split('^.*?<start>|<end>.*?<start>|<end>.*?$', my_str) #menghilangkan diluar <start> dan <end>
my_print = ' '.join(my_list).strip() #menghilangkan spasi di sisi kanan dan kiri

print(my_print, file = file_out) # mengeluarkan input ke dalam file_out 

file_out.close() #close onject
file_in.close() #close object