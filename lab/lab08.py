class Staff:
    def __init__(self, nama):
        self.nama = nama
        self.jam_kerja = 0
        self.progress = 0

    def kerja(self, jam):
        self.jam_kerja += jam

    def hitung_gaji(self):
        pass

class StaffAcara(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    def kerja(self, jam):
        super().kerja(jam)
        self.progress += jam * 4

    def hitung_gaji(self):
        return self.progress * 2000


class StaffPartnership(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    def kerja(self, jam):
        super().kerja(jam)
        self.progress += jam * 1

    def hitung_gaji(self):
        return self.progress * 4000 * self.jam_kerja

class StaffPublikasi(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    def kerja(self, jam):
        super().kerja(jam)
        self.progress += jam * 20

    def hitung_gaji(self):
        return self.jam_kerja* 1500

class Manager:
    def __init__(self):
        self.staffs = {}

    def recruit_staff(self, staf):
        self.staffs[staf.nama] = staf

    def get_staff(self,nama):
        return self.staffs[nama]

    def is_staff_recruited(self, nama):
        return nama in self.staffs

if __name__ == "__main__":
    manager = Manager()
    while(True):
        #meminta input dari user
        n = input().split(";")
        usr_cmd = n[0].upper()
        usr_name = n[1].lower().capitalize()
        #program bekersja sesuai command user
        if usr_cmd == 'REKRUT':
            usr_div = n[2].lower().capitalize()
            if not manager.is_staff_recruited(usr_name):
                if usr_div == 'Acara':
                    manager.recruit_staff(StaffAcara(usr_name))
                elif usr_div == 'Partnership':
                    manager.recruit_staff(StaffPartnership(usr_name))
                elif usr_div == 'Publikasi':
                    manager.recruit_staff(StaffPublikasi(usr_name))
                print("{} direkrut".format(usr_name))
            else:
                #jika sudah ada dalam manager
                print("{} sudah direkrut sebelumnya".format(usr_name))
        #saatnya kerja
        elif usr_cmd == 'KERJA':
            usr_jam = int(n[2])
            if manager.get_staff(usr_name).progress < 100:
                manager.get_staff(usr_name).kerja(usr_jam)
                print("{} Bekerja selama {} jam".format(usr_name, usr_jam))
            else:
                print("{} sudah mencapai {}% progress".format(usr_name,
                manager.get_staff(usr_name).progress))
            #log history
        elif usr_cmd == 'LOG':
            print(">>> {}\nTelah bekerjah selama {} jam\nProgress: {} persen\nGaji sementara: {} bencoin".format(manager.get_staff(usr_name).nama,
            manager.get_staff(usr_name).jam_kerja, manager.get_staff(usr_name).progress, manager.get_staff(usr_name).hitung_gaji()))
        #break loop saat command nya exit
        elif usr_cmd == 'EXIT':
            break
