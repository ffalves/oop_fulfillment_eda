from data_generator.data_generator import DataGenerator
import os

# Generate order data for the month of October 2024
def main():
    try:
        generator = DataGenerator(
            num_orders=10000,
            start_date='2024-10-01',
            end_date='2024-10-31'
        )

        df = generator.generate_order_data() # Generate order data

        # Defining the path and the folder datasets
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, '..', 'datasets')
        os.makedirs(output_dir, exist_ok=True) 

        # Saving the data to a CSV file
        output_file = os.path.join(output_dir, 'orders_october.csv')
       
        generator.save_to_csv(df, output_file)

    except RuntimeError as e:
        print(f"Runtime error: { str(e)}.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}.")
# 
if __name__ == '__main__':
    main()