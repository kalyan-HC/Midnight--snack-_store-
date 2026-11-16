# 🌙 Midnight Snack Store

A simple desktop GUI app built with Python's **Tkinter** library. It's a mini snack-ordering store for late-night hostel cravings: browse products, add them to a cart, apply a coupon and check out.

> Built as a college assignment to practise GUI (frontend) development in Python.

---

## 📸 Screenshot

![App Screenshot](screenshots/app.png)

---

## ✨ Features

- **Product list** with 7 snacks and their prices
- **Quantity selector** (1–10) using a Spinbox
- **Add to Cart**: adding the same item again increases its quantity
- **Remove Selected** item from the cart
- **Live total** that updates after every action
- **Coupon code** support: `HOSTEL10` gives **10% off**
- **Checkout** shows a bill summary in a popup and clears the cart
- **Input checks**: warnings if no product is selected, the quantity is invalid, or the cart is empty

---

## 🛠️ Tech Stack

| Component | Used |
|-----------|------|
| Language  | Python 3 |
| GUI Library | Tkinter (built into Python) |
| Widgets | Label, Listbox, Spinbox, Entry, Button, Frame, messagebox |

No external libraries are needed.

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Malhar150/midnight-snack-store.git
cd midnight-snack-store
```

**2. Check that Tkinter is installed**
```bash
python -m tkinter
```
A small test window should open. If you get an error instead:
- **Windows / macOS:** reinstall Python from [python.org](https://www.python.org/downloads/) and keep the "tcl/tk" option ticked
- **Ubuntu / Debian:** `sudo apt install python3-tk`

**3. Run the app**
```bash
python midnight_snack_store.py
```

---

## 🧾 How to Use

1. Select a product from the **Products** list
2. Pick a quantity and click **Add to Cart**
3. To remove an item, select it in **Your Cart** and click **Remove Selected**
4. Enter `HOSTEL10` in the coupon box and click **Apply** for 10% off
5. Click **Checkout** to place the order

---

## 📂 Project Structure

```
midnight-snack-store/
├── midnight_snack_store.py   # Main application (GUI + logic)
├── requirements.txt          # Dependencies (none, Tkinter is built in)
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── .gitignore                # Files Git should ignore
└── screenshots/
    └── app.png               # App screenshot
```

---

## 🧠 Concepts Used

- **Event-driven programming**: buttons call handler functions through `command=`
- **Layout managers**: `pack()` and `grid()` used together inside separate Frames
- **Dictionaries**: product catalogue and cart (`item → quantity`)
- **Global state**: the discount value is updated with the `global` keyword
- **Exception handling**: `try/except` catches invalid quantity input
- **Dialog boxes**: `messagebox` for warnings, errors and confirmations

---

## 🔮 Possible Improvements

- Save orders to a file or a SQLite database
- Show the discount amount separately in the cart
- Add product images
- Add a quantity edit option inside the cart

---

## 👤 Author

**Malhar Jardosh**
B.Tech CSE, SRM Institute of Science and Technology, KTR
GitHub: [@Malhar150](https://github.com/Malhar150)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
