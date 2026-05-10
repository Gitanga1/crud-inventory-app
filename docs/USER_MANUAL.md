```markdown
# Product Manager - User Manual

## Getting Started

### Accessing the System
1. Open your web browser (Chrome, Firefox, Edge, or Safari)
2. Go to: `https://crud-inventory-app.onrender.com`
3. No login required to view products

## Features Guide

### 1. Adding a Product

1. Locate the **"Add New Product"** form at the top of the page
2. Enter the **Product Name** (e.g., "Laptop")
3. Enter the **Price** in Ksh (numbers only, e.g., "28000")
4. Enter the **Quantity** in stock (e.g., "10")
5. Click the **"Add Product"** button

✅ The product will appear immediately in the table below.

### 2. Viewing Products

All products are displayed in a table showing:
- **Name** - Product description
- **Price (Ksh)** - Cost in Kenyan Shillings
- **Quantity** - Number in stock
- **Actions** - Edit and Delete buttons

### 3. Updating a Product

1. Find the product row you want to edit
2. Change the **Name**, **Price**, or **Quantity** in the input fields
3. Click the **"Update"** button (yellow)

✅ Your changes are saved instantly.

### 4. Deleting a Product

⚠️ **Only managers can delete products**

1. Find the product row
2. Click the red **"Delete"** button
3. Add `?password=admin123` to the end of the URL
4. Press Enter to confirm deletion

**Example URL:** `https://crud-inventory-app.onrender.com/delete/1?password=admin123`

### 5. Searching for Products

1. Type a product name in the **search box** (e.g., "Laptop")
2. Click **"Search"** button
3. Only matching products will appear
4. Click **"Clear"** to see all products again

### 6. Low Stock Alerts

When any product has less than 5 items in stock:
- An orange alert box appears at the top of the page
- The alert shows how many products are running low

### 7. Exporting Data to Excel

1. Click the **"Export to CSV"** button at the bottom of the page
2. A file named `products_export.csv` will download
3. Open with Microsoft Excel or Google Sheets
4. You can print, email, or save the file

## Troubleshooting

### Problem: "Access Denied" when deleting
**Solution:** Add `?password=admin123` to the URL

### Problem: Can't add product
**Solution:** Make sure all fields are filled (Name, Price, Quantity)

### Problem: App is slow to load
**Solution:** Free tier "sleeps" after inactivity. Refresh and wait 30 seconds.

### Problem: Changes don't save
**Solution:** Refresh the page (F5) and try again

## Support

For technical support or custom features:
- Email: gitangagrace@gmail.com

## Tips for Business Owners

1. **Daily backup:** Export CSV at the end of each day
2. **Stock management:** Check low stock alerts every morning
3. **Staff training:** Show staff how to add/update products only (not delete)
4. **Price updates:** Use the Update button when prices change
5. **Inventory count:** Compare quantities with physical stock weekly