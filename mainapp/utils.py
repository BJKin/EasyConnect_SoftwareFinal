import paho.mqtt.publish as publish
import ssl
import json

def assign_ticket(device_id, ticket_id):
    topic = f"device/{clientId}/#"
    payload = {
        "command": "assignment",
        "ticket_id": ticket_id
    }
    publish.single(
        topic,
        json.dumps(payload),
        hostname="easy-connect-41c0ff2f.a02.usw2.aws.hivemq.cloud",
        port=8883,
        auth={"username": "EasyConnect", "password": "Easyconnect-ece140b"},
        tls={"cert_reqs": ssl.CERT_REQUIRED}
    )
