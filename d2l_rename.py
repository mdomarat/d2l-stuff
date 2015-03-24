import os,sys,re

def un_d2l (filename,ext):
 r = r"[0-9]*-[0-9]* - ([\w-]* )*[\w-]* - [\w-]* [0-9]{1,2}, [0-9]{4} [0-9]{3,4} ([AP]M)?- (.*."+ext+")"  
 x = re.match(r,filename)
 if x:
   return x.groups()[2]
 else:
   return filename
 
ext = sys.argv[1]
rel = [ os.rename (f, un_d2l(f,ext)) for f in os.listdir('.') if f.endswith('.'+ext) ]

