#Sai Khay Kham
#sorting array

def sort012(arr):
        arr.sort() #sorting array
        
if __name__ == "__main__":
    new_arr = []    #declare new array
    arr = [0,1,2,0,1,2]
    sort012(arr)    #calling sort method
    
    for num in arr: #loop through the array
        new_arr.append(num) #add sorted array into new array
    print(new_arr)