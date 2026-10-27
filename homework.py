from fastapi import FastAPI

app = FastAPI()

invoices = [
    {
        "invoice_id": "INDSA_01",
        "vendor": "Insafari Pvt Limited",
        "amount": 60000,
        "status": "Payment paid"
    }
]


@app.get("/invoices")
def get_invoices():
    return invoices
