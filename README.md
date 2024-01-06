<h2 align="center">Demonstration video</h2>
<p align="center">
<a href="https://youtu.be/Ha5XNsRvKi0"><img src="images\multiple_space_allocation_video_thumbnail.png" height="70%" width="70%"></a>
</p>

## Problem Statement
Urban parking is often inconvenient, congested, and inefficient. Users struggle to find parking spaces, make payments, and have a smooth experience. Manual ticketing and payment systems are slow and error-prone, lacking technological efficiency.

## What I am Trying to Solve:
+ **License Plate Recognition:** Eliminate the need for physical tickets and enhance security.
- **Parking Space Allocation:** Intelligently allocating available parking spaces to vehicles, ensuring efficient space utilization.
+ **Hands-Free Payment** (Future scope): Automatically charges users based on their parking duration.

## System Components
+ **License Plate Recognition (LPR) System:** Identifying and recognizing the alphanumeric characters on the plates.
- **Camera System:**  To capture images of vehicles and their license plates as they enter the parking area.
+ **Database:** Stores information about registered users, their license plate data, parking space assignments, and payment details.
* **User Interface:** Web application allows users to register their vehicles, view parking availability, make reservations.
+ **Server:** Hosts the web application
- **Parking Space Management:** Optimizes parking space allocation.
+ **Central Processing Unit:** Processes the data received from cameras, manages the recognition of license plates, allocates parking spaces.

## Interaction between Components
<p align="center">
<img src="images\interaction_between_components.png" height="80%" width="80%">
</p>
<p align="center">Figure 1 Flow diagram of interaction between components</p>

## Tradeoffs in the Design
+ This project only focuses on Entry and Exit management System. Only one camera setup will be used for both the systems.
- Parking Space Management algorithms allocates random space based on the free space data in database. In future, either sensors will be used or Computer vision algorithms will be used to detect free space.
+ Presence of card credentials of the user are only checked and payment APIs are not used for transaction.

## Tech Stacks
+ Web application: **HTML, CSS, JavaScript, EJS**
- Database Management System: **MongoDB Atlas**
+ Server side script: **Node.js**
- License Plate Recognition (LPR )algorithm: **Haar cascade classifier, EasyOCR**
+ Atlas CRUD operations: **Python, Node.js**
- Cloud Service: **AWS**
* LPR Deployment: **Raspberry Pi 4**

## Process Flow
<p align="center">
<img src="images\Flowchart.jpeg" height="90%" width="90%">
</p>
<p align="center">Figure 2 Process Flow Diagram</p>

## License Plate Recognition
* Number Plate Detection – **Haar cascade classifier**
+ Number Plate Recognition - **EasyOCR**

<p align="center">
<img src="images\raspberry_pi_setup.jpg" height="90%" width="90%">
</p>
<p align="center">Figure 3 Raspberry Pi Setup</p>

<p align="center">
<img src="images\number_plate_detection_and_recognition.png" height="90%" width="90%">
</p>
<p align="center">Figure 4 Number Plate Detection and Recognition</p>

## Hosting Node Sever in AWS
<p align="center">
<img src="images\node_served_on_AWS.PNG" height="90%" width="90%">
</p>
<p align="center">Figure 5 Node Sever hosted on AWS</p>

## Database
+ Database - **MongoDB Atlas**
- Database Name – **VehicleDB**
+ Collections – **users, vehicleStatus**
- Users collection – Contains sign up details of the users.
* vehicleStatus – Gets updated based on vehicle entry and exit.

<p align="center">
<img src="images\mongodb_when_vehicle_recognized_for_second_time.PNG" height="90%" width="90%">
</p>
<p align="center">Figure 6 vehicleStatus collection after the vehicle exits</p>

<p align="center">
<img src="images\mongodb_user_signup_data1.PNG" height="90%" width="90%">
</p>
<p align="center">Figure 7 users collection – updated after users sign up</p>

## User Interface
<p align="center">
<img src="images\home_page_after_plate_recognition_and_allocation.PNG" height="90%" width="90%">
</p>
<p align="center">Figure 8 Home Page for Displaying Parking Lot Information</p>

<p align="center">
<img src="images\home_after_recognition_no_plate_second_time.PNG" height="90%" width="90%">
</p>
<p align="center">Figure 9 Display Payment Information When the Vehicle Exits Parking Lot</p>

## References
- https://ejs.co/
- https://www.mongodb.com/languages/python
- https://www.mongodb.com/docs/drivers/node/current/quick-start/connect-to-mongodb/
- https://www.w3schools.com/
- https://www.youtube.com/watch?v=O5kh3sTVSvA&list=WL&index=4
- https://youtu.be/0uaSi8v5CHQ?si=qqC_NH3DNHsixA0U
- https://github.com/Maleehak/Car-number-plate-recognition-using-OpenCV
