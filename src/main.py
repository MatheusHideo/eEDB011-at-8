import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.database import import_bancos
from src.producer import  producer 
from src.consumer import consumer
import sys
import os




def main():
    import_bancos.main()
    producer.main()
    consumer.main()
    
if __name__ == "__main__":
    main()