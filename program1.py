def get_season(month):
    seasons = ('winter', 'spring', 'summer', 'autumn')
    month_to_season = {
        1: 'winter', 2: 'winter', 3: 'spring',
        4: 'spring', 5: 'spring', 6: 'summer',
        7: 'summer', 8: 'summer', 9: 'autumn',
        10: 'autumn', 11: 'autumn', 12: 'winter'
    }
    return month_to_season.get(month)

def main():
    month = int(input("Enter month (1-12): "))
    if 1 <= month <= 12:
        season = get_season(month)
        print(f"The season corresponding to month {month} is {season}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
