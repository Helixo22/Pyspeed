import tkinter 
import customtkinter
import subprocess

# Function
def perform_speed_test():
    status_label.configure(text="Running speed test...")

    try:
        result = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        if len(output_lines) >= 2:
            download_speed = float(output_lines[0].split()[1]) / 1000000  # Convert to Mbps
            upload_speed = float(output_lines[1].split()[1]) / 1000000  # Convert to Mbps

            # Update the text of finishLabel
            finishLabel.configure(text="Download Speed: {:.2f} Mbps\nUpload Speed: {:.2f} Mbps".format(download_speed, upload_speed))
            status_label.configure(text="Speed test completed.")
        else:
            finishLabel.configure(text="Error: Unable to retrieve speed test results.")
            status_label.configure(text="Speed test failed.")
    except Exception as e:
        finishLabel.configure(text="Error: {}".format(e))
        status_label.configure(text="Speed test failed.")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("PySpeed")

# UI elements
title = customtkinter.CTkLabel(app, text="PySpeed")
title.pack(padx=10, pady=10)

# Finished label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack()

# SpeedTest Button
speedtest_button = customtkinter.CTkButton(app, text="Start the test", command=perform_speed_test)
speedtest_button.pack(padx=10, pady=10)

# Run App 
app.mainloop()
