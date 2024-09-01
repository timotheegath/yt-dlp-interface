from app.app import DownloaderApplication
import sys
from os import getcwd

print(f"Current wd: {getcwd()}")
print(f"Sys args: {sys.argv}")
app = DownloaderApplication(sys.argv, root=getcwd(), load_dev_ui=True)

sys.exit(app.exec())