import time
import json
import random
import paho.mqtt.client as mqtt

# MQTT Configuration
broker = '127.0.0.1'  # Replace with your broker's IP address
port = 1883  # Replace with your broker's port if different
topic = 'home/machine/work_order'

# MQTT Client Setup
client = mqtt.Client()

# Connect to MQTT Broker
client.connect(broker, port)
client.loop_start()  # Start the loop to handle network traffic, callbacks, etc.

# Machine names
machines = ["Filler", "Capper", "Labeler", "Palletizer", "Packer", "Wrapper"]

# Initialize work order counts for 6 machines
def generate_work_order_counts():
    return {machine: random.randint(10, 30) for machine in machines}

# Initialize random values for "Yet to Start", "In Progress", and "On Hold"
def generate_status_counts():
    return {
        "YetToStart": random.randint(20, 40),
        "InProgress": random.randint(40, 60),
        "OnHold": random.randint(10, 20)
    }

# Initialize pending orders and deviations
pending_orders = 0
deviations = 0

# Function to publish work order status
def publish_work_order_status(work_order_counts, status_counts, total_orders, pending_orders, deviations):
    payload = {
        "filler_work_order": work_order_counts["Filler"],
        "capper_work_order": work_order_counts["Capper"],
        "labeler_work_order": work_order_counts["Labeler"],
        "palletizer_work_order": work_order_counts["Palletizer"],
        "packer_work_order": work_order_counts["Packer"],
        "wrapper_work_order": work_order_counts["Wrapper"],
        "InProgress_work_order_count": status_counts["InProgress"],
        "YetToStart_work_order_count": status_counts["YetToStart"],
        "OnHold_work_order_count": status_counts["OnHold"],
        "total_orders_today": total_orders,
        "pending_orders": pending_orders,
        "deviations": deviations
    }
    client.publish(topic, json.dumps(payload))
    print(f"Published: {payload} to topic {topic}")

# Main function to generate and publish data every minute
def generate_and_publish_data():
    global pending_orders, deviations

    while True:
        # Generate random work order counts for each machine
        work_order_counts = generate_work_order_counts()

        # Generate random counts for In Progress, Yet to Start, and On Hold
        status_counts = generate_status_counts()

        # Calculate total orders today (sum of all work order counts of the machines)
        total_orders = sum(work_order_counts.values())

        # Increment deviations when InProgress is updated
        deviations += 1

        # Increment pending orders if there's an update to OnHold
        if random.choice([True, False]):  # Simulate if a machine is moved to OnHold randomly
            pending_orders += 1

        # Publish the generated data
        publish_work_order_status(work_order_counts, status_counts, total_orders, pending_orders, deviations)

        # Wait for 1 minute before the next update
        time.sleep(60)

if __name__ == "__main__":
    generate_and_publish_data()
