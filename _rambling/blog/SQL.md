# SQL

-   Relational DB (RDBMS (Relational Database Management System)) √
-   NoSQL

RDBMS

-   MySQL
-   SQL Server 
-   Oracle

### Terminology

- 列: 相同类型的数据,
  - 全都是电话号码
  - 全都是名字
- 行: 一组相关的数据
  - 一个用户
- 

# MySQL

`USE`: specify the current database 

```mysql 
USE sql_inventory;

SELECT * 
FROM sql_store.order_items oi 
JOIN products p 
	ON oi.product_id = p.product_id;
    
-- is the same as 
USE sql_store;

SELECT * 
FROM order_items oi 
JOIN sql_inventory.products p 
	ON oi.product_id = p.product_id;

```

`BETWEEN`

```mysql
SELECT * FROM sql_store.orders
WHERE order_date BETWEEN '2010-01-01' AND '2020-01-01'
ORDER BY order_date;
```

`IN` xx或者xx或者xx

```mysql
SELECT *, quantity * unit_price AS total_price FROM sql_store.order_items
WHERE order_id IN (2, 3, 4)
```



`LIKE` 含有某些特征

```mysql
SELECT * FROM sql_store.customers
WHERE 
	address LIKE '%TRAIL%' OR 
    address LIKE '%AVENUE%';
    
    
SELECT * FROM sql_store.customers
WHERE 
	phone NOT LIKE '%9';
```

- `%` 任意别的东西;
- `—` 单个别的东西;

`REGEXP` 正则表达式

```mySql 
SELECT * FROM sql_store.customers
-- WHERE last_name LIKE '%field%'
WHERE last_name REGEXP 'field$|mac|rose'
```

```mysql
SELECT * FROM sql_store.customers
WHERE last_name REGEXP '[a-h]e'
```

```
REGEXP basical usage:
^ beginning 
$ end
| logical or 
[abcd]
[a-h]

```

`NULL`: find something null.

```mysql 
SELECT * FROM customers
WHERE phone IS NULL;
```

```mysql
SELECT * FROM orders
WHERE shipped_date IS NOT NULL;
```

`DESC`: in a descending order

```mysql
SELECT * FROM customers
ORDER BY first_name DESC
```

```mysql 
SELECT  *, quantity * unit_price as total_price FROM order_items
WHERE order_id = 2 
ORDER BY total_price DESC
```

`LIMIT` 

```mysql
SELECT * FROM customers 
LIMIT 3
```

```mysql
-- consider a website 
-- page 1: 1 - 3
-- page 2: 4 - 6
-- page 3: 7 - 9
-- want to get items on page 3
SELECT * FROM customers
LIMIT 6, 3
```



```mysql
-- select 3 loyal customers
SELECT * FROM customers  
-- WHERE ...
ORDER BY points DESC
LIMIT 3
```

`JOIN`, `INNER JOIN`

```mysql
SELECT order_Id, customers.customer_id, first_name, last_name 
FROM orders
INNER JOIN customers 
	ON orders.customer_id = customers.customer_id;
    
    
--  alias
SELECT order_Id, c.customer_id, first_name, last_name 
FROM orders o
INNER JOIN customers c
	ON o.customer_id = c.customer_id;
   
```

```mysql
--     
SELECT 
	p.product_id, name, quantity, 
    p.unit_price AS 'product unit price', 
    oi.unit_price AS 'order_item unit price'
FROM products p 
JOIN order_items oi
	ON p.product_id = oi.product_id;
```

'Self join'

```mysql
USE sql_hr;

 SELECT 
	e.employee_id,
    e.first_name AS employee_name,
    m.first_name AS manager_name
 FROM employees e 
 JOIN employees m
	ON e.reports_to = m.employee_id
```

'Multiple join'

```mysql 
USE sql_store;

SELECT 
	o.order_id,
	c.customer_id,
  p.name as product_name,
	os.name as order_status
FROM orders o 
JOIN customers c 
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
JOIN order_items oi 
	ON o.order_id = oi.order_Id
JOIN products p 
	ON oi.product_id = p.product_id;
```

```mysql 
USE sql_invoicing;

SELECT 
	p.date,
    p.invoice_id,
    p.amount,
    c.name,
    pm.name
FROM payments p
JOIN clients c
	ON p.client_id = c.client_id
JOIN payment_methods pm 
	ON p.payment_method = pm.payment_method_id
-- ORDER BY date
```

