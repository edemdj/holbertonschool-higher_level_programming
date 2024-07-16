import os
from tempfile import template

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return
    
    # Check if the template is empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    # Check if the list of attendees is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation = template.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Generate the output file name
        output_filename = f"output_{index}.txt"
        
        try:
            # Check if the file already exists
            if os.path.exists(output_filename):
                print(f"Error: The file {output_filename} already exists.")
                continue
            
            # Write the invitation to the file
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
            
            print(f"File {output_filename} generated.")
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")

# function call
generate_invitations(template, attendees)
