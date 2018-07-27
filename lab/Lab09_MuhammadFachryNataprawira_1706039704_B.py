
#program untuk mengetahui angka cantik
def cantik(num):
    #convert num ke str agar bisa dihhitung length nya
    num = str(num)
    #basecase: saat panjang string dari number nya satu maka return number
    if len(num) <=1:
        return num
    #recursive section: saat panjang belum mencapai 1, maka terjadi rekursif
    else:
        sums = sum([int(x) for x in num])
        #rekursif call
        return cantik(sums)

if __name__ == "__main__":
    #getting user input
    userInput = int(input())
    print(cantik(userInput))
