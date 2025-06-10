import paho.mqtt.client as mqtt
import ssl
import json
from django.utils.timezone import now
from mainapp.models import Device
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Broker config
MQTT_BROKER = "easy-connect-41c0ff2f.a02.usw2.aws.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "EasyConnect"
MQTT_PASS = "Easyconnect-ece140b"

def on_connect(client, userdata, flags, rc):
    print("[MQTT] Connected with result code", rc)
    client.subscribe("event/+/available_devices/+")
    client.subscribe("device/+/status")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"[MQTT] {topic} -> {payload}")

    try:
        if "available_devices" in topic:
            parts = topic.split("/")
            event_id = parts[1]
            device_id = parts[3]
            Device.objects.update_or_create(
                device_id=device_id,
                defaults={
                    "available": True,
                    "last_seen": now()
                }
            )

        elif "status" in topic:
            print(f"[MQTT] Status from device: {payload}")
            # Optionally process receipts here

    except Exception as e:
        print("[MQTT ERROR]", e)

def start_mqtt():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT)
    client.loop_start()