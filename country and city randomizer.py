from tkinter import*
import random

root=Tk()
root.geometry("500x500")
root.title("Country Randomizer")

country_name = Entry(root)
city_name=Entry(root)
country_label=Label(root)
city_label=Label(root)
list_of_country=Label(root)
list_of_city=Label(root)
random_number_label=Label(root)
random_number_label1=Label(root)
list_country=[]
list_city=[]


def add():
    country=country_name.get()
    list_country.append(country)
    list_of_country["text"]="Country list : " + str(list_country)
    city=city_name.get()
    list_city.append(city)
    list_of_city["text"]="City list : " + str(list_city)
    
def random_number():
    length = len(list_country)
    random_no = random.randint(0,length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list_country[random_no]
    country_label["text"]= "your country is: " + str(generated_random_number)
    length1 = len(list_city)
    random_no1 = random.randint(0,length1-1)
    random_number_label1["text"] = str(random_no1)
    generated_random_number1 = list_city[random_no1]
    city_label["text"]= "your city is: " + str(generated_random_number1)
    
    
country_name.place(relx=0.4, rely=0.1, anchor=CENTER)
city_name.place(relx=0.4, rely=0.2, anchor=CENTER)

country_label.place(relx=0.5, rely=0.3, anchor= CENTER)
city_label.place(relx=0.5, rely=0.5, anchor= CENTER)



btn = Button(root, text="Add to the country list", command=add)
btn.place(relx = 0.6, rely=0.1, anchor= CENTER)

btn2 = Button(root, text="Add to the city list", command=add)
btn2.place(relx = 0.6, rely=0.2, anchor= CENTER)

list_of_country.place(relx=0.5, rely=0.4, anchor= CENTER)
list_of_city.place(relx=0.5, rely=0.6, anchor= CENTER)

btn1 = Button(root, text="Random city and country", command = random_number)
btn1.place(relx=0.5, rely=0.7, anchor = CENTER) 

random_number_label.place(relx=0.5, rely = 0.8, anchor = CENTER)
random_number_label1.place(relx=0.5, rely=0.9, anchor = CENTER)

root.mainloop()
    

