from tkinter import *
from tkinter import messagebox
from parking import *
from car import *
import os

class ParkingApp :
    def __init__(self,root):
        self.root = root
        self.root.title ("Parking")
        self.root.geometry('500x500')
        self.root.iconbitmap("icon.ico")
       #وارد کردن غکس به برنامه
        self.img = PhotoImage (file='car.png')
        self.lbl_bg = Label(root,image = self.img)
        self.lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.parking = Parking(10)
        self.creat_widget()
        self.load_current_cars()



    def creat_widget (self):
        font_fa = ("B Kamran",20)

        self.frame_info = Frame(self.root,bg='#6CCFF6')
        self.frame_info.pack(pady=30)
        #ساخت لیبل و ورودی پلاک
        Label(self.frame_info, text="پلاک : ", font=font_fa, fg='black', bg='#6CCFF6').grid(row=0, column=0, padx=10, pady=10)
        self.en_pelak_1 = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182',width =5)
        self.en_pelak_2 = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182',width =4,justify='left')
        self.en_pelak_3 = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182',width =6)
        self.en_pelak_4 = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182',width =13)

        self.en_pelak_1.grid(row=0, column=1 ,padx=5,pady=10)
        self.en_pelak_2.grid(row=0, column=2, padx=5, pady=10)
        self.en_pelak_3.grid(row=0, column=3, padx=5, pady=10)
        self.en_pelak_4.grid(row=0, column=4, padx=5, pady=10)
        self.en_pelak_4.insert(0,"ایران|")

        #ساخت لیبل و ورودی مدل
        Label(self.frame_info, text="مدل : ", font=font_fa, fg='black', bg='#6CCFF6').grid(row=1, column=0, padx=10, pady=10)
        self.en_model = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182', width=10)
        self.en_model.grid(row=1, column=1,columnspan=2, padx=5, pady=10)

        # ساخت لیبل و ورودی رنگ
        Label(self.frame_info, text="رنگ : ", font=font_fa, fg='black', bg='#6CCFF6').grid(row=2, column=0, padx=10, pady=10)
        self.en_color = Entry(self.frame_info, font=font_fa, fg='white', bg='#286182', width=10)
        self.en_color.grid(row=2, column=1,columnspan=2 , padx=5, pady=10)

        self.button_frame = Frame(self.root, bg='')
        self.button_frame.pack(pady=30)
        #ساخت دکمه
        Button(self.button_frame, text = "پارک خودرو", font=font_fa ,command=self.d_park_khodro).grid(row=0,column=0,padx=(10,100),pady=10)

        Button(self.button_frame, text="حذف خودرو", font=font_fa ,command=self.d_hazf_khodro).grid(row=0, column=2, padx=10, pady=10)

        Button(self.button_frame, text="اطلاعات خودرو ها", font=font_fa ,command=self.d_namayesh_kol_khodro).grid(row=1, column=0, padx=(10,140), pady=10)

        Button(self.button_frame, text="وضعیت پارکینگ", font=font_fa ,command=self.d_namayesh_vaziat).grid(row=1, column=2, padx=(50,10), pady=10)

    def load_current_cars (self):
        entered_cars = {}
        exited_cars  = set() #نوع تعریف دیگه مجموعه
        #یررسی فایل ورودی
        if os.path.exists("VORODI.txt"):
            with open ("VORODI.txt","r",encoding="utf-8") as file :
                for line in file :
                    parts = line.strip().split(" و پلاک :")
                    if len(parts) >= 2:
                        pelak_next_part = parts[1]
                        try  :
                            pelak = pelak_next_part.split(" و مدل : ")[0].strip()
                            model = pelak_next_part.split(" و مدل : ")[1].strip()
                            color = pelak_next_part.split(" و رنگ : ")[1].strip()
                            entered_cars[pelak] = Car(pelak,color,model)
                        except :
                            continue #نادیده گرقتن خطوط با فرمت نادرست
        #بررسی فایل خروجی
        if os.path.exists("KHOROJI.txt"):
            with open ("KHOROJI.txt","r",encoding="utf-8") as file :
                for line in file:
                    parts = line.strip().split(" و پلاک :")
                    if len(parts) >= 2:
                        pelak_next_part = parts[1]
                        try :
                            pelak = pelak_next_part.split(" و مدل : ")[0].strip()
                            exited_cars.add(pelak)
                        except :
                            continue
        #شناسایی خودرد های فعلی
        current_cars = [car for p,car in entered_cars.items() if p not in exited_cars]
        #اضافه کردن خودرو های فعلی به سیستم پارکینگ
        for car in current_cars :
            self.parking.ezafe_khodro(car)

    def write_to_file_entry (self,car):
        try :
            with open("VORODI.txt","a",encoding="utf-8") as file :
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"زمان : {time_now} و پلاک :{car.pelak} و مدل : {car.model} و رنگ : {car.rang} \n")
        except Exception as e :
            messagebox.showerror("خطا",f"در ذخیره سازی اطلاعات به دلیل ارور {e} به مشکل خورده")

    def write_to_file_exit(self, car,cost):
        try:
            with open("KHOROJI.txt", "a", encoding="utf-8") as file:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"زمان : {time_now} و پلاک :{car.pelak} و مدل : {car.model} و رنگ : {car.rang} و هزینه آن {cost} \n")
        except Exception as e:
            messagebox.showerror("خطا", f"در ذخیره سازی اطلاعات به دلیل ارور {e} به مشکل خورده")

    def d_park_khodro (self):
        pelak = ""
        pelak_1 = self.en_pelak_1.get()
        pelak_2 = self.en_pelak_2.get()
        pelak_3 = self.en_pelak_3.get()
        pelak_4 = self.en_pelak_4.get()
        model = self.en_model.get()
        rang  = self.en_color.get()

        if not pelak_1 or not pelak_2 or not pelak_3 or not model or not rang:
            messagebox.showerror("اخطار","لطفا همه فیلد ها رو پر کنید")
            return

        if pelak_4 =="ایران|":
            messagebox.showerror("اخطار","فیلد 4 پر نشده است")
            return
        pelak += pelak_1
        pelak += pelak_2
        pelak += pelak_3
        pelak += pelak_4
        khodro = Car(pelak,rang,model)
        if self.parking.ezafe_khodro(khodro):
            messagebox.showinfo("نتیجه",f"خودرو با پلاک{pelak} با موفقیت وارد شد")
            self.write_to_file_entry(khodro)
        else :
            messagebox.showerror("اخطار","پارکینیگ پر است")

    def d_hazf_khodro (self):

        pelak = ""
        pelak_1 = self.en_pelak_1.get()
        pelak_2 = self.en_pelak_2.get()
        pelak_3 = self.en_pelak_3.get()
        pelak_4 = self.en_pelak_4.get()

        if not pelak_1 or not pelak_2 or not pelak_3 :
            messagebox.showerror("اخطار", "لطفا همه فیلد ها رو پر کنید")
            return

        if pelak_4 == "ایران|":
            messagebox.showerror("اخطار", "فیلد 4 پر نشده است")
            return
        pelak += pelak_1
        pelak += pelak_2
        pelak += pelak_3
        pelak += pelak_4

        khodro = self.parking.hazf_khodro(pelak)
        if khodro :
            pol = self.parking.mohasebe_hazine(khodro)
            messagebox.showinfo("هزینه",f"خودرو با پلاک {pelak}\n هزینه ={pol} با موفقیت خارج شد")
            self.write_to_file_exit(khodro,pol)
        else :
            messagebox.showerror("اخطار","چنین خودرویی موجود نمی باشد")

    def d_namayesh_vaziat (self):
        messagebox.showinfo("وضعیت",f"جایگای های خالی شما برابر با {self.parking.jaygah_khali()}\nجایگاه های اشغال شده {10-self.parking.jaygah_khali()}")

    def d_namayesh_kol_khodro (self):
        info = self.parking.namayesh_hame_khodro()
        messagebox.showinfo("اطلاعات",info)


root =Tk()
App =ParkingApp(root)
root.mainloop()

