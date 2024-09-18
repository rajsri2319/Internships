# Grafana-Dashboards under Integrated Circumstances  
*Theme*: To get simulation and visualization of the data under the manipulation of different servers.  


## Prerequisite  
* Install the Grafana through the link [Grafna](https://grafana.com/grafana/download?platform=windows) and create the account of it through that link.  
* Install the InfluxDB through the link [InfluxDB](https://www.influxdata.com/downloads/) and follow the instructions given in that link.  
* Install the KepserverEX through link [KepserverEX](https://my.kepware.com/s/login/SelfRegister) for a free trial.  
* Install Telegraf through the [InfluxDB](https://www.influxdata.com/downloads/) of version 2.x and follow the instructions.

## KepserverEX  
* Open the file **Cococola.opf** and go to the tags provided in the devices of it.  
* Open a tag properties and extract the data of address row which is in the format of **Extracted_Data + tag_purpose**.
* Now after that before going to restart the KepserverEX which is present in the the above of the Kep panel just make sure to install MOSQUITTO software for MQTT purpose and JRE software.
* ### MQTT  
> Download the MOSQUITO software through the [Link](https://mosquitto.org/download/) and follow the instructions for further and strat the server.
> **Note_1**: Download java JRE software through the [Link](https://www.java.com/en/download/) and start the server.
* Now restart the program of KepserverEX which is the play button present on top of the KepserverEx panel.
**Note_2**: Before going to restart the program just run the file "Json_Payload.py" which is the data generation python file to generate the data.
* Check whether the MQTT server is taking values or not throught the opc client which is prensent on the top of the Kep panel or just right click on the Device_1 and select the opc-client their.


## Telegraf  
* Open the **telegraf.conf** file and just make changes of **outputs.influxdb_v2** and change the bucket, token, and organization their.
* Before going to execute the telegraf.conf file just run the InfluxDB server after navigating to influxd .exe file in command prompt as
~~~
influxd
~~~
* After that execute the telegraf.conf file by navigating to that file in cmd and execute it through the command
~~~
.\telegraf.exe --config telegraf.conf
~~~

## grafana-dashboard.json
* Before going to extract .json file just add the datasouce of InfluxDB in grafana official_website "http://localhost:3000/"
* Copy and paste the .json code to the import dashboards of grafana official_website and execute it.
**Note_4**: Make sure that InfluxDB, Telegraf.exe, Python code or JSON payload are running in the background.


For more details just go through the Grafana.pdf and to get the overall things go through the "Flowchart.jpg"
