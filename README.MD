# Dashboards in Grafana of Simulated Data from KepserverEX through InfluxDB  
*Theme*: To get simulation and visualization of the data under the manipulation of different servers.    


## Prerequisite  
* Install Grafana using [this link](https://grafana.com/grafana/download?platform=windows) and create an account through the provided link  
* Install the InfluxDB using [this link](https://www.influxdata.com/downloads/) and follow the instructions provided there.  
* Install the KepserverEX using [this link](https://my.kepware.com/s/login/SelfRegister) for a free trial.  
* Install Telegraf(version 2.x) from [this link](https://www.influxdata.com/downloads/) and follow provided instructions.  

## KepserverEX  
* Open the file **Cococola.opf** and go to the tags provided in the devices of it.  
* Open a tag properties and extract the data of address row which is in the format of **Extracted_Data + tag_purpose**.  
* Now after that before going to restart the KepserverEX which is present in the the above of the Kep panel just make sure to install MOSQUITTO software for MQTT purpose and JRE software.  
* ### MQTT  
> Download the MOSQUITO software using [this link](https://mosquitto.org/download/) and follow provided instructions and start the server.  
> **Note**: Download java JRE software through the [Link](https://www.java.com/en/download/) and start the server.  
* Now restart the program of KepserverEX which is the play button present on top of the KepserverEx panel.  
**Note**: Before going to restart the program just run the file "Json_Payload.py" which is the data generation python file.  
* Check whether the MQTT server is taking values or not throught the opc client which is prensent on the top of the KepserverEX panel or just right click on the Device_1 and select the opc-client.  


## Telegraf  
* Open the **telegraf.conf** file and just make changes of **outputs.influxdb_v2** and change the bucket, token, and organization in it.
* ### InfluxDB  
> Create a bucket and a token in InfluxDB before including them in **telegraf.conf** file.   
> Before going to execute the telegraf.conf file run the InfluxDB server after navigating to influxd .exe file in command prompt as
> ~~~
influxd
~~~
> Check the data points in data_explorer of InfluxDB after executing telegraf.conf file.  
* After that execute the telegraf.conf file by navigating to that file in cmd and execute it through the command
~~~
.\telegraf.exe --config telegraf.conf
~~~  


## grafana-dashboard.json  
* Before going to extract .json file just add the datasouce of InfluxDB in grafana official_website "http://localhost:3000/"  
* Copy and paste the .json code to the import dashboards of grafana official_website and execute it.  
**Note**: Make sure that InfluxDB, Telegraf.exe, Python code or JSON payload are running in the background.


For more details just go through the Grafana.pdf and to get the overall things go through the "Flowchart.jpg"
