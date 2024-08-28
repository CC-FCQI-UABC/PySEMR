#Installing and running instructions

There are two simulations in this repository. If you are running this simulation for the first time, 
then you must run the first version of the simulation, here below I write the instructions:

1. Do **git clone https://github.com/CC-FCQI-UABC/PySEMR.git**

3. Afterwards you must install the python dependencies inside the requirements.txt by executing **pip install -r requirements.txt**

4. Then, head to the database_API directory and **run the mysql_connector_to_domicilios.py file**
   
5. Then you must **head to the directory PySEMR/_mesa/simulacion/** and run the python file run.py with **python ./run.py**

7. In your terminal, the mesa simulation should start generating multiple patients and in the end, it will leave a couple of .csv files in the directory.
   Those .csv files can be converted into sql files with the csv_to_sql.py script, all you have to do is run this script and you will get the sql files.
   These sql files will be necessary to run the second simulation.

**Now, to run the second simulation you must do the next:**

1. Upload the generated sql files to a database
   
2. Open the directory **./database_API** and configure the connection in **"mysql_connector_to_open_emr.py"** and make sure it connects to your database with
   the generated sql data and then run the file.
   
3. Once done, head to the directory **PySEMR/_mesa/simulacion.2/** and run the second version of the simulation.

4. This simulation will drop multiple statistical graphics at the **PySEMR/_mesa/simulacion.2/templates/static**
   and has a little more complexity than the previous version. **You can view this data by accessing the localhost
   with the port 8081 in the web browser.**

   *Note that You can run this simulation again by clicking on the button **"Run Simulation"** at the top of the page.
   
   *This simulation will also generate new sql files with the same patients every time but now with new or different disease data.
