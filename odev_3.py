#1 ila 1000 arasindaki kusursuz numaralari bulmaya calsiyoruz.
#ilk once bir sayi aliriz kullanicidan.
#sonra bin ila bin arasinda olup olmadigindan emin oluruz
#sonra girilen sayiya kadar dondururuz ve topla

number = int(input('1 ila 1000 arasinda bir sayi giriniz: '))
toplam = 0 
if 1 < number <= 1000:
    for i in range(1, number):
        if number % i == 0 :
            toplam = toplam+ i
    if toplam == number:
        print(f'{number} kusursuz bir sayidir.')
            
    else:
        print(f' {number} kusursuz bir sayi degildir tekrar deneyiniz')
            
            

else: 
    print('Yanlis giri, lutfen tekrar deneyin!')


------------------------


# 2-Reading Number 
# cok zorlandim, cokca copy past ile yaptim
#numara aliriz, iki haneli mi onu kontrol ederiz
#try except ile kontrolu saglariz
#dict ile numaralari veririz
#if else kontrol blogu ile kontrolu tamamlariz.
def reading_number(number):
    try:
        number = str(number)

        if len(number) != 2:
            return ("Iki haneli bir numara giriniz: ")

        tens_digit_dic = {1:"Ten", 2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty",9:"Ninety"}
        units_digit_dic = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",9:"Nine"}
        digits_ten_to_twenty = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]        

        unit_digit = int(number[1])
        ten_digit = int(number[0])
        
        if unit_digit == 0: #10,20,30,40...
            return (tens_digit_dic[ten_digit])
        elif ten_digit == 1: #11,12,13
            return (digits_ten_to_twenty[unit_digit -1])
        else:
            return (tens_digit_dic[ten_digit] + " " + units_digit_dic[unit_digit])
    except:
        return ("Bir NUMARA giriniz!!")





# 3- Alphabetical_order 
#coklu girdi alacagimiz icin args kullaniriz
#bos bir liste koyariz ki append edip siralama yapalim
#sonra join ile stringe cevirir formatting islemini yapariz
def liste1(*args):
    liste = []
    
    for i in args:
        liste.append(i)
        liste.sort()
        
        
    return '-'.join(liste)

# 4-Unique_list
# yiner args kullaniriz
#bos liste ve append sonra uniq degerleri bulmak icin set
#tekrar listeyecevirip istenen sonuc dondurulur
def unik(*args):
    liste = []
    for i in args:
        liste.append(i)
    kum =set(liste)
    liste2= list(kum)
    
    return liste2



# 5- Equal_reverse
#once ifadenin tersi alinir
#if else esitlik kontrolu return
#map'le fonksiyonu given liste uygulama veyahut istenirse input ile de alinabilir

def eq_rev(n):
    
    k = n[::-1]
    if n == k:
        return True 
    else:
        return False
giv_list = ['madam', 'tacocat', 'utrecht']
son = map(eq_rev, (giv_list) )
print(list(son))


