import insertData
 #Протарифицировать трафик
def total(num_ip):
    _,data = insertData.insert_data(num_ip)
    sour = 0 # источник 
    dst = 1  # target 
    byte = 2
    
    k = 0.5 # коэффициентом k: 0.5руб/Мб 
    total = 0
    for row in data:
        a = row[sour].split()[0]
        if a == num_ip:
            b = row[dst].split()[0]
            c = row[byte].split()[0]
            total += float(c)


    total /= pow(2,20)
    print(total ,"data traffic")
    free = 1 #с коэффициентом k: 0,5руб/Мб после достижения 1000Мб 
    if total < free:
        return 0
    internet_bill = (total-free) * k
    print("price: " ,internet_bill , "rub")
