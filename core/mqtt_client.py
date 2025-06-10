import paho.mqtt.client as mqtt
import ssl
import json
from django.utils.timezone import now
from mainapp.models import Device
import os
import django
from dotenv import load_dotenv

load_dotenv()
print("[DEBUG] MQTT Config:", MQTT_BROKER, MQTT_PORT, MQTT_USER)

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Broker config
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8883))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASS = os.getenv("MQTT_PASS")


def on_connect(client, userdata, flags, rc):
    print("[MQTT] Connected with result code", rc)
    client.subscribe("event/#")
    client.subscribe("device/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"[MQTT] {topic} -> {payload}")

    try:
        if "available_devices" in topic:
            data = json.loads(payload)
            _device_id = data.get("device_id")
            _event_id = data.get("event_id")
            _is_available = data.get("_is_available")
            Device.objects.update_or_create(
                device_id=_device_id,
                event_id=_event_id,
                available=_is_available
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
