from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Invoice(BaseModel):
    invoice_id: str
    vendor: str
    amount: float
    status: str


invoices = [
    {
        "invoice_id": "INDSA_01",
        "vendor": "Indsafri Pvt Limited",
        "amount": 60000,
        "status": "Payment paid"
    }
]


# POST: Create a new invoice
@app.post("/invoices")
def create_invoice(invoice: Invoice):

    # Check whether the invoice already exists
    for existing_invoice in invoices:
        if existing_invoice["invoice_id"] == invoice.invoice_id:
            raise HTTPException(
                status_code=400,
                detail="Invoice already exists"
            )

    # Add the invoice if it does not exist
    new_invoice = invoice.model_dump()
    invoices.append(new_invoice)

    return new_invoice


# GET: Retrieve all invoices
@app.get("/all_invoices")
def get_invoices():
    return invoices


# DELETE: Delete an invoice by ID
@app.delete("/delete_invoices/{invoice_id}")
def delete_invoice(invoice_id: str):

    for index, invoice in enumerate(invoices):
        if invoice["invoice_id"] == invoice_id:
            deleted = invoices.pop(index)
            return deleted

    raise HTTPException(
        status_code=404,
        detail="Invoice not found"
    )


# PUT: Update an existing invoice
@app.put("/update_invoice/{invoice_id}")
def update_invoice(invoice_id: str, updated_invoice: Invoice):

    for index, invoice in enumerate(invoices):
        if invoice["invoice_id"] == invoice_id:

            # Prevent changing the invoice ID during an update
            if updated_invoice.invoice_id != invoice_id:
                raise HTTPException(
                    status_code=400,
                    detail="Invoice ID in the body must match the URL"
                )

            invoices[index] = updated_invoice.model_dump()
            return invoices[index]

    raise HTTPException(
        status_code=404,
        detail="Invoice not found"
    )
