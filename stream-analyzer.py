import json
import random
import time
import uuid
import sys
from tqdm import tqdm

data_collection = []
time_array= []

# This is the upper bound of the records that needed to be created in the Memory.
x = [999, 9999, 99999, 999999,9999999,99999999,999999999]
#  <1k , <10k , <100k , <1M , <10M , <100M ,<1000M

def generateData(value):
    start_time = time.time()
    for i in tqdm(range(value), desc="Processing",ascii =False):
        record = {
            'sale_id': str(uuid.uuid4()),
            'order_timestamp': str(int(time.time())),
            'products_sold': random.choice(
                         [
                            'idly', 
                            'wada',
                            'dosa',
                            'poori',
                            'biryani',
                            'kheema biryani', 
                            'Parota',
                            'Ice cream',
                            'Rasmalai',
                         ]
                    ),
            'num_items_ordered': random.choice([1, 1, 2, 2, 3, 4, 5]),
                }
        data_collection.append(json.dumps(record))
    print(time.time()-start_time)
    print("bytes taken for "+ str(value+1)+ " json records",sys.getsizeof(data_collection))
    time_array.append(time.time()-start_time)



for i in range(0,len(x)):
            generateData(x[i])
            # This code will remove all the data from the list, to free up memory.
            data_collection.clear()
            print(data_collection)

