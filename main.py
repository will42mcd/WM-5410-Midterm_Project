from mergeSort import *
from get_EOD_data import *

def main():
    while True:
        try:
            start_date = input("Please enter a start date that you would like to pull Nvidia options from (yyyymmdd)\n  Press Q to quit: ")
            if start_date == 'Q':
                break
            elif start_date == 'q':
                break
            end_date = input("Please enter an end date that you would like to pull Nvidia options from (yyyymmdd)\n  Press Q to quit: ")
            if end_date == 'Q':
                break
            elif start_date == 'q':
                break
            bid_tuple = get_EOD_bids(start_date, end_date)

        except ValueError:
            print("\nThere was a Json code error from the API.\nPlease try your dates again.\nPlease select an end date after 2023/06/01.\n")
            continue
        sorted_list = merge_sort(bid_tuple, 0, len(bid_tuple) - 1)
        print(f"\nThe maximum amount of money to be made per Nvidia contract in the date given is ${sorted_list[len(sorted_list)-1]}")
        print(f"\nThe minimum amount of money to be made per Nvidia contract in the date given is ${sorted_list[0]}\n")


if __name__ == "__main__":
    main()
    print(f"\nDocumentation of get_EOD_bids:\n{get_EOD_bids.__doc__}")
