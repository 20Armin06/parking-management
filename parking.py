from car import *
from datetime import*
class Parking :
    def __init__(self,tedad_jaighah):
        self.tedad_jaighah = tedad_jaighah
        self.tedad_eshghal = []
    def ezafe_khodro (self,khodro):
        if len(self.tedad_eshghal)< self.tedad_jaighah :
            self.tedad_eshghal.append(khodro)
            return True
        else :
            return False

    def hazf_khodro (self,pelak):
        for khodro in self.tedad_eshghal :
            if khodro.pelak == pelak :
                self.tedad_eshghal.remove(khodro)
                return khodro

    def jaygah_khali (self):
        return self.tedad_jaighah - len(self.tedad_eshghal)

    def mohasebe_hazine (self,khodro):
        zaman_feli = datetime.now()
        zaman_park = zaman_feli - khodro.time
        saat_park = zaman_park.total_seconds() /3600
        return round(saat_park*5000,2)

    def namayesh_hame_khodro (self):
        if not self.tedad_eshghal :
            return "هیچ خودرویی درون پارکینگ نیست"
        else :
            info_list = [khodro.info_mashin() for khodro in self.tedad_eshghal]
            return "\n".join(info_list)