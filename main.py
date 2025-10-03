from pyscript import display 

def ordercreate(e):

    # simple criterias

    customerName= document.getElementById('nameinput').value
    customerAddress = document.getElementById('addressinput').value
    customerNumber = document.getElementById('numberinput').value

    # base price, so prices can add up

    price = 0

    # menu item values, .checked to get from the checkboxes in the input

    if document.getElementById('overloadedsigsand').checked:
        price = price + float(document.getElementById('overloadedsigsand').value)

    if document.getElementById('fries').checked:
        price = price + float(document.getElementById('fries').value)

    if document.getElementById('macaroni').checked:
        price = price + float(document.getElementById('macaroni').value)

    if document.getElementById('wings').checked:
        price = price + float(document.getElementById('wings').value)

    if document.getElementById('cokefloat').checked:
        price = price + float(document.getElementById('cokefloat').value)

     if document.getElementById('rootbeerfloat').checked:
        price = price + float(document.getElementById('rootbeerfloat').value)

    # locations for the order summary, top half ensures no repetition of data

    document.getElementById('orderersummary').innerHTML = "Order for:" 
    document.getElementById('addresssummary').innerHTML = "Address:" 
    document.getElementById('numbersummary').innerHTML = "Contact Number:"
    document.getElementById('price').innerHTML = "Total:" 
    
    display( f"{customerName}", target="orderersummary")
    display( f"{customerAddress}", target="addresssummary")
    display( f"{customerNumber}", target="numbersummary")
    display( f"{price}", target="price")






