"""
We can use datetime library to help us
"""

import datetime as d

def main():
    total_sunday = 0
    for year in range(1901,2001):
        for month in range(1,13):
            if d.datetime(year, month, 1).weekday() == 6:
                total_sunday += 1

    print(total_sunday)


if __name__ == "__main__":
    main()
