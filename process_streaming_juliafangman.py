"""

Streaming Process: Uses port 9999

Create a fake stream of data. 
Use temperature data from the batch process.

Reverse the order of the rows to read OLDEST data first.

"""

# Import from Python Standard Library

import csv
import socket
import time
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "supermarket_sales.csv"

def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
    InvoiceID, Branch, City, Customertype, Gender, Productline, Unitprice, Quantity, Tax5, Total, Date, Time, Payment, cogs, gross_margin_percentage, gross_income, Rating = row
    MESSAGE = f"[{InvoiceID}, {Branch}, {City}, {Customertype}, {Gender}, {Productline}, {Unitprice}, {Quantity}, {Tax5}, {Total}, {Date}, {Time}, {Payment}, {cogs}, {gross_margin_percentage}, {gross_income}, {Rating}]".encode()
    logging.debug(f"Prepared message: {MESSAGE}")
    return MESSAGE

def stream_row(input_file_name, address_tuple):
    """Read from input file and stream data."""
    logging.info(f"Starting to stream data from {input_file_name} to {address_tuple}.")
    try:
        with open(input_file_name, "r") as input_file:
            logging.info(f"Opened for reading: {input_file_name}.")
            reader = csv.reader(input_file, delimiter=",")
            next(reader)  # Skip header row

            sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for row in reversed(list(reader)):
                MESSAGE = prepare_message_from_row(row)
                sock_object.sendto(MESSAGE, address_tuple)
                logging.info(f"Sent: {MESSAGE} on port {PORT}. Hit CTRL-C to stop.")
                time.sleep(3)  # wait 3 seconds between messages
    except FileNotFoundError:
        logging.error(f"File {input_file_name} not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if 'sock_object' in locals():
            sock_object.close()

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, ADDRESS_TUPLE)
        logging.info("Streaming complete!")
        logging.info("===============================================")
    except KeyboardInterrupt:
        logging.info("Streaming stopped by user.")
