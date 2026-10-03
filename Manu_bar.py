import tkinter as tk  # Professional way to import widgets

# 1. Main Application Structural Frame
window = tk.Tk()
window.geometry("950x600")  # Perfectly sized to show menu and cart side-by-side
window.title("Smart POS System Engine")
window.config(bg="#f8f9fa")  # Modern light-grey background

# 2. Data Catalogs with Pricing Structures
food = ["pizza", "burgger", "KFC", "chicken wings", "french fries"]
food_prices = {"pizza": 250, "burgger": 150, "KFC": 350, "chicken wings": 200, "french fries": 90}

jucie = ["orange jucie", "mango jucie", "blueberry jucie", "apple jucie", "lemon jucie"]
jucie_prices = {"orange jucie": 80, "mango jucie": 90, "blueberry jucie": 120, "apple jucie": 100, "lemon jucie": 60}

# 3. Persistent Cart Memory Storage Dictionary
order_cart = {}

# 4. Clean Event Handling Logic
def add_to_cart(item_name, price):
    """Increments item count in state memory and triggers a screen refresh."""
    if item_name in order_cart:
        order_cart[item_name] += 1
    else:
        order_cart[item_name] = 1
        
    print(f"[LOG]: Added {item_name.title()} to cart. Current Qty: {order_cart[item_name]}")
    refresh_billing_ledger()

def clear_cart():
    """Flushes transient memory state completely and refreshes display."""
    order_cart.clear()
    refresh_billing_ledger()

def refresh_billing_ledger():
    """Recalculates all mathematical subtotals and updates the right ledger screen area."""
    # Clear out the previous layout lines
    for widget in ledger_scroll_frame.winfo_children():
        widget.destroy()
        
    grand_total = 0
    
    # Loop over cart keys and draw summary labels
    for item, qty in order_cart.items():
        unit_price = food_prices.get(item) or jucie_prices.get(item)
        subtotal = unit_price * qty
        grand_total += subtotal
        
        # Build text string block formatted cleanly
        item_line = f"• {item.title():<15} x{qty:<2} = ₹{subtotal}"
        lbl = tk.Label(ledger_scroll_frame, text=item_line, font=("Consolas", 12, "bold"), fg="#334155", bg="#ffffff")
        lbl.pack(anchor=tk.W, pady=3, padx=10)
        
    # Update the big Grand Total box text value
    total_label.config(text=f"Grand Total: ₹{grand_total}")

def show_receipt_custom_popup():
    """Compiles selected data items and displays a styled confirmation layout popup window."""
    if not order_cart:
        return
        
    popup = tk.Toplevel(window)
    popup.title("🧾 Your Bill Receipt")
    popup.geometry("450x450")
    popup.config(bg="#fef3c7")  # Clean Light-Yellow color background
    
    header = tk.Label(popup, text="=== FINAL INVOICE ===", font=("Consolas", 18, "bold"), fg="#1e3a8a", bg="#fef3c7")
    header.pack(pady=(20, 10))
    
    grand_total = 0
    for item, qty in order_cart.items():
        unit_price = food_prices.get(item) or jucie_prices.get(item)
        subtotal = unit_price * qty
        grand_total += subtotal
        
        item_label = tk.Label(
            popup, text=f"• {item.title():<15} x{qty} : ₹{subtotal}", 
            font=("Consolas", 13, "bold"), fg="#1e40af", bg="#fef3c7"
        )
        item_label.pack(pady=3, anchor=tk.W, padx=40)
        
    divider = tk.Label(popup, text="-----------------------------------", font=("Consolas", 14), fg="#6b7280", bg="#fef3c7")
    divider.pack(pady=10)
    
    total_label_popup = tk.Label(popup, text=f"💰 GRAND TOTAL : ₹{grand_total}", font=("Consolas", 18, "bold"), fg="#065f46", bg="#fef3c7")
    total_label_popup.pack(pady=10)
    
    close_button = tk.Button(popup, text="Close & Clear", font=("Arial", 11, "bold"), fg="#ffffff", bg="#dc2626", command=lambda: [popup.destroy(), clear_cart()], padx=15, pady=5)
    close_button.pack(pady=15)

# 5. Image Asset Management Pipeline (Crash-Proof Wrapper)
try:
    foodimages = [
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 091305.png").subsample(6, 6),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 091612.png").subsample(9, 9),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 092054.png").subsample(7, 7),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 092130.png").subsample(9, 9),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 092513.png").subsample(7, 7)
    ]
    
    jucieimages = [
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 092700.png").subsample(7, 7),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 092800.png").subsample(6, 6),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 093106.png").subsample(9, 9),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 093431.png").subsample(7, 7),
        tk.PhotoImage(file=r"C:\Users\sk799\OneDrive\Pictures\Screenshots\Screenshot 2026-06-15 093733.png").subsample(7, 7)
    ]
except Exception:
    foodimages = [None] * 5
    jucieimages = [None] * 5

# --- SPLIT SCREEN ARRAYS ---
menu_catalog_frame = tk.Frame(window, bg="#f8f9fa")
menu_catalog_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=15)

# CRITICAL FIX applied here: 'width=380' is defined safely inside the widget creator method context
ledger_panel_frame = tk.LabelFrame(window, text="🛒 Active Billing Ledger", font=("Consolas", 13, "bold"), fg="#1e3a8a", bg="#ffffff", bd=2, relief="groove", width=380)
ledger_panel_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 20), pady=25)

# 6. UI Layout Generation: Menu Subcolumns (Food Left, Drinks Right)
food_subframe = tk.Frame(menu_catalog_frame, bg="#f8f9fa")
food_subframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

drink_subframe = tk.Frame(menu_catalog_frame, bg="#f8f9fa")
drink_subframe.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 0))

label_food = tk.Label(food_subframe, text="Food Menu Catalog", font=("Consolas", 13, "bold"), fg="#1e3a8a", bg="#f8f9fa")
label_food.pack(anchor=tk.W, pady=(5, 5))

for index in range(len(food)):
    name = food[index]
    price = food_prices[name]
    display_text = f"{name.title()}\n₹{price}"
    
    btn = tk.Button(
        food_subframe, text=display_text, font=("Arial", 10, "bold"),
        image=foodimages[index], compound="left", width=220, bg="#ffffff",
        activebackground="#f1f5f9", command=lambda n=name, p=price: add_to_cart(n, p),
        bd=1, relief="groove", cursor="hand2"
    )
    btn.pack(anchor=tk.W, pady=4)

label_drink = tk.Label(drink_subframe, text="Beverage Catalog", font=("Consolas", 13, "bold"), fg="#1e3a8a", bg="#f8f9fa")
label_drink.pack(anchor=tk.W, pady=(5, 5))

for index in range(len(jucie)):
    name = jucie[index]
    price = jucie_prices[name]
    display_text = f"{name.title()}\n₹{price}"
    
    btn1 = tk.Button(
        drink_subframe, text=display_text, font=("Arial", 10, "bold"),
        image=jucieimages[index], compound="left", width=220, bg="#ffffff",
        activebackground="#f1f5f9", command=lambda n=name, p=price: add_to_cart(n, p),
        bd=1, relief="groove", cursor="hand2"
    )
    btn1.pack(anchor=tk.W, pady=4)

# 7. UI Layout Generation: Right Transaction Ledger Inner Elements
ledger_scroll_frame = tk.Frame(ledger_panel_frame, bg="#ffffff")
ledger_scroll_frame.pack(fill=tk.BOTH, expand=True, pady=10)

initial_msg = tk.Label(ledger_scroll_frame, text="Ledger empty.\nClick items to add to order.", font=("Arial", 11, "italic"), fg="#94a3b8", bg="#ffffff")
initial_msg.pack(pady=40)

total_label = tk.Label(ledger_panel_frame, text="Grand Total: ₹0", font=("Consolas", 16, "bold"), fg="#ffffff", bg="#10b981", padx=15, pady=8, bd=0)
total_label.pack(fill="x", padx=15, pady=5)

print_button = tk.Button(ledger_panel_frame, text="✨ Print Final Receipt", font=("Arial", 12, "bold"), fg="#ffffff", bg="#1e3a8a", activebackground="#1e40af", activeforeground="#ffffff", command=show_receipt_custom_popup, pady=8, bd=1, relief="raised", cursor="hand2")
print_button.pack(fill="x", padx=15, pady=(5, 10))

# Start Application Process loop
window.mainloop()

