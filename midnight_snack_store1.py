import tkinter as tk
from tkinter import messagebox

# ---------- DATA ----------
PRODUCTS = {
    "Maggi Pack": 15,
    "Cold Coffee": 40,
    "Chips": 20,
    "Chocolate Bar": 30,
    "Energy Drink": 90,
    "Instant Noodles Cup": 50,
    "Biscuit Pack": 10,
}
COUPON_CODE = "HOSTEL10"   # gives 10% off
cart = {}                  # item name -> quantity
discount = 0               # becomes 0.10 after coupon is applied

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Midnight Snack Store")
root.geometry("640x470")
root.config(bg="#fff3e0")

tk.Label(root, text="Midnight Snack Store", font=("Arial", 20, "bold"),
         bg="#ff9800", fg="white").pack(fill="x")
tk.Label(root, text="Late-night hostel cravings, delivered to your room",
         bg="#fff3e0", font=("Arial", 10, "italic")).pack()

main = tk.Frame(root, bg="#fff3e0")
main.pack(pady=10)

# ---------- LEFT SIDE: products ----------
left = tk.Frame(main, bg="#fff3e0")
left.grid(row=0, column=0, padx=15)

tk.Label(left, text="Products", font=("Arial", 13, "bold"), bg="#fff3e0").pack()
product_list = tk.Listbox(left, width=28, height=9, font=("Arial", 11))
for name, price in PRODUCTS.items():
    product_list.insert(tk.END, f"{name} - Rs.{price}")
product_list.pack()

tk.Label(left, text="Quantity:", bg="#fff3e0").pack(pady=(8, 0))
qty_box = tk.Spinbox(left, from_=1, to=10, width=5, font=("Arial", 12))
qty_box.pack()

# ---------- RIGHT SIDE: cart ----------
right = tk.Frame(main, bg="#fff3e0")
right.grid(row=0, column=1, padx=15)

tk.Label(right, text="Your Cart", font=("Arial", 13, "bold"), bg="#fff3e0").pack()
cart_list = tk.Listbox(right, width=30, height=9, font=("Arial", 11))
cart_list.pack()

total_label = tk.Label(right, text="Total: Rs.0", font=("Arial", 14, "bold"),
                       bg="#fff3e0", fg="darkgreen")
total_label.pack(pady=5)


# ---------- FUNCTIONS (event handlers) ----------
def get_total():
    total = sum(PRODUCTS[item] * qty for item, qty in cart.items())
    return total - total * discount


def refresh_cart():
    cart_list.delete(0, tk.END)
    for item, qty in cart.items():
        cart_list.insert(tk.END, f"{item} x{qty} = Rs.{PRODUCTS[item] * qty}")
    total_label.config(text=f"Total: Rs.{get_total():.2f}")


def add_to_cart():
    selected = product_list.curselection()
    if not selected:
        messagebox.showwarning("Oops", "Please select a product first!")
        return
    name = list(PRODUCTS.keys())[selected[0]]
    try:
        qty = int(qty_box.get())
        if qty < 1:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Oops", "Quantity must be a positive number!")
        return
    cart[name] = cart.get(name, 0) + qty
    refresh_cart()


def remove_item():
    selected = cart_list.curselection()
    if not selected:
        messagebox.showwarning("Oops", "Select an item in the cart to remove.")
        return
    name = list(cart.keys())[selected[0]]
    del cart[name]
    refresh_cart()


def apply_coupon():
    global discount
    if coupon_entry.get().strip().upper() == COUPON_CODE:
        discount = 0.10
        messagebox.showinfo("Coupon", "10% discount applied!")
    else:
        discount = 0
        messagebox.showerror("Coupon", "Invalid coupon code.")
    refresh_cart()


def checkout():
    if not cart:
        messagebox.showwarning("Empty", "Your cart is empty!")
        return
    bill = "\n".join(f"{i} x{q}" for i, q in cart.items())
    messagebox.showinfo("Order Placed!",
                        f"{bill}\n\nTotal paid: Rs.{get_total():.2f}\n\nSnacks on the way!")
    cart.clear()
    refresh_cart()


# ---------- BUTTONS ----------
tk.Button(left, text="Add to Cart", bg="#4caf50", fg="white",
          font=("Arial", 11, "bold"), command=add_to_cart).pack(pady=8)

tk.Button(right, text="Remove Selected", bg="#f44336", fg="white",
          command=remove_item).pack()

bottom = tk.Frame(root, bg="#fff3e0")
bottom.pack(pady=5)
tk.Label(bottom, text="Coupon:", bg="#fff3e0").grid(row=0, column=0)
coupon_entry = tk.Entry(bottom, width=14)
coupon_entry.grid(row=0, column=1, padx=5)
tk.Button(bottom, text="Apply", command=apply_coupon).grid(row=0, column=2)
tk.Button(bottom, text="Checkout", bg="#2196f3", fg="white",
          font=("Arial", 12, "bold"), width=12,
          command=checkout).grid(row=0, column=3, padx=20)

root.mainloop()
