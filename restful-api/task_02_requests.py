import requests
import csv

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request to fetch posts
    response = requests.get(url)
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Convert the response to JSON
        posts = response.json()
        
        # Print the titles of the posts
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request to fetch posts
    response = requests.get(url)
    
    if response.status_code == 200:
        # Convert the response to JSON
        posts = response.json()
        
        # Create a list of dictionaries with the desired data
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Define the CSV file name and columns
        csv_filename = 'posts.csv'
        csv_columns = ['id', 'title', 'body']
        
        try:
            # Write the data to the CSV file
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                writer.writerows(posts_data)
            print(f"Posts successfully saved to {csv_filename}")
        except IOError as e:
            print(f"Failed to write to {csv_filename}: {e}")
    else:
        print("Failed to fetch posts")

# Call the functions
fetch_and_print_posts()
fetch_and_save_posts()
