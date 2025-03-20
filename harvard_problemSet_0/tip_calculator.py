def dollars_to_float(d):
    if d.find('$')>-1:
        d = d.strip('$')
        return float(d)
    elif d.find('$')==-1:
       return float(d)
def percent_to_float(p):
    if p.find('%')>-1:
        p = p.strip('%')
        return float(p)/100
    elif p.find('%')==-1:
        return float(p)/100
def main():
   dollars = dollars_to_float(input("How much was the meal?: "))
   percent = percent_to_float(input("What percentage would you like to tip? "))
   tip = dollars * percent
   print(f"Leave ${tip:.2f}")
main()