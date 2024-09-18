import time
import json
import paho.mqtt.client as mqtt

# MQTT Configuration
broker = '127.0.0.1'  # Replace with your broker's IP address
port = 1883  # Replace with your broker's port if different
topic = 'home/sensor/status'

# MQTT Client Setup
client = mqtt.Client()

# Connect to MQTT Broker
client.connect(broker, port)
client.loop_start()  # Start the loop to handle network traffic, callbacks, etc.

# Initialize the status and metrics
statuses = {
    "Capper_status": True,
    "Filler_status": False,
    "Labeling_status": True,
    "Packaging_status": False,
    "Palletizing_status": True,
    "Wrapping_status": False
}

# Dictionaries to keep track of operating time, failure counts, and overall scrap count
operating_time = {
    "Capper": 0,
    "Filler": 0,
    "Labeling": 0,
    "Packaging": 0,
    "Palletizing": 0,
    "Wrapping": 0
}

failure_count = {
    "Capper": 0,
    "Filler": 0,
    "Labeling": 0,
    "Packaging": 0,
    "Palletizing": 0,
    "Wrapping": 0
}

overall_scrap_count = 0  # Initialize overall scrap count

# Function to publish status, operating time, failure count, and overall scrap count
def publish_status():
    payload = {
        "Capper_status": statuses["Capper_status"],
        "Filler_status": statuses["Filler_status"],
        "Labeling_status": statuses["Labeling_status"],
        "Packaging_status": statuses["Packaging_status"],
        "Palletizing_status": statuses["Palletizing_status"],
        "Wrapping_status": statuses["Wrapping_status"],
        "Capper_operating_time": operating_time["Capper"],
        "Filler_operating_time": operating_time["Filler"],
        "Labeling_operating_time": operating_time["Labeling"],
        "Packaging_operating_time": operating_time["Packaging"],
        "Palletizing_operating_time": operating_time["Palletizing"],
        "Wrapping_operating_time": operating_time["Wrapping"],
        "Capper_failure_count": failure_count["Capper"],
        "Filler_failure_count": failure_count["Filler"],
        "Labeling_failure_count": failure_count["Labeling"],
        "Packaging_failure_count": failure_count["Packaging"],
        "Palletizing_failure_count": failure_count["Palletizing"],
        "Wrapping_failure_count": failure_count["Wrapping"],
        "Overall_scrap_count": overall_scrap_count  # Publish overall scrap count
    }
    client.publish(topic, json.dumps(payload))
    print(f"Published: {payload} to topic {topic}")

# Function to simulate operation, failure, and scrap tracking
def update_metrics():
    global operating_time, failure_count, overall_scrap_count
    for machine in operating_time.keys():
        # Simulate operating time increment
        if statuses[f"{machine}_status"]:
            operating_time[machine] += 30  # Increment by 30 minutes
        
        # Simulate failure detection (example: if status is False, increment failure count)
        if not statuses[f"{machine}_status"]:
            failure_count[machine] += 1  # Increment failure count

        # Simulate scrap count increment (example: if status is False, increment overall scrap count)
        if not statuses[f"{machine}_status"]:
            overall_scrap_count += 1  # Increment overall scrap count

def get_opposite_statuses():
    return {key: not value for key, value in statuses.items()}

def monitor_status():
    global statuses
    while True:
        # Publish current status, metrics
        publish_status()
        
        # Update metrics
        update_metrics()
        
        # Wait for 30 minutes
        time.sleep(1800)  # 30 minutes = 1800 seconds
        
        # Update statuses with opposite values
        statuses = get_opposite_statuses()
        publish_status()  # Publish the updated statuses and metrics

if __name__ == "__main__":
    monitor_status()
