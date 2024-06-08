from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load the credentials from the JSON file
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your-service-account-file.json',
    scopes=['https://www.googleapis.com/auth/androidpublisher']
)

# Build the API client
service = build('androidpublisher', 'v3', credentials=credentials)

# Get a list of your app's reviews
package_name = 'your.package.name'
reviews = service.reviews().list(packageName=package_name).execute()

for review in reviews.get('reviews', []):
    print(f'Review: {review.get("reviewId")}, Rating: {review.get("starRating")}, Comment: {review.get("comments")[0]["userComment"]["text"]}')
import ser