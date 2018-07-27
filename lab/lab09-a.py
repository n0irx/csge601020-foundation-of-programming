#fungsi untuk kompress string
def kompress(str_me):
    #basecase nya pada saat tidak ada lagi huruf yang sama pada satu seq
    if len(str_me) <= 1:
        return str_me
    #jika terdapat duplikat pada string idx = 0 dan idx = 1
    #maka rekursif kan sisanya
    elif str_me[0] == str_me[1]:
        return kompress(str_me[1:])
    #jika tidak, lanjut pada seq selanjutnya
    else:
        return str_me[0] + kompress(str_me[1:])

if __name__ == "__main__":
    #getting user input
    usrInput = input()
    print(kompress(usrInput))
