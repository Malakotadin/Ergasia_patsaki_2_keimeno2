from mpmath import mp,mpf
import time 
from p_tqdm  import p_map
import sys
import pickle

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

def olika_pososta(kato_orio,ano_orio,lista_pithanotiton):
    oliko_pososto=[kato_orio]
    diafora=ano_orio-kato_orio
    kato_orio_xarakthra=kato_orio
    for pithanotita in lista_pithanotiton:
        ano_orio_xarakthra=kato_orio_xarakthra+(diafora*pithanotita)
        oliko_pososto.append(ano_orio_xarakthra)
        kato_orio_xarakthra=ano_orio_xarakthra
    return oliko_pososto

#mp.dps=1
#hex_bin=bin.hex()#μετατροπή σε hex
#print(type(hex_bin))
#arithmos_bit=len(hex_bin)
file_to_send=open("tag_ls2",'rb')
tag_ls=pickle.load(file_to_send)
file_to_send.close()

file_to_send=open("lista_kopsimatos",'rb')
lista_kopsimatos2=pickle.load(file_to_send)
file_to_send.close()
#file_to_send=open("ls_pososta_ls",'rb')
#ls_pososta_ls=pickle.load(file_to_send)
#file_to_send.close()
#file_to_send=open("ls_xarakthres_ls",'rb')
#ls_xarakthres_ls=pickle.load(file_to_send)
#file_to_send.close()
file_to_send=open("arithmos_bit2",'rb')
arithmos_bit=pickle.load(file_to_send)
file_to_send.close()
#file_to_send=open("noumero",'rb')
#noumero=pickle.load(file_to_send)
#file_to_send.close()
#file_to_send=open("diafora",'rb')
#diafora=pickle.load(file_to_send)
#file_to_send.close()

#  message = perioehomeno

mp.dps=10000

#demo_string=demo_string[:100]

#arithmos_bit=len(demo_string)
#arithmos_bit=256
lista_kopsimatos=[]




  
#print(type(demo_string))
#exit()

#breakpoint()



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
#lista_metaforas_dedomenon=[] 
#lista_kopsimatos2=[]

#breakpoint()#να διερευνησω την λιστα κοπσιματος 2 γιατι κατι ισως να μην παει καλα
#hη λιστα κοπσιματος εχει την λιστα αρχικων ποσοστων , την λιστα μοναδικων χαρακτηρων και το string που θελουμε να κοψουμε
#θα μπορουσε τα συγκεκριμενα να τα βρισκει και η ιδια η encoder συναρτηση , αυτο θα επρεπε να κανω
lista_epistrofis_timon=tag_ls
#lista_kopsimatos=
lista_orismaton=[]
#breakpoint()# να ελεγξω την λιστα αρχικων ποσοστων
#breakpoint()#ελεγξε την λιστα κοπσιματος 2 για λιστα μοναδικων χαρακτηρων και την λιστα αρχικων ποσοστων i beg you
for i in range(0,len(lista_epistrofis_timon)):
    lista_orismaton.append([lista_epistrofis_timon[i],arithmos_bit,lista_kopsimatos2[i][0],lista_kopsimatos2[i][1]])#γιατι εχζω μονο 31 κομματια στην λιστα αρχικων ποσοστων και 1198 στην λιστα επιστροφης τιμων γαμωτο μου ????
#  ωραια αυτο εχει μηκος 256 ???? μα γιατι ??? 
# οχι γιατ ιεχει 3 ρε μαλακα η λιστα και η λιστα κοψιματος 2 εχουν το ιδιο μηκος
#breakpoint()
#print(timoula)
#breakpoint()
#exit()
#final_output="".join(decoderv2(timoula,arithmos_bit,lista_arhikon_pososton))
def list_joiner(arg_list):# παιρνει μια λιστα που έχει πολλες λιστες μέσα και τις ενώνει 
    lista_epistrofis2=[]# κατι εδώ κάνει infinite recursion , αλλα τι ?? 

    if type(arg_list[0])==list:
        for item in arg_list:
            lista_epistrofis2.extend(list_joiner(arg_list))
        return lista_epistrofis2
    elif type(arg_list[0]==str):
        lista_epistrofhs="".join(arg_list)
        return lista_epistrofhs        
    else:
        print(watafak)

        exit()

def list_joiner2(input_list):
    big_lista=[]   
    for item in input_list :
        big_lista.extend(item)
    return "".join(big_lista)


#breakpoint()#τι εχω πριν το decoding  #μαλακια η λιστα ορισματων μου εχει μονο ενα κομματι , οπου σημαινει πωςτο tag επιστρεφει μονο ενα σκελος ? ισως αυτο φταει που ο αριθμος  bit  ειναι το μηκος του κειμενου 
output_list=p_map(decoderv3,lista_orismaton)
#breakpoint()
final_output=list_joiner2(output_list)#γιατι μου ανατιναζεσαι μπουρδελο γαμω γαμω
#final_output="".join(output_list) # για αρχή επιστρεφουν πολλές λιστες , γαμήσια , επίσης επιστρέφουν με λάθος σειρά , γαμισια2
#breakpoint()# τελος κωδικα πριν συγγραφη , δοκιμασε να γραψεις κα τι θα γραψεις # κατι δεν κανω σιγουρα καλα στο decoding , ας διερευνησουμε
f=open("vivlio2.txt","w")
f.write(final_output)
f.close()
print(arithmos_bit)
#print(demo_string)
print(final_output)
#print(starting_string==final_output)