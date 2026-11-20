while True:
 o = input("What do you want to knwo? (p, v, cw, A, fw) ").lower().strip()#asks the user for the missing variable 
 input("EVERY UNIT HAS TO BE FROM THE SI. Do not enter the unit. Press enter to continue")
 print("")#only design

 if o == "fw":#if the option is fw (Drag Force)
     p = float(input("Enter air density "))
     v = float(input("Enter velocity "))
     cw = float(input("Enter drag coefficient "))
     A = float(input("Enter frontal area "))
     print("")#only design
     print("Fw = ", 0.5*p*(v**2)*cw * A, "N")#calculates

 if o == "p":#if the option is p (air density)
     v = float(input("Enter velocity "))#asks for every necessary  information
     cw = float(input("Enter drag coefficient "))
     A = float(input("Enter frontal area "))
     fw = float(input("Enter drag force "))
     print("")#only design
     print("p= ", (2*fw)/((v**2)*cw*A), "kg/m^3")#calculates

 if o == "v":#if the option is v (velocity)
     cw = float(input("Enter drag coefficient "))#asks for every necessary  information
     A = float(input("Enter frontal area "))
     p = float(input("Enter air density "))
     fw = float(input("Enter drag force "))
     print()#only design
     print("v= ", (2*fw/(p*A*cw))**0.5, "m/s")#calculates

 if o == "cw":#if the option is cw (drag coefficient)
     A = float(input("Enter frontal area "))#asks for every necessary  information
     p = float(input("Enter air density "))
     fw = float(input("Enter drag force "))
     v = float(input("Enter velocity "))
     print()#only design
     print("cw= ", ((2*fw)/(p*A*(v**2))))#calculates

 if o == "a":#if the option is a
     cw = float(input("Enter drag coefficient "))#asks for every necessary  information
     v = float(input("enter velocity "))
     fw = float(input("Enter drag force "))
     p = float(input("Enter air density "))
     print()#only design
     print("a= ", (2*fw)/(p*cw*(v**2)),"m^2")#calculates

 print("")#only design