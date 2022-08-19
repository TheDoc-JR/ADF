# ABLORH DATA FINDER
ABLORH DATA FINDER is a desktop application to manage clinic data of patients. It was made for authorized medical personnel only.

DISCLAIMER:
It was made only for training purposes, that is why I used my local database and the tables are deleted and created everytime the program runs. It was made only with 3 types of tests (3 tables) and with 3 types of records by each test.

# Login Window
![Captura de pantalla 2022-08-19 144256](https://user-images.githubusercontent.com/108229433/185621223-7b61972e-78f6-4c4c-a34b-a7810b965ca7.jpg)

A message appears when the user enters a wrong password:
![Captura de pantalla 2022-08-19 144334](https://user-images.githubusercontent.com/108229433/185621227-795e7984-bcc7-4072-89f5-59005828bd38.jpg)

# Data Finder Window
After entering the correct password the Data Finder Window appears. We have a frame and 5 buttons to add a new patient, search a patient's data, add records to a patient, search records from a patient and exit.

![Captura de pantalla 2022-08-18 192019](https://user-images.githubusercontent.com/108229433/185598449-761c3b8d-e66a-4560-9f9b-f600a0dc50e6.jpg)

## 1-Add patient
When clicking the Add-patient button; entry boxes, comboboxes and radiobuttons appears in order to get the patient data.
![Captura de pantalla 2022-08-18 192049](https://user-images.githubusercontent.com/108229433/185598451-155e0c60-e9e7-4289-89f6-2a8663073d8c.jpg)

After entering the data in the correct way and click the Add-new-patient button, if process goes well a message appears to inform the user.
![Captura de pantalla 2022-08-18 192154](https://user-images.githubusercontent.com/108229433/185598455-dd614ea1-294a-4eff-9c6e-45c5aad78e6f.jpg)

If data is entered the wrong way (non numeric ID or age, numeric name or surname) and the button is clicked, an error message appears to inform the user and the window is cleared.
![Captura de pantalla 2022-08-18 192258](https://user-images.githubusercontent.com/108229433/185598457-1218337f-d49b-4b26-b4d8-cd406ad69360.jpg)

## 2-Search patient
When clicking the Search-patient button; an entry box appears in order to check if the patient is in the database.
![Captura de pantalla 2022-08-18 192321](https://user-images.githubusercontent.com/108229433/185598461-8992c0bd-2655-4098-b0e1-517aa7131f20.jpg)

If not, an error message informs the user and the window is cleared.
![Captura de pantalla 2022-08-18 192351](https://user-images.githubusercontent.com/108229433/185598466-66234072-71b5-4aab-a4c4-add56d5ee5eb.jpg)

If patient in database, a treeview appears to show the patient's data.
![Captura de pantalla 2022-08-19 134423](https://user-images.githubusercontent.com/108229433/185611560-bf0eb5d6-2983-4cf8-b7bc-2d7cc37bad57.jpg)

## 3-Add tests
When clicking the Add-tests button; an entry box appears in order to check if the patient is in the database (If not, an error message informs the user and the window is cleared).
![Captura de pantalla 2022-08-18 192446](https://user-images.githubusercontent.com/108229433/185598469-f753cf82-7feb-4605-aa87-64322aef3293.jpg)

If patient in database, radiobuttons appears in order to select the test you want to add data in.
![Captura de pantalla 2022-08-18 192512](https://user-images.githubusercontent.com/108229433/185598470-b10e726c-de58-4f80-a685-02ff89ce82b4.jpg)

When we select a test (Biochemistry for example) entry boxes and comboboxes appears to get the tests records and the date they were made.
![Captura de pantalla 2022-08-18 192609](https://user-images.githubusercontent.com/108229433/185598471-14247200-b644-4f4c-811d-c6e267d60fb2.jpg)

After entering the data in the correct way and click the Add-tests button, if process goes well a message appears to inform the user.
![Captura de pantalla 2022-08-18 192658](https://user-images.githubusercontent.com/108229433/185598473-3bed5d39-3489-4463-8958-120c4eaf88ea.jpg)

If data is entered the wrong way and the button is clicked, an error message appears to inform the user and the window is cleared.
![Captura de pantalla 2022-08-18 192853](https://user-images.githubusercontent.com/108229433/185598476-49dee66d-7833-4907-bec9-332c93ad88f8.jpg)

## 4-Search tests
When clicking the Add-tests button; an entry box appears in order to check if the patient is in the database (If not, an error message informs the user and the window is cleared).
![Captura de pantalla 2022-08-18 192925](https://user-images.githubusercontent.com/108229433/185598479-bb2d85b3-6635-415a-adc0-c167486e2564.jpg)

If patient in database, radiobuttons appears in order to select the test you want to show data from. We can show records by table or also all the records that patient has.
![Captura de pantalla 2022-08-18 193042](https://user-images.githubusercontent.com/108229433/185598480-4ba94ba5-317c-4364-90b8-43fee293ef7a.jpg)

After selecting a table, if patient has no data in that test, an error message informs the user and the window is cleared.
![Captura de pantalla 2022-08-18 193101](https://user-images.githubusercontent.com/108229433/185598483-bd767881-134c-4d5a-9733-707dc5d3bce0.jpg)

If patient has records in the test selected, a treeview shows the data.
![Captura de pantalla 2022-08-18 193128](https://user-images.githubusercontent.com/108229433/185598485-f054a2e4-a895-445f-b5f5-e3a248d94def.jpg)

## 5.Exit
When clicking the Exit button a question message appears to confirm the exit request.
![Captura de pantalla 2022-08-18 193154](https://user-images.githubusercontent.com/108229433/185598488-b135cf33-c543-4aa7-be17-2be032aa1fac.jpg)
