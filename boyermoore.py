#Boyer moore algoritmasının çalışması için gerekli ön işlem fonksiyonu tanımlanır.
def duzenle(x, y, aranan, m):
	i = m
	j = m + 1
	y[i] = j
	
	while i > 0:
		while j <= m and aranan[i - 1] != aranan[j - 1]:
			if x[j] == 0:
				x[j] = j - i
			j = y[j]
		i -= 1
		j -= 1
		y[i] = j

	j = y[0]
	
	for i in range(m + 1):
		if x[i] == 0:
			x[i] = j
		if i == j:
			j = y[j]

#Arama fonksiyonu tanımlanır.
def boyermoore(yazi, aranan):
	toplam=0
	s = 0
	m = len(aranan)
	n = len(yazi)
	y = [0] * (m + 1)
	x = [0] * (m + 1)
	duzenle(x, y, aranan, m)
	while s <= n - m:
		j = m - 1
		while j >= 0 and aranan[j] == yazi[s + j]:
			j -= 1
		if j < 0:
			toplam=toplam+1
			s += x[0]
		else:
			s += x[j + 1]
	return toplam

#Toplam kelime sayısını veren değişken tanımlanır.
toplamkelime=0

#Dosya okunmak üzere açıldı ve tek tek istenen kelimeler arandı.
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"upon")
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"sigh")
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"Dormouse")
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"jury-box")
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"swim")
dosya=open("alice_in_wonderland.txt","r")
toplamkelime+=boyermoore(dosya.read(),"NOT BAREMİ")

#Toplanan kelimeler değişkene aktarıldı ve yazdırıldı.
print("Aranan kelimelerin toplam sayısı = {}".format(toplamkelime))