examples = [

# PRODUCTS

{
"question":"Show all products",
"sql":"SELECT * FROM PRODUCTS"
},

{
"question":"List furniture products",
"sql":"SELECT * FROM PRODUCTS WHERE CATEGORY='Furniture'"
},

{
"question":"Display electronics products",
"sql":"SELECT * FROM PRODUCTS WHERE CATEGORY='Electronics'"
},

{
"question":"Show products above 5000",
"sql":"SELECT * FROM PRODUCTS WHERE PRICE > 5000"
},

{
"question":"Show products below 2000",
"sql":"SELECT * FROM PRODUCTS WHERE PRICE < 2000"
},

# INVENTORY

{
"question":"Show products with low stock",
"sql":"SELECT * FROM PRODUCTS WHERE STOCK < 50"
},

{
"question":"Which product has the lowest stock",
"sql":"SELECT * FROM PRODUCTS ORDER BY STOCK FETCH FIRST 1 ROW ONLY"
},

{
"question":"Which product has the highest stock",
"sql":"SELECT * FROM PRODUCTS ORDER BY STOCK DESC FETCH FIRST 1 ROW ONLY"
},

{
"question":"Show inventory by category",
"sql":"SELECT CATEGORY,SUM(STOCK) FROM PRODUCTS GROUP BY CATEGORY"
},

{
"question":"Total inventory available",
"sql":"SELECT SUM(STOCK) FROM PRODUCTS"
},

# CUSTOMERS

{
"question":"Show all customers",
"sql":"SELECT * FROM CUSTOMERS"
},

{
"question":"List customers from Mumbai",
"sql":"SELECT * FROM CUSTOMERS WHERE CITY='Mumbai'"
},

{
"question":"List customers from Delhi",
"sql":"SELECT * FROM CUSTOMERS WHERE CITY='Delhi'"
},

{
"question":"Count customers by city",
"sql":"SELECT CITY,COUNT(*) FROM CUSTOMERS GROUP BY CITY"
},

{
"question":"Total customers",
"sql":"SELECT COUNT(*) FROM CUSTOMERS"
},

# ORDERS

{
"question":"Show all orders",
"sql":"SELECT * FROM ORDERS"
},

{
"question":"Total number of orders",
"sql":"SELECT COUNT(*) FROM ORDERS"
},

{
"question":"Latest order",
"sql":"SELECT * FROM ORDERS ORDER BY ORDER_DATE DESC FETCH FIRST 1 ROW ONLY"
},

{
"question":"Oldest order",
"sql":"SELECT * FROM ORDERS ORDER BY ORDER_DATE FETCH FIRST 1 ROW ONLY"
},

{
"question":"Orders by customer",
"sql":"SELECT CUSTOMER_ID,COUNT(*) FROM ORDERS GROUP BY CUSTOMER_ID"
},

# SALES

{
"question":"Most sold product",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY)
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
ORDER BY SUM(oi.QUANTITY) DESC
FETCH FIRST 1 ROW ONLY
"""
},

{
"question":"Least sold product",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY)
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
ORDER BY SUM(oi.QUANTITY)
FETCH FIRST 1 ROW ONLY
"""
},

{
"question":"Units sold by product",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY)
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
"""
},

{
"question":"Total units sold",
"sql":"SELECT SUM(QUANTITY) FROM ORDER_ITEMS"
},

{
"question":"Average quantity per order",
"sql":"SELECT AVG(QUANTITY) FROM ORDER_ITEMS"
},

# REVENUE

{
"question":"Which product generated highest revenue",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
ORDER BY REVENUE DESC
FETCH FIRST 1 ROW ONLY
"""
},

{
"question":"Revenue by product",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
"""
},

{
"question":"Total revenue",
"sql":"""
SELECT SUM(oi.QUANTITY*p.PRICE)
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
"""
},

{
"question":"Average revenue per product",
"sql":"""
SELECT AVG(REVENUE)
FROM(
SELECT SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
)
"""
},

{
"question":"Top 3 products by revenue",
"sql":"""
SELECT p.PRODUCT_NAME,
SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.PRODUCT_NAME
ORDER BY REVENUE DESC
FETCH FIRST 3 ROWS ONLY
"""
},

# CUSTOMER ANALYTICS

{
"question":"Top customer by spending",
"sql":"""
SELECT c.CUSTOMER_NAME,
SUM(oi.QUANTITY*p.PRICE) SPENDING
FROM CUSTOMERS c
JOIN ORDERS o
ON c.CUSTOMER_ID=o.CUSTOMER_ID
JOIN ORDER_ITEMS oi
ON o.ORDER_ID=oi.ORDER_ID
JOIN PRODUCTS p
ON oi.PRODUCT_ID=p.PRODUCT_ID
GROUP BY c.CUSTOMER_NAME
ORDER BY SPENDING DESC
FETCH FIRST 1 ROW ONLY
"""
},

{
"question":"Customer spending report",
"sql":"""
SELECT c.CUSTOMER_NAME,
SUM(oi.QUANTITY*p.PRICE) SPENDING
FROM CUSTOMERS c
JOIN ORDERS o
ON c.CUSTOMER_ID=o.CUSTOMER_ID
JOIN ORDER_ITEMS oi
ON o.ORDER_ID=oi.ORDER_ID
JOIN PRODUCTS p
ON oi.PRODUCT_ID=p.PRODUCT_ID
GROUP BY c.CUSTOMER_NAME
"""
},

{
"question":"Customer with most orders",
"sql":"""
SELECT c.CUSTOMER_NAME,
COUNT(*) ORDERS
FROM CUSTOMERS c
JOIN ORDERS o
ON c.CUSTOMER_ID=o.CUSTOMER_ID
GROUP BY c.CUSTOMER_NAME
ORDER BY ORDERS DESC
FETCH FIRST 1 ROW ONLY
"""
},

# CATEGORY ANALYTICS

{
"question":"Revenue by category",
"sql":"""
SELECT p.CATEGORY,
SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.CATEGORY
"""
},

{
"question":"Best performing category",
"sql":"""
SELECT p.CATEGORY,
SUM(oi.QUANTITY*p.PRICE) REVENUE
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.CATEGORY
ORDER BY REVENUE DESC
FETCH FIRST 1 ROW ONLY
"""
},

{
"question":"Units sold by category",
"sql":"""
SELECT p.CATEGORY,
SUM(oi.QUANTITY)
FROM PRODUCTS p
JOIN ORDER_ITEMS oi
ON p.PRODUCT_ID=oi.PRODUCT_ID
GROUP BY p.CATEGORY
"""
},

# ADVANCED

{
"question":"Average product price",
"sql":"SELECT AVG(PRICE) FROM PRODUCTS"
},

{
"question":"Most expensive product",
"sql":"SELECT * FROM PRODUCTS ORDER BY PRICE DESC FETCH FIRST 1 ROW ONLY"
},

{
"question":"Cheapest product",
"sql":"SELECT * FROM PRODUCTS ORDER BY PRICE FETCH FIRST 1 ROW ONLY"
},

{
"question":"Average stock by category",
"sql":"SELECT CATEGORY,AVG(STOCK) FROM PRODUCTS GROUP BY CATEGORY"
},

{
"question":"Products never sold",
"sql":"""
SELECT *
FROM PRODUCTS
WHERE PRODUCT_ID NOT IN
(
SELECT PRODUCT_ID
FROM ORDER_ITEMS
)
"""
}
]