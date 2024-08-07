import asyncio
from aiokafka import AIOKafkaConsumer
from sqlmodel import Session
from inventory_service.crud import update_inventory_item
from inventory_service.db import get_session
from inventory_service.kafka import inventory_pb2
from inventory_service.db import engine

KAFKA_BROKER_URL = "broker:19092"
INVENTORY_TOPIC = "inventory"

class KafkaConsumer:
    def __init__(self, broker_url: str, topic: str):
        self.consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=broker_url,
            group_id="inventory_group",
            auto_offset_reset="earliest"
        )

    async def start(self):
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()

    async def consume(self):
        await self.start()
        try:
            async for msg in self.consumer:
                inventory_update = inventory_pb2.InventoryUpdate()
                inventory_update.ParseFromString(msg.value)
                session = Session(engine)  # Create session inside the loop
                try:
                    # Update the item using the correct deserialized data
                    update_inventory_item(session, inventory_update.product_id, inventory_update.quantity)
                finally:
                    session.close()  # Close session after each message processing
        finally:
            await self.stop()

async def start_consumer():
    consumer = KafkaConsumer(KAFKA_BROKER_URL, INVENTORY_TOPIC)
    await consumer.consume()
