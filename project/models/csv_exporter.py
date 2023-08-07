import csv

class CSVExporter:

    def __init__(self, write_path):
        self.write_path = write_path

    def export_data(self, content: str):

        # Split string into a list.
        columns = content.split(',')

        with open(self.write_path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write csv headers.
            writer.writerow(['id', 'title', 'url', 'publication_date', 'views', 'apple_music_url', 'spotify_url'])
            
            writer.writerow(columns)