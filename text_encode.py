from mpmath import mp,mpf
import time 
from p_tqdm  import p_map
import sys
import pickle
sys.setrecursionlimit(3000)# χοντρες μαλακιες θα επρεπε αντι να προσπαθω επιθετικα να ανατιναξω τον υπολογιστη μου
# να κατσω να φτιαξω πρωτα τα πάντα να ειναι αρθμημενα ώστε να επιστρεφουν και να κωδικοποιουνται με την σωστη σειρα
flag=0


#mp.dps=1
#hex_bin=bin.hex()#μετατροπή σε hex
#print(type(hex_bin))
#arithmos_bit=len(hex_bin)

perioehomeno=open("Fahrenheit_451.txt","r")

#  message = perioehomeno
perioehomeno=perioehomeno.readlines()
perioehomeno="".join(perioehomeno)
message=perioehomeno
message_len = len(message)
demo_string=message
starting_string=demo_string
mp.dps=10000

#demo_string=demo_string[:100]

#arithmos_bit=len(demo_string)
arithmos_bit=256
lista_kopsimatos=[]
splicing_counter=0
#να βαλω και εδω παραλληλια καθως και στην δημιουργια ορισματων διοτι χανω χρόνο
while(True):
    if splicing_counter+arithmos_bit>len(demo_string):
        arg=demo_string[splicing_counter:len(demo_string)]
        temp=arg
        lista_kopsimatos.append(arg)
        diafora=len(demo_string)-splicing_counter
        print(diafora)
      #p  breakpoint()
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
      #  encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
      #  timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=threading.Thread(target=encoder,args=arg)
        
        
        break
    else: 
        arg=demo_string[splicing_counter:splicing_counter+arithmos_bit]
        lista_kopsimatos.append(arg)
      #  saving_list=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
        #timoula=subprocess.check_output(['python','encode_to_files3.py',arg,strnoumero])
       # breakpoint()
        #timoula,lista_arhikon_pososton,lista_monadikon_xarakthron=encoder(arg)
        #saving_list
       # print(saving_list)
      #  print(lista_arhikon_pososton)
     #  timoula=timoula.decode()
       # print(timoula)
       # print(timoula)
       # encode=threading.Thread(None,encoder(arg,tag_ls,ls_pososta_ls,ls_xarakthres_ls,noumero))
       # ls_xarakthres_ls[noumero]=lista_monadikon_xarakthron
       ## ls_pososta_ls[noumero]=lista_arhikon_pososton
        #tag_ls[noumero]=timoula
    #noumero+=1
    #strnoumero=str(noumero)
    splicing_counter+=arithmos_bit
    print(splicing_counter)


    #if i==len(lista_kopsimatos):
       # tagl_ls,ls_pososta_ls,ls_xarakthres_ls=list(map(encoder(diafora)))



def string_yparhei(dictionary_xarakthron_kai_pososton,char):
    for key in dictionary_xarakthron_kai_pososton:
        if char==key:
            dictionary_xarakthron_kai_pososton[char]=dictionary_xarakthron_kai_pososton[char] +1
            return dictionary_xarakthron_kai_pososton
    dictionary_xarakthron_kai_pososton[char]=1
    return dictionary_xarakthron_kai_pososton

def diavasma_string(string):
    dictionary_xarakthron_kai_pososton={}
    
    
    for char in string:
      #  print(type(char))
       # if type(char)==list:
        #    breakpoint()# οοκκ εδω για καποιο λογο πεταει σα νορισμα μια  λιστα , η οποια περιεχει τα δεδομενα συμπιεσης και απο συμπιεσης του κειμενου , γαμω
        dictionary_xarakthron_kai_pososton=string_yparhei(dictionary_xarakthron_kai_pososton,char)
        
    return dictionary_xarakthron_kai_pososton 
       
  
#print(type(demo_string))
#exit()
dictionary_xarakthron_kai_pososton=diavasma_string(demo_string)
lista_monadikon_xarakthron=[]
for key in dictionary_xarakthron_kai_pososton:
    lista_monadikon_xarakthron.append(key)
temp=0
print(lista_monadikon_xarakthron)
#breakpoint()
lista_arhikon_pososton=[]
lista_olikon_poston=[]
metritis_monadikon_xarakthron=0
for key in dictionary_xarakthron_kai_pososton:
    lista_arhikon_pososton.append(dictionary_xarakthron_kai_pososton[key])
    metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
    dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]/arithmos_bit +temp
    lista_olikon_poston.append(dictionary_xarakthron_kai_pososton[key])
    temp= dictionary_xarakthron_kai_pososton[key]
    
print(lista_arhikon_pososton)
#breakpoint()
print(dictionary_xarakthron_kai_pososton)
#breakpoint()
start_range=0
end_range=1
start_range=mp.mpf(start_range)
end_range=mp.mpf(end_range)
print(lista_arhikon_pososton)


lista_arhikon_pososton=[timi/arithmos_bit for timi in lista_arhikon_pososton]
print(lista_olikon_poston)
#breakpoint()

def olika_pososta(kato_orio,ano_orio,lista_pithanotiton):
    oliko_pososto=[kato_orio]
    diafora=ano_orio-kato_orio
    kato_orio_xarakthra=kato_orio
    for pithanotita in lista_pithanotiton:
        ano_orio_xarakthra=kato_orio_xarakthra+(diafora*pithanotita)
        oliko_pososto.append(ano_orio_xarakthra)
        kato_orio_xarakthra=ano_orio_xarakthra
    return oliko_pososto

def apostasi_tou_kleidou(lista_olikon_poston,lista_monadikon_xarakthron):
    interval={}
    i=0
    j=0 
    while i <len(lista_olikon_poston)-1:
        #print(len(lista_olikon_poston)-i)
        key = lista_monadikon_xarakthron[i]
        kato_orio=lista_olikon_poston[i]#εδω περα οριζονται τα ορια 
        ano_orio=lista_olikon_poston[i+1]
        interval[key]=[kato_orio,ano_orio]
        i+=1
        j+=1
    return interval

def encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string):
    
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
    print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    timoula=0
    timoula=mp.mpf(timoula)
    for character in demo_string:
        char_diastima=dictionary_diastimaton.get(character)
        kato_orio_xarakthra=char_diastima[0]
        ano_orio_xarakthra=char_diastima[1]
        timoula=(kato_orio_xarakthra+ano_orio_xarakthra)/2.0
        oliki_lista_pososton=olika_pososta(kato_orio_xarakthra,ano_orio_xarakthra,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)

    return timoula

def encoderv3(orismata):#υπαρχει τροπος να υλοποιηθηει αυτο πιο εξυπνα με την συναρτηση pack της python αλλα αυτο ειναι προβλημα για τον μελλοντικο κωστα
    lista_arhikon_pososton=orismata[0]
    lista_monadikon_xarakthron=orismata[1]
    demo_string=orismata[2]
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
 #   print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    timoula=0
    timoula=mp.mpf(timoula)
    for character in demo_string:
        char_diastima=dictionary_diastimaton.get(character)
        kato_orio_xarakthra=char_diastima[0]
        ano_orio_xarakthra=char_diastima[1]
        timoula=(kato_orio_xarakthra+ano_orio_xarakthra)/2.0
        oliki_lista_pososton=olika_pososta(kato_orio_xarakthra,ano_orio_xarakthra,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)

    return timoula

timoula=encoderv2(lista_arhikon_pososton,lista_monadikon_xarakthron,demo_string)#ωραια αυτο επιστρεφει επιτυχως τιμη

def decoderv2(timoula,arithmos_bit,lista_arhikon_pososton):# ρε μαλακα γαμω το σπιτι μου ξεχασες να περασεις σαν input την λιστα των μοναδικων χαρακτηρων
    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
    print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    i=0
    teliko_string=[]
    kato_orio=0
    ano_orio=1
    torino_kato_orio=mp.mpf(kato_orio)
    torino_ano_orio=mp.mpf(ano_orio)
    while i < arithmos_bit:
        print(i)
        for key,value in dictionary_diastimaton.items():
            kato_orio=value[0]
            ano_orio=value[1]
           # print((timoula >= kato_orio) and (timoula <= ano_orio))
            print(float(kato_orio)==float(timoula))
            print(float(ano_orio)==float(timoula))
            print("".join(teliko_string))
            print(timoula,kato_orio)
           # breakpoint()
            print("xamilo orio",kato_orio)
            print("timoula",timoula)
            print("psilo",ano_orio)
            if (timoula >= kato_orio) and (timoula<=ano_orio):
                
                torino_kato_orio=kato_orio
                torino_ano_orio=ano_orio
                teliko_string.append(key)
                break
          
        oliki_lista_pososton=olika_pososta(torino_kato_orio,torino_ano_orio,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)#
        i+=1
    
    return teliko_string


# ειμαι τελειως εγκεφαλικά νεκρός και απαιτώ να με εκτελέσουν δεν περνάω την λίστα μοναδικών χαρακτήρων , αλλα πέρα απο αυτο  tings might be alright
#+ συναρτησουλα οπου επειδη το τελικο output  ειναι αρκετες λιστες να τις κανει conjoin 

def decoderv3(lista_orismaton):#john  κωδικας , κάτι πάει λάθος εδώ πέρα , 1) δεν σταματάει στα  breakpoihnts επειδη εχω πολλες μαλακιες νατρεχουν παραλληλα   i guess
    #+ γυρναει κενά αποτελέσματα , γιατι αυτό ? ποιος ξέρει πρέπει να το μελετήσω κοιτάζοντας αμα 1) περνιουνται σωστα τα ορισματα 2) τι στο μπουρδελο γινεται εκει κατω 
    lista_arhikon_pososton=lista_orismaton[2]

    arithmos_bit=lista_orismaton[1]
    timoula=lista_orismaton[0]
    lista_monadikon_xarakthron=lista_orismaton[3]
   # breakpoint()# ας κοιταξουμε τις τιμες που παιρνιουνται

    start=0
    start=mp.mpf(start)
    end=1
    end=mp.mpf(end)
    oliki_lista_pososton=olika_pososta(start,end,lista_arhikon_pososton)
    dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
   # print("η λιστα ολικων ποσοστων ειναι η ",oliki_lista_pososton)
    i=0
    teliko_string=[]
    kato_orio=0
    ano_orio=1
    torino_kato_orio=mp.mpf(kato_orio)
    torino_ano_orio=mp.mpf(ano_orio)
    while i < arithmos_bit:
    #    print(i)
        print(teliko_string)
        for key,value in dictionary_diastimaton.items():# να τσεκαρω αυτο το entry 
            kato_orio=value[0]
            ano_orio=value[1]
            print(" μπηκα")
            print(key)
           # print((timoula >= kato_orio) and (timoula <= ano_orio))
      #      print(float(kato_orio)==float(timoula))
       #     print(float(ano_orio)==float(timoula))
           # print("".join(teliko_string))###πολυ προσοχη εδω περα κατι ισως συμβει

         #   print(timoula,kato_orio)
           # breakpoint()
        #    print("xamilo orio",kato_orio)
        #    print("timoula",timoula)
        #    print("psilo",ano_orio)
            if (timoula >= kato_orio) and (timoula<=ano_orio):
                
                torino_kato_orio=kato_orio
                torino_ano_orio=ano_orio
                teliko_string.append(key)
                print("i happened")
                #exit()
                break
         # καπου κρασαρει η πουτανα  και δεν εχω την παραμικρη ιδεα που 
        print(teliko_string)
        oliki_lista_pososton=olika_pososta(torino_kato_orio,torino_ano_orio,lista_arhikon_pososton)
        dictionary_diastimaton=apostasi_tou_kleidou(oliki_lista_pososton,lista_monadikon_xarakthron)
        i+=1
    print(teliko_string)
  #  breakpoint()
    print("yay")


    return teliko_string

def iterator(timoula,arithmos_bit,arhiki_lista_sinolon,start,end,decoded_string):
    if arithmos_bit==0:
        return decoded_string
    for i in range(0,len(arhiki_lista_sinolon)):
       # breakpoint()
        if timoula<arhiki_lista_sinolon[0]: #and start==0:# εδω περα ισως να το θελει αυτο , θα το δουμε i guess
            end=arhiki_lista_sinolon[0]
            decoded_string=decoded_string+lista_monadikon_xarakthron[0]
            return iterator(timoula,arithmos_bit-1,[item*lista_arhikon_pososton[0] for item in arhiki_lista_sinolon],start,end,decoded_string)
        elif timoula<arhiki_lista_sinolon[i]:
            print("mpika_elif")
            start=arhiki_lista_sinolon[i-1]
            end=arhiki_lista_sinolon[i]

            decoded_string=decoded_string+lista_monadikon_xarakthron[i]
            print(decoded_string)
            return(timoula,arithmos_bit-1,[item*lista_arhikon_pososton[i] for item in arhiki_lista_sinolon],start,end,decoded_string)
            

        

def decoder(timoula,arithmos_bit,arhiki_lista_sinolon):
    start=0
    end=1
    decoded_string=""
    decoded_string=iterator(timoula,arithmos_bit,arhiki_lista_sinolon,start,end,decoded_string)
    print("bgika_decoder")
    return decoded_string


def parametroi_maker(demo_string):
    print(type(demo_string))
    #exit()
    dictionary_xarakthron_kai_pososton=diavasma_string(demo_string)
    lista_monadikon_xarakthron=[]
    for key in dictionary_xarakthron_kai_pososton:
        lista_monadikon_xarakthron.append(key)
    temp=0
    print(lista_monadikon_xarakthron)
    #breakpoint()
    lista_arhikon_pososton=[]
    lista_olikon_poston=[]
    metritis_monadikon_xarakthron=0
    for key in dictionary_xarakthron_kai_pososton:
        lista_arhikon_pososton.append(dictionary_xarakthron_kai_pososton[key])
        metritis_monadikon_xarakthron=metritis_monadikon_xarakthron+1
        dictionary_xarakthron_kai_pososton[key]=dictionary_xarakthron_kai_pososton[key]/arithmos_bit +temp
        lista_olikon_poston.append(dictionary_xarakthron_kai_pososton[key])
        temp= dictionary_xarakthron_kai_pososton[key]
        
    print(lista_arhikon_pososton)
    #breakpoint()
    print(dictionary_xarakthron_kai_pososton)
    #breakpoint()
    start_range=0
    end_range=1
    start_range=mp.mpf(start_range)
    end_range=mp.mpf(end_range)
    print(lista_arhikon_pososton)


    lista_arhikon_pososton=[timi/arithmos_bit for timi in lista_arhikon_pososton]
    print(lista_olikon_poston)
    #breakpoint()# οκ εδωγυρναει λιστα καλα + γυρναει πανω απο 31 λιστες αρα καλα ειμαστε εδω
    return lista_arhikon_pososton,lista_monadikon_xarakthron

#νιωθω αυτη η υλοποίηση είναι πολύ καλή
lista_metaforas_dedomenon=[] 
lista_kopsimatos2=[]
for demo_string in lista_kopsimatos:
    lista_arhikon_pososton,listamonadikon_xarakthron=parametroi_maker(demo_string)#εδω περα σε καποια φαση παιρνει για input lista , γιατι>???

    lista_kopsimatos2.append([lista_arhikon_pososton,listamonadikon_xarakthron,demo_string])#κατι παει λαθος σε αυτη την λουπα

#breakpoint()#να διερευνησω την λιστα κοπσιματος 2 γιατι κατι ισως να μην παει καλα
lista_epistrofis_timon=p_map(encoderv3,lista_kopsimatos2)#hη λιστα κοπσιματος εχει την λιστα αρχικων ποσοστων , την λιστα μοναδικων χαρακτηρων και το string που θελουμε να κοψουμε
#θα μπορουσε τα συγκεκριμενα να τα βρισκει και η ιδια η encoder συναρτηση , αυτο θα επρεπε να κανω
tag_ls=lista_epistrofis_timon
file_to_send=open("tag_ls2",'wb')
pickle.dump(tag_ls,file_to_send)
file_to_send.close()
file_to_send=open("lista_kopsimatos",'wb')
pickle.dump(lista_kopsimatos2,file_to_send)
file_to_send.close()
#exit()
file_to_send=open("arithmos_bit2",'wb')
pickle.dump(arithmos_bit,file_to_send)
file_to_send.close()

file_to_send=open("ls_pososta_ls2",'wb')
pickle.dump(lista_arhikon_pososton,file_to_send)
file_to_send.close()
file_to_send=open("ls_xarakthres_ls2",'wb')
pickle.dump(lista_monadikon_xarakthron,file_to_send)
file_to_send.close()
#file_to_send=open("noumero2",'wb')#μαλακα τι εστελνα εδω πέρα
#pickle.dump(noumero,file_to_send)
#file_to_send.close()
#file_to_send=open("diafora2",'wb')
#pickle.dump(diafora,file_to_send)
#file_to_send.close()
