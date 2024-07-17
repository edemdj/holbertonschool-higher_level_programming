import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        content = template
        content = content.replace("{name}", str(attendee.get("name", "N/A") or "N/A"))
        content = content.replace("{event_title}", str(attendee.get("event_title", "N/A") or "N/A"))
        content = content.replace("{event_date}", str(attendee.get("event_date", "N/A") or "N/A"))
        content = content.replace("{event_location}", str(attendee.get("event_location", "N/A") or "N/A"))

        # Write the processed template to output files
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(content)

        print(f"File {output_filename} generated.")

    print("Invitations generated successfully.")
