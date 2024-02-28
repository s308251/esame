#Importazione librerie Python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os
import math

#acquisizione dati e organizzazione dati

data_python_esame_Papini=os.environ.get("DATA_FILE_PATH")
data=np.loadtxt(data_python_esame_Papini, delimiter=' ',usecols=(0,1,4,8,12),unpack=True)
MsuH=data[0] #metallicità 
m_ini=data[1] #massa iniziale
M_ass=data[2] #magnitudine assoluta
b_y=data[3]  #indice di colore/ Temperatura
age_parent=data[4] #età stella
indices=[]
M_ass_split=[]
b_y_split=[]
bins=[]
labels=[]
medie=[]
mediane=[]
#Elenco estremi dei bins dell'istogramma con relative etichette

binn=0.00
for i in range(6):
    binn=round(binn+0.05,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.05)*100)/100) 
    labels.append(label)
for i in range(6):
    binn=round(binn+0.10,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.10)*100)/100)
    labels.append(label)
for i in range(7):
    binn=round(binn+0.20,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.20)*100)/100)
    labels.append(label)
for i in range(4):
    binn=round(binn+0.30,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.30)*100)/100)
    labels.append(label)
for i in range(4):
    binn=round(binn+0.40,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.40)*100)/100)
    labels.append(label)
for i in range(3):
    binn=round(binn+0.50,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.50)*100)/100)
    labels.append(label)
for i in range(2):
    binn=round(binn+0.60,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.60)*100)/100)
    labels.append(label)
for i in range(2):
    binn=round(binn+0.75,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.75)*100)/100)
    labels.append(label)
for i in range(2):    
    binn=round(binn+0.90,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*100)/100,math.trunc((binn+0.90)*100)/100)
    labels.append(label)
for i in range(2):
    binn=round(binn+1.2,2)
    bins.append(binn)
    label="{0} Gyr-{1} Gyr".format(math.trunc(binn*10000)/10000,math.trunc((binn+1.20)*10000)/10000)
    labels.append(label)

#Verifica della struttura dei gruppi di età   
#print(bins)
#print(labels)

#print(len(bins))
#print(len(labels))

# Definizione della mappa di colori 
cmap = plt.get_cmap('gist_rainbow')
colori= cmap(np.linspace(0,1,((len(bins)-1))))



# Distribuzione dei dati age_parent nei bins
num = np.digitize(age_parent, bins=bins)
#print(num)




#Creazione del grafico di magnitudine in funzione del colore delle stelle suddivise in gruppi d'età 

for j in range(1,(len(bins))):

    colori= cmap(np.linspace(0,1,(len(bins)-1)))
    color_sottogruppo=[colori[j-1]]
    b_y_split=[b_y[k] for k in range(len(b_y)) if j== num[k]]
    M_ass_split=[M_ass[k] for k in range(len(M_ass)) if j == num[k]]
    plt.scatter(b_y_split, M_ass_split, c=color_sottogruppo,label=labels[j-1],marker='.')
    
    
#Inversione asse y
plt.gca().invert_yaxis()  

#Limitazione assi

plt.ylim(9, -4)
plt.xlim(-0.1, 1)

#Layout del grafico

plt.xlabel("b_y",fontsize=10)
plt.ylabel("M_ass",fontsize=10)
plt.legend(fontsize=7)
plt.title("Magnitudine assoluta in funzione della temperatura",fontweight='bold',fontsize=13)
plt.grid(True) #crea griglia
plt.show()

#estremi dei tre gruppi di età
indici=[0,1,5,14]
label=['<1 Gyr','1-5 Gyr', '>5 Gyr']

#selezione colori diversi istogrammi
colori=["salmon","cornflowerblue","limegreen"]

#creazione degli istogrammi

for i in range(len(indici)-1):
    indice=np.where((age_parent>i) & (age_parent<=i+1))[0]
    plt.hist(np.array(MsuH)[indice],bins=30,color=colori[i],alpha=0.5,label="{}".format(label[i]))
    media=np.mean(np.array(MsuH)[indice])
    medie.append(media)
    mediana=np.median(np.array(MsuH)[indice])
    mediane.append(mediana)
    plt.axvline(media,color=colori[i],linestyle="--",label="Media:{}".format(round(medie[i],3)))
    plt.axvline(mediana,color=colori[i],linestyle="--",label="Mediana:{}".format(round(mediane[i],3)))




#Layout del grafico

plt.xlabel("Metallicità",fontsize=10)
plt.ylabel("frequenza",fontsize=10)
plt.legend(fontsize=11)
plt.title("Istogramma metallicità stelle suddivise per età",fontweight='bold',fontsize=13)
plt.show()


#Grafico della metallicità in funzione della massa iniziale della stella e dell'età

for i in range(len(indici)-1):
    indice=np.where((age_parent>=indici[i]) & (age_parent<indici[i+1]))[0]
    plt.scatter(m_ini[indice],MsuH[indice],color=colori[i-1],label="{}".format(label[i]),marker='.')
    

#Layout del grafico

plt.xlabel("massa iniziale",fontsize=10)
plt.ylabel("metallicità",fontsize=10)
plt.legend(fontsize=11)
plt.title("Metallicità stelle in funzione della massa iniziale suddivise per età",fontweight='bold',fontsize=13)
plt.show()





