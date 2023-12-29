import tkinter 
import customtkinter
import speedtest

# Function
def perform_speed_test():
    status_label.configure(text="Running speed test...")
    progress_bar.set(0)  

    try:
        st = speedtest.Speedtest()
        
        
        status_label.configure(text="Loading server list...")
        st.get_servers()
        app.update_idletasks()

       
        status_label.configure(text="Searching for the best server...")
        best = st.get_best_server()
        status_label.configure(text=f"Found: {best['host']} located in {best['country']}")
        app.update_idletasks()

        status_label.configure(text="Performing download test...")
        app.update_idletasks()
        progress_bar.start() 

        def update_progress():
            progress = progress_bar.get()
            if progress < 50:
                progress += 1
                progress_bar.set(progress)
                app.after(50, update_progress)  
            elif progress < 75:
                progress += 5
                progress_bar.set(progress)
                app.after(50, update_progress) 
            else:
                app.after(50, lambda: progress_bar.set(50))  

        app.after(50, update_progress) 
        download_result = st.download()

     
        status_label.configure(text="Performing upload test...")
        app.update_idletasks()

        def update_progress_upload():
            progress = progress_bar.get()
            if progress < 100:
                progress += 5
                progress_bar.set(progress)
                app.after(50, update_progress_upload)  
            else:
                app.after(50, lambda: progress_bar.set(75))  

        app.after(50, update_progress_upload)  
        upload_result = st.upload()

        
        ping_result = st.results.ping

      
        progress_bar.stop()
        app.update_idletasks()

        
        finishLabel.configure(text=f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s\nUpload speed: {upload_result / 1024 / 1024:.2f} Mbit/s\nPing: {ping_result} ms")
        status_label.configure(text="Speed test completed.")
    except Exception as e:
       
        progress_bar.stop()
        finishLabel.configure(text=f"Error: {e}")
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

# Progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.pack(pady=10)

# Run App 
app.mainloop()
