import requests
import urllib.request
import time
import csv
import Product_details

counter = 0

product_details = []

with open("tintealarm_product_url.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        if counter != 0:
            print(lines[8])
            info = Product_details.get_product_info(lines[8])
            final_dt = str(lines[4]) + "~" + info
            product_details.append(final_dt)
            print(product_details)
        counter = counter + 1
csv_file.close()

print("Writing to CSV ....")

with open('tintealarm_product_list.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["OEM", "BRAND", "MODEL", "TYPE", "TITLE", "PRICE", "IMAGE"])

    for data in product_details:
        data_split = data.split("~")
        OEM = data_split[1]
        BRAND = data_split[2]
        MODEL = data_split[0]
        TYPE = data_split[4]
        TITLE = data_split[3]
        PRICE = data_split[5]
        IMAGE = data_split[6]

        csv_writer.writerow([OEM, BRAND, MODEL, TYPE, TITLE, PRICE, IMAGE])

        output = OEM + "~" + BRAND + "~" + MODEL + "~" + TYPE + "~" + TITLE + "~" + PRICE + "~" + IMAGE

        print(output)
csv_file.close()