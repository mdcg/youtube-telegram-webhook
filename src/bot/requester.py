import requests
from src.settings import CALLBACK_URL
from src.bot import logger


def subscribe_in_pubsubhubbub(channel_id):
    logger.info("Sending subscribe request to Pubsubhubbub..")
    payload = {
        "hub.callback": CALLBACK_URL,
        "hub.topic": f"https://www.youtube.com/xml/feeds/videos.xml?channel_id={channel_id}",
        "hub.mode": "subscribe",
        "hub.lease_seconds": 60 * 60 * 24 * 5,
    }
    r = requests.post(
        "https://pubsubhubbub.appspot.com/subscribe", data=payload
    )
    return r.status_code
