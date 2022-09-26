# ABLORH DATA FINDER Webapp
ABLORH DATA FINDER is a Django web application to manage clinic data of patients. It was made for authorized medical personnel only.

DISCLAIMER:
It was made only for training purposes, that is why I used the default Django database. It was made only with 3 types of tests (3 tables) and with 3 types of records by each test.

# Login Window

![Captura de pantalla 2022-09-25 225148](https://user-images.githubusercontent.com/108229433/192169816-7e112365-1bb6-43ba-96bb-8fab0b2a2fa3.jpg)

A message appears when the user enters a wrong password:

![Captura de pantalla 2022-09-25 225521](https://user-images.githubusercontent.com/108229433/192169820-dfac8eb8-b6f1-4575-818e-5a37aa356a5f.jpg)

# Register Window

![Captura de pantalla 2022-09-25 225225](https://user-images.githubusercontent.com/108229433/192169817-806d963a-04e0-4b2c-8e60-72622eefe632.jpg)
![Captura de pantalla 2022-09-25 225352](https://user-images.githubusercontent.com/108229433/192169818-aaf0dd6d-8ee0-46e5-9bc3-82b369bfca53.jpg)

A message informs if new user was sucessfully created.

![Captura de pantalla 2022-09-25 225419](https://user-images.githubusercontent.com/108229433/192169819-69931caa-10ca-4e90-bd60-cc370410f339.jpg)

# Data Finder Window
After entering the correct password the Data Finder Window appears. We have a navigation bar and 5 options to add a new patient, find a patient's data, add records to a patient, find records from a patient and logout. We can also see the user who is logged in at the moment.

![Captura de pantalla 2022-09-25 225551](https://user-images.githubusercontent.com/108229433/192169821-ef64e6e8-a2e7-4041-aa78-6516b7f0deab.jpg)

## 1-Add patient
When clicking the Add-patient button a form appears in order to get the patient's data.
After entering the data in the correct way and click the Add-new-patient button, if process goes well a message appears to inform the user.

![Captura de pantalla 2022-09-25 232627](https://user-images.githubusercontent.com/108229433/192169822-d5b264d8-1816-4618-9a9f-4203691de14c.jpg)
![Captura de pantalla 2022-09-25 232819](https://user-images.githubusercontent.com/108229433/192169823-c21627b5-e8c5-4eba-af57-056e65a7ac3a.jpg)

If data is entered the wrong way and the button is clicked, an error message appears to inform the user the process failed.

![Captura de pantalla 2022-09-25 233345](https://user-images.githubusercontent.com/108229433/192169824-acd5792b-c70b-4fe7-9dd2-14a514a1f6a9.jpg)
![Captura de pantalla 2022-09-25 233404](https://user-images.githubusercontent.com/108229433/192169825-c775efd6-bfb5-4a70-89a7-c6d52a5bc19d.jpg)

## 2-Find patient
When clicking the Find-patient button; a table appears with info of all patients in the database.

![Captura de pantalla 2022-09-26 001812](https://user-images.githubusercontent.com/108229433/192169826-55e4f214-5467-4c50-a0fb-936821f41116.jpg)

We can filter the results by various elements, gender (for example) to show all male patients in the database:

![Captura de pantalla 2022-09-26 001848](https://user-images.githubusercontent.com/108229433/192169827-c38c021b-b1b5-4fb6-b5fc-5fd411e73b5f.jpg)

We can search for all male patients named "Jordan".

![Captura de pantalla 2022-09-26 001919](https://user-images.githubusercontent.com/108229433/192169829-ac99e77f-66f7-4784-8b84-8eba935312f2.jpg)

We can search for all patients born on April 22th, 2020.

![Captura de pantalla 2022-09-26 002002](https://user-images.githubusercontent.com/108229433/192169830-ca92ef77-8064-4d04-b03d-1ed1c1d389a4.jpg)

Or we can just find an specific patient by it's ID.

![Captura de pantalla 2022-09-26 002044](https://user-images.githubusercontent.com/108229433/192169831-30aeacee-9942-4460-9753-5228d8a59891.jpg)

## 3-Add records
When clicking the Add-records button; a form appears in order to select what type of test we want to add data in.

![Captura de pantalla 2022-09-26 002108](https://user-images.githubusercontent.com/108229433/192169833-c386d568-7129-4dd0-95dc-9595379e2432.jpg)

If we select for example "COMPLETE_BLOOD_COUNT" test, another form appears with this type of test data to fill. (The exact same thing happens when we select any other test). 

![Captura de pantalla 2022-09-26 002210](https://user-images.githubusercontent.com/108229433/192169834-a0d9ec9d-5ed5-4fa7-abcd-b40e69422683.jpg)

We can select the test name as well as the test unit and reference values (wich as said before are only 3 for training purposes).

![Captura de pantalla 2022-09-26 002524](https://user-images.githubusercontent.com/108229433/192169808-b6b2526b-59e1-4a09-a695-f7e4bcb2119b.jpg)

After entering the data in the correct way and click the Add-tests button, if process goes well a message appears to inform the user. (A message also appears when data is incorrect).

![Captura de pantalla 2022-09-26 002421](https://user-images.githubusercontent.com/108229433/192169806-5b33d6ef-8b02-4218-9ebc-0b183db0329e.jpg)

## 4-Find records
When clicking the Find-records button; a form appears in order to select what type of test we want to show data from.

![Captura de pantalla 2022-09-26 003309](https://user-images.githubusercontent.com/108229433/192169810-7a3f5b99-1df2-4f20-9105-03125047a028.jpg)

If we select for example "COMPLETE_BLOOD_COUNT" test, a table appears with this type of test data to show. (The exact same thing happens when we select any other test).

![Captura de pantalla 2022-09-26 003334](https://user-images.githubusercontent.com/108229433/192169811-ee1e4fa2-1a47-4c45-8ca1-7cc64bd72e7e.jpg)

We can filter the results by various elements, Patients ID for example shows all COMPLETE_BLOOD_COUNT tests of patient with the patient's ID selected:

![Captura de pantalla 2022-09-26 003420](https://user-images.githubusercontent.com/108229433/192169812-f46d03b6-a4ac-4190-8a67-725dfe4a9f14.jpg)

We can filter by test date:

![Captura de pantalla 2022-09-26 003456](https://user-images.githubusercontent.com/108229433/192169813-73e9905e-50ea-42e4-a16f-4f85f7ab9d63.jpg)

We can filter by test name:

![Captura de pantalla 2022-09-26 003524](https://user-images.githubusercontent.com/108229433/192169814-c2d144a7-a007-4dfe-bb46-56b60463d8c5.jpg)

Or we can be more specific and filter by test name and patient's ID:

![Captura de pantalla 2022-09-26 003547](https://user-images.githubusercontent.com/108229433/192169815-ea66fcd5-9b60-471b-8d2c-926d788895b3.jpg)

We can filter the results as specific as we want to, combining filter elements to get the data we are looking for.
