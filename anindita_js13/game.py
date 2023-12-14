def guess_number():
    secret_number = 6
    guess_count = 0
    guess_limit = 3

    while(guess_count < guess_limit):
        answer = int(input("Masukkan tebakanmu: "))
        if(int(answer) == secret_number):
            print ("Anda berhasil menebak angkanya.")
            break
        else:
            print("Salah")
            guess_count = guess_count + 1
    else:
        print ("Kesempatan Anda habis.")