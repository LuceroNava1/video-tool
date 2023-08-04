import psycopg2
import os
import csv


class DataBase:
   def __init__(self):
       self.connection = None

   def connect(self):
      try:
         self.connection = psycopg2.connect(
            host="localhost",
            database="videos",
            user="postgres",
            password="admin",
            port='5432'
         )
         print("Database connection successful!")

      except (Exception, psycopg2.Error) as error:
         print("Error connecting to database", error)


   def create_table(self):
      create_table = '''
      CREATE TABLE video_data (
          clip_name VARCHAR(60),
          clip_file_extension  VARCHAR(25),
          clip_duration  FLOAT,
          clip_location  VARCHAR,
          insert_timestamp  TIMESTAMP
      );
      '''
      try:
         cursor = self.connection.cursor()
         cursor.execute(create_table)
         self.connection.commit()
         print("Table successfully created.")

      except (Exception, psycopg2.Error) as error:
         print("Error creating table:", error)

      finally:
         if cursor is not None:
            cursor.close()

   def insert_data(self, data):
       columns = ', '.join(data.keys())
       values = ', '.join(['%s'] * len(data))
       insert_query = f'INSERT INTO video_data ({columns}) VALUES ({values});'

       try:
           cursor = self.connection.cursor()
           cursor.execute(insert_query, tuple(data.values()))
           self.connection.commit()
           print("Data inserted correctly.")

       except (Exception, psycopg2.Error) as error:
           print("Error inserting data:", error)


   def create_csv(self):
        table_name = "video_data"
        query = f"SELECT * FROM {table_name};"
        output_folder = "report"
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            file_name = os.path.join(output_folder, "generated_video_files.csv")
            print("Data inserted correctly.")
            with open(file_name, 'w', newline='') as file_csv:
                csv_writer = csv.writer(file_csv)
                csv_writer.writerow([i[0] for i in cursor.description]) #Headers
                csv_writer.writerows(data)

            print(f"File CSV '{file_name}' created.")

        except (Exception, psycopg2.Error) as error:
            print("Error inserting data:", error)

   def close(self):
       if self.connection is not None:
           self.connection.close()
           print("Close connection.")

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.create_table()
    db.insert_data(dict)
    db.create_csv()
    db.close()