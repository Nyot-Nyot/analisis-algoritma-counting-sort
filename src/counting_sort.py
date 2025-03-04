def sortir_perhitungan(arr):  
    if not arr:  
        return []  
    
    nilai_maks = max(arr)  
    nilai_min = min(arr)  
    rentang = nilai_maks - nilai_min + 1  
    hitung = [0] * rentang  
    hasil = [0] * len(arr)  
    
    for angka in arr:  
        offset = angka - nilai_min  
        hitung[offset] += 1  
    
    for i in range(1, rentang):  
        hitung[i] += hitung[i-1]  
    
    for i in range(len(arr)-1, -1, -1):  
        offset = arr[i] - nilai_min  
        posisi = hitung[offset] - 1  
        hasil[posisi] = arr[i]  
        hitung[offset] -= 1  
    
    return hasil 