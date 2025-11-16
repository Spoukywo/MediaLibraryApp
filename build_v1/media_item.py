import json 

class MediaItem:

    all_media = []

    def __init__(self, media_type, format, title, artist, year):
        self.media_type = media_type
        self.format = format
        self.title = title 
        self.artist = artist 
        self.year = year
    
    def add_item_to_list(self):
        MediaItem.all_media.append(self)

    def to_dict(self):
        return {"Media Type": self.media_type,"Format": self.format, "Title": self.title, "Artist": self.artist, "Year": self.year }
        

    @classmethod
    def save_json(cls, filename = "app_info.json"):
        data = [item.to_dict() for item in cls.all_media]
        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename="app_info.json"):
        cls.all_media.clear()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    print(f"File '{filename}' is empty. No media loaded.")
                    return
            data = json.loads(content)
            for spec in data:
                media_item = cls(
                    spec["Media Type"],
                    spec["Format"],
                    spec["Title"],
                    spec["Artist"],
                    spec["Year"]
                )
                cls.all_media.append(media_item)
        except FileNotFoundError:
            print(f"File '{filename}' not found. No media loaded.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    @classmethod
    def create_from_input(cls):
        media_type = input("Enter media type: ")
        format = input ("Enter media format: ") 
        title = input("Enter media title: ")
        artist  = (input("Enter media artist: "))
        
        while True:
            try:
                year = int(input("Enter year of release: "))
                break
            except ValueError:
                print("Please enter a valid integer for the year of release: ")

        media_item = cls(media_type, format, title, artist, year)
        media_item.add_item_to_list()
        print(f"Media {title} added successfully!")
    @classmethod
    def show_all(cls):
         for item in cls.all_media:
              print(f"{item.media_type}, {item.format}, {item.title}, {item.artist}, {item.year}")     

MediaItem.load_from_json()
if __name__ == "__main__":
    MediaItem.load_from_json()
    MediaItem.create_from_input()
    MediaItem.save_json()
    MediaItem.show_all()

