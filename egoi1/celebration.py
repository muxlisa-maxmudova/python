def format_date(day, month, year):
    formatted_year = str(year).zfill(4)  # Ensures year has 4 digits
    formatted_date = f"{str(day).zfill(2)}/{str(month).zfill(2)}/{formatted_year}"
    return formatted_date
def main():
    year = int(input('Year: '))
    if year%400 ==0 or year%4==0:
        print(format_date(12, 9, year))
    else:
        print(format_date(13, 9, year))
main()