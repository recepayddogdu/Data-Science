select*from CUSTOMER
order by CUSTOMERNAME --isme göre a-z siralar.
---------------------------------------------------
select*from CUSTOMER
order by CITY,CUSTOMERNAME -- sehirleri a-z siralar ve isimleri de a-z siralar.
------------------------------------
select*from CUSTOMER
order by CITY,CUSTOMERNAME desc --sehirleri a-z siralar, isimleri z-a siralar.
---------------------------------
select*from CUSTOMER
order by CITY desc,CUSTOMERNAME desc --sehirleri ve isimleri z-a siralar.