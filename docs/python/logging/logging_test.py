# Import standard library's logging
import logging

# Create function that converts dollars to cents
def convert_dollars_to_cents(dollars):
    
    # Convert dollars to cents (as an integer)
    cents = int(dollars * 100)

    logging.debug("debug") 
    logging.info("info") 
    logging.warning("warning") 
    logging.error("error")
    logging.critical("critical")
    
    # Return cents
    return cents

# Create dollar amount
dollars = 12.40

# Run dollars to cents convert function
convert_dollars_to_cents(dollars)