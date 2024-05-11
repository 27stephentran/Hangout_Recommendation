def process_checkbox_data(form):
    # Dictionary to store checkbox values
    checkbox_data = {}

    # List of preference choices
    preferences = [
        "art galleries", "dance clubs", "juice bars", "restaurants",
        "museums", "resorts", "parks picnic spots", "beaches", "theaters"
    ]

    # Iterate over preference choices
    for preference in preferences:
        # Check if the preference checkbox is checked in the form data
        if preference in form:
            checkbox_data[preference] = 1  # Checkbox is checked
        else:
            checkbox_data[preference] = 0  # Checkbox is not checked

    return checkbox_data