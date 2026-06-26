
while True:

    print("N IN KP (kp -> Kilopond the same as kgf ->kilogram‑force) CALCULATOR - by JanWood2013")#title of the programm
    o = input("kgf in N OR N in kgf OR Formula? Write without space between kn, in and N ").strip().lower()#asks the option

    if o == "kginn":#if the user wants to calculate kn in N
     kgf = input("Type in kg ")#asks for kg
     print("This are ",float(kgf)* 9.80665, "N")
     print()#only design

    elif o =="formula":#if the user wants to see the formula
       print("kgf (or kp) in N:")
       print("Formula: [N = kgf * 9,80665]")#shows the formula
       print()#only design
       print("N in kgf (or kp):")
       print("kgf = N/9,80665")

    elif o == "ninkg":#if the user wants to calculate N in kg
       n = input("Type in N ")
       print("This are ", float(n)/9.80665, "kgf")
       print()#only design
       
    else:#if the input isnt right
       print("Wrong input please try again")#error note for wrong input
       print()#only design