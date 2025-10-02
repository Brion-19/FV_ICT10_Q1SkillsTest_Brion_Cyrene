from pyscript import document

prices = {
        "Strawberry Cake": 85,
        "Chocolate Chip Cookie": 75,
        "Vanilla Cupcake": 50,
        "Red Velvet Cake": 90,
        "Macarons": 60
    }

def calculate_order(e):
    name = document.getElementById("customerName").value
    address = document.getElementById("customerAddress").value
    contact = document.getElementById("customerContact").value

    item = document.getElementById("food").value
    quantity = int(document.getElementById("quantity").value or 0)

    if quantity <= 0:
        document.getElementById("summary").innerHTML = "<b>Please enter a valid quantity.</b>"
        return

    total = prices[item] * quantity

    summary = f"""
    <p><b>Order for:</b> {name}</p>
    <p><b>Address:</b> {address}</p>
    <p><b>Contact:</b> {contact}</p>
    <p><b>Items Ordered:</b> {', '.join(selected)}</p>
    <p><b>Total:</b> ₱{total:.2f}</p>
    """

    document.getElementById("summary").innerHTML = summary

submit_btn = document.getElementById("submitBtn")
submit_btn.addEventListener("click", calculate_order)

