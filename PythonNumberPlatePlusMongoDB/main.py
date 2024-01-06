from dotenv import load_dotenv, find_dotenv
import os
import pprint
from  pymongo import MongoClient
from bson.objectid import ObjectId

import cv2
import easyocr

import random
import time

parking_space_list = [i for i in range(1,11)]
print("parking_space_list before space allocation: ",parking_space_list)

# cascade model location
haarcascade = "model/haarcascade_russian_plate_number.xml"

# create object for video capture
cap = cv2.VideoCapture(0)

cap.set(3, 640) # specify frame width
cap.set(4, 480) # specify frame height

min_area = 500 # minimum area to consider as number plate
reader = easyocr.Reader(['en']) # create Reader object for English language.
plate_cascade = cv2.CascadeClassifier(haarcascade) # create CascadeClassifier object for number plate detection

# Automatically loads the .env file without the need for location 
#provided .env file is in the same directory as python file. 
load_dotenv(find_dotenv())

# os.environ.get("") will access the value of the provided environment variable.
password = os.environ.get("MONGODB_PWD")

# connection string for MongoDb Atlas. Enter the password string name here.
connection_string = f"mongodb+srv://Nithish007:{password}@mycluster.dkov5yi.mongodb.net/?retryWrites=true&w=majority"

# create a client for connecting to Database server
client = MongoClient(connection_string)

# list the databases in the cluster
dbs = client.list_database_names()
print(dbs)

# Create database and collection if not present already (vehicle_DB)
vehicle_DB = client.vehicleDB
vehicle_collection = vehicle_DB.vehicleStatus
collections_of_vehicle_DB = vehicle_DB.list_collection_names()
print(collections_of_vehicle_DB)

user_collection = vehicle_DB.users

# check the user registration
def verify_registration(vehicle_number):
    vehicle_park_status = None
    vehicle_registration_status = user_collection.find_one({"userId":vehicle_number})
    if(vehicle_registration_status):
        #print(vehicle_registration_status)
        print(f"Vehicle {vehicle_number} is registered already")
        try:
            vehicle_park_status = vehicle_collection.find_one({"userId":vehicle_number})
        except:
            print("No vehicle in Parking lot")
        print(vehicle_park_status)
        if(vehicle_park_status):
            print("Inside vehicle park status")
            if(vehicle_park_status["status"]==2):
                exit_time = time.time()
                entry_time = vehicle_park_status["entryTime"]
                parking_time = exit_time - entry_time
                payment_amount = parking_time*0.01
                print("payment amount: $", round(payment_amount,2))
                exiting_vehicle_parking_space_number = vehicle_park_status["parkingSpaceNumber"]
                parking_space_list.append(exiting_vehicle_parking_space_number)
                print("parking_space_list after removing vehicle: ", parking_space_list)
                #vehicle_collection.delete_one({"userId":vehicle_number})
                updates = {
                    "$inc": {"status":1},
                    "$set": {"exitTime": exit_time}
                }
                vehicle_collection.update_one({"userId":vehicle_number}, updates)
                updates = {
                    "$set": {"totalAmount": round(payment_amount,2)}
                }
                vehicle_collection.update_one({"userId":vehicle_number}, updates)
                vehicle_park_status = None
            elif(vehicle_park_status["status"]>=3):
                current_status = 3
                vehicle_registered_and_recognized(vehicle_number, current_status)
                select_parking_space(vehicle_number)
                vehicle_park_status = None
        else:
            status = 1
            vehicle_registered_and_recognized(vehicle_number, 1)
            select_parking_space(vehicle_number)
    else:
        #print(vehicle_registration_status)
        print(f"Vehicle {vehicle_number} is not registered. Please Signup and come back later")


def select_parking_space(vehicle_number):
    parking_space_number = random.choice(parking_space_list)
    parking_space_list.remove(parking_space_number)
    print("parking_space_list after space allocation: ",parking_space_list)
    vehicle_space_allotment(vehicle_number, parking_space_number)

# create document
def vehicle_registered_and_recognized(vehicle_number, status):
    if(status==1):
        doc = {"userId": vehicle_number, "status": status}
        vehicle_collection.insert_one(doc)
        print("Status 1")
    else:
        updates = {
        "$set": {"status": 1}
        }
        vehicle_collection.update_one({"userId":vehicle_number}, updates)


def vehicle_space_allotment(vehicle_number, parking_space_number):
    entry_time = time.time()
    updates = {
        "$inc": {"status":1},
        "$set": {"parkingSpaceNumber": parking_space_number},
    }
    vehicle_collection.update_one({"userId":vehicle_number}, updates)

    updates = {
        "$set": {"entryTime": time.time()}
    }
    vehicle_collection.update_one({"userId":vehicle_number}, updates)

while True:
    success, img = cap.read()

    if not success:
        print("Unable to capture video frame")
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1.1: This parameter represents the scale factor. It determines how much the image size is reduced at each image scale. 
    # In this case, the image is reduced by 10% at each scale. A smaller scale factor may increase the chance of detecting 
    # smaller objects but may also increase false positives.

    # 2: This parameter represents the minimum number of neighbors a candidate rectangle should have to be considered as a plate. 
    #Increasing this value can reduce false positives but may miss some true positives.

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 2)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    
    if cv2.waitKey(50) & 0xFF == ord('r'):
        result = reader.readtext(img_roi)
        result = result[0][1].replace(" ", "")
        print(result)
        #create_doc(result, 1)
        verify_registration(result)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

