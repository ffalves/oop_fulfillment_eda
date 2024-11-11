import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

class DataGenerator:
    '''
    This class generates a fake dataset for this Exploration Data Analysis (EDA).
    '''
    def __init__(self, num_orders: int, start_date: str, end_date: str):
        '''
        Initialize the DataGenerator with the numbers of orders and the data range.
        
        param num_orders: int, the number of orders to generate.
        param start_date: str, the start date of the data range.
        param end_date: str, the end date of the data range.
        '''
        self.num_orders = num_orders
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        self.fake = Faker() # Create a Faker object to generate fake data.

    def generate_order_data(self) -> pd.DataFrame: # -> pd.DataFrame is the return type hint.
        '''
        Generates the fake orders to dataset.
        
        return: pd.DataFrame.
        '''
        order_data = []
        order_status_list = ['pending', 'shipped', 'delivered', 'cancelled', 'processing', 'returned']
        payment_method_list = ['credit_card', 'debit_card', 'paypal', 'cash_on_delivery']
        product_category_list = ['electronics', 'clothing', 'books', 'furniture', 'grocery', 'beauty',
                            'sports', 'automotive', 'toys', 'stationery']
        neighboorhood = ['Downtown', 'Midtown', 'Uptown', 'East Side', 'West Side', 'North Side', 
                          'South Side']
        city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
                  'San Antonio', 'San Diego', 'Dallas', 'San Jose']
        vehicle = ['bicycle', 'motorcycle', 'car', 'van', 'truck']
        courier = ['Courier A', 'Courier B', 'Courier C', 'Courier D', 'Courier E']
        center = ['Center A', 'Center B', 'Center C', 'Center D', 'Center E']
        
        for _ in range(self.num_orders): # _ is a throwaway variable.
            order_id = self.fake.unique.uuid4()
            order_date = self.fake.date_between(start_date=self.start_date,
                                                      end_date=self.end_date)
            timestamp_buy = self.fake.date_time_between(start_date=datetime.combine(order_date, datetime.min.time()),
                                                        end_date=datetime.combine(order_date, datetime.max.time()))
            order_status = random.choice(order_status_list)
            payment_method = random.choice(payment_method_list)
            product_category = random.choice(product_category_list)
            customer_neighborhood = random.choice(neighboorhood)
            customer_city = random.choice(city)
            delivery_time = random.uniform(1, 24)
            timestamp_delivery = timestamp_buy + timedelta(hours=delivery_time)
            delivery_status = 'within_12hs' if delivery_time <= 12 else 'delayed'
            distance_to_customer = random.uniform(1, 100)
            order_amount = round(random.uniform(10,1000), 2)
            courier_lastmile = random.choice(vehicle)
            fulfillment_center = random.choice(center)
            courier_partner = random.choice(courier)

            order_data.append({
                'order_id': order_id,
                'order_date': order_date,
                'timestamp_buy': timestamp_buy,
                'timestamp_delivery': timestamp_delivery,
                'order_status': order_status,
                'payment_method': payment_method,
                'product_category': product_category,
                'customer_neighborhood': customer_neighborhood,
                'customer_city': customer_city,
                'delivery_time': delivery_time,
                'delivery_status': delivery_status,
                'distance_to_customer': distance_to_customer,
                'order_amount': order_amount,
                'courier_lastmile': courier_lastmile,
                'fulfillment_center': fulfillment_center,
                'courier_partner': courier_partner
                
            })
        
        return pd.DataFrame(order_data)
    
    
    def save_to_csv(self, df:pd.DataFrame, file_path:str) -> None:
        '''
        Save the DataFrame to a CSV file.
        
        param df: pd.DataFrame, the DataFrame to save.
        param file_path: str, the file path to save the DataFrame.
        '''
        try:
            output_dir = os.path.dirname(file_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
                
            df.to_csv(file_path, index=False)
            print(f"Dataset successfully saved to { file_path }")
        
        except FileNotFoundError:
            print(f"Error: the file path '{ file_path }'is invalid or inaccessible.")

        except PermissionError:
            print(f"Error: permission dedined when attempting to save to '{ file_path }'.")

        except Exception as e:    
            print(f"An unexpected error occurred while saving the dataset to '{ file_path }'. Error: { str(e)}.")


