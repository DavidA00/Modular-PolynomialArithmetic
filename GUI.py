import tkinter as tk
from tkinter import ttk
from PolynomialArithmetic import *

selected_option = None
selected_option2 = None
def PolyPrint(arr, text_widget):
    if len(arr) == 0:
        text_widget.insert(tk.END, "There is no Polynomial!\n")
        return
    for i in range(len(arr) - 1):
        arr[i] = arr[i] % 2
    for i in range(len(arr) - 1):
        if arr[i] == 1 and (len(arr) - i - 1 != 1):
            text_widget.insert(tk.END, f"x^{len(arr)-i-1} + ")
        elif arr[i] == 1 and (len(arr) - i - 1 == 1):
            text_widget.insert(tk.END, "x + ")
    if arr[len(arr) - 1] == 1:
        text_widget.insert(tk.END, "1\n")
    else:
        text_widget.insert(tk.END, "0\n")

def get_selected_option():
    global selected_option
    global selected_option2
    for entry, label in zip(entry_boxes1, label_boxes1):
       entry.destroy()
       label.destroy()

    for entry, label in zip(entry_boxes2, label_boxes2):
       entry.destroy()
       label.destroy()

    selected_option = var.get()
    selected_option2 = var2.get()
    if selected_option2 == "BIN":
        # Create one entry box and label for each polynomial
        row1 = len(options) + 3
        label_text1 = "Polynomial 1 Binary:"
        label1 = tk.Label(canvas_frame2, text=label_text1)
        label1.grid(row=row1, column=0, padx=3, pady=2, sticky='e')
    
        entry1 = tk.Entry(canvas_frame2, width=120)
        entry1.grid(row=row1, column=1, padx=3, pady=2, sticky='w')
        entry1.bind('<Key>', lambda event: enforce_max_length(entry1, selected_option-1))
    
        label_boxes1.append(label1)
        entry_boxes1.append(entry1)
        
        row2 = len(options) + 13 + len(options) + selected_option + 3 // 10
        label_text2 = "Polynomial 2 Binary:"
        label2 = tk.Label(canvas_frame2, text=label_text2)
        label2.grid(row=row2, column=0, padx=3, pady=2, sticky='e')
    
        entry2 = tk.Entry(canvas_frame2, width=120)
        entry2.grid(row=row2, column=1, padx=3, pady=2, sticky='w')
        entry2.bind('<Key>', lambda event: enforce_max_length(entry2, selected_option-1))

        label_boxes2.append(label2)
        entry_boxes2.append(entry2)
        
        
        # Move the "Collect Values" button below the entry boxes and make it visible
        collect_binary_button = tk.Button(canvas_frame2, text="Collect Binary Input", command=lambda: collect_binary(selected_option))
        collect_binary_button.grid(row=row2 + 2, column=0, pady=10, sticky='w')

        # Move the "Print Arrays" button below the "Collect Values" button
        print_array_button.grid(row=row2+3, column=0, pady=10, sticky='w')

        # Move the "Calculate Result" button below the "Print Arrays" button
        calculate_result_button1.grid(row=row2+4, column=0, pady=10, sticky='w')
        calculate_result_button2.grid(row=row2+5, column=0, pady=10, sticky='w')
        calculate_result_button3.grid(row=row2+6, column=0, pady=10, sticky='w')
        calculate_result_button4.grid(row=row2+8, column=0, pady=10, sticky='w')
        calculate_result_button5.grid(row=row2+7, column=0, pady=10, sticky='w')


        # After creating or modifying widgets, update the canvas scroll region
        canvas_frame.update_idletasks()
        canvas_frame2.update_idletasks()
        
        # Calculate total height of both frames
        total_height = canvas_frame.winfo_reqheight() + canvas_frame2.winfo_reqheight()
        
        extra_space = 70
        canvas.config(scrollregion=(0, 0, canvas_frame.winfo_reqwidth(), total_height + extra_space))
    
    elif selected_option2 == "HEX":     
         # Create one entry box and label for each polynomial
         row1 = len(options) + 3
         label_text1 = "Polynomial 1 HEX:"
         label1 = tk.Label(canvas_frame2, text=label_text1)
         label1.grid(row=row1, column=0, padx=3, pady=2, sticky='e')
     
         entry1 = tk.Entry(canvas_frame2, width=120)
         entry1.grid(row=row1, column=1, padx=3, pady=2, sticky='w')
         entry1.bind('<Key>', lambda event: enforce_max_length(entry1, selected_option-1))

         label_boxes1.append(label1)
         entry_boxes1.append(entry1)
         
         row2 = len(options) + 13 + len(options) + selected_option + 3 // 10
         label_text2 = "Polynomial 2 HEX:"
         label2 = tk.Label(canvas_frame2, text=label_text2)
         label2.grid(row=row2, column=0, padx=3, pady=2, sticky='e')
     
         entry2 = tk.Entry(canvas_frame2, width=120)
         entry2.grid(row=row2, column=1, padx=3, pady=2, sticky='w')
         entry2.bind('<Key>', lambda event: enforce_max_length(entry2, selected_option-1))

        
         label_boxes2.append(label2)
         entry_boxes2.append(entry2)
         
         
         # Move the "Collect Values" button below the entry boxes and make it visible
         collect_hex_button = tk.Button(canvas_frame2, text="Collect Hexadecimal Input", command=lambda: collect_hex(selected_option))

         collect_hex_button.grid(row=row2 + 2, column=0, pady=10, sticky='w')

         # Move the "Print Arrays" button below the "Collect Values" button
         print_array_button.grid(row=row2+3, column=0, pady=10, sticky='w')

         # Move the "Calculate Result" button below the "Print Arrays" button
         calculate_result_button1.grid(row=row2+4, column=0, pady=10, sticky='w')
         calculate_result_button2.grid(row=row2+5, column=0, pady=10, sticky='w')
         calculate_result_button3.grid(row=row2+6, column=0, pady=10, sticky='w')
         calculate_result_button4.grid(row=row2+8, column=0, pady=10, sticky='w')
         calculate_result_button5.grid(row=row2+7, column=0, pady=10, sticky='w')

         # After creating or modifying widgets, update the canvas scroll region
         canvas_frame.update_idletasks()
         canvas_frame2.update_idletasks()
         
         # Calculate total height of both frames
         total_height = canvas_frame.winfo_reqheight() + canvas_frame2.winfo_reqheight()
         
         extra_space = 70
         canvas.config(scrollregion=(0, 0, canvas_frame.winfo_reqwidth(), total_height + extra_space))
        
    elif selected_option2 == "DEC":
         # Create one entry box and label for each polynomial
         row1 = len(options) + 3
         label_text1 = "Polynomial 1 DEC:"
         label1 = tk.Label(canvas_frame2, text=label_text1)
         label1.grid(row=row1, column=0, padx=3, pady=2, sticky='e')
     
         entry1 = tk.Entry(canvas_frame2, width=120)
         entry1.grid(row=row1, column=1, padx=3, pady=2, sticky='w')
         entry1.bind('<Key>', lambda event: enforce_max_length(entry1, selected_option-1))

     
         label_boxes1.append(label1)
         entry_boxes1.append(entry1)
         
         row2 = len(options) + 13 + len(options) + selected_option + 3 // 10
         label_text2 = "Polynomial 2 DEC:"
         label2 = tk.Label(canvas_frame2, text=label_text2)
         label2.grid(row=row2, column=0, padx=3, pady=2, sticky='e')
     
         entry2 = tk.Entry(canvas_frame2, width=120)
         entry2.grid(row=row2, column=1, padx=3, pady=2, sticky='w')
         entry2.bind('<Key>', lambda event: enforce_max_length(entry2, selected_option-1))

     
         label_boxes2.append(label2)
         entry_boxes2.append(entry2)
         
         
         # Move the "Collect Values" button below the entry boxes and make it visible
         collect_dec_button = tk.Button(canvas_frame2, text="Collect Decimal Input", command=lambda: collect_dec(selected_option))

         collect_dec_button.grid(row=row2 + 2, column=0, pady=10, sticky='w')

         # Move the "Print Arrays" button below the "Collect Values" button
         print_array_button.grid(row=row2+3, column=0, pady=10, sticky='w')

         # Move the "Calculate Result" button below the "Print Arrays" button
         calculate_result_button1.grid(row=row2+4, column=0, pady=10, sticky='w')
         calculate_result_button2.grid(row=row2+5, column=0, pady=10, sticky='w')
         calculate_result_button3.grid(row=row2+6, column=0, pady=10, sticky='w')
         calculate_result_button4.grid(row=row2+8, column=0, pady=10, sticky='w')
         calculate_result_button5.grid(row=row2+7, column=0, pady=10, sticky='w')
         
         # After creating or modifying widgets, update the canvas scroll region
         canvas_frame.update_idletasks()
         canvas_frame2.update_idletasks()
         
         # Calculate total height of both frames
         total_height = canvas_frame.winfo_reqheight() + canvas_frame2.winfo_reqheight()
         
         extra_space = 70
         canvas.config(scrollregion=(0, 0, canvas_frame.winfo_reqwidth(), total_height + extra_space))
        
    elif selected_option2=='Array':
        # Destroy any existing entry boxes and labels before creating new ones
        for entry, label in zip(entry_boxes1, label_boxes1):
            entry.destroy()
            label.destroy()
    
        for entry, label in zip(entry_boxes2, label_boxes2):
            entry.destroy()
            label.destroy()
    
        # Create title labels for Array 1 and Array 2
        label_array1_title = tk.Label(canvas_frame2, text="Polynomial 1:")
        label_array1_title.grid(row=len(options) + 2, column=0, pady=10, sticky='w')
    
        label_array2_title = tk.Label(canvas_frame2, text="Polynomial 2:")
        label_array2_title.grid(row=len(options) + 12 + len(options) + selected_option // 10, column=0, pady=10, sticky='w')
    
        # Create new entry boxes and labels for the first array
        entry_boxes1.clear()
        label_boxes1.clear()
        label_text = 'A: \n'
        for i in range(selected_option):
            row = len(options) + 3 + i // 10
            col = i % 10
    
            label_text = f"x^{i}"
            label = tk.Label(canvas_frame2, text=label_text)
            label.grid(row=row, column=col * 2, padx=3, pady=2, sticky='e')
    
            entry = tk.Entry(canvas_frame2, width=5)
            entry.grid(row=row, column=col * 2 + 1, padx=3, pady=2, sticky='w')
    
            label_boxes1.append(label)
            entry_boxes1.append(entry)
            
            
    
        # Create new entry boxes and labels for the second array
        entry_boxes2.clear()
        label_boxes2.clear()
        for i in range(selected_option):
            row = len(options) + 13 + i // 10 + len(options) + selected_option + 3 // 10  # Adjusted row value
            col = i % 10
    
            label_text = f"x^{i}:"
            label = tk.Label(canvas_frame2, text=label_text)
            label.grid(row=row, column=col * 2, padx=3, pady=2, sticky='e')
    
            entry = tk.Entry(canvas_frame2, width=5)
            entry.grid(row=row, column=col * 2 + 1, padx=3, pady=2, sticky='w')

            label_boxes2.append(label)
            entry_boxes2.append(entry)
    
        # Initialize arrays of zeros based on the selected option
        initialized_array1 = [0] * selected_option
        initialized_array2 = [0] * selected_option
        
        root.initialized_array1 = initialized_array1
        root.initialized_array2 = initialized_array2
        collect_button.grid_remove()
    
        # Move the "Collect Values" button below the entry boxes and make it visible
        collect_button.grid(row=row + 1, column=0, pady=10, sticky='w')
    
        # Move the "Print Arrays" button below the "Collect Values" button
        print_array_button.grid(row=row + 2, column=0, pady=10, sticky='w')
    
        # Move the "Calculate Result" button below the "Print Arrays" button
        calculate_result_button1.grid(row=row + 3, column=0, pady=10, sticky='w')
        calculate_result_button2.grid(row=row + 4, column=0, pady=10, sticky='w')
        calculate_result_button3.grid(row=row + 5, column=0, pady=10, sticky='w')
        calculate_result_button4.grid(row=row + 7, column=0, pady=10, sticky='w')
        calculate_result_button5.grid(row=row + 6, column=0, pady=10, sticky='w')
    
        # After creating or modifying widgets, update the canvas scroll region
        canvas_frame.update_idletasks()
        canvas_frame2.update_idletasks()
        
        # Calculate total height of both frames
        total_height = canvas_frame.winfo_reqheight() + canvas_frame2.winfo_reqheight()
        
        extra_space = 70
        canvas.config(scrollregion=(0, 0, canvas_frame.winfo_reqwidth(), total_height + extra_space))
    
def collect_values():
    
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2

    # Update the initialized arrays with the collected values
    for i, (entry1, entry2) in enumerate(zip(entry_boxes1, entry_boxes2)):
        value1 = entry1.get()
        value2 = entry2.get()

        if value1.isdigit() or (value1.startswith('-') and value1[1:].isdigit()):
            initialized_array1[i] = int(value1)
        else:
            initialized_array1[i] = 0  # Reset the value to zero if it's not a valid integer

        if value2.isdigit() or (value2.startswith('-') and value2[1:].isdigit()):
            initialized_array2[i] = int(value2)
        else:
            initialized_array2[i] = 0  # Reset the value to zero if it's not a valid integer
    initialized_array1.reverse()
    initialized_array2.reverse()
            
def collect_binary(selected_option):
    binary_str1 = entry_boxes1[0].get()  # Assuming the first entry box is for binary input
    binary_str2 = entry_boxes2[0].get()  # Assuming the first entry box is for binary input

    # Transform binary strings into arrays using your custom function
    array1 = BintoPoly(binary_str1,selected_option)
    array2 = BintoPoly(binary_str2,selected_option)

    # Update the initialized arrays with the collected values
    root.initialized_array1 = array1
    root.initialized_array2 = array2
    
def collect_hex(selected_option):
    hex_str1 = entry_boxes1[0].get()  # Assuming the first entry box is for binary input
    hex_str2 = entry_boxes2[0].get()  # Assuming the first entry box is for binary input

    # Transform binary strings into arrays using your custom function
    array1 = HextoPoly(hex_str1,selected_option)
    array2 = HextoPoly(hex_str2,selected_option)

    # Update the initialized arrays with the collected values
    root.initialized_array1 = array1
    root.initialized_array2 = array2
    
def collect_dec(selected_option):
    dec_str1 = entry_boxes1[0].get()  # Assuming the first entry box is for binary input
    dec_str2 = entry_boxes2[0].get()  # Assuming the first entry box is for binary input

    # Transform binary strings into arrays using your custom function
    array1 = DectoPoly(dec_str1,selected_option)
    array2 = DectoPoly(dec_str2,selected_option)

    # Update the initialized arrays with the collected values
    root.initialized_array1 = array1
    root.initialized_array2 = array2
    
def print_array_popup():
    
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Printed Polynomials")

    # Create a Text widget for displaying arrays
    output_text_popup = tk.Text(popup_window, height=25, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display both arrays in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Input Polynomial 1:\n")
    PolyPrint(initialized_array1, output_text_popup)

    output_text_popup.insert(tk.END, "\nInput Polynomial 2:\n")
    PolyPrint(initialized_array2, output_text_popup)
    
    output_text_popup.insert(tk.END, "\nInput Polynomial 1 in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(initialized_array1) + "\n")

    output_text_popup.insert(tk.END, "\nInput Polynomial 2 in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(initialized_array2) + "\n")

    # Display both arrays in HEX format
    output_text_popup.insert(tk.END, "\nInput Polynomial 1 in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(initialized_array1) + "\n")

    output_text_popup.insert(tk.END, "\nInput Polynomial 2 in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(initialized_array2) + "\n")

    # Display both arrays in DEC format
    output_text_popup.insert(tk.END, "\nInput Polynomial 1 in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(initialized_array1)) + "\n")

    output_text_popup.insert(tk.END, "\nInput Polynomial 2 in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(initialized_array2)) + "\n")

    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()

def Add1():
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2
    # Perform the calculation using your function (assuming ModAddition for illustration)
    result_array = Mod(Add(initialized_array1, initialized_array2),selected_option)
    
    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Result of Addition")

    # Create a Text widget for displaying the result
    output_text_popup = tk.Text(popup_window, height=15, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display the result array in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Resulting Polynomial:\n")
    PolyPrint(result_array, output_text_popup)
    
    output_text_popup.insert(tk.END, "\nInput Resulting Polynomial in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nInput Resulting Polynomial in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nInput Resulting Polynomial in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(result_array)) + "\n")

    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()

def Sub1():
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2

    # Perform the calculation using your function (assuming ModAddition for illustration)
    result_array = Mod(Sub(initialized_array1, initialized_array2),selected_option)

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Result of Substraction")

    # Create a Text widget for displaying the result
    output_text_popup = tk.Text(popup_window, height=15, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display the result array in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Resulting Polynomial:\n")
    PolyPrint(result_array, output_text_popup)
    
        
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(result_array)) + "\n")

    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()

def Mult1():
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2
    
    # Perform the calculation using your function (assuming ModAddition for illustration)
    result_array = Mod(Mult(initialized_array1, initialized_array2),selected_option)

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Result of Multiplication")

    # Create a Text widget for displaying the result
    output_text_popup = tk.Text(popup_window, height=15, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display the result array in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Resulting Polynomial:\n")
    PolyPrint(result_array, output_text_popup)

    output_text_popup.insert(tk.END, "\nResulting Polynomial in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(result_array)) + "\n")
    
    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()

def Div1():
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2
    
    # Perform the calculation using your function (assuming ModAddition for illustration)
    result_array = Mod(Div(initialized_array1, initialized_array2,selected_option),selected_option)

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Result of Multiplication")

    # Create a Text widget for displaying the result
    output_text_popup = tk.Text(popup_window, height=15, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display the result array in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Resulting Polynomial:\n")
    PolyPrint(result_array, output_text_popup)

    output_text_popup.insert(tk.END, "\nResulting Polynomial in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(result_array) + "\n")
    
    output_text_popup.insert(tk.END, "\nResulting Polynomial in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(result_array)) + "\n")
    
    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()

def Inv1():
    # Retrieve the stored initialized arrays
    initialized_array1 = root.initialized_array1
    initialized_array2 = root.initialized_array2
    
    # Call the inverse function from your external file
    result_array1 = Inverse(initialized_array1, selected_option)
    result_array2 = Inverse(initialized_array2, selected_option)

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Inverse of Polynomials")

    # Create a Text widget for displaying the result
    output_text_popup = tk.Text(popup_window, height=25, width=300, wrap='char')
    output_text_popup.pack(padx=10, pady=10)

    # Display the result arrays in the Text widget using PolyPrint function
    output_text_popup.insert(tk.END, "Inverse of Polynomial 1:\n")
    PolyPrint(result_array1, output_text_popup)

    output_text_popup.insert(tk.END, "\nInverse of Polynomial 2:\n")
    PolyPrint(result_array2, output_text_popup)
    
    output_text_popup.insert(tk.END, "\nInverse of Polynomial 1 in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(initialized_array1) + "\n")

    output_text_popup.insert(tk.END, "\nInverse of Polynomial 2 in Binary:\n")
    output_text_popup.insert(tk.END, PolytoBin(initialized_array2) + "\n")

    # Display both arrays in HEX format
    output_text_popup.insert(tk.END, "\nInverse of Polynomial 1 in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(initialized_array1) + "\n")

    output_text_popup.insert(tk.END, "\nInverse of Polynomial 2 in Hexadecimal:\n")
    output_text_popup.insert(tk.END, PolytoHex(initialized_array2) + "\n")

    # Display both arrays in DEC format
    output_text_popup.insert(tk.END, "\nInverse of Polynomial 1 in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(initialized_array1)) + "\n")

    output_text_popup.insert(tk.END, "\nInverse of Polynomial 2 in Decimal:\n")
    output_text_popup.insert(tk.END, str(PolytoDec(initialized_array2)) + "\n")

    # Make the Text widget read-only
    output_text_popup.config(state='disabled')

    # Run the pop-up window
    popup_window.mainloop()    

def enforce_max_length(entry, MAX_INPUT_LENGTH):
    current_text = entry.get()
    if len(current_text) > MAX_INPUT_LENGTH:
        entry.delete(MAX_INPUT_LENGTH, tk.END)  # Remove the excess characters



# Create the main Tkinter window
root = tk.Tk()
root.title("Polynomial Arithmetic GUI")
root.geometry("1300x650")

# Add a canvas to the root
canvas = tk.Canvas(root)
canvas.pack(side='left', fill='both', expand=True)

# Add a label above the options
text_label = tk.Label(canvas, text="Please choose (m):")
text_label.grid(row=0, column=0, pady=10, sticky='w')

# Add a frame to the canvas
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 50), window=canvas_frame, anchor='nw')  # Adjust the y-coordinate to control placement

var = tk.IntVar()
options = ["2", "3", "4", "5", "6", "7", "8", "163", "233", "239", "283", "409", "571"]
for i, option in enumerate(options):
    tk.Radiobutton(canvas_frame, text=option, variable=var, value=int(option)).grid(row=i + 1, column=0, padx=6, sticky='w')

# Add a frame to the canvas for the second set of options
canvas_frame2 = tk.Frame(canvas)
canvas.create_window((0, len(options) * 25 + 180), window=canvas_frame2, anchor='nw')  # Adjust the y-coordinate

# Add a label for the second set of options
text_label2 = tk.Label(canvas_frame2, text="Please choose the format of the input:")
text_label2.grid(row=0, column=0, pady=10, sticky='w')

options2 = ["BIN", "HEX", "DEC", "Array"]
var2 = tk.StringVar()
for i, option in enumerate(options2):
    tk.Radiobutton(canvas_frame2, text=option, variable=var2, value=str(option)).grid(row=i + 1, column=0, padx=6, sticky='w')



# List to store entry widgets and labels for the first array
entry_boxes1 = []
label_boxes1 = []

# List to store entry widgets and labels for the second array
entry_boxes2 = []
label_boxes2 = []

# Create a button to collect values
collect_button = tk.Button(canvas_frame2, text="Collect Values", command=collect_values)

# Create a button to print the input arrays
print_array_button = tk.Button(canvas_frame2, text="Print Arrays", command=print_array_popup)

# Create a button to calculate and print the result
calculate_result_button1 = tk.Button(canvas_frame2, text="Mod Addition", command=Add1)
calculate_result_button2 = tk.Button(canvas_frame2, text="Mod Substraction", command=Sub1)
calculate_result_button3 = tk.Button(canvas_frame2, text="Mod Multiplication", command=Mult1)
calculate_result_button4 = tk.Button(canvas_frame2, text="Mod Inverse", command=Inv1)
calculate_result_button5 = tk.Button(canvas_frame2, text="Mod Division", command=Div1)




# Create a button to get the selected option and initialize arrays of zeros
choose_button = tk.Button(canvas_frame, text="Choose", command=get_selected_option)
choose_button.grid(row=len(options) + 1, column=0, pady=10, sticky='w')

#
choose_button2 = tk.Button(canvas_frame2, text="Choose", command=get_selected_option)
choose_button2.grid(row=len(options2) + 6, column=0, pady=10, sticky='w')




# Add a vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
vertical_scrollbar.pack(side='right', fill='y')

# Add a horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(root, orient='horizontal', command=canvas.xview)
horizontal_scrollbar.pack(side='bottom', fill='x')

# Configure the canvas to work with the scrollbars
canvas.config(yscrollcommand=vertical_scrollbar.set)


root.mainloop()
